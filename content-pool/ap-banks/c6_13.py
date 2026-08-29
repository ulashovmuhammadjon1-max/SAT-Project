# CALC 6.13 Evaluating Improper Integrals — 25 questions  [BC only]
# Answers verified with sympy; see verify_c6_13.py, which evaluates each
# improper integral the way the topic requires -- as the limit of a proper
# integral over a finite interval -- and confirms divergence by showing that
# limit is infinite rather than by trusting a single sp.integrate call.
# Questions 1, 11, 17, 23 are conceptual (the limit definition, why the limit
# notation is required, what makes an integral improper, and the comparison
# test).
TOPIC = ("6.13", "Evaluating Improper Integrals", 6)
QUESTIONS = [
 dict(q="For a function f continuous on [1, infinity), int from 1 to infinity of f(x) dx is defined as", choices=[
   "the limit as b -> infinity of int from 1 to b of f(x) dx",
   "int from 1 to b of f(x) dx with b replaced by infinity",
   "the limit as x -> infinity of f(x)",
   "the sum from n = 1 to infinity of f(n)"], ans=0,
   why="An infinite limit of integration is handled by integrating to a finite b and then taking a limit."),
 dict(q="What is the value of int from 1 to infinity of 1/x^2 dx?", choices=[
   "1",
   "1/2",
   "2",
   "The integral diverges."], ans=0,
   why="The limit as b -> infinity of (-1/b + 1) is 1."),
 dict(q="What is the value of int from 1 to infinity of 1/x dx?", choices=[
   "The integral diverges.",
   "0",
   "1",
   "ln(2)"], ans=0,
   why="The antiderivative ln(b) grows without bound as b -> infinity, so no finite limit exists."),
 dict(q="What is the value of int from 1 to infinity of 1/x^3 dx?", choices=[
   "1/2",
   "1/3",
   "1",
   "The integral diverges."], ans=0,
   why="The limit of -1/(2b^2) + 1/2 as b -> infinity is 1/2."),
 dict(q="The integral int from 1 to infinity of 1/x^p dx converges exactly when", choices=[
   "p > 1",
   "p >= 1",
   "p < 1",
   "p is any positive number"], ans=0,
   why="For p > 1 the antiderivative x^(1-p)/(1 - p) tends to 0, and for p <= 1 it grows without bound; the case p = 1 gives the divergent logarithm."),
 dict(q="What is the value of int from 0 to 1 of 1/sqrt(x) dx?", choices=[
   "2",
   "1",
   "1/2",
   "The integral diverges."], ans=0,
   why="The integrand is unbounded at 0, so the value is the limit as a -> 0 from the right of 2 - 2 sqrt(a), which is 2."),
 dict(q="What is the value of int from 0 to 1 of 1/x dx?", choices=[
   "The integral diverges.",
   "0",
   "1",
   "-1"], ans=0,
   why="The limit as a -> 0 from the right of -ln(a) is infinite, so the integral has no finite value."),
 dict(q="What is the value of int from 0 to infinity of e^(-x) dx?", choices=[
   "1",
   "0",
   "e",
   "The integral diverges."], ans=0,
   why="The limit of -e^(-b) + 1 as b -> infinity is 1, since e^(-b) tends to 0."),
 dict(q="What is the value of int from 0 to infinity of e^(-2x) dx?", choices=[
   "1/2",
   "1",
   "2",
   "The integral diverges."], ans=0,
   why="An antiderivative is -e^(-2x)/2, and the limit at infinity leaves 1/2."),
 dict(q="What is the value of int from -infinity to 0 of e^x dx?", choices=[
   "1",
   "0",
   "-1",
   "The integral diverges."], ans=0,
   why="The limit as a -> -infinity of 1 - e^a is 1."),
 dict(q="Why must int from 1 to infinity of f(x) dx be written using a limit rather than by substituting infinity into an antiderivative?", choices=[
   "Infinity is not a number, so it cannot be substituted; the limit is what gives the expression meaning",
   "Because antiderivatives do not exist on infinite intervals",
   "Because the Fundamental Theorem applies only to positive functions",
   "Because the integral is always divergent otherwise"], ans=0,
   why="The notation F(infinity) is meaningless; the definition replaces the upper limit with b and takes the limit of the resulting number."),
 dict(q="What is the value of int from 1 to infinity of 1/sqrt(x) dx?", choices=[
   "The integral diverges.",
   "2",
   "1",
   "1/2"], ans=0,
   why="Here p = 1/2, which is not greater than 1, and 2 sqrt(b) - 2 grows without bound."),
 dict(q="What is the value of int from 2 to infinity of 1/x^4 dx?", choices=[
   "1/24",
   "1/12",
   "1/3",
   "The integral diverges."], ans=0,
   why="An antiderivative is -1/(3x^3), and the limit leaves 1/(3 times 8) = 1/24."),
 dict(q="What is the value of int from 0 to 1 of 1/x^2 dx?", choices=[
   "The integral diverges.",
   "1",
   "-1",
   "2"], ans=0,
   why="The integrand is unbounded at 0 and the limit of 1/a - 1 as a -> 0 from the right is infinite; the naive answer -1 is negative for a positive integrand, which is impossible."),
 dict(q="What is the value of int from -infinity to infinity of 1/(1 + x^2) dx?", choices=[
   "pi",
   "pi/2",
   "2pi",
   "The integral diverges."], ans=0,
   why="Splitting at 0, each half contributes pi/2 as a limit of arctangent values."),
 dict(q="What is the value of int from 0 to infinity of 1/(1 + x^2) dx?", choices=[
   "pi/2",
   "pi",
   "1",
   "The integral diverges."], ans=0,
   why="The limit of arctan(b) as b -> infinity is pi/2."),
 dict(q="Which feature makes a definite integral improper?", choices=[
   "an infinite limit of integration, or an integrand unbounded somewhere on the interval",
   "an integrand that changes sign on the interval",
   "an integrand that is not differentiable at an endpoint",
   "limits of integration that are not integers"], ans=0,
   why="Improper means either the interval is infinite or the integrand has an infinite discontinuity in it; sign changes and corners are ordinary."),
 dict(q="What is the value of int from e to infinity of 1/(x (ln(x))^2) dx?", choices=[
   "1",
   "1/2",
   "e",
   "The integral diverges."], ans=0,
   why="With u = ln(x) the integral becomes int from 1 to infinity of 1/u^2 du, which equals 1."),
 dict(q="What is the value of int from 0 to 3 of 1/(x - 1)^2 dx?", choices=[
   "The integral diverges.",
   "-3/2",
   "3/2",
   "1/2"], ans=0,
   why="The integrand is unbounded at x = 1, which lies inside the interval, and the piece from 0 to 1 already diverges; the tidy negative answer comes from ignoring that discontinuity."),
 dict(q="What is the value of int from 0 to 1 of ln(x) dx?", choices=[
   "-1",
   "1",
   "0",
   "The integral diverges."], ans=0,
   why="The antiderivative x ln(x) - x tends to 0 as x -> 0 from the right, so the value is (0 - 1) - 0 = -1."),
 dict(q="What is the value of int from 1 to infinity of x e^(-x^2) dx?", choices=[
   "1/(2e)",
   "1/e",
   "2/e",
   "The integral diverges."], ans=0,
   why="An antiderivative is -e^(-x^2)/2, and the limit at infinity leaves e^(-1)/2."),
 dict(q="What is the value of int from 1 to infinity of x^(-3/2) dx?", choices=[
   "2",
   "1",
   "3/2",
   "The integral diverges."], ans=0,
   why="Here p = 3/2 > 1, and -2/sqrt(b) + 2 tends to 2."),
 dict(q="Suppose 0 <= f(x) <= g(x) for all x >= 1 and int from 1 to infinity of g(x) dx converges. What follows?", choices=[
   "int from 1 to infinity of f(x) dx converges",
   "int from 1 to infinity of f(x) dx diverges",
   "the two integrals are equal",
   "nothing can be concluded"], ans=0,
   why="The comparison test: an accumulation trapped between 0 and a convergent one is increasing and bounded above, so it converges."),
 dict(q="What is the value of int from 0 to infinity of x e^(-x) dx?", choices=[
   "1",
   "0",
   "1/2",
   "The integral diverges."], ans=0,
   why="Integration by parts gives -(x + 1)e^(-x), which tends to 0 at infinity and equals -1 at 0, so the value is 1."),
 dict(q="A student evaluates int from -1 to 1 of 1/x dx as ln|1| - ln|-1| = 0. What is wrong?", choices=[
   "The integrand is unbounded at x = 0, so the integral must be split there, and each piece diverges",
   "The antiderivative should be -1/x^2",
   "The limits should be reversed",
   "Nothing is wrong; the value is 0"], ans=0,
   why="An infinite discontinuity inside the interval makes the integral improper, and a symmetric cancellation argument cannot rescue two divergent halves."),
]
