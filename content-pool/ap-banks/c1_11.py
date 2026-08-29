# CALC 1.11 Defining Continuity at a Point — 25 questions
# f is continuous at c exactly when all three of these hold:
#   (1) f(c) is defined;
#   (2) lim as x -> c of f(x) exists;
#   (3) that limit equals f(c).
# Many questions below single out which one of the three fails, since that is
# where students conflate "undefined" with "no limit".
# Verified with sympy; see verify_c1_11.py, which decides for each function
# which of the three conditions hold rather than trusting the key.
TOPIC = ("1.11", "Defining Continuity at a Point", 1)
QUESTIONS = [
 dict(q="A function f is continuous at x = c if and only if", choices=[
   "f(c) is defined",
   "lim as x -> c of f(x) exists",
   "lim as x -> c of f(x) exists, f(c) is defined, and the two are equal",
   "f is increasing on an interval containing c"], ans=2,
   why="Continuity at a point is the single equation lim f(x) = f(c), which silently requires both sides to exist."),
 dict(q="Which list gives the three conditions that must all hold for f to be continuous at x = c?", choices=[
   "f(c) is defined; lim as x -> c of f(x) exists; the limit equals f(c)",
   "f is defined near c; f is increasing at c; f(c) > 0",
   "f(c) = 0; the limit exists; f is a polynomial",
   "the left limit exists; the right limit exists; f(c) is positive"], ans=0,
   why="Those three, in that order, are the standard checklist, and failing any one of them breaks continuity."),
 dict(q="For f(x) = (x^2 - 4)/(x - 2), which condition for continuity at x = 2 is the one that fails?", choices=[
   "f(2) is not defined",
   "the limit as x approaches 2 does not exist",
   "the limit exists but differs from f(2)",
   "none of them fail; f is continuous at 2"], ans=0,
   why="The limit exists and equals 4, but substituting 2 gives 0/0, so the function simply has no value there."),
 dict(q="Let f(x) = -1 for x < 0 and f(x) = 1 for x >= 0. Which condition for continuity at x = 0 fails?", choices=[
   "f(0) is not defined",
   "the limit as x approaches 0 does not exist, because the one-sided limits are -1 and 1",
   "the limit exists but differs from f(0)",
   "none of them fail; f is continuous at 0"], ans=1,
   why="Here f(0) = 1 is perfectly well defined; it is the two-sided limit that is missing."),
 dict(q="Let f(x) = x + 1 for x not equal to 3, with f(3) = 7. Which condition for continuity at x = 3 fails?", choices=[
   "f(3) is not defined",
   "the limit as x approaches 3 does not exist",
   "the limit exists and equals 4, but f(3) = 7, so the two are not equal",
   "none of them fail; f is continuous at 3"], ans=2,
   why="Both the value and the limit exist; only the third condition, that they agree, is violated."),
 dict(q="At which points is the polynomial f(x) = 3x^3 - 5x + 2 continuous?", choices=[
   "only at x = 0",
   "at every real number",
   "only where f(x) > 0",
   "nowhere"], ans=1,
   why="Every polynomial's limit at any point is found by substitution, so the limit always equals the value."),
 dict(q="Is f(x) = 1/x continuous at x = 0?", choices=[
   "Yes",
   "No, because f(0) is undefined",
   "No, because the limit equals 0",
   "Yes, because 1/x is a rational function"], ans=1,
   why="The first condition already fails; there is no value f(0) for a limit to match."),
 dict(q="Is f(x) = 1/x continuous at x = 2?", choices=[
   "Yes, because f(2) = 1/2 and the limit as x approaches 2 is also 1/2",
   "No, because the function has a discontinuity somewhere",
   "No, because 1/x is undefined at 0",
   "It cannot be determined"], ans=0,
   why="Continuity is a local property, so a break at 0 says nothing about the behavior at 2."),
 dict(q="Let f(x) = x^2 for x <= 1 and f(x) = 2x - 1 for x > 1. Is f continuous at x = 1?", choices=[
   "Yes, because the left limit, the right limit, and f(1) are all 1",
   "No, because the one-sided limits differ",
   "No, because f(1) is undefined",
   "It cannot be determined"], ans=0,
   why="The left rule gives 1, the right rule gives 2 - 1 = 1, and f(1) = 1, so all three conditions hold."),
 dict(q="Let g(x) = x^2 for x <= 1 and g(x) = 2x for x > 1. Is g continuous at x = 1?", choices=[
   "Yes",
   "No, because the left limit is 1 and the right limit is 2",
   "No, because g(1) is undefined",
   "No, because the limit exists but differs from g(1)"], ans=1,
   why="The two rules disagree at the seam, so the two-sided limit does not exist."),
 dict(q="Which statement about f(x) = sqrt(x) at x = 0 is correct?", choices=[
   "f is continuous at 0 in the two-sided sense",
   "f is continuous from the right at 0, since f is not defined for x < 0 and the two-sided limit therefore does not exist",
   "f is continuous from the left at 0",
   "f is discontinuous at 0 because f(0) is undefined"], ans=1,
   why="f(0) = 0 exists and the right-hand limit is 0, but there is no left-hand approach at all."),
 dict(q="A function f is continuous from the left at x = c exactly when", choices=[
   "lim as x -> c^- of f(x) = f(c)",
   "lim as x -> c^+ of f(x) = f(c)",
   "f(c) = 0",
   "f is defined on both sides of c"], ans=0,
   why="One-sided continuity replaces the two-sided limit in the definition with the corresponding one-sided limit."),
 dict(q="Is f(x) = |x| continuous at x = 0?", choices=[
   "Yes, because both one-sided limits and f(0) all equal 0",
   "No, because the graph has a corner there",
   "No, because |x| is not differentiable at 0",
   "No, because the one-sided limits differ"], ans=0,
   why="Continuity asks only that the approached height match the value, which a corner does not disturb."),
 dict(q="Is the greatest integer function, which rounds each input down to the nearest integer, continuous at x = 2?", choices=[
   "Yes",
   "No, because the left limit is 1 while the value is 2",
   "No, because the function is undefined at 2",
   "No, because the limit is infinite"], ans=1,
   why="Approaching 2 from the left gives values just below 2, all rounding down to 1, so the limit fails to match the value 2."),
 dict(q="Is the greatest integer function continuous at x = 2.5?", choices=[
   "Yes, because it equals the constant 2 throughout an interval around 2.5",
   "No, because the function jumps at every integer",
   "No, because it is not differentiable there",
   "It cannot be determined"], ans=0,
   why="Between consecutive integers the function is constant, and a constant function is continuous."),
 dict(q="Which of the following functions is continuous at x = 0?", choices=[
   "f(x) = 1/x",
   "f(x) = |x|/x",
   "f(x) = x^2 + 3",
   "f(x) = (x^2 - x)/x"], ans=2,
   why="Only that one has a value at 0 that matches its limit; the other three are all undefined at 0."),
 dict(q="If f is known to be continuous at x = c, which statement must be true?", choices=[
   "lim as x -> c of f(x) = f(c)",
   "f(c) = 0",
   "f is increasing at c",
   "f has a maximum at c"], ans=0,
   why="That equation is precisely what continuity at a point asserts."),
 dict(q="If lim as x -> c of f(x) = f(c) holds, how many of the three conditions for continuity at c are satisfied?", choices=[
   "one", "two", "all three", "none"], ans=2,
   why="The equation cannot even be written unless both sides exist, so it carries all three conditions at once."),
 dict(q="Suppose f(2) = 5 and lim as x -> 2 of f(x) = 5. Is f continuous at x = 2?", choices=[
   "Yes, because the limit and the value both exist and agree",
   "No, because f might be undefined nearby",
   "No, because the one-sided limits were not given separately",
   "It cannot be determined"], ans=0,
   why="A two-sided limit of 5 already means both one-sided limits are 5, so all three conditions hold."),
 dict(q="Suppose lim as x -> 4 of f(x) = 9 but f(4) is undefined. Which statement is correct?", choices=[
   "f is continuous at 4",
   "f is discontinuous at 4, and the discontinuity is removable by defining f(4) = 9",
   "f is discontinuous at 4, and no definition of f(4) can repair it",
   "lim as x -> 4 of f(x) must also fail to exist"], ans=1,
   why="Only the first condition fails, and the existing limit supplies exactly the value that repairs it."),
 dict(q="Let f(x) = (x^2 - 1)/(x - 1) for x not equal to 1, with f(1) = 2. Is f continuous at x = 1?", choices=[
   "Yes, because the limit is 2 and f(1) = 2",
   "No, because the original formula is undefined at 1",
   "No, because the limit does not exist",
   "No, because the limit is 1"], ans=0,
   why="Away from 1 the function equals x + 1, whose limit is 2, and the assigned value matches it exactly."),
 dict(q="How is continuity handled at an endpoint of a closed interval, such as x = a for a function defined on [a, b]?", choices=[
   "Continuity is impossible at an endpoint",
   "The one-sided limit is used, so f is continuous at a when lim as x -> a^+ of f(x) = f(a)",
   "The two-sided limit is used, as at any interior point",
   "The endpoint is ignored"], ans=1,
   why="Only one side of the endpoint lies in the domain, so the definition is applied with the available one-sided limit."),
 dict(q="Let f(x) = sin(x)/x for x not equal to 0, with f(0) = 1. Is f continuous at x = 0?", choices=[
   "Yes, because the limit as x approaches 0 is 1, matching f(0)",
   "No, because sin(x)/x is undefined at 0",
   "No, because the limit is 0",
   "No, because the one-sided limits differ"], ans=0,
   why="The original formula has a removable hole at 0, and defining f(0) = 1 fills it exactly."),
 dict(q="Let g(x) = sin(x)/x for x not equal to 0, with g(0) = 0. Which condition for continuity at x = 0 fails?", choices=[
   "g(0) is not defined",
   "the limit as x approaches 0 does not exist",
   "the limit exists and equals 1, but g(0) = 0, so they are not equal",
   "none of them fail"], ans=2,
   why="Both the limit and the value exist here; the assigned value is simply the wrong one."),
 dict(q="Which of the following does NOT follow from f being continuous at x = c?", choices=[
   "lim as x -> c of f(x) exists",
   "f(c) is defined",
   "f is differentiable at c",
   "lim as x -> c^- of f(x) = lim as x -> c^+ of f(x)"], ans=2,
   why="f(x) = |x| is continuous at 0 but has a corner there, so continuity never guarantees differentiability."),
]
