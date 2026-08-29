# CALC 1.7 Selecting Procedures for Determining Limits — 25 questions
# Limits verified with sympy; see verify_c1_7.py.  Questions 1, 3, 5, 10, 19
# and 25 ask which procedure fits rather than for a value; their reasoning is
# stated in `why` and the underlying limits are still confirmed in the verifier.
# Infinite behavior is described with "infinity" as shorthand for "the values
# increase without bound", which is how the AP exam writes it.
TOPIC = ("1.7", "Selecting Procedures for Determining Limits", 1)
QUESTIONS = [
 dict(q="Which procedure is appropriate for evaluating lim as x -> 2 of (x^2 + 1)/(x + 3)?", choices=[
   "Direct substitution, because the denominator's limit is not 0",
   "Factoring and cancelling, because the form is 0/0",
   "Multiplying by the conjugate",
   "Examining one-sided limits separately"], ans=0,
   why="Substitution gives 5/5, a defined value, so no manipulation is needed."),
 dict(q="Evaluate lim as x -> 2 of (x^2 + 1)/(x + 3).", choices=[
   "0", "1", "5", "the limit does not exist"], ans=1,
   why="Substitution is valid here and gives 5/5 = 1."),
 dict(q="Substituting x = 1 into (x^2 - 1)/(x - 1) produces the form 0/0. The appropriate next step is to", choices=[
   "conclude that the limit is 1",
   "conclude that the limit does not exist",
   "factor the numerator and cancel the common factor x - 1",
   "multiply by the conjugate of the denominator"], ans=2,
   why="The form 0/0 signals a shared factor, and cancelling it leaves x + 1, whose limit is 2."),
 dict(q="Evaluate lim as x -> 0 of (sqrt(16 + x) - 4)/x.", choices=[
   "0", "1/8", "1/4", "the limit does not exist"], ans=1,
   why="Multiplying by the conjugate leaves 1/(sqrt(16 + x) + 4), which approaches 1/8."),
 dict(q="For lim as x -> 3 of (x + 1)/(x - 3), the numerator approaches 4 and the denominator approaches 0. The appropriate procedure is to", choices=[
   "cancel a common factor",
   "examine the one-sided limits separately, since the sign of the denominator changes at 3",
   "use direct substitution",
   "apply the squeeze theorem"], ans=1,
   why="A nonzero numerator over a denominator that changes sign gives opposite infinite behavior on the two sides, which only a one-sided analysis reveals."),
 dict(q="Evaluate lim as x -> 3^+ of (x + 1)/(x - 3).", choices=[
   "-infinity", "0", "4", "infinity"], ans=3,
   why="For x slightly greater than 3 the denominator is a small positive number and the numerator is near 4, so the quotient grows without bound."),
 dict(q="Evaluate lim as x -> 3^- of (x + 1)/(x - 3).", choices=[
   "-infinity", "0", "4", "infinity"], ans=0,
   why="For x slightly less than 3 the denominator is a small negative number, so the quotient falls without bound."),
 dict(q="Evaluate lim as x -> 0 of x^2 cos(1/x).", choices=[
   "0", "1", "does not exist because cos(1/x) oscillates", "infinity"], ans=0,
   why="Since -x^2 <= x^2 cos(1/x) <= x^2 and both bounds approach 0, the squeeze theorem forces the limit to be 0."),
 dict(q="Evaluate lim as x -> infinity of (3x^2 + 1)/(2x^2 - x).", choices=[
   "0", "1", "3/2", "infinity"], ans=2,
   why="Dividing numerator and denominator by x^2 leaves (3 + 1/x^2)/(2 - 1/x), which approaches 3/2."),
 dict(q="For which of the following can the limit be found by direct substitution?", choices=[
   "lim as x -> 4 of (x - 4)/(x^2 - 16)",
   "lim as x -> 1 of (x^2 - 1)/(x - 1)",
   "lim as x -> 1 of (x^2 + 2)/(x + 3)",
   "lim as x -> 0 of sin(x)/x"], ans=2,
   why="Only that one has a denominator whose limit, 4, is not 0; the other three all give 0/0."),
 dict(q="Evaluate lim as x -> 4 of (x^2 - 16)/(x^2 - 3x - 4).", choices=[
   "0", "8/5", "5/8", "the limit does not exist"], ans=1,
   why="Both parts carry the factor x - 4, leaving (x + 4)/(x + 1), which approaches 8/5."),
 dict(q="Evaluate lim as x -> 0 of sin(5x)/(2x).", choices=[
   "0", "2/5", "5/2", "5"], ans=2,
   why="Writing it as (5/2) * sin(5x)/(5x) and using that sin(u)/u approaches 1 gives 5/2."),
 dict(q="For lim as x -> 2 of |x - 2|/(x - 2), the appropriate procedure is to", choices=[
   "cancel the absolute value bars",
   "rewrite the absolute value piecewise and compute the two one-sided limits",
   "multiply by the conjugate",
   "substitute x = 2"], ans=1,
   why="The absolute value has different formulas on the two sides of 2, and here the one-sided limits come out 1 and -1, so the limit fails to exist."),
 dict(q="Evaluate lim as x -> 0 of (1/x - 1/(x^2 + x)).", choices=[
   "0", "1", "infinity", "the limit does not exist"], ans=1,
   why="Over the common denominator x(x + 1) the numerator becomes x, leaving 1/(x + 1), which approaches 1."),
 dict(q="Evaluate lim as x -> 5 of (sqrt(x - 1) - 2)/(x - 5).", choices=[
   "0", "1/4", "1/2", "4"], ans=1,
   why="The conjugate turns the numerator into x - 5, leaving 1/(sqrt(x - 1) + 2), which approaches 1/4."),
 dict(q="Evaluate lim as x -> 0^+ of ln(x).", choices=[
   "-infinity", "0", "1", "infinity"], ans=0,
   why="The natural logarithm falls without bound as its input shrinks toward 0 from above."),
 dict(q="Evaluate lim as x -> -infinity of (2x^3 - x)/(5x^3 + 4).", choices=[
   "-2/5", "0", "2/5", "-infinity"], ans=2,
   why="Dividing by x^3 leaves (2 - 1/x^2)/(5 + 4/x^3), which approaches 2/5 from either direction."),
 dict(q="Evaluate lim as x -> 0 of (e^(2x) - 1)/x.", choices=[
   "0", "1", "2", "e^2"], ans=2,
   why="Writing it as 2 * (e^(2x) - 1)/(2x) and using that (e^u - 1)/u approaches 1 gives 2."),
 dict(q="Which procedure settles lim as x -> 0 of x sin(1/x)?", choices=[
   "Direct substitution",
   "The squeeze theorem, using -|x| <= x sin(1/x) <= |x|",
   "Factoring and cancelling",
   "Dividing by the highest power of x"], ans=1,
   why="The factor sin(1/x) never leaves [-1, 1], so the product is trapped between two functions that both approach 0."),
 dict(q="Evaluate lim as x -> 1 of (x^3 - 1)/(x^2 - 1).", choices=[
   "0", "1", "3/2", "3"], ans=2,
   why="Cancelling x - 1 leaves (x^2 + x + 1)/(x + 1), which approaches 3/2."),
 dict(q="Evaluate lim as x -> pi of sin(x)/(x - pi).", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=0,
   why="Substituting u = x - pi gives sin(pi + u)/u = -sin(u)/u, which approaches -1."),
 dict(q="Evaluate lim as x -> 0 of (cos(x) - 1)/x.", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=1,
   why="The numerator behaves like -x^2/2 near 0, so dividing by x leaves something that approaches 0."),
 dict(q="Evaluate lim as x -> 2 of (x^2 - 4)/|x - 2|.", choices=[
   "-4", "0", "4", "the limit does not exist"], ans=3,
   why="From the left the expression is -(x + 2), approaching -4, and from the right it is x + 2, approaching 4."),
 dict(q="Evaluate lim as x -> 0 of (1 - cos(x))/sin(x).", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=1,
   why="Multiplying by (1 + cos(x))/(1 + cos(x)) turns it into sin(x)/(1 + cos(x)), which approaches 0/2 = 0."),
 dict(q="A student substitutes x = 1 into (x^2 - 1)/(x - 1), obtains 0/0, and reports that the limit is 1. The error in this reasoning is that", choices=[
   "the substitution was done incorrectly",
   "0/0 is an indeterminate form, not a value, and it signals that more work is needed rather than giving an answer",
   "the limit does not exist",
   "limits can never be found by substitution"], ans=1,
   why="An indeterminate form carries no value on its own; cancelling the common factor here shows the limit is actually 2."),
]
