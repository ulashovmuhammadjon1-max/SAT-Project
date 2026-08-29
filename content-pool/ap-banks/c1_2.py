# CALC 1.2 Defining Limits and Using Limit Notation — 25 questions
# Computational answers verified with sympy; see verify_c1_2.py.
# Questions 1-5, 19 and 22 are conceptual (what the notation asserts, the
# existence criterion, and translating English into limit notation); no sympy
# check is possible for those and the reasoning is stated in `why`.
TOPIC = ("1.2", "Defining Limits and Using Limit Notation", 1)
QUESTIONS = [
 dict(q="The statement lim as x -> c of f(x) = L means that", choices=[
   "f(c) = L",
   "the values of f(x) can be made as close to L as desired by taking x sufficiently close to c but not equal to c",
   "f(x) is never equal to L near c",
   "f is defined on an interval containing c and increases toward L"], ans=1,
   why="A limit describes the behavior of f near c, deliberately excluding what happens at c itself."),
 dict(q="The two-sided limit lim as x -> c of f(x) exists if and only if", choices=[
   "f is defined at c",
   "the left-hand limit and the right-hand limit at c both exist and are equal",
   "f(c) equals the left-hand limit at c",
   "f is increasing on both sides of c"], ans=1,
   why="Approaching from the two sides must give the same finite value for the two-sided limit to exist."),
 dict(q="Suppose f(3) = 5 but the values of f(x) approach 3 as x approaches 3 from either side. Then lim as x -> 3 of f(x) is", choices=[
   "3", "5", "8", "nonexistent, because f(3) does not match"], ans=0,
   why="A limit ignores the value of the function at the point itself, so the limit is 3 even though f(3) = 5."),
 dict(q="Which notation stands for the limit of f(x) as x approaches c from the left?", choices=[
   "lim as x -> c^- of f(x)",
   "lim as x -> c^+ of f(x)",
   "lim as x -> -c of f(x)",
   "lim as x -> c of (-f(x))"], ans=0,
   why="A superscript minus sign marks approach through values less than c."),
 dict(q="If lim as x -> 2^- of f(x) = 1 and lim as x -> 2^+ of f(x) = 4, then lim as x -> 2 of f(x)", choices=[
   "equals 1", "equals 4", "equals 2.5", "does not exist"], ans=3,
   why="The one-sided limits disagree, so no single value is approached from both sides."),
 dict(q="The value of lim as x -> 3 of (x^2 - 9)/(x - 3) is", choices=[
   "0", "3", "6", "9"], ans=2,
   why="For x not equal to 3 the expression equals x + 3, which approaches 6."),
 dict(q="Let f(x) = 2x + 1 for x < 1 and f(x) = 5 - x for x >= 1. Then lim as x -> 1^- of f(x) is", choices=[
   "1", "2", "3", "4"], ans=2,
   why="Approaching from the left uses the rule 2x + 1, giving 2(1) + 1 = 3."),
 dict(q="For the function f with f(x) = 2x + 1 for x < 1 and f(x) = 5 - x for x >= 1, the value of lim as x -> 1^+ of f(x) is", choices=[
   "1", "3", "4", "5"], ans=2,
   why="Approaching from the right uses the rule 5 - x, giving 5 - 1 = 4."),
 dict(q="For the same piecewise function, f(x) = 2x + 1 for x < 1 and f(x) = 5 - x for x >= 1, the two-sided limit lim as x -> 1 of f(x)", choices=[
   "equals 3", "equals 4", "equals 3.5", "does not exist"], ans=3,
   why="The one-sided limits are 3 and 4, and because they differ the two-sided limit fails to exist."),
 dict(q="The value of lim as x -> 0^- of |x|/x is", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=0,
   why="For x < 0, |x| = -x, so the quotient is identically -1."),
 dict(q="The two-sided limit lim as x -> 0 of |x|/x", choices=[
   "equals -1", "equals 0", "equals 1", "does not exist"], ans=3,
   why="The quotient is -1 on the left and 1 on the right, so the one-sided limits disagree."),
 dict(q="The value of lim as x -> 3 of (x^2 - 5) is", choices=[
   "-5", "4", "9", "14"], ans=1,
   why="The expression is a polynomial, so the limit is found by substituting: 9 - 5 = 4."),
 dict(q="The value of lim as x -> 0 of (x^2 + 2x)/x is", choices=[
   "0", "1", "2", "the limit does not exist"], ans=2,
   why="For x not equal to 0 the quotient equals x + 2, which approaches 2."),
 dict(q="Let g(x) = x^2 for x <= 2 and g(x) = 4 for x > 2. The value of lim as x -> 2 of g(x) is", choices=[
   "0", "2", "4", "the limit does not exist"], ans=2,
   why="The left-hand limit is 2^2 = 4 and the right-hand limit is 4, so both sides agree."),
 dict(q="The value of lim as x -> 2 of 7 is", choices=[
   "0", "2", "7", "14"], ans=2,
   why="A constant function takes the value 7 at every input, so its limit is 7 at every point."),
 dict(q="The value of lim as x -> -1 of (3x + 2) is", choices=[
   "-1", "1", "2", "5"], ans=0,
   why="Substituting into the linear expression gives 3(-1) + 2 = -1."),
 dict(q="Which best describes lim as x -> 0^+ of 1/x?", choices=[
   "It equals 0",
   "It equals 1",
   "It does not exist, because 1/x increases without bound as x approaches 0 from the right",
   "It equals -1"], ans=2,
   why="The quotient grows past every bound, so no finite value is approached."),
 dict(q="Let f(x) = (x^2 - 1)/(x - 1) for x not equal to 1, and let f(1) = 7. The value of lim as x -> 1 of f(x) is", choices=[
   "1", "2", "7", "the limit does not exist"], ans=1,
   why="Away from x = 1 the function equals x + 1, which approaches 2; the assigned value f(1) = 7 is irrelevant."),
 dict(q="If lim as x -> 3 of f(x) = 5, which of the following must be true?", choices=[
   "f(3) = 5",
   "f(x) is close to 5 whenever x is close to 3 and not equal to 3",
   "f is defined at x = 3",
   "f(x) never takes the value 5"], ans=1,
   why="The limit constrains the behavior of f near 3 only, saying nothing about whether f(3) exists or what it is."),
 dict(q="Which statement about lim as x -> 1 of (x - 1)/|x - 1| is correct?", choices=[
   "The limit equals 1",
   "The limit equals -1",
   "The limit equals 0",
   "The limit does not exist, because the one-sided limits are -1 and 1"], ans=3,
   why="For x < 1 the quotient is -1 and for x > 1 it is 1, so the two sides disagree."),
 dict(q="Which statement about lim as x -> 0 of sin(1/x) is correct?", choices=[
   "The limit equals 0",
   "The limit equals 1",
   "The limit does not exist, because the values oscillate between -1 and 1 no matter how close x is to 0",
   "The limit equals infinity"], ans=2,
   why="Every interval around 0 contains inputs where sin(1/x) equals 1 and inputs where it equals -1, so no single value is approached."),
 dict(q="Which limit statement expresses the sentence 'as x approaches 2 from the right, the values of f(x) approach 6'?", choices=[
   "lim as x -> 2^+ of f(x) = 6",
   "lim as x -> 2^- of f(x) = 6",
   "lim as x -> 6^+ of f(x) = 2",
   "lim as x -> 2 of f(x) = 6"], ans=0,
   why="Approach from the right is written with a plus superscript on the value being approached."),
 dict(q="The value of lim as x -> -2 of (x^2 - 4)/(x + 2) is", choices=[
   "-4", "0", "4", "the limit does not exist"], ans=0,
   why="For x not equal to -2 the expression equals x - 2, which approaches -4."),
 dict(q="The value of lim as x -> 3^+ of |x - 3|/(x - 3) is", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=2,
   why="For x > 3 the quantity x - 3 is positive, so |x - 3| = x - 3 and the quotient is 1."),
 dict(q="Suppose lim as x -> 1^- of f(x) = 2, lim as x -> 1^+ of f(x) = 2, and f(1) = 6. Then lim as x -> 1 of f(x) is", choices=[
   "2", "4", "6", "nonexistent"], ans=0,
   why="Both one-sided limits equal 2, so the two-sided limit is 2 regardless of the value f(1) = 6."),
]
