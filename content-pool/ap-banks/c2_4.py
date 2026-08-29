# CALC 2.4 Connecting Differentiability and Continuity — 25 questions
# One-sided difference quotients, piecewise matching conditions and the two
# pathological examples are all recomputed in verify_c2_4.py.
# Questions 1, 2, 7, 13, 20, 24 and 25 are conceptual (the implication and its
# false converse, stated in both directions); their reasoning is in the
# verifier's docstring.
TOPIC = ("2.4", "Connecting Differentiability and Continuity", 2)
QUESTIONS = [
 dict(q="If f is differentiable at x = a, which of the following must be true?", choices=[
   "f is continuous at x = a",
   "f is not continuous at x = a",
   "f'' exists at x = a",
   "f has a maximum or minimum at x = a"], ans=0,
   why="Differentiability at a point forces continuity there, because the difference quotient can have a finite limit only if f(x) - f(a) tends to 0."),
 dict(q="If f is continuous at x = a, which of the following must be true?", choices=[
   "None of the other statements must be true",
   "f is differentiable at x = a",
   "f'(a) = 0",
   "f has no corner at x = a"], ans=0,
   why="Continuity does not imply differentiability: f(x) = |x| is continuous at 0 but has no derivative there, so none of the listed consequences is forced."),
 dict(q="At x = 0, the function f(x) = |x| is", choices=[
   "continuous but not differentiable",
   "differentiable but not continuous",
   "both continuous and differentiable",
   "neither continuous nor differentiable"], ans=0,
   why="The limit of f at 0 equals f(0) = 0, but the difference quotient tends to 1 from the right and -1 from the left, so f'(0) does not exist."),
 dict(q="At x = 0, the function f(x) = x^(1/3) is", choices=[
   "continuous, with a vertical tangent line, so f'(0) does not exist",
   "continuous and differentiable, with f'(0) = 0",
   "discontinuous",
   "continuous, with a corner at x = 0"], ans=0,
   why="f'(x) = 1/(3 x^(2/3)) increases without bound as x -> 0 from either side, so the tangent line is vertical and f'(0) does not exist."),
 dict(q="At x = 0, the function f(x) = x^(2/3) is", choices=[
   "continuous, with a cusp, so f'(0) does not exist",
   "differentiable, with f'(0) = 0",
   "discontinuous",
   "differentiable, with f'(0) = 2/3"], ans=0,
   why="f'(x) = 2/(3 x^(1/3)) tends to +infinity from the right and -infinity from the left, which is a cusp rather than a derivative."),
 dict(q="Which of the following functions is NOT differentiable at x = 0?", choices=[
   "f(x) = x^2", "f(x) = x^3", "f(x) = sin(x)", "f(x) = |x|"], ans=3,
   why="The first three are smooth at 0, while |x| has one-sided difference quotients of 1 and -1 there."),
 dict(q="If f is NOT continuous at x = 2, then", choices=[
   "f is not differentiable at x = 2",
   "f may still be differentiable at x = 2",
   "f'(2) = 0",
   "nothing at all can be said about f'(2)"], ans=0,
   why="This is the contrapositive of 'differentiable implies continuous', so a discontinuity rules a derivative out."),
 dict(q="Let f(x) = x^2 for x <= 1 and f(x) = 2x - 1 for x > 1. At x = 1, f is", choices=[
   "differentiable, with f'(1) = 2",
   "continuous but not differentiable",
   "not continuous",
   "differentiable, with f'(1) = 1"], ans=0,
   why="Both pieces give the value 1 at x = 1 and both one-sided derivatives equal 2, so f'(1) = 2."),
 dict(q="Let g(x) = x^2 for x <= 1 and g(x) = 3x - 1 for x > 1. At x = 1, g is", choices=[
   "not continuous, and therefore not differentiable",
   "continuous but not differentiable",
   "differentiable, with g'(1) = 2",
   "differentiable, with g'(1) = 3"], ans=0,
   why="The left piece approaches 1 and the right piece approaches 2, so g jumps at x = 1 and no derivative can exist there."),
 dict(q="Let f(x) = x^2 for x <= 2 and f(x) = ax + 1 for x > 2. For what value of a is f continuous at x = 2?", choices=[
   "4", "3", "2", "3/2"], ans=3,
   why="Continuity needs 2a + 1 = 4, so a = 3/2; a = 4 is what matching the derivatives would require, and it leaves a jump."),
 dict(q="Let f(x) = x^3 for x <= 1 and f(x) = ax + b for x > 1. For what values of a and b is f differentiable at x = 1?", choices=[
   "a = 3, b = -2",
   "a = 3, b = 1",
   "a = 1, b = 0",
   "a = 2, b = -1"], ans=0,
   why="Matching derivatives gives a = 3(1)^2 = 3, and matching values then gives 3 + b = 1, so b = -2."),
 dict(q="For f(x) = |x|, the right-hand and left-hand limits of the difference quotient at x = 0 are, respectively,", choices=[
   "1 and -1", "1 and 1", "0 and 0", "-1 and 1"], ans=0,
   why="For h > 0 the quotient |h|/h is 1, and for h < 0 it is -1, so the two one-sided derivatives disagree."),
 dict(q="Which statement correctly describes the relationship between differentiability and continuity?", choices=[
   "Differentiability implies continuity, but continuity does not imply differentiability",
   "Continuity implies differentiability, but differentiability does not imply continuity",
   "Each one implies the other",
   "Neither one implies the other"], ans=0,
   why="Every differentiable function is continuous, and |x| shows the converse fails."),
 dict(q="Let f(x) = 1 for x < 0 and f(x) = 2 for x >= 0. At x = 0, f is", choices=[
   "not differentiable, because it is not continuous there",
   "differentiable, with f'(0) = 0, because each piece is constant",
   "differentiable, with f'(0) = 1",
   "continuous but not differentiable"], ans=0,
   why="Each piece is flat, but f jumps from 1 to 2 at x = 0, and a function with a jump has no derivative there."),
 dict(q="The function f(x) = |x - 3| fails to be differentiable at", choices=[
   "x = 3 only", "x = 0 only", "x = -3 only", "no value of x"], ans=0,
   why="The corner sits where the expression inside the absolute value changes sign, at x = 3."),
 dict(q="The function f(x) = |x^2 - 4| fails to be differentiable at", choices=[
   "x = -2 and x = 2", "x = 0 only", "x = 2 only", "no value of x"], ans=0,
   why="x^2 - 4 changes sign at x = -2 and x = 2, producing a corner at each."),
 dict(q="At how many values of x is f(x) = |x - 1| + |x + 2| not differentiable?", choices=[
   "0", "1", "2", "3"], ans=2,
   why="Each absolute value contributes one corner, at x = 1 and at x = -2, and they occur at different points."),
 dict(q="Let f(x) = x^2 sin(1/x) for x not 0, and f(0) = 0. At x = 0, f is", choices=[
   "differentiable, with f'(0) = 0",
   "continuous but not differentiable",
   "not continuous",
   "differentiable, with f'(0) = 1"], ans=0,
   why="The difference quotient is h sin(1/h), which is squeezed between -|h| and |h| and therefore tends to 0."),
 dict(q="Let g(x) = x sin(1/x) for x not 0, and g(0) = 0. At x = 0, g is", choices=[
   "continuous but not differentiable",
   "differentiable, with g'(0) = 0",
   "not continuous",
   "differentiable, with g'(0) = 1"], ans=0,
   why="The squeeze theorem gives continuity, but the difference quotient is sin(1/h), which oscillates without approaching any limit."),
 dict(q="If f'(2) exists, which of the following must be true?", choices=[
   "lim as x -> 2 of f(x) = f(2)",
   "lim as x -> 2 of f(x) = f'(2)",
   "f(2) = 0",
   "f is differentiable at every x"], ans=0,
   why="A derivative at a point forces continuity at that point, which is exactly the statement that the limit of f equals f(2)."),
 dict(q="At x = 0, the function f(x) = sqrt(|x|) is", choices=[
   "continuous but not differentiable",
   "differentiable, with f'(0) = 0",
   "not continuous",
   "differentiable, with f'(0) = 1/2"], ans=0,
   why="f(0) = 0 and f is continuous, but the difference quotient sqrt(|h|)/h tends to +infinity from the right and -infinity from the left."),
 dict(q="Which of the following functions has a vertical tangent line at x = 0?", choices=[
   "f(x) = x^(1/3)", "f(x) = |x|", "f(x) = x^2", "f(x) = x^(4/3)"], ans=0,
   why="For x^(1/3) the derivative 1/(3 x^(2/3)) tends to +infinity from both sides, which is a vertical tangent; |x| gives a corner and the other two are differentiable at 0."),
 dict(q="Let f(x) = ax^2 for x <= 2 and f(x) = x + b for x > 2. For what values of a and b is f differentiable at x = 2?", choices=[
   "a = 1/4, b = -1",
   "a = 1/4, b = 1",
   "a = 1/2, b = -1",
   "a = 1, b = -2"], ans=0,
   why="Matching derivatives gives 4a = 1, so a = 1/4, and matching values then gives 1 = 2 + b, so b = -1."),
 dict(q="If f is differentiable at every point of the open interval (-2, 2), which of the following must be true on that interval?", choices=[
   "f is continuous on (-2, 2)",
   "f' is constant on (-2, 2)",
   "f has no zeros on (-2, 2)",
   "f is increasing on (-2, 2)"], ans=0,
   why="Differentiability at each point gives continuity at each point; nothing about the sign or constancy of f' follows."),
 dict(q="A function f is continuous at x = 1, but f'(1) does not exist. Which feature could the graph of f have at x = 1?", choices=[
   "a corner",
   "a jump",
   "a removable hole",
   "a vertical asymptote"], ans=0,
   why="The other three features all destroy continuity at x = 1, while a corner leaves f continuous with mismatched one-sided slopes."),
]
