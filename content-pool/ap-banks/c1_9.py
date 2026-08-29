# CALC 1.9 Connecting Multiple Representations of Limits — 25 questions
# This topic is about moving between the symbolic, tabular, verbal and graphical
# forms of the same limit.  There are no figures in this bank, so graphs are
# specified in words (which segments, where the holes and dots and asymptotes
# are) and tables are written inline in the stem.
# Every formula named in a stem or a choice is checked in verify_c1_9.py: the
# limits, the hole locations, and the table entries.
TOPIC = ("1.9", "Connecting Multiple Representations of Limits", 1)
QUESTIONS = [
 dict(q="Which limit statement expresses the sentence 'as x gets arbitrarily close to 4 from either side, the values of f(x) get arbitrarily close to 6'?", choices=[
   "lim as x -> 4 of f(x) = 6",
   "lim as x -> 6 of f(x) = 4",
   "f(4) = 6",
   "lim as x -> 4^+ of f(x) = 6"], ans=0,
   why="Both sides are involved and the approached height is 6, which is the two-sided statement."),
 dict(q="The graph of f(x) = (x^2 - x - 2)/(x - 2) is a straight line with a single hole. That hole is at the point", choices=[
   "(2, 0)", "(2, 1)", "(2, 3)", "(-1, 0)"], ans=2,
   why="The numerator factors as (x - 2)(x + 1), so away from 2 the function is x + 1, whose height at x = 2 is 3."),
 dict(q="A table gives f(1.9) = 3.9, f(1.99) = 3.99, f(2.01) = 4.01, and f(2.1) = 4.1. Which formula, undefined at x = 2, could produce this table?", choices=[
   "f(x) = 2x", "f(x) = (x^2 - 4)/(x - 2)", "f(x) = x^2 - 2", "f(x) = (x^2 + 4)/(x + 2)"], ans=1,
   why="That quotient equals x + 2 wherever it is defined, matching every entry, and it is undefined at x = 2."),
 dict(q="Which function has a graph that is a straight line with a hole at the point (3, 7)?", choices=[
   "f(x) = (x^2 + x - 12)/(x - 3)",
   "f(x) = (x^2 - 2x - 3)/(x - 3)",
   "f(x) = (x^2 - 9)/(x - 3)",
   "f(x) = (x^2 - 3x)/(x - 3)"], ans=0,
   why="That numerator factors as (x + 4)(x - 3), leaving x + 4, whose height at x = 3 is 7."),
 dict(q="Which notation expresses the sentence 'the values of f(x) increase without bound as x approaches 1 from the right'?", choices=[
   "lim as x -> 1^- of f(x) = infinity",
   "lim as x -> 1^+ of f(x) = infinity",
   "lim as x -> infinity of f(x) = 1",
   "lim as x -> 1 of f(x) = 1"], ans=1,
   why="Approach from the right is marked with a plus superscript, and unbounded growth is written as infinity."),
 dict(q="The statement lim as x -> infinity of f(x) = 2 corresponds to which feature of the graph of f?", choices=[
   "a vertical asymptote at x = 2",
   "a horizontal asymptote at y = 2 on the right",
   "a hole at (2, 0)",
   "an x-intercept at x = 2"], ans=1,
   why="Heights settling toward 2 as x runs to the right is exactly a horizontal asymptote y = 2."),
 dict(q="A function is defined by f(x) = x + 2 for x not equal to 0 and f(0) = 5. Which pair of statements is correct?", choices=[
   "lim as x -> 0 of f(x) = 5 and f(0) = 5",
   "lim as x -> 0 of f(x) = 2 and f(0) = 5",
   "lim as x -> 0 of f(x) = 2 and f(0) = 2",
   "lim as x -> 0 of f(x) does not exist"], ans=1,
   why="Near 0 the function agrees with x + 2, so the limit is 2, while the separate assignment makes f(0) = 5."),
 dict(q="Which piecewise definition produces a function with lim as x -> 1 of f(x) = 2 and f(1) = 5?", choices=[
   "f(x) = 2x for all x",
   "f(x) = 5 for all x",
   "f(x) = 2x for x not equal to 1, and f(1) = 5",
   "f(x) = x + 1 for x < 1 and f(x) = 5 for x >= 1"], ans=2,
   why="Away from 1 the rule 2x approaches 2, and the separate assignment at 1 makes f(1) = 5."),
 dict(q="The graph of f has an open circle at (2, 5) and a solid dot at (2, 1), with the curve approaching height 5 from both sides. Which pair of statements matches this graph?", choices=[
   "lim as x -> 2 of f(x) = 5 and f(2) = 1",
   "lim as x -> 2 of f(x) = 1 and f(2) = 5",
   "lim as x -> 2 of f(x) = 5 and f(2) = 5",
   "lim as x -> 2 of f(x) does not exist and f(2) = 1"], ans=0,
   why="The open circle marks the approached height 5 and the solid dot gives the actual value 1."),
 dict(q="Which table is consistent with the function f(x) = (sqrt(1 + x) - 1)/x near x = 0?", choices=[
   "f(-0.01) = 0.501256, f(0.01) = 0.498756",
   "f(-0.01) = 0.990000, f(0.01) = 1.010000",
   "f(-0.01) = 0.010000, f(0.01) = 0.010000",
   "f(-0.01) = 2.005013, f(0.01) = 1.995012"], ans=0,
   why="Rationalizing gives 1/(sqrt(1 + x) + 1), which is near 1/2 for x near 0, and only the first table shows that."),
 dict(q="Which of the following functions has a jump at x = 1, in the sense that its one-sided limits there exist but differ?", choices=[
   "f(x) = (x^2 - 1)/(x - 1)",
   "f(x) = 1/(x - 1)",
   "f(x) = |x - 1|/(x - 1)",
   "f(x) = x^2 + 1"], ans=2,
   why="That quotient is -1 to the left of 1 and 1 to the right, so both one-sided limits exist and disagree."),
 dict(q="A parking garage charges 3 dollars for any stay up to and including 1 hour, and 5 dollars for a stay longer than 1 hour but at most 2 hours. If C(t) is the charge for a stay of t hours, then lim as t -> 1^- of C(t) and lim as t -> 1^+ of C(t) are", choices=[
   "3 and 3", "3 and 5", "5 and 3", "5 and 5"], ans=1,
   why="Just before one hour the charge is still 3 dollars, and just after it the charge has risen to 5 dollars."),
 dict(q="For the same parking charge C, which costs 3 dollars up to one hour and 5 dollars beyond it, the two-sided limit lim as t -> 1 of C(t)", choices=[
   "equals 3", "equals 4", "equals 5", "does not exist"], ans=3,
   why="The one-sided limits are 3 and 5, so no single value is approached."),
 dict(q="The statement lim as x -> 3^- of f(x) = -infinity says in words that", choices=[
   "f(3) = -infinity",
   "the values of f fall without bound as x approaches 3 from the left",
   "the values of f approach -3 as x approaches 3",
   "the graph has a horizontal asymptote at y = -3"], ans=1,
   why="A minus superscript is approach from the left, and -infinity describes values falling past every bound."),
 dict(q="Values of f(x) = (x^3 - 1)/(x - 1) near x = 1 would cluster near which number?", choices=[
   "0", "1", "3", "the values grow without bound"], ans=2,
   why="Away from 1 the function equals x^2 + x + 1, whose value at x = 1 is 3."),
 dict(q="Which representation shows most directly that lim as x -> 0 of |x|/x does not exist?", choices=[
   "The single value f(0)",
   "The piecewise form, which is -1 for x < 0 and 1 for x > 0, exhibiting two different one-sided limits",
   "The fact that the numerator is never negative",
   "The formula alone, without any rewriting"], ans=1,
   why="Rewriting piecewise displays the two one-sided limits side by side, and their disagreement is the reason the limit fails."),
 dict(q="Let f(x) = (x^2 - 9)/(x - 3) for x not equal to 3, with f(3) = k. For which value of k does the solid dot land exactly in the hole, so the graph has no break?", choices=[
   "0", "3", "6", "9"], ans=2,
   why="Away from 3 the function is x + 3, which approaches 6, so k = 6 fills the hole."),
 dict(q="The graph of f is the line y = 3x - 1 with a hole at x = 2. What is lim as x -> 2 of f(x)?", choices=[
   "2", "3", "5", "the limit does not exist"], ans=2,
   why="The line's height at x = 2 is 3(2) - 1 = 5, and removing one point does not change what nearby values approach."),
 dict(q="A table of values for which function would show entries growing without bound on both sides of x = 2?", choices=[
   "f(x) = 1/(x - 2)", "f(x) = 1/(x - 2)^2", "f(x) = (x^2 - 4)/(x - 2)", "f(x) = |x - 2|/(x - 2)"], ans=1,
   why="Squaring keeps the denominator positive, so the values climb without bound from both sides rather than splitting in sign."),
 dict(q="A student enters f(x) = (x^2 - 4)/(x - 2) into a calculator, asks for the value at x = 2, and gets an error. What is the correct interpretation?", choices=[
   "The limit as x approaches 2 does not exist",
   "The function is undefined at x = 2, but the limit as x approaches 2 still exists and equals 4",
   "The calculator is broken",
   "The function has a vertical asymptote at x = 2"], ans=1,
   why="A limit never consults the value at the point, and away from 2 the function equals x + 2, which approaches 4."),
 dict(q="If both lim as x -> c of f(x) = L and f(c) = L hold, the graph of f near x = c", choices=[
   "has a hole at (c, L)",
   "passes through (c, L) with no hole, jump, or asymptote there",
   "has a vertical asymptote at x = c",
   "has a solid dot above the hole"], ans=1,
   why="The approached height and the actual value agree, so nothing interrupts the graph at that point."),
 dict(q="Which function satisfies both lim as x -> 1^- of f(x) = 4 and lim as x -> 1^+ of f(x) = 4?", choices=[
   "f(x) = 3x + 1 for x < 1 and f(x) = 5 - x for x >= 1",
   "f(x) = 4x for x < 1 and f(x) = x + 2 for x >= 1",
   "f(x) = 1/(x - 1)",
   "f(x) = |x - 1|/(x - 1)"], ans=0,
   why="The left rule approaches 3 + 1 = 4 and the right rule approaches 5 - 1 = 4, so the two sides agree."),
 dict(q="A function is given by f(x) = (x^2 + bx)/(x) for x not equal to 0. A table shows values clustering near 7 as x approaches 0. What is b?", choices=[
   "0", "1", "7", "it cannot be determined"], ans=2,
   why="Away from 0 the function equals x + b, which approaches b, so the table forces b = 7."),
 dict(q="Which single statement captures all three observations: a table shows values approaching 7 from both sides at x = 5, the graph has a hole at (5, 7), and f(5) produces an error?", choices=[
   "f(5) = 7",
   "lim as x -> 5 of f(x) = 7 while f is undefined at 5",
   "lim as x -> 5 of f(x) does not exist",
   "f has a vertical asymptote at x = 5"], ans=1,
   why="The three observations are the tabular, graphical, and symbolic faces of a limit that exists at a point where the function has no value."),
 dict(q="Describe the graph of f(x) = (x - 1)/(x^2 - 1) near x = 1 and near x = -1.", choices=[
   "A hole at (1, 1/2) and a vertical asymptote at x = -1",
   "A vertical asymptote at x = 1 and a hole at (-1, 1/2)",
   "Holes at both x = 1 and x = -1",
   "Vertical asymptotes at both x = 1 and x = -1"], ans=0,
   why="Cancelling x - 1 leaves 1/(x + 1), which is defined and equal to 1/2 at x = 1 but blows up at x = -1."),
]
