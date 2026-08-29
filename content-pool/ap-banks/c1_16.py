# CALC 1.16 Working with the Intermediate Value Theorem — 25 questions
# The hypotheses carry as much weight here as the conclusion, so roughly a third
# of these questions are cases where the IVT does NOT apply: a function with a
# pole inside the interval, a step function, tan(x) across pi/2, and a piecewise
# function that jumps over the target value.  In each of those, the target value
# is genuinely never attained, which verify_c1_16.py confirms rather than
# asserting — an "IVT does not apply" question whose value happens to be
# attained anyway would be misleading.
TOPIC = ("1.16", "Working with the Intermediate Value Theorem", 1)
QUESTIONS = [
 dict(q="The Intermediate Value Theorem states that if f is continuous on [a, b] and k is any number between f(a) and f(b), then", choices=[
   "f(c) = k for exactly one c in (a, b)",
   "there exists at least one c in (a, b) with f(c) = k",
   "f is increasing on (a, b)",
   "k = (f(a) + f(b))/2"], ans=1,
   why="The theorem asserts existence of at least one such c and says nothing about how many there are."),
 dict(q="Which hypothesis must be checked before applying the Intermediate Value Theorem on [a, b]?", choices=[
   "f is differentiable on (a, b)",
   "f is continuous on the closed interval [a, b]",
   "f(a) and f(b) have the same sign",
   "f is a polynomial"], ans=1,
   why="Continuity on the whole closed interval is the only hypothesis, and it is exactly what fails in the cases where the conclusion breaks down."),
 dict(q="When its hypotheses hold, the Intermediate Value Theorem guarantees", choices=[
   "a unique solution",
   "at least one solution, with no information about uniqueness",
   "exactly two solutions",
   "no solutions"], ans=1,
   why="A continuous function may cross a given height many times, so only existence is guaranteed."),
 dict(q="Does the Intermediate Value Theorem tell you the value of c for which f(c) = k?", choices=[
   "Yes, c is always the midpoint of [a, b]",
   "No; it is an existence theorem and provides no method for finding c",
   "Yes, c = k",
   "Yes, whenever f is a polynomial"], ans=1,
   why="The theorem asserts that such a c exists without giving any way to locate it."),
 dict(q="Suppose f is continuous on [1, 4] with f(1) = -2 and f(4) = 5. What does the Intermediate Value Theorem guarantee?", choices=[
   "f has a zero somewhere in (1, 4)",
   "f is increasing on (1, 4)",
   "f(2.5) = 1.5",
   "f has exactly one zero in (1, 4)"], ans=0,
   why="0 lies between -2 and 5, so continuity forces the function to take the value 0 at some interior point."),
 dict(q="For f(x) = x^3 - x - 1 on the interval [1, 2], what does the Intermediate Value Theorem guarantee?", choices=[
   "There is a zero of f in (1, 2), because f(1) = -1 and f(2) = 5",
   "There is no zero of f in (1, 2)",
   "f is negative throughout (1, 2)",
   "Nothing, because f is not continuous"], ans=0,
   why="A polynomial is continuous everywhere and the endpoint values straddle 0."),
 dict(q="For f(x) = x^2 on [-1, 2] and k = 3, what does the Intermediate Value Theorem guarantee?", choices=[
   "Nothing, because 3 is not between f(-1) and f(2)",
   "There is a c in (-1, 2) with f(c) = 3, since f(-1) = 1 and f(2) = 4",
   "There are exactly two such values of c",
   "c must equal 1.5"], ans=1,
   why="3 lies between 1 and 4 and x^2 is continuous, so some c in the interval satisfies c^2 = 3."),
 dict(q="Let f(x) = 1/x on the interval [-1, 1], with f(-1) = -1 and f(1) = 1. Does the Intermediate Value Theorem guarantee a c with f(c) = 0?", choices=[
   "Yes, because 0 lies between -1 and 1",
   "No, because f is not continuous on [-1, 1]; it has an infinite discontinuity at 0, and in fact 1/x is never 0",
   "Yes, and c = 0",
   "No, because 0 is not between -1 and 1"], ans=1,
   why="The hypothesis of continuity on the closed interval fails, and the conclusion genuinely fails too, since 1/x takes no value of 0 anywhere."),
 dict(q="For the greatest integer function on [0, 2] and k = 0.5, does the Intermediate Value Theorem apply?", choices=[
   "Yes, and there is a c with f(c) = 0.5",
   "No; the function jumps at each integer, so it is not continuous on [0, 2], and it never takes a non-integer value",
   "Yes, because the function is defined on all of [0, 2]",
   "No, but a value c with f(c) = 0.5 exists anyway"], ans=1,
   why="Continuity fails at 1, and a step function only ever outputs integers, so no c can give 0.5."),
 dict(q="Consider f(x) = tan(x) on [pi/4, 3pi/4], where f(pi/4) = 1 and f(3pi/4) = -1. Does some c in that interval satisfy f(c) = 0?", choices=[
   "Yes, by the Intermediate Value Theorem",
   "No; tan is undefined at pi/2, so it is not continuous on the interval, and tan(x) = 0 has no solution there",
   "Yes, and c = pi/2",
   "Yes, and c = pi"], ans=1,
   why="The discontinuity at pi/2 breaks the hypothesis, and the zeros of tan are the multiples of pi, none of which lie in this interval."),
 dict(q="Why does the Intermediate Value Theorem apply to every polynomial on every closed interval?", choices=[
   "Because polynomials are increasing",
   "Because polynomials are continuous at every real number",
   "Because polynomials have integer coefficients",
   "Because polynomials are bounded"], ans=1,
   why="The single hypothesis is continuity on the closed interval, and polynomials satisfy it everywhere."),
 dict(q="Suppose f is continuous on [0, 3] with f(0) = 4 and f(3) = 10. Does the Intermediate Value Theorem guarantee a c in (0, 3) with f(c) = 12?", choices=[
   "Yes",
   "No, because 12 is not between 4 and 10",
   "Yes, because f is continuous",
   "No, because f is not differentiable"], ans=1,
   why="The theorem applies only to values k lying between f(a) and f(b), and 12 lies above both."),
 dict(q="With f continuous on [0, 3], f(0) = 4, and f(3) = 10, does the Intermediate Value Theorem guarantee a c in (0, 3) with f(c) = 7?", choices=[
   "Yes, because 7 lies between 4 and 10 and f is continuous on the closed interval",
   "No, because 7 is not the average of 4 and 10",
   "No, because c is not specified",
   "Only if f is increasing"], ans=0,
   why="Both hypotheses hold, so the conclusion follows immediately."),
 dict(q="Suppose f is continuous on [0, 5] with f(0) = 1 and f(5) = 1. Does the Intermediate Value Theorem guarantee a c with f(c) = 3?", choices=[
   "Yes, because f is continuous",
   "No, because 3 does not lie between f(0) and f(5), which are both 1",
   "Yes, and c = 2.5",
   "No, because f might not be defined at 3"], ans=1,
   why="The theorem gives nothing when k lies outside the range spanned by the two endpoint values, even though such a c may happen to exist."),
 dict(q="A continuous function g satisfies g(1) = -5, g(2) = -1, g(3) = 2, and g(4) = 6. On which interval does the Intermediate Value Theorem guarantee a zero of g?", choices=[
   "(1, 2)", "(2, 3)", "(3, 4)", "(1, 4) but no smaller interval"], ans=1,
   why="Only between x = 2 and x = 3 do the tabulated values change sign, from -1 to 2."),
 dict(q="For f(x) = x^3 + 2x - 1 on [0, 1], what does the Intermediate Value Theorem establish?", choices=[
   "f has a zero in (0, 1), because f(0) = -1 and f(1) = 2",
   "f has no zero in (0, 1)",
   "f has exactly three zeros in (0, 1)",
   "Nothing, because f is not continuous at 0"], ans=0,
   why="The polynomial is continuous and its endpoint values straddle 0."),
 dict(q="For f(x) = e^x + x on the interval [-1, 0], what does the Intermediate Value Theorem establish?", choices=[
   "f has a zero in (-1, 0), because f(-1) is negative and f(0) = 1 is positive",
   "f has no zero in (-1, 0)",
   "f is negative throughout (-1, 0)",
   "Nothing, because e^x is not continuous"], ans=0,
   why="f(-1) = 1/e - 1 is about -0.632 and f(0) = 1, so a continuous function must cross 0 between them."),
 dict(q="For f(x) = cos(x) - x on [0, 1], what does the Intermediate Value Theorem establish?", choices=[
   "The equation cos(x) = x has a solution in (0, 1), because f(0) = 1 and f(1) is negative",
   "The equation cos(x) = x has no solution",
   "cos(x) > x throughout (0, 1)",
   "Nothing, because cos is not continuous"], ans=0,
   why="f(1) = cos(1) - 1 is about -0.460 while f(0) = 1, so the continuous difference must be 0 somewhere between."),
 dict(q="If there is a c in (a, b) with f(c) = k, does it follow that f is continuous on [a, b]?", choices=[
   "Yes, that is the converse of the Intermediate Value Theorem",
   "No; a discontinuous function can still attain the value k, so attaining a value says nothing about continuity",
   "Yes, provided k is between f(a) and f(b)",
   "Only if f is a polynomial"], ans=1,
   why="The theorem runs one way only, from continuity to the existence of c, and the converse is false."),
 dict(q="Let f(x) = x - 2 for 0 <= x < 1 and f(x) = x for 1 <= x <= 2, so that f(0) = -2 and f(2) = 2. Is there a c in (0, 2) with f(c) = 0?", choices=[
   "Yes, by the Intermediate Value Theorem",
   "No; f jumps from just under -1 to 1 at x = 1, skipping 0 entirely, and the theorem does not apply because f is discontinuous there",
   "Yes, and c = 1",
   "Yes, and c = 2"], ans=1,
   why="On the left piece the values stay below -1 and on the right piece they stay at or above 1, so the value 0 is never attained."),
 dict(q="How many solutions of f(x) = k does the Intermediate Value Theorem guarantee when its hypotheses are satisfied?", choices=[
   "exactly one", "at least one", "exactly two", "at most one"], ans=1,
   why="Existence is all the theorem provides; a continuous function may hit the value k many times."),
 dict(q="The Intermediate Value Theorem shows that f(x) = x^5 + x - 3 has at least one zero in (1, 2). What additional fact would establish that the zero is unique?", choices=[
   "that f is a polynomial",
   "that f is strictly increasing on the interval, so it can take any value at most once",
   "that f(1) and f(2) have opposite signs",
   "that f is continuous"], ans=1,
   why="Strict monotonicity rules out a second crossing, which existence alone cannot do."),
 dict(q="Suppose f is continuous on [2, 6] with f(2) = -3 and f(6) = 8. Which statement must be true?", choices=[
   "f(c) = 0 for some c in (2, 6)",
   "f is increasing on (2, 6)",
   "f(4) = 2.5",
   "f has exactly one zero in (2, 6)"], ans=0,
   why="0 lies between -3 and 8, so the theorem forces a zero, while nothing forces monotonicity, a particular value, or uniqueness."),
 dict(q="A function h is defined on [0, 2] with h(0) = -1 and h(2) = 1, but h has a jump discontinuity at x = 1. Must h take the value 0 somewhere on (0, 2)?", choices=[
   "Yes, because the endpoint values straddle 0",
   "Not necessarily; without continuity the graph can jump across 0 without ever attaining it",
   "Yes, because h is defined on all of [0, 2]",
   "No, it is impossible for h to take the value 0"], ans=1,
   why="Continuity is what forbids skipping a value, and such an h may or may not hit 0, so nothing is guaranteed."),
 dict(q="Which of the following is the best statement of what must be verified before citing the Intermediate Value Theorem to conclude that f has a zero on [a, b]?", choices=[
   "that f is continuous on [a, b] and that f(a) and f(b) have opposite signs",
   "that f is differentiable on (a, b) and f(a) < f(b)",
   "that f(a) and f(b) have the same sign",
   "that f is defined at a and at b"], ans=0,
   why="Opposite signs place 0 strictly between the endpoint values, and continuity on the closed interval is the theorem's hypothesis."),
]
