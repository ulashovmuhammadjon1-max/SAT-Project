# CALC 1.6 Determining Limits Using Algebraic Manipulation — 25 questions
# Every limit is confirmed with sympy; see verify_c1_6.py.  Questions 5, 11 and
# 25 ask which manipulation to reach for rather than for a value, and question
# 20 asks about a limit that fails to exist; those carry the reasoning in `why`.
TOPIC = ("1.6", "Determining Limits Using Algebraic Manipulation", 1)
QUESTIONS = [
 dict(q="Evaluate lim as x -> 5 of (x^2 - 25)/(x - 5).", choices=[
   "0", "5", "10", "the limit does not exist"], ans=2,
   why="Factoring gives (x - 5)(x + 5)/(x - 5) = x + 5 for x not equal to 5, which approaches 10."),
 dict(q="Evaluate lim as x -> -3 of (x^2 + x - 6)/(x + 3).", choices=[
   "-5", "-1", "1", "5"], ans=0,
   why="The numerator factors as (x + 3)(x - 2), so the expression reduces to x - 2, which approaches -5."),
 dict(q="Evaluate lim as x -> 1 of (x^2 - 3x + 2)/(x^2 - 1).", choices=[
   "-1/2", "0", "1/2", "the limit does not exist"], ans=0,
   why="Both parts carry a factor of x - 1, leaving (x - 2)/(x + 1), which approaches -1/2."),
 dict(q="Evaluate lim as x -> 4 of (x - 4)/(x^2 - 16).", choices=[
   "0", "1/8", "1/4", "8"], ans=1,
   why="The denominator factors as (x - 4)(x + 4), leaving 1/(x + 4), which approaches 1/8."),
 dict(q="When evaluating lim as x -> 3 of (x^2 - 9)/(x - 3), cancelling the factor x - 3 from the numerator and denominator is legitimate because", choices=[
   "the two functions are equal everywhere",
   "the limit depends only on values of x near 3 with x not equal to 3, and there the factor x - 3 is not zero",
   "cancelling never changes a function",
   "the limit of the denominator is not 0"], ans=1,
   why="The limit process deliberately excludes x = 3, and away from 3 the cancelled expression agrees with the original."),
 dict(q="Evaluate lim as x -> 0 of (sqrt(x + 4) - 2)/x.", choices=[
   "0", "1/4", "1/2", "the limit does not exist"], ans=1,
   why="Multiplying by the conjugate gives x/(x(sqrt(x + 4) + 2)) = 1/(sqrt(x + 4) + 2), which approaches 1/4."),
 dict(q="Evaluate lim as x -> 9 of (x - 9)/(sqrt(x) - 3).", choices=[
   "0", "1/6", "3", "6"], ans=3,
   why="Writing x - 9 = (sqrt(x) - 3)(sqrt(x) + 3) leaves sqrt(x) + 3, which approaches 6."),
 dict(q="Evaluate lim as x -> 0 of (sqrt(1 + x) - sqrt(1 - x))/x.", choices=[
   "0", "1/2", "1", "2"], ans=2,
   why="The conjugate turns the numerator into 2x, leaving 2/(sqrt(1 + x) + sqrt(1 - x)), which approaches 2/2 = 1."),
 dict(q="Evaluate lim as x -> 0 of (1/(x + 3) - 1/3)/x.", choices=[
   "-1/9", "-1/3", "1/9", "1/3"], ans=0,
   why="Combining over the common denominator 3(x + 3) gives -x/(3x(x + 3)) = -1/(3(x + 3)), which approaches -1/9."),
 dict(q="Evaluate lim as x -> 2 of (1/x - 1/2)/(x - 2).", choices=[
   "-1/2", "-1/4", "1/4", "1/2"], ans=1,
   why="The numerator becomes (2 - x)/(2x), so the quotient is -1/(2x), which approaches -1/4."),
 dict(q="Which algebraic step is the most useful first move in evaluating lim as x -> 0 of (1/(x + 4) - 1/4)/x?", choices=[
   "Multiply the numerator and denominator by the conjugate",
   "Combine the two fractions in the numerator over a common denominator, then cancel the factor of x",
   "Substitute x = 0 directly",
   "Expand (x + 4)^2"], ans=1,
   why="A difference of fractions over x is cleared by combining the numerator into a single fraction, which exposes the cancelling factor of x."),
 dict(q="Evaluate lim as x -> 3 of (x^3 - 27)/(x - 3).", choices=[
   "3", "9", "18", "27"], ans=3,
   why="Factoring the difference of cubes leaves x^2 + 3x + 9, which approaches 9 + 9 + 9 = 27."),
 dict(q="Evaluate lim as x -> -2 of (x^3 + 8)/(x + 2).", choices=[
   "-12", "0", "4", "12"], ans=3,
   why="The sum of cubes factors as (x + 2)(x^2 - 2x + 4), leaving x^2 - 2x + 4, which approaches 4 + 4 + 4 = 12."),
 dict(q="Evaluate lim as x -> 1 of (x^4 - 1)/(x - 1).", choices=[
   "1", "2", "4", "the limit does not exist"], ans=2,
   why="Dividing out x - 1 leaves x^3 + x^2 + x + 1, which approaches 4."),
 dict(q="Evaluate lim as x -> 0 of sin(2x)/x.", choices=[
   "0", "1/2", "1", "2"], ans=3,
   why="Writing sin(2x)/x = 2 * sin(2x)/(2x) and using that sin(u)/u approaches 1 gives 2."),
 dict(q="Evaluate lim as x -> 0 of sin(3x)/sin(5x).", choices=[
   "0", "3/5", "1", "5/3"], ans=1,
   why="Dividing numerator and denominator by x gives (3 sin(3x)/(3x))/(5 sin(5x)/(5x)), which approaches 3/5."),
 dict(q="Evaluate lim as x -> 0 of (1 - cos(x))/x^2.", choices=[
   "-1/2", "0", "1/2", "1"], ans=2,
   why="Multiplying by (1 + cos(x))/(1 + cos(x)) gives sin^2(x)/(x^2(1 + cos(x))), which approaches 1/2."),
 dict(q="Evaluate lim as x -> 0 of tan(x)/(3x).", choices=[
   "0", "1/3", "1", "3"], ans=1,
   why="tan(x)/x approaches 1, so dividing by the constant 3 leaves 1/3."),
 dict(q="Evaluate lim as x -> 4 of (2 - sqrt(x))/(4 - x).", choices=[
   "0", "1/4", "1/2", "4"], ans=1,
   why="Writing 4 - x = (2 - sqrt(x))(2 + sqrt(x)) leaves 1/(2 + sqrt(x)), which approaches 1/4."),
 dict(q="Evaluate lim as x -> 2 of (x - 2)/|x - 2|.", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=3,
   why="No cancellation removes the absolute value: the quotient is -1 for x < 2 and 1 for x > 2, so the one-sided limits differ."),
 dict(q="Evaluate lim as x -> 1 of (sqrt(x) - 1)/(x - 1).", choices=[
   "0", "1/2", "1", "2"], ans=1,
   why="Factoring x - 1 = (sqrt(x) - 1)(sqrt(x) + 1) leaves 1/(sqrt(x) + 1), which approaches 1/2."),
 dict(q="Evaluate lim as x -> 0 of x^2/(1 - cos(x)).", choices=[
   "0", "1/2", "1", "2"], ans=3,
   why="This is the reciprocal of the limit of (1 - cos(x))/x^2, which is 1/2, so the value is 2."),
 dict(q="Evaluate lim as x -> -1 of (x^2 - 1)/(x^2 + 3x + 2).", choices=[
   "-2", "-1/2", "1/2", "2"], ans=0,
   why="Both parts carry a factor of x + 1, leaving (x - 1)/(x + 2), which approaches -2/1 = -2."),
 dict(q="Evaluate lim as x -> 0 of ((2 + x)^3 - 8)/x.", choices=[
   "0", "6", "8", "12"], ans=3,
   why="Expanding gives (12x + 6x^2 + x^3)/x = 12 + 6x + x^2, which approaches 12."),
 dict(q="The most useful first step in evaluating lim as x -> 0 of (sqrt(x + 25) - 5)/x is to", choices=[
   "factor the numerator as a difference of squares",
   "multiply the numerator and the denominator by sqrt(x + 25) + 5",
   "substitute x = 0 into the expression",
   "divide the numerator and the denominator by x"], ans=1,
   why="Multiplying by the conjugate turns the numerator into x, which then cancels the x in the denominator."),
]
