# CALC 1.8 Determining Limits Using the Squeeze Theorem — 25 questions
# Limits verified with sympy; see verify_c1_8.py.  For the questions that supply
# bounds rather than a formula for f, the verifier confirms that the two bounds
# really do have a common limit (and, where the bounds are claimed to hold for
# all x, that the inequality between them is genuinely true), which is what makes
# the squeeze conclusion valid.
TOPIC = ("1.8", "Determining Limits Using the Squeeze Theorem", 1)
QUESTIONS = [
 dict(q="The squeeze theorem states that if g(x) <= f(x) <= h(x) for all x near c (except possibly at c) and lim as x -> c of g(x) = lim as x -> c of h(x) = L, then", choices=[
   "f(c) = L",
   "lim as x -> c of f(x) = L",
   "f is continuous at c",
   "g(x) = h(x) for all x"], ans=1,
   why="Trapping f between two functions that converge to the same value forces f to converge to that value too."),
 dict(q="Which set of conditions is required before the squeeze theorem may be applied to conclude something about f at x = c?", choices=[
   "f must be continuous at c",
   "g(x) <= f(x) <= h(x) must hold near c, and g and h must have the same limit at c",
   "f must be differentiable near c",
   "g and h must be polynomials"], ans=1,
   why="The theorem needs only the trapping inequality near c and a shared limit for the two bounding functions."),
 dict(q="Suppose g(x) <= f(x) <= h(x) near c, with lim as x -> c of g(x) = 2 and lim as x -> c of h(x) = 3. What does the squeeze theorem allow one to conclude about lim as x -> c of f(x)?", choices=[
   "The limit is 2",
   "The limit is 3",
   "The limit is 2.5",
   "Nothing, because the two bounding limits are not equal"], ans=3,
   why="The theorem applies only when the outer functions share a single limit; here they do not, so the trap is too loose."),
 dict(q="To apply the squeeze theorem at x = c, the function f", choices=[
   "must be defined at c",
   "need not be defined at c, since the inequality is only needed for x near c but not equal to c",
   "must equal g at c",
   "must be increasing near c"], ans=1,
   why="Like every limit statement, the conclusion concerns behavior near c and never requires a value at c."),
 dict(q="Which inequality correctly traps f(x) = x^2 sin(1/x) for x not equal to 0?", choices=[
   "-1 <= x^2 sin(1/x) <= 1",
   "-x^2 <= x^2 sin(1/x) <= x^2",
   "0 <= x^2 sin(1/x) <= x^2",
   "-x <= x^2 sin(1/x) <= x"], ans=1,
   why="Since sin(1/x) lies between -1 and 1 and x^2 is nonnegative, multiplying the inequality by x^2 gives bounds of -x^2 and x^2."),
 dict(q="Evaluate lim as x -> 0 of x^2 sin(1/x).", choices=[
   "0", "1", "does not exist because sin(1/x) oscillates", "infinity"], ans=0,
   why="The bounds -x^2 and x^2 both approach 0, so the squeeze theorem gives 0."),
 dict(q="Evaluate lim as x -> 0 of x cos(1/x).", choices=[
   "-1", "0", "1", "does not exist"], ans=1,
   why="Since -|x| <= x cos(1/x) <= |x| and both bounds approach 0, the limit is 0."),
 dict(q="Evaluate lim as x -> 0 of x^4 cos(2/x).", choices=[
   "0", "1", "2", "does not exist"], ans=0,
   why="The cosine factor stays within [-1, 1], so the product is trapped between -x^4 and x^4, both approaching 0."),
 dict(q="Suppose 3x <= f(x) <= x^3 + 2 for all x near 1. What is lim as x -> 1 of f(x)?", choices=[
   "1", "2", "3", "it cannot be determined"], ans=2,
   why="Both bounds approach 3 at x = 1, so the squeeze theorem pins the limit at 3."),
 dict(q="If 2x - 1 <= f(x) <= x^2 for all x near 1, then lim as x -> 1 of f(x) equals", choices=[
   "0", "1", "2", "it cannot be determined"], ans=1,
   why="Both bounds approach 1 at x = 1, and the gap x^2 - (2x - 1) = (x - 1)^2 is never negative, so the trap is valid and the limit is 1."),
 dict(q="It is known that 1 - x^2/6 <= sin(x)/x <= 1 for all x near 0 with x not equal to 0. What does this establish?", choices=[
   "lim as x -> 0 of sin(x)/x = 0",
   "lim as x -> 0 of sin(x)/x = 1",
   "lim as x -> 0 of sin(x)/x does not exist",
   "sin(x)/x is continuous at 0"], ans=1,
   why="Both bounds approach 1 as x approaches 0, so the quotient is squeezed to 1."),
 dict(q="Evaluate lim as x -> 0^+ of sqrt(x) sin(1/x).", choices=[
   "0", "1", "infinity", "does not exist"], ans=0,
   why="For x > 0 the product lies between -sqrt(x) and sqrt(x), and both bounds approach 0."),
 dict(q="Evaluate lim as x -> infinity of sin(x)/x.", choices=[
   "-1", "0", "1", "does not exist because sin(x) keeps oscillating"], ans=1,
   why="The quotient is trapped between -1/x and 1/x, and both approach 0 as x grows."),
 dict(q="Evaluate lim as x -> infinity of cos(x)/x^2.", choices=[
   "0", "1", "infinity", "does not exist"], ans=0,
   why="The bounds -1/x^2 and 1/x^2 both approach 0."),
 dict(q="Evaluate lim as x -> 0 of x^2 (3 + sin(1/x)).", choices=[
   "0", "2", "3", "4"], ans=0,
   why="The factor 3 + sin(1/x) stays between 2 and 4, so the product is trapped between 2x^2 and 4x^2, both approaching 0."),
 dict(q="Suppose |f(x) - 5| <= 2|x - 3| for every real x. What is lim as x -> 3 of f(x)?", choices=[
   "0", "2", "3", "5"], ans=3,
   why="The inequality traps f between 5 - 2|x - 3| and 5 + 2|x - 3|, and both bounds approach 5."),
 dict(q="If |f(x)| <= x^2 for every real x, then lim as x -> 0 of f(x) equals", choices=[
   "0", "1", "2", "it cannot be determined"], ans=0,
   why="The inequality means -x^2 <= f(x) <= x^2, and both bounds approach 0."),
 dict(q="Suppose -x^2 <= f(x) <= x^2 holds for every real x. Which statement must be true?", choices=[
   "f(0) = 0 and lim as x -> 0 of f(x) = 0",
   "f(0) = 1 and lim as x -> 0 of f(x) = 0",
   "f is constant",
   "nothing can be concluded about f(0)"], ans=0,
   why="At x = 0 the inequality reads 0 <= f(0) <= 0, forcing f(0) = 0, and the same bounds squeeze the limit to 0."),
 dict(q="Evaluate lim as x -> 0 of x^3 cos(1/x^2).", choices=[
   "-1", "0", "1", "does not exist"], ans=1,
   why="The product lies between -|x|^3 and |x|^3, both of which approach 0."),
 dict(q="Evaluate lim as x -> 2 of (x - 2)^2 sin(1/(x - 2)).", choices=[
   "0", "1", "2", "does not exist"], ans=0,
   why="The squared factor drives the bounds -(x - 2)^2 and (x - 2)^2 to 0 while the sine factor stays bounded."),
 dict(q="Assume g(x) <= f(x) <= h(x) for every real x, with lim as x -> 4 of g(x) = 7 and lim as x -> 4 of h(x) = 7, while f(4) = 100. What is lim as x -> 4 of f(x)?", choices=[
   "7", "53.5", "100", "it cannot be determined"], ans=0,
   why="The squeeze theorem gives 7; the value f(4) = 100 is irrelevant to the limit, though it does mean f is not continuous at 4."),
 dict(q="For which of the following functions does the squeeze theorem fail to establish a limit as x approaches 0?", choices=[
   "x^2 sin(1/x)", "x cos(1/x)", "sin(1/x)", "x^3 sin(1/x)"], ans=2,
   why="Without a factor shrinking to 0 the only available bounds are the constants -1 and 1, which do not share a limit, and in fact that limit does not exist."),
 dict(q="Evaluate lim as x -> infinity of (2x + sin(x))/x.", choices=[
   "0", "1", "2", "does not exist"], ans=2,
   why="The expression equals 2 + sin(x)/x, and sin(x)/x is squeezed to 0, leaving 2."),
 dict(q="Evaluate lim as x -> 0 of x^2 e^(sin(1/x)).", choices=[
   "0", "1", "e", "does not exist"], ans=0,
   why="Since sin(1/x) lies in [-1, 1], the exponential factor lies between 1/e and e, so the product is trapped between x^2/e and e x^2, both approaching 0."),
 dict(q="Suppose 2x <= f(x) <= x^2 + 1 for every real x. What is lim as x -> 1 of f(x)?", choices=[
   "0", "1", "2", "it cannot be determined"], ans=2,
   why="The two bounds meet only at x = 1, where both equal 2, so the squeeze theorem gives 2 there."),
]
