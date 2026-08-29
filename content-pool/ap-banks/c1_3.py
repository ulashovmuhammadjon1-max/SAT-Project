# CALC 1.3 Estimating Limit Values from Graphs — 25 questions
# No figures exist in this bank, so every graph is specified in words precisely
# enough to be reconstructed: which segments and curves it is built from, where
# the open circles and solid dots sit, and where the asymptotes are.
# Each described graph is modeled as an explicit function in verify_c1_3.py and
# the limit is confirmed with sympy.  Questions 10, 19, 22, 23 and 25 reason
# about graphs in general rather than one particular graph and carry no sympy
# check.
TOPIC = ("1.3", "Estimating Limit Values from Graphs", 1)
QUESTIONS = [
 dict(q="The graph of f approaches height 3 from both sides as x approaches 2. At x = 2 the graph shows an open circle at (2, 3) and a solid dot at (2, 5). The value of lim as x -> 2 of f(x) is", choices=[
   "2", "3", "5", "the limit does not exist"], ans=1,
   why="The open circle marks the height the graph approaches, and the limit reads that height, not the plotted value."),
 dict(q="For the graph that approaches height 3 from both sides at x = 2 but has an open circle at (2, 3) and a solid dot at (2, 5), the value of f(2) is", choices=[
   "2", "3", "5", "undefined"], ans=2,
   why="The solid dot is the point actually on the graph, so f(2) = 5."),
 dict(q="The graph of g rises along a curve to an open circle at (1, 4) for x < 1, and for x > 1 it starts at a solid dot at (1, -1) and rises. The value of lim as x -> 1 of g(x) is", choices=[
   "-1", "1.5", "4", "the limit does not exist"], ans=3,
   why="The graph jumps at x = 1, so the left limit 4 and the right limit -1 disagree."),
 dict(q="For that same graph of g, with an open circle at (1, 4) on the left piece and a solid dot at (1, -1) on the right piece, the value of lim as x -> 1^- of g(x) is", choices=[
   "-1", "1", "4", "the limit does not exist"], ans=2,
   why="Approaching from the left follows the piece that ends at the open circle (1, 4)."),
 dict(q="The graph of h is the line y = 2x + 1 with the single point at x = 4 removed, leaving a hole. The value of lim as x -> 4 of h(x) is", choices=[
   "4", "8", "9", "the limit does not exist"], ans=2,
   why="The line's height at x = 4 is 2(4) + 1 = 9, and removing that one point does not change what the nearby values approach."),
 dict(q="The graph of f(x) = (x^2 - 16)/(x - 4) is a straight line with one hole in it. The hole is located at the point", choices=[
   "(4, 0)", "(4, 4)", "(4, 8)", "(0, -4)"], ans=2,
   why="For x not equal to 4 the function equals x + 4, whose height at x = 4 is 8, and x = 4 is exactly where the function is undefined."),
 dict(q="The graph of f has a vertical asymptote at x = 3, and the graph rises without bound on both sides of x = 3. The value of lim as x -> 3 of f(x) is", choices=[
   "0", "3", "the limit does not exist, because the values increase without bound", "1/3"], ans=2,
   why="No finite value is approached when the graph climbs past every height."),
 dict(q="The graph of k has a vertical asymptote at x = -2. To the left of the asymptote the graph falls without bound, and to the right it rises without bound. Which statement is correct?", choices=[
   "lim as x -> -2 of k(x) = 0",
   "lim as x -> -2 of k(x) = -2",
   "lim as x -> -2^- of k(x) = infinity and lim as x -> -2^+ of k(x) = -infinity",
   "lim as x -> -2^- of k(x) = -infinity and lim as x -> -2^+ of k(x) = infinity"], ans=3,
   why="Falling without bound on the left is described by -infinity, and rising without bound on the right by infinity."),
 dict(q="The graph of f is the parabola y = x^2 for x < 1, an isolated solid dot at (1, 3), and the line y = 2 - x for x > 1. The value of lim as x -> 1 of f(x) is", choices=[
   "1", "2", "3", "the limit does not exist"], ans=0,
   why="Both pieces approach height 1 at x = 1, so the limit is 1 even though the plotted point sits at height 3."),
 dict(q="For that graph — the parabola y = x^2 on the left, a solid dot at (1, 3), and the line y = 2 - x on the right — which statement is correct?", choices=[
   "lim as x -> 1 of f(x) = f(1)",
   "lim as x -> 1 of f(x) = 1 while f(1) = 3",
   "lim as x -> 1 of f(x) = 3 while f(1) = 1",
   "neither the limit nor f(1) exists"], ans=1,
   why="The limit reads the height the two pieces approach, which is 1, and the solid dot gives f(1) = 3."),
 dict(q="The graph of y = |x| has a sharp corner at the origin. The value of lim as x -> 0 of |x| is", choices=[
   "-1", "0", "1", "the limit does not exist, because of the corner"], ans=1,
   why="Both branches approach height 0; a corner affects smoothness, not the existence of the limit."),
 dict(q="The graph of a step function is the horizontal ray y = 1 for x < 0 and the horizontal ray y = 2 for x >= 0. The value of lim as x -> 0 of f(x) is", choices=[
   "1", "1.5", "2", "the limit does not exist"], ans=3,
   why="The left limit is 1 and the right limit is 2, so the two sides disagree."),
 dict(q="The graph of f oscillates infinitely often between the heights -1 and 1 in every interval around x = 0, never settling toward a single height. The value of lim as x -> 0 of f(x) is", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=3,
   why="Values near 0 keep reaching both -1 and 1, so no single height is approached."),
 dict(q="The graph of f passes through the point (5, -2) with no break, hole, or jump anywhere near x = 5. The value of lim as x -> 5 of f(x) is", choices=[
   "-5", "-2", "2", "5"], ans=1,
   why="An unbroken graph approaches the height it actually attains, so the limit equals f(5) = -2."),
 dict(q="The graph of f coincides with the horizontal line y = 4 for every x in the interval (6, 8). The value of lim as x -> 7 of f(x) is", choices=[
   "0", "4", "7", "the limit does not exist"], ans=1,
   why="The graph is flat at height 4 throughout a neighborhood of 7."),
 dict(q="The graph of p has a hole at x = -3 with the hole located at height 7, and no point of the graph lies above or below x = -3. Which statement is correct?", choices=[
   "p(-3) = 7 and lim as x -> -3 of p(x) = 7",
   "p(-3) is undefined and lim as x -> -3 of p(x) = 7",
   "p(-3) is undefined and lim as x -> -3 of p(x) does not exist",
   "p(-3) = 0 and lim as x -> -3 of p(x) = 0"], ans=1,
   why="A hole with no filled point means p(-3) is undefined, while the surrounding graph still approaches height 7."),
 dict(q="The graph of f is the upper half of the circle x^2 + y^2 = 4, so f is defined only for -2 <= x <= 2. The value of lim as x -> 2^- of f(x) is", choices=[
   "-2", "0", "2", "the limit does not exist"], ans=1,
   why="The semicircle meets the x-axis at (2, 0), so the heights approach 0 as x approaches 2 from inside the domain."),
 dict(q="The graph of y = 1/x^2 rises without bound on both sides of x = 0. Which statement about lim as x -> 0 of 1/x^2 is correct?", choices=[
   "The limit equals 0",
   "The limit equals 1",
   "The limit does not exist as a finite number; the values increase without bound on both sides",
   "The left limit is -infinity and the right limit is infinity"], ans=2,
   why="Squaring makes the denominator positive on both sides, so both branches climb without bound and no finite limit exists."),
 dict(q="For which of the following described graphs does lim as x -> 0 of f(x) exist?", choices=[
   "A graph with a jump at x = 0, approaching height 2 from the left and height 5 from the right",
   "A graph with a hole at (0, 4) and no other point above x = 0",
   "A graph with a vertical asymptote at x = 0",
   "A graph that oscillates between heights -1 and 1 in every interval around 0"], ans=1,
   why="A hole leaves the approach from both sides intact, so the limit exists and equals the height of the hole."),
 dict(q="The graph of f consists of the segment from (0, 0) to (3, 6) with a solid dot at (3, 6), together with the segment from (3, 1) to (6, 4) with an open circle at (3, 1). The value of lim as x -> 3^+ of f(x) is", choices=[
   "1", "3", "4", "6"], ans=0,
   why="The right-hand piece begins at the open circle (3, 1), so the approach from the right is toward height 1."),
 dict(q="For that same two-segment graph, with a solid dot at (3, 6) and an open circle at (3, 1), the value of lim as x -> 3 of f(x) is", choices=[
   "1", "3.5", "6", "the limit does not exist"], ans=3,
   why="The left limit is 6 and the right limit is 1, so the two-sided limit fails."),
 dict(q="Reading a graph, a limit at x = c can exist even when", choices=[
   "the graph has a vertical asymptote at x = c",
   "the graph has a hole at x = c and f(c) is undefined",
   "the graph jumps at x = c",
   "the graph oscillates without settling near x = c"], ans=1,
   why="A hole removes only the single point at c, and the limit never depended on that point."),
 dict(q="If the graph of f has a vertical asymptote at x = c, then lim as x -> c of f(x)", choices=[
   "equals c",
   "equals 0",
   "does not exist as a finite number",
   "equals f(c)"], ans=2,
   why="An asymptote means the values grow without bound, so no finite number is approached."),
 dict(q="The graph of f is the parabola y = x^2 with the point (1, 1) removed and the point (1, 4) plotted instead. Which statement is correct?", choices=[
   "lim as x -> 1 of f(x) = 4 and f(1) = 4",
   "lim as x -> 1 of f(x) = 1 and f(1) = 4",
   "lim as x -> 1 of f(x) = 1 and f(1) = 1",
   "lim as x -> 1 of f(x) does not exist"], ans=1,
   why="Moving one point changes f(1) to 4 but leaves every nearby value on the parabola, so the limit is still 1."),
 dict(q="The graph of f approaches height 5 from both sides at x = 1. The graph of g approaches height 2 from the left at x = 1 and height -2 from the right. What can be said about lim as x -> 1 of (f(x) + g(x))?", choices=[
   "It equals 7",
   "It equals 3",
   "It equals 5",
   "It does not exist, because the sum approaches 7 from the left and 3 from the right"], ans=3,
   why="Adding the one-sided limits gives 7 on the left and 3 on the right, and unequal one-sided limits mean the two-sided limit fails."),
]
