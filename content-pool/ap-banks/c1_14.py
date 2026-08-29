# CALC 1.14 Connecting Infinite Limits and Vertical Asymptotes — 25 questions
# Verified with sympy; see verify_c1_14.py, which computes the one-sided limits
# and, for the "how many asymptotes" questions, works out the full asymptote set
# so that a removable hole is not miscounted as an asymptote.
# "infinity" is used as the AP exam does, as shorthand for "the values increase
# without bound"; several questions make the point that such a limit still does
# not exist as a number.
TOPIC = ("1.14", "Connecting Infinite Limits and Vertical Asymptotes", 1)
QUESTIONS = [
 dict(q="The statement lim as x -> c of f(x) = infinity means that", choices=[
   "f(c) is equal to infinity",
   "the values of f(x) increase without bound as x approaches c",
   "the limit of f at c is a very large number",
   "f is increasing on an interval containing c"], ans=1,
   why="Infinity is not a value f attains; the notation records that the values eventually exceed every bound."),
 dict(q="If lim as x -> c of f(x) = infinity, does the limit exist?", choices=[
   "Yes, and it equals infinity",
   "No; the notation describes how the limit fails to exist rather than naming a number the function approaches",
   "Yes, because infinity is a real number",
   "It depends on whether f(c) is defined"], ans=1,
   why="A limit exists only when the values approach a single real number, and no real number is being approached here."),
 dict(q="The line x = c is a vertical asymptote of the graph of f exactly when", choices=[
   "f(c) is undefined",
   "at least one of the one-sided limits of f at c is infinity or -infinity",
   "both one-sided limits at c are finite but unequal",
   "lim as x -> infinity of f(x) = c"], ans=1,
   why="Unbounded behavior on at least one side is what makes the graph hug the vertical line."),
 dict(q="Evaluate lim as x -> 4^+ of 1/(x - 4).", choices=[
   "-infinity", "0", "1/4", "infinity"], ans=3,
   why="Just to the right of 4 the denominator is a small positive number, so the reciprocal grows without bound."),
 dict(q="Evaluate lim as x -> 4^- of 1/(x - 4).", choices=[
   "-infinity", "0", "1/4", "infinity"], ans=0,
   why="Just to the left of 4 the denominator is a small negative number, so the reciprocal falls without bound."),
 dict(q="Which statement describes the behavior of f(x) = 1/(x - 4)^2 near x = 4?", choices=[
   "Both one-sided limits are infinity, so x = 4 is a vertical asymptote",
   "The left limit is -infinity and the right limit is infinity",
   "The limit is 0",
   "There is no vertical asymptote"], ans=0,
   why="Squaring keeps the denominator positive on both sides, so the values climb without bound from either direction."),
 dict(q="Evaluate lim as x -> 2^+ of (x + 1)/(x - 2).", choices=[
   "-infinity", "0", "3", "infinity"], ans=3,
   why="The numerator approaches 3 while the denominator is a small positive number, so the quotient grows without bound."),
 dict(q="Evaluate lim as x -> 2^- of (x + 1)/(x - 2).", choices=[
   "-infinity", "0", "3", "infinity"], ans=0,
   why="The numerator approaches 3 while the denominator is a small negative number, so the quotient falls without bound."),
 dict(q="Does the graph of f(x) = (x^2 - 4)/(x - 2) have a vertical asymptote at x = 2?", choices=[
   "Yes, because the denominator is 0 there",
   "No, because the factor x - 2 cancels, leaving a removable hole at (2, 4) rather than unbounded behavior",
   "Yes, because f(2) is undefined",
   "It cannot be determined"], ans=1,
   why="A zero denominator only creates an asymptote when it is not cancelled by the numerator."),
 dict(q="The graph of f(x) = 1/(x^2 - 9) has vertical asymptotes at which values of x?", choices=[
   "x = 9 only", "x = 3 only", "x = 3 and x = -3", "there are none"], ans=2,
   why="The denominator vanishes at both 3 and -3, and neither zero is cancelled by the numerator."),
 dict(q="The graph of f(x) = (x - 3)/(x^2 - 9) has a vertical asymptote at which value of x?", choices=[
   "x = 3 only", "x = -3 only", "x = 3 and x = -3", "there are none"], ans=1,
   why="The factor x - 3 cancels, leaving 1/(x + 3), so x = 3 is only a hole while x = -3 is a genuine asymptote."),
 dict(q="Which limit statement shows that the graph of f(x) = ln(x) has a vertical asymptote at x = 0?", choices=[
   "lim as x -> 0^+ of ln(x) = -infinity",
   "lim as x -> 0^+ of ln(x) = infinity",
   "lim as x -> 0 of ln(x) = 0",
   "lim as x -> infinity of ln(x) = infinity"], ans=0,
   why="Only the right side of 0 lies in the domain, and there the values fall without bound."),
 dict(q="At which values of x does the graph of f(x) = tan(x) have vertical asymptotes?", choices=[
   "at every multiple of pi",
   "at every odd multiple of pi/2",
   "at every integer",
   "nowhere"], ans=1,
   why="tan(x) = sin(x)/cos(x), and the cosine vanishes exactly at the odd multiples of pi/2 while the sine does not."),
 dict(q="Evaluate lim as x -> 0^- of 1/x^3.", choices=[
   "-infinity", "0", "1", "infinity"], ans=0,
   why="For x slightly less than 0 the cube is a small negative number, so its reciprocal falls without bound."),
 dict(q="Evaluate lim as x -> 0^+ of 1/x^3.", choices=[
   "-infinity", "0", "1", "infinity"], ans=3,
   why="For x slightly greater than 0 the cube is a small positive number, so its reciprocal grows without bound."),
 dict(q="Which of the following functions has a vertical asymptote at x = 5?", choices=[
   "f(x) = (x - 5)/(x^2 - 25)",
   "f(x) = (x^2 - 25)/(x - 5)",
   "f(x) = (x + 5)/(x - 5)",
   "f(x) = x^2 - 25"], ans=2,
   why="Only that one has a zero denominator at 5 that the numerator does not cancel."),
 dict(q="Evaluate lim as x -> 1^+ of (x^2 + 1)/(x - 1).", choices=[
   "-infinity", "0", "2", "infinity"], ans=3,
   why="The numerator approaches 2 while the denominator is a small positive number."),
 dict(q="Evaluate lim as x -> 2^- of (x - 5)/(x - 2)^2.", choices=[
   "-infinity", "-3", "0", "infinity"], ans=0,
   why="The numerator approaches -3 while the squared denominator is a small positive number, so the quotient falls without bound on both sides."),
 dict(q="Evaluate lim as x -> 3^+ of (x^2 - 9)/(x - 3)^2.", choices=[
   "-infinity", "0", "6", "infinity"], ans=3,
   why="Cancelling one factor leaves (x + 3)/(x - 3), whose numerator approaches 6 over a small positive denominator."),
 dict(q="Evaluate lim as x -> 1^- of (x^2 - 1)/(x - 1)^3.", choices=[
   "-infinity", "0", "2", "infinity"], ans=3,
   why="Cancelling gives (x + 1)/(x - 1)^2, and the squared denominator stays positive, so the quotient grows without bound from either side."),
 dict(q="How many vertical asymptotes does the graph of f(x) = (x - 2)/(x^2 - 4) have?", choices=[
   "0", "1", "2", "3"], ans=1,
   why="The factor x - 2 cancels, leaving 1/(x + 2), so there is a hole at x = 2 and a single asymptote at x = -2."),
 dict(q="How many vertical asymptotes does the graph of f(x) = (x^2 - x - 6)/(x^2 - 4) have?", choices=[
   "0", "1", "2", "3"], ans=1,
   why="The expression reduces to (x - 3)/(x - 2), so x = -2 is a hole and only x = 2 is an asymptote."),
 dict(q="Suppose lim as x -> c^+ of f(x) = infinity and lim as x -> c^- of f(x) = -infinity. Which statement is correct?", choices=[
   "The two-sided limit is 0 by symmetry",
   "x = c is a vertical asymptote and the two-sided limit does not exist",
   "f is continuous at c",
   "x = c is a removable discontinuity"], ans=1,
   why="Unbounded behavior on both sides gives an asymptote, and running off in opposite directions means no value is approached."),
 dict(q="How many vertical asymptotes does the graph of f(x) = 1/(x - 1) + 1/(x - 2) have?", choices=[
   "0", "1", "2", "3"], ans=2,
   why="Combined over a common denominator the function is (2x - 3)/((x - 1)(x - 2)), and neither zero of the denominator is cancelled."),
 dict(q="Can the graph of a function cross one of its vertical asymptotes?", choices=[
   "Yes, at exactly one point",
   "No, because the function has no value at the asymptote, so the graph has no point there",
   "Yes, infinitely often",
   "Only if the function is a rational function"], ans=1,
   why="A vertical asymptote occurs where the function is undefined, so there is no point of the graph on that line."),
]
