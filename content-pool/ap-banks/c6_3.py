# CALC 6.3 Riemann Sums, Summation Notation, and Definite Integral Notation — 25 questions
# Answers verified with sympy; see verify_c6_3.py, which evaluates every sum
# with sp.Sum and every limit of a Riemann sum with sp.limit, then confirms the
# matching definite integral independently with sp.integrate.
# Questions 1, 12, 13, 14, 19, 20, 23 are conceptual (notation and definitions).
TOPIC = ("6.3", "Riemann Sums, Summation Notation, and Definite Integral Notation", 6)
QUESTIONS = [
 dict(q="The interval [0, 4] is divided into n subintervals of equal width. What is that common width, and what is the right endpoint of the ith subinterval?", choices=[
   "width 4/n and right endpoint 4i/n",
   "width n/4 and right endpoint 4i/n",
   "width 4/n and right endpoint i/n",
   "width 4/n and right endpoint 4 + i/n"], ans=0,
   why="The width is (b - a)/n = 4/n, and the ith right endpoint is a + i(b - a)/n = 0 + 4i/n."),
 dict(q="The interval [1, 5] is divided into n subintervals of equal width. What is the right endpoint of the ith subinterval?", choices=[
   "1 + 4i/n",
   "4i/n",
   "1 + i/n",
   "5i/n"], ans=0,
   why="The endpoint is a + i(b - a)/n = 1 + 4i/n, so it starts at 1 when i = 0 and reaches 5 when i = n."),
 dict(q="What is the value of the limit as n -> infinity of the sum from i = 1 to n of (2i/n)^2 (2/n)?", choices=[
   "4/3",
   "8/3",
   "4",
   "8"], ans=1,
   why="The sum is a right Riemann sum for int from 0 to 2 of x^2 dx, whose value is 8/3."),
 dict(q="Which limit expresses int from 1 to 3 of x^3 dx as the limit of a right Riemann sum?", choices=[
   "the limit as n -> infinity of the sum from i = 1 to n of (1 + 2i/n)^3 (2/n)",
   "the limit as n -> infinity of the sum from i = 1 to n of (1 + 2i/n)^3 (1/n)",
   "the limit as n -> infinity of the sum from i = 1 to n of (2i/n)^3 (2/n)",
   "the limit as n -> infinity of the sum from i = 1 to n of (1 + 3i/n)^3 (3/n)"], ans=0,
   why="Here b - a = 2, so the width is 2/n and the right endpoints are 1 + 2i/n."),
 dict(q="The limit as n -> infinity of the sum from i = 1 to n of (1/n) sqrt(i/n) is equal to which definite integral?", choices=[
   "int from 0 to 1 of sqrt(x) dx",
   "int from 0 to n of sqrt(x) dx",
   "int from 1 to n of sqrt(x) dx",
   "int from 0 to 1 of x dx"], ans=0,
   why="The factor 1/n is the width and i/n runs over the right endpoints of [0, 1], so the integrand is sqrt(x) on [0, 1]."),
 dict(q="What is the value of the sum from i = 1 to 5 of (2i + 1)?", choices=[
   "11",
   "25",
   "35",
   "45"], ans=2,
   why="The terms are 3, 5, 7, 9, and 11, whose total is 35, or 2(15) + 5(1) = 35."),
 dict(q="For a constant c, the sum from i = 1 to n of c is equal to", choices=[
   "c",
   "cn",
   "cn(n + 1)/2",
   "c/n"], ans=1,
   why="The same constant is added n times."),
 dict(q="What is the value of the sum from i = 1 to 10 of i?", choices=[
   "45",
   "55",
   "100",
   "110"], ans=1,
   why="The sum of the first n positive integers is n(n + 1)/2, which is 10(11)/2 = 55."),
 dict(q="What is the value of the sum from i = 1 to 6 of i^2?", choices=[
   "21",
   "36",
   "91",
   "441"], ans=2,
   why="The formula n(n + 1)(2n + 1)/6 gives 6(7)(13)/6 = 91."),
 dict(q="Which expression is a right Riemann sum for int from 2 to 6 of f(x) dx using four subintervals of equal width?", choices=[
   "f(2) + f(3) + f(4) + f(5)",
   "f(3) + f(4) + f(5) + f(6)",
   "4[f(3) + f(4) + f(5) + f(6)]",
   "(1/4)[f(3) + f(4) + f(5) + f(6)]"], ans=1,
   why="The width is 1 and the right endpoints are 3, 4, 5, and 6, so each value is multiplied by 1."),
 dict(q="What is the value of the limit as n -> infinity of the sum from i = 1 to n of (3/n)(1 + 3i/n)?", choices=[
   "3",
   "7.5",
   "9",
   "15"], ans=1,
   why="This is a right Riemann sum for int from 1 to 4 of x dx, which equals (16 - 1)/2 = 7.5."),
 dict(q="In the notation int from a to b of f(x) dx, the symbol dx", choices=[
   "indicates the variable of integration",
   "means the answer is a function of x",
   "is a factor that must be multiplied at the end",
   "represents the width of the interval [a, b]"], ans=0,
   why="The dx names the variable of integration; it comes from the width of the subintervals in the Riemann sum, but it does not by itself equal b - a."),
 dict(q="Which statement about int from 0 to 2 of x^2 dx is true?", choices=[
   "It equals int from 0 to 2 of t^2 dt, because the variable of integration is a dummy variable.",
   "It is a function of x.",
   "It cannot be compared with int from 0 to 2 of t^2 dt, since the variables differ.",
   "It equals 2x^2."], ans=0,
   why="A definite integral evaluates to a number, and renaming the variable of integration changes nothing about that number."),
 dict(q="A function f is defined on [a, b]. The definite integral int from a to b of f(x) dx is defined as", choices=[
   "the limit of Riemann sums as the width of the largest subinterval approaches zero, provided the limit exists",
   "the antiderivative of f evaluated at b",
   "the sum of f at every point of [a, b]",
   "the average of f(a) and f(b) times b - a"], ans=0,
   why="The definite integral is defined as a limit of Riemann sums; the Fundamental Theorem later provides the antiderivative method for evaluating it."),
 dict(q="What is the right Riemann sum approximation of int from 0 to 4 of (2x + 1) dx using four subintervals of equal width?", choices=[
   "16",
   "20",
   "24",
   "28"], ans=2,
   why="With width 1 the right endpoints are 1, 2, 3, and 4, where 2x + 1 equals 3, 5, 7, and 9, so the sum is 24."),
 dict(q="What is the value of the limit as n -> infinity of the sum from i = 1 to n of (pi/n) sin(pi i/n)?", choices=[
   "0",
   "1",
   "2",
   "pi"], ans=2,
   why="This is a right Riemann sum for int from 0 to pi of sin(x) dx, which equals -cos(pi) + cos(0) = 2."),
 dict(q="What is the value of the sum from k = 1 to 4 of k^2?", choices=[
   "10",
   "20",
   "30",
   "100"], ans=2,
   why="The terms are 1, 4, 9, and 16, whose total is 30."),
 dict(q="What is the value of the limit as n -> infinity of the sum from i = 1 to n of i^2/n^3?", choices=[
   "0",
   "1/6",
   "1/3",
   "1/2"], ans=2,
   why="Rewriting the term as (i/n)^2 (1/n) shows a right Riemann sum for int from 0 to 1 of x^2 dx, which is 1/3."),
 dict(q="Which limit of a Riemann sum represents int from 0 to 1 of e^x dx?", choices=[
   "the limit as n -> infinity of the sum from i = 1 to n of (1/n) e^(i/n)",
   "the limit as n -> infinity of the sum from i = 1 to n of (1/n) e^i",
   "the limit as n -> infinity of the sum from i = 1 to n of e^(i/n)",
   "the limit as n -> infinity of the sum from i = 1 to n of (1/n) e^(1/n)"], ans=0,
   why="The width 1/n must multiply the integrand evaluated at the sample points i/n of [0, 1]."),
 dict(q="In a general Riemann sum for f on [a, b], the sample point used in each subinterval", choices=[
   "may be any point of that subinterval",
   "must be the left endpoint",
   "must be the midpoint",
   "must be the point where f is largest"], ans=0,
   why="A Riemann sum allows any sample point in each subinterval; for a continuous function all such sums share the same limit."),
 dict(q="What is the value of the limit as n -> infinity of the sum from i = 1 to n of (1/n)(1/(1 + i/n))?", choices=[
   "ln(2)",
   "ln(3)",
   "1/2",
   "1"], ans=0,
   why="This is a right Riemann sum for int from 0 to 1 of 1/(1 + x) dx, which is ln(2) - ln(1) = ln(2)."),
 dict(q="The limit as n -> infinity of the sum from i = 1 to n of (4/n) sqrt(1 + 4i/n) is equal to which definite integral?", choices=[
   "int from 1 to 5 of sqrt(x) dx",
   "int from 0 to 4 of sqrt(x) dx",
   "int from 0 to 4 of sqrt(1 + 4x) dx",
   "int from 1 to 4 of sqrt(x) dx"], ans=0,
   why="A width of 4/n with sample points 1 + 4i/n means a = 1 and b - a = 4, so the interval is [1, 5] and the integrand is sqrt(x)."),
 dict(q="For sequences a_i and b_i, the sum from i = 1 to n of (a_i + b_i) is equal to", choices=[
   "the sum from i = 1 to n of a_i plus the sum from i = 1 to n of b_i",
   "the sum from i = 1 to n of a_i times the sum from i = 1 to n of b_i",
   "n times (a_1 + b_1)",
   "the sum from i = 1 to n of a_i plus b_n"], ans=0,
   why="Summation distributes over addition, since the terms may be regrouped freely in a finite sum."),
 dict(q="What is the value of the sum from i = 1 to 20 of (3i - 2)?", choices=[
   "570",
   "590",
   "610",
   "630"], ans=1,
   why="The sum is 3(20)(21)/2 - 2(20) = 630 - 40 = 590."),
 dict(q="Using the right Riemann sum definition, int from 0 to 1 of x dx is the limit as n -> infinity of (1/n^2) times the sum from i = 1 to n of i. What is that limit?", choices=[
   "0",
   "1/2",
   "1",
   "the limit does not exist"], ans=1,
   why="The sum from i = 1 to n of i is n(n + 1)/2, so the expression is (n + 1)/(2n), which approaches 1/2."),
]
