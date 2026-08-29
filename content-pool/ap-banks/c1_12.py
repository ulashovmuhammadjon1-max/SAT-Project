# CALC 1.12 Confirming Continuity over an Interval — 25 questions
# Intervals are written in plain text, e.g. "(-infinity, 2) and (2, infinity)"
# for a union.  verify_c1_12.py recomputes each function's set of
# discontinuities with sympy (singularities plus domain restrictions) and
# compares it against the interval the key names, so a key that omits or invents
# a break point fails the check.
TOPIC = ("1.12", "Confirming Continuity over an Interval", 1)
QUESTIONS = [
 dict(q="A function f is continuous on the open interval (a, b) when", choices=[
   "f is continuous at every point of (a, b)",
   "f is continuous at a and at b",
   "f is defined at a and at b",
   "f has no maximum on (a, b)"], ans=0,
   why="Continuity on a set is just continuity at each of its points."),
 dict(q="What does it mean for f to be continuous on the closed interval [a, b]?", choices=[
   "f is continuous at every point of (a, b), continuous from the right at a, and continuous from the left at b",
   "f is continuous at every real number",
   "f is continuous at a and at b only",
   "f is defined at every point of [a, b]"], ans=0,
   why="At the endpoints only one side lies in the interval, so the one-sided version of the definition is used there."),
 dict(q="On which set is every polynomial continuous?", choices=[
   "only where the polynomial is positive",
   "all real numbers",
   "only on closed intervals",
   "only at integers"], ans=1,
   why="A polynomial's limit at any point is found by substitution, so the limit always matches the value."),
 dict(q="On which set is f(x) = 1/(x - 2) continuous?", choices=[
   "all real numbers",
   "(-infinity, 2) and (2, infinity)",
   "(2, infinity) only",
   "[2, infinity)"], ans=1,
   why="The only break is where the denominator vanishes, at x = 2."),
 dict(q="At which values of x is f(x) = (x + 1)/((x - 3)(x + 4)) discontinuous?", choices=[
   "x = -1 only", "x = 3 and x = -4", "x = -3 and x = 4", "nowhere"], ans=1,
   why="A rational function breaks exactly where its denominator is 0, which happens at 3 and at -4."),
 dict(q="On which set is f(x) = sqrt(x - 5) continuous?", choices=[
   "all real numbers", "(5, infinity)", "[5, infinity)", "(-infinity, 5]"], ans=2,
   why="The radicand must be nonnegative, and at the left endpoint the function is continuous from the right."),
 dict(q="On which set is f(x) = sqrt(9 - x^2) continuous?", choices=[
   "[-3, 3]", "(-3, 3)", "all real numbers", "[0, 3]"], ans=0,
   why="The radicand 9 - x^2 is nonnegative exactly on [-3, 3], and the endpoints carry one-sided continuity."),
 dict(q="On which set is f(x) = ln(x) continuous?", choices=[
   "all real numbers", "[0, infinity)", "(0, infinity)", "(-infinity, 0)"], ans=2,
   why="The natural logarithm is defined and continuous exactly for positive inputs."),
 dict(q="At which values of x is f(x) = tan(x) discontinuous?", choices=[
   "at every integer",
   "at every odd multiple of pi/2, where cos(x) = 0",
   "at every multiple of pi",
   "nowhere"], ans=1,
   why="tan(x) = sin(x)/cos(x), so it breaks exactly where the cosine vanishes."),
 dict(q="On which set is f(x) = e^x continuous?", choices=[
   "all real numbers", "(0, infinity)", "[0, infinity)", "only where e^x > 1"], ans=0,
   why="The natural exponential function is defined and continuous at every real number."),
 dict(q="A rational function is continuous at exactly which points?", choices=[
   "every real number",
   "every point where its denominator is not 0",
   "every point where its numerator is not 0",
   "only on intervals where it is increasing"], ans=1,
   why="Numerator and denominator are polynomials, so the quotient law applies wherever the denominator's value is not 0."),
 dict(q="On which set is f(x) = 1/(x^2 + 1) continuous?", choices=[
   "all real numbers",
   "(-infinity, -1) and (-1, 1) and (1, infinity)",
   "(-1, 1)",
   "[-1, 1]"], ans=0,
   why="The denominator x^2 + 1 is at least 1 for every real x, so it never vanishes."),
 dict(q="If f and g are both continuous at x = c, which of the following must also be continuous at c?", choices=[
   "f + g", "f/g", "f composed with 1/g", "none of them"], ans=0,
   why="Sums of continuous functions are continuous, while quotients need the extra condition that the denominator is not 0 at c."),
 dict(q="If f and g are continuous at x = c, the quotient f/g is continuous at c provided that", choices=[
   "f(c) is not 0", "g(c) is not 0", "f(c) = g(c)", "both f and g are polynomials"], ans=1,
   why="The quotient law needs a nonzero denominator value, and nothing is required of the numerator."),
 dict(q="If g is continuous at c and f is continuous at g(c), what can be said about the composition f(g(x)) at x = c?", choices=[
   "It is continuous at c",
   "It is discontinuous at c",
   "It is continuous only if f = g",
   "Nothing can be said"], ans=0,
   why="The limit passes inside a continuous outer function, giving f(g(c)) as the limit of the composition."),
 dict(q="Let f(x) = x^2 for 0 <= x <= 2 and f(x) = 4 for 2 < x <= 4. Is f continuous on [0, 4]?", choices=[
   "Yes, because the two rules agree at the seam, where both give 4",
   "No, because the rules are different",
   "No, because f is undefined at 2",
   "No, because the left limit at 2 is 2"], ans=0,
   why="Each piece is continuous on its own part, and at x = 2 the left limit, the right limit, and f(2) are all 4."),
 dict(q="Let g(x) = x + 1 for 0 <= x < 3 and g(x) = 2x for 3 <= x <= 5. Is g continuous on [0, 5]?", choices=[
   "Yes",
   "No, because the left limit at 3 is 4 while g(3) = 6",
   "No, because g is undefined at 3",
   "No, because g is not a polynomial"], ans=1,
   why="Everything is fine except the seam at 3, where the two rules disagree and produce a jump."),
 dict(q="On which set is f(x) = |x| continuous?", choices=[
   "all real numbers",
   "(-infinity, 0) and (0, infinity)",
   "[0, infinity)",
   "only where x is not 0"], ans=0,
   why="The corner at 0 stops the function from being differentiable there but not from being continuous."),
 dict(q="On which set is f(x) = (x^2 - 1)/(x - 1) continuous?", choices=[
   "all real numbers",
   "(-infinity, 1) and (1, infinity)",
   "(-infinity, -1) and (-1, infinity)",
   "(1, infinity)"], ans=1,
   why="The hole at x = 1 is removable, but until it is filled the function is still not continuous there."),
 dict(q="On which set is f(x) = sqrt(x)/(x - 4) continuous?", choices=[
   "[0, 4) and (4, infinity)",
   "(0, 4) and (4, infinity)",
   "[0, infinity)",
   "all real numbers except 4"], ans=0,
   why="The square root requires x >= 0 and the denominator excludes x = 4, and at x = 0 the function is continuous from the right."),
 dict(q="On which set is f(x) = 1/sqrt(x - 1) continuous?", choices=[
   "[1, infinity)", "(1, infinity)", "all real numbers except 1", "(-infinity, 1)"], ans=1,
   why="The radicand must be positive here, since x = 1 would put 0 in the denominator as well as under the root."),
 dict(q="On which set is f(x) = ln(x - 2) continuous?", choices=[
   "all real numbers", "[2, infinity)", "(2, infinity)", "(-infinity, 2)"], ans=2,
   why="The logarithm needs a strictly positive input, so x - 2 > 0."),
 dict(q="At which values of x is f(x) = sin(x)/(x^2 - 4) discontinuous?", choices=[
   "at x = 2 only", "at x = 2 and x = -2", "at every multiple of pi", "nowhere"], ans=1,
   why="The sine in the numerator is continuous everywhere, so the only breaks come from the zeros of x^2 - 4."),
 dict(q="On which set is f(x) = (x - 3)/(x^2 - 9) continuous?", choices=[
   "all real numbers except 3",
   "(-infinity, -3) and (-3, 3) and (3, infinity)",
   "all real numbers except -3",
   "all real numbers"], ans=1,
   why="Both zeros of the denominator break the function; the one at 3 is removable but is still a point of discontinuity until it is filled."),
 dict(q="Which of the following functions is continuous on the entire closed interval [0, 2]?", choices=[
   "f(x) = 1/(x - 1)",
   "f(x) = (x^2 - x)/(x - 1)",
   "f(x) = sqrt(4 - x^2)",
   "f(x) = 1/(x - 2)"], ans=2,
   why="That radicand is nonnegative throughout [0, 2]; the other three each break at a point inside or at the end of the interval."),
]
