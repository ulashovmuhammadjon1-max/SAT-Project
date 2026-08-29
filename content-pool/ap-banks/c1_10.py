# CALC 1.10 Exploring Types of Discontinuities — 25 questions
# Classifications verified with sympy; see verify_c1_10.py, which decides each
# type from the two one-sided limits and the function's value rather than
# trusting the label written here.
# The three types are used in their standard senses: removable when the
# two-sided limit exists but the function's value there is different or missing;
# jump when both one-sided limits exist finitely but differ; infinite when at
# least one one-sided limit is +/- infinity.
TOPIC = ("1.10", "Exploring Types of Discontinuities", 1)
QUESTIONS = [
 dict(q="A function f has a removable discontinuity at x = c when", choices=[
   "lim as x -> c of f(x) exists but either f(c) is undefined or f(c) differs from that limit",
   "the one-sided limits at c exist and are different",
   "at least one one-sided limit at c is infinite",
   "f is undefined on an interval around c"], ans=0,
   why="The break is a single misplaced or missing point, which is exactly what redefining f(c) would repair."),
 dict(q="A jump discontinuity at x = c is characterized by the condition that", choices=[
   "the two-sided limit exists but f(c) does not",
   "both one-sided limits at c exist and are finite but are not equal to each other",
   "both one-sided limits at c are infinite",
   "f is continuous from the left but not defined at c"], ans=1,
   why="Two different finite approach heights make the graph step from one level to another at c."),
 dict(q="An infinite discontinuity at x = c occurs when", choices=[
   "f(c) is a very large number",
   "at least one of the one-sided limits at c is infinite, so the graph has a vertical asymptote at x = c",
   "the two one-sided limits differ by a finite amount",
   "f is undefined at exactly one point"], ans=1,
   why="Unbounded behavior on at least one side is what produces a vertical asymptote."),
 dict(q="The function f(x) = (x^2 - 4)/(x - 2) has which type of discontinuity at x = 2?", choices=[
   "removable", "jump", "infinite", "no discontinuity"], ans=0,
   why="Away from 2 the function equals x + 2, so the limit is 4 while f(2) is undefined, and defining f(2) = 4 would repair it."),
 dict(q="The function f(x) = 1/(x - 3) has which type of discontinuity at x = 3?", choices=[
   "removable", "jump", "infinite", "no discontinuity"], ans=2,
   why="The one-sided limits are -infinity and infinity, giving a vertical asymptote at x = 3."),
 dict(q="The function f(x) = |x|/x has which type of discontinuity at x = 0?", choices=[
   "removable", "jump", "infinite", "no discontinuity"], ans=1,
   why="The one-sided limits are -1 and 1, both finite and unequal, which is a jump."),
 dict(q="For f(x) = (x - 1)/(x^2 - 1), the discontinuity at x = 1 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=0,
   why="Cancelling x - 1 leaves 1/(x + 1), so the limit at 1 is 1/2 while f(1) is undefined."),
 dict(q="For the same function f(x) = (x - 1)/(x^2 - 1), the discontinuity at x = -1 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=2,
   why="After cancelling, the function behaves like 1/(x + 1) near -1, which is unbounded on both sides."),
 dict(q="Let f(x) = x^2 for x < 2 and f(x) = x + 3 for x >= 2. The discontinuity at x = 2 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=1,
   why="The left limit is 4 and the right limit is 5, both finite and different."),
 dict(q="Let f(x) = x + 1 for x not equal to 3, with f(3) = 7. The discontinuity at x = 3 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=0,
   why="The limit is 4 but the assigned value is 7, so redefining f(3) as 4 would repair the graph."),
 dict(q="The function f(x) = (x^2 - x - 6)/(x - 3) has a removable discontinuity at x = 3. What value should be assigned to f(3) to remove it?", choices=[
   "-2", "0", "3", "5"], ans=3,
   why="The numerator factors as (x - 3)(x + 2), so the limit is 3 + 2 = 5."),
 dict(q="The function f(x) = tan(x) has which type of discontinuity at x = pi/2?", choices=[
   "removable", "jump", "infinite", "no discontinuity"], ans=2,
   why="tan(x) = sin(x)/cos(x) and the denominator vanishes at pi/2 while the numerator does not, so the values are unbounded."),
 dict(q="The function f(x) = 1/x^2 has which type of discontinuity at x = 0?", choices=[
   "removable", "jump", "infinite", "no discontinuity"], ans=2,
   why="Both one-sided limits are infinity, which is still an infinite discontinuity."),
 dict(q="The function f(x) = sin(1/x), with f(0) defined to be 0, has a discontinuity at x = 0 that is", choices=[
   "removable", "jump", "infinite", "none of removable, jump, or infinite, because the values oscillate without approaching anything"], ans=3,
   why="Neither one-sided limit exists, finitely or infinitely, so the break fits none of the three standard categories."),
 dict(q="For f(x) = (x^2 - 9)/(x^2 - 3x), the discontinuity at x = 3 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=0,
   why="The expression reduces to (x + 3)/x, which is defined and equal to 2 at x = 3, so only the single point is missing."),
 dict(q="For the same function f(x) = (x^2 - 9)/(x^2 - 3x), the discontinuity at x = 0 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=2,
   why="After reducing to (x + 3)/x the numerator approaches 3 while the denominator approaches 0, so the values are unbounded."),
 dict(q="Which type of discontinuity can always be eliminated by redefining the function at a single point?", choices=[
   "removable", "jump", "infinite", "all three types"], ans=0,
   why="Only a removable discontinuity has a two-sided limit available to assign as the new value."),
 dict(q="Which of the following functions has a jump discontinuity at x = 0?", choices=[
   "f(x) = x^2/x",
   "f(x) = 1/x",
   "f(x) = x/|x|",
   "f(x) = x sin(1/x) with f(0) = 0"], ans=2,
   why="That quotient equals -1 for x < 0 and 1 for x > 0, giving two different finite one-sided limits."),
 dict(q="The greatest integer function, which rounds each input down to the nearest integer, has which type of discontinuity at every integer?", choices=[
   "removable", "jump", "infinite", "no discontinuity"], ans=1,
   why="At an integer n the function approaches n - 1 from the left and n from the right, a step of exactly 1."),
 dict(q="For f(x) = (x + 2)/(x^2 - 4), the discontinuity at x = -2 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=0,
   why="Cancelling x + 2 leaves 1/(x - 2), which is defined and equal to -1/4 at x = -2."),
 dict(q="For f(x) = (x^2 - 5x + 6)/(x^2 - 4), the discontinuity at x = 2 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=0,
   why="Both parts carry the factor x - 2, leaving (x - 3)/(x + 2), which is defined and equal to -1/4 at x = 2."),
 dict(q="For that same function f(x) = (x^2 - 5x + 6)/(x^2 - 4), the discontinuity at x = -2 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=2,
   why="After cancelling, the numerator approaches -5 at x = -2 while the denominator approaches 0, so the values are unbounded."),
 dict(q="Why can a jump discontinuity never be removed by redefining the function at the single point x = c?", choices=[
   "Because f(c) is always undefined at a jump",
   "Because no single value can equal two different one-sided limits at once, so the two-sided limit still fails to exist",
   "Because the function is unbounded there",
   "Because jump discontinuities occur only at integers"], ans=1,
   why="Removal requires a two-sided limit to assign, and at a jump the two-sided limit does not exist no matter what value is chosen."),
 dict(q="For f(x) = |x - 1|/(x^2 - 1), the discontinuity at x = 1 is", choices=[
   "removable", "jump", "infinite", "not a discontinuity"], ans=1,
   why="For x > 1 the expression is 1/(x + 1), approaching 1/2, while for x < 1 it is -1/(x + 1), approaching -1/2."),
 dict(q="The function f(x) = (x^2 - 1)/(x^3 - x) is discontinuous at three points. How many of those discontinuities are removable?", choices=[
   "0", "1", "2", "3"], ans=2,
   why="The expression reduces to 1/x, so x = 1 and x = -1 are removable holes while x = 0 is an infinite discontinuity."),
]
