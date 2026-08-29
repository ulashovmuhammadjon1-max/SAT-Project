# CALC 1.13 Removing Discontinuities — 25 questions
# Two families run through this topic: assigning the limit as the missing value
# at a removable hole, and solving for a parameter that makes the two branches
# of a piecewise function meet.  Both are staples, so both appear several times
# with different structures.
# Verified with sympy; see verify_c1_13.py, which solves each seam equation
# independently and confirms the resulting function really is continuous.
TOPIC = ("1.13", "Removing Discontinuities", 1)
QUESTIONS = [
 dict(q="To remove a removable discontinuity of f at x = c means to", choices=[
   "delete the point x = c from the domain",
   "define or redefine f(c) to be the value of lim as x -> c of f(x)",
   "change the formula for f on an interval around c",
   "show that f has no limit at c"], ans=1,
   why="The limit already exists, so assigning it as the value makes the limit and the value agree, which is continuity."),
 dict(q="Which type of discontinuity can be removed by redefining the function at a single point?", choices=[
   "a jump discontinuity", "an infinite discontinuity", "a removable discontinuity", "any discontinuity"], ans=2,
   why="Only a removable discontinuity has a two-sided limit available to assign as the new value."),
 dict(q="Let f(x) = (x^2 - 16)/(x - 4) for x not equal to 4 and f(4) = k. What value of k makes f continuous at x = 4?", choices=[
   "0", "4", "8", "16"], ans=2,
   why="Away from 4 the function equals x + 4, whose limit at 4 is 8."),
 dict(q="Let f(x) = (x^2 - x - 12)/(x - 4) for x not equal to 4 and f(4) = k. What value of k makes f continuous at x = 4?", choices=[
   "-3", "0", "4", "7"], ans=3,
   why="The numerator factors as (x - 4)(x + 3), so the limit is 4 + 3 = 7."),
 dict(q="Let f(x) = (x^3 - 8)/(x - 2) for x not equal to 2 and f(2) = k. What value of k makes f continuous at x = 2?", choices=[
   "0", "4", "8", "12"], ans=3,
   why="Factoring the difference of cubes leaves x^2 + 2x + 4, whose value at 2 is 4 + 4 + 4 = 12."),
 dict(q="Let f(x) = (x - 2)/(x^2 - 4) for x not equal to 2 and f(2) = k. What value of k makes f continuous at x = 2?", choices=[
   "0", "1/4", "1/2", "4"], ans=1,
   why="Cancelling x - 2 leaves 1/(x + 2), whose value at 2 is 1/4."),
 dict(q="Let f(x) = (x^2 - 5x + 6)/(x^2 - 4) for x not equal to 2 and f(2) = k. What value of k makes f continuous at x = 2?", choices=[
   "-1/4", "0", "1/4", "1"], ans=0,
   why="Both parts carry the factor x - 2, leaving (x - 3)/(x + 2), whose value at 2 is -1/4."),
 dict(q="Let f(x) = (x^2 + 2x - 3)/(x^2 - 1) for x not equal to 1 and f(1) = k. What value of k makes f continuous at x = 1?", choices=[
   "0", "1", "2", "4"], ans=2,
   why="Cancelling x - 1 leaves (x + 3)/(x + 1), whose value at 1 is 4/2 = 2."),
 dict(q="Let f(x) = (sqrt(x) - 3)/(x - 9) for x not equal to 9 and f(9) = k. What value of k makes f continuous at x = 9?", choices=[
   "1/6", "1/3", "3", "6"], ans=0,
   why="Writing x - 9 = (sqrt(x) - 3)(sqrt(x) + 3) leaves 1/(sqrt(x) + 3), whose value at 9 is 1/6."),
 dict(q="Let f(x) = (sqrt(x + 4) - 2)/x for x not equal to 0 and f(0) = k. What value of k makes f continuous at x = 0?", choices=[
   "0", "1/4", "1/2", "2"], ans=1,
   why="The conjugate leaves 1/(sqrt(x + 4) + 2), whose value at 0 is 1/4."),
 dict(q="Let f(x) = sin(3x)/x for x not equal to 0 and f(0) = k. What value of k makes f continuous at x = 0?", choices=[
   "0", "1", "3", "1/3"], ans=2,
   why="Writing it as 3 sin(3x)/(3x) and using that sin(u)/u approaches 1 gives a limit of 3."),
 dict(q="Let f(x) = (1 - cos(x))/x for x not equal to 0 and f(0) = k. What value of k makes f continuous at x = 0?", choices=[
   "-1", "0", "1/2", "1"], ans=1,
   why="The numerator behaves like x^2/2 near 0, so after dividing by x the limit is 0."),
 dict(q="Let f(x) = (e^x - 1)/x for x not equal to 0 and f(0) = k. What value of k makes f continuous at x = 0?", choices=[
   "0", "1", "e", "e - 1"], ans=1,
   why="The quotient (e^u - 1)/u approaches 1 as u approaches 0."),
 dict(q="Let f(x) = tan(x)/x for x not equal to 0 and f(0) = k. What value of k makes f continuous at x = 0?", choices=[
   "0", "1", "pi", "the function cannot be made continuous"], ans=1,
   why="tan(x)/x = (sin(x)/x)(1/cos(x)), and both factors approach 1."),
 dict(q="Let f(x) = x^2 for x < 2 and f(x) = kx for x >= 2. What value of k makes f continuous at x = 2?", choices=[
   "1", "2", "4", "8"], ans=1,
   why="The left limit is 4 and the right value is 2k, so 2k = 4 gives k = 2."),
 dict(q="Let f(x) = kx + 1 for x <= 3 and f(x) = x^2 + 1 for x > 3. What value of k makes f continuous at x = 3?", choices=[
   "1", "2", "3", "10"], ans=2,
   why="Matching 3k + 1 to the right-hand limit 10 gives 3k = 9, so k = 3."),
 dict(q="Let f(x) = 3x + a for x < 1 and f(x) = x^2 + 2 for x >= 1. What value of a makes f continuous at x = 1?", choices=[
   "-3", "0", "2", "3"], ans=1,
   why="The left limit is 3 + a and the right value is 3, so a = 0."),
 dict(q="Let f(x) = a*x^2 for x < 2 and f(x) = x + 10 for x >= 2. What value of a makes f continuous at x = 2?", choices=[
   "1", "2", "3", "6"], ans=2,
   why="The left limit is 4a and the right value is 12, so 4a = 12 gives a = 3."),
 dict(q="Let f(x) = 2x + b for x <= -1 and f(x) = x^2 for x > -1. What value of b makes f continuous at x = -1?", choices=[
   "-3", "-1", "1", "3"], ans=3,
   why="The value at -1 is -2 + b and the right-hand limit is 1, so b = 3."),
 dict(q="Let f(x) = c*x^2 + 1 for x <= 1 and f(x) = 4x - c for x > 1. What value of c makes f continuous at x = 1?", choices=[
   "1/2", "1", "3/2", "3"], ans=2,
   why="Matching c + 1 to 4 - c gives 2c = 3, so c = 3/2."),
 dict(q="Let f(x) = |x - 3|/(x - 3) for x not equal to 3 and f(3) = k. Which value of k makes f continuous at x = 3?", choices=[
   "-1", "0", "1", "no value of k makes f continuous at 3"], ans=3,
   why="The one-sided limits are -1 and 1, so the two-sided limit does not exist and no single value can match both sides."),
 dict(q="Let f(x) = x^2 for x < 1, f(x) = ax + b for 1 <= x < 2, and f(x) = 6 for x >= 2. What is the value of a that makes f continuous everywhere?", choices=[
   "1", "3", "5", "6"], ans=2,
   why="Continuity at 1 gives a + b = 1 and continuity at 2 gives 2a + b = 6; subtracting yields a = 5."),
 dict(q="For that same three-piece function, with f(x) = x^2 for x < 1, f(x) = ax + b for 1 <= x < 2, and f(x) = 6 for x >= 2, what is b?", choices=[
   "-4", "-1", "1", "4"], ans=0,
   why="With a = 5, the equation a + b = 1 gives b = -4."),
 dict(q="Let a be a constant and let f(x) = (x^2 - a^2)/(x - a) for x not equal to a, with f(a) = k. In terms of a, what value of k makes f continuous at x = a?", choices=[
   "0", "a", "2a", "a^2"], ans=2,
   why="The numerator factors as (x - a)(x + a), leaving x + a, whose value at a is 2a."),
 dict(q="After f(x) = (x^2 - 1)/(x - 1) is redefined so that f(1) = 2, is the resulting function continuous at every real number?", choices=[
   "Yes, because the only discontinuity was the hole at x = 1 and it has now been filled",
   "No, because the original formula is still undefined at 1",
   "No, because there is another discontinuity at x = -1",
   "No, because a redefined function is never continuous"], ans=0,
   why="Away from 1 the function agrees with the polynomial x + 1, which is continuous everywhere, and the single hole has been filled with its limit."),
]
