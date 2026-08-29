# CALC 8.6 Finding the Area Between Curves That Intersect at More Than Two
# Points — 25 questions
# Solve for every crossing, test which curve is on top on each subinterval, and
# add the pieces. verify_c8_6.py finds the crossings with sympy and integrates
# each piece separately.
TOPIC = ("8.6", "Finding the Area Between Curves That Intersect at More Than Two Points", 8)
QUESTIONS = [
 dict(q="Why must the area between two curves that cross inside the interval be computed with more than one integral?", choices=[
   "the curve that is on top changes at each crossing, so a single top-minus-bottom expression is not valid throughout",
   "the functions stop being continuous at a crossing",
   "the integral does not exist at a crossing",
   "the region becomes unbounded at a crossing"], ans=0,
   why="Area needs the positive difference on each piece, and which difference is positive switches at every crossing."),
 dict(q="For curves f and g on [a, b] that may cross, the total area between them equals", choices=[
   "int from a to b of |f(x) - g(x)| dx",
   "int from a to b of (f(x) - g(x)) dx",
   "|int from a to b of (f(x) - g(x)) dx|",
   "int from a to b of (f(x) + g(x)) dx"], ans=0,
   why="The absolute value inside the integral keeps each piece positive, which is exactly what splitting at the crossings accomplishes."),
 dict(q="The points at which the area integral must be split are found by", choices=[
   "solving f(x) = g(x)",
   "solving f'(x) = g'(x)",
   "setting f(x) = 0",
   "finding where f is increasing"], ans=0,
   why="A crossing is a point where the two curves have the same value."),
 dict(q="After finding the crossings, how do you decide which curve is on top on a subinterval?", choices=[
   "evaluate both functions at a test point inside that subinterval",
   "compare the values at the crossings",
   "the one with the larger leading coefficient is always on top",
   "compare the derivatives at the crossings"], ans=0,
   why="Between consecutive crossings the difference cannot change sign, so one test point settles the order for the whole subinterval."),
 dict(q="Two curves cross at three points inside an interval. Into how many subintervals is the area integral split?", choices=[
   "2",
   "3",
   "4",
   "6"], ans=2,
   why="Three interior crossings cut the interval into four pieces."),
 dict(q="What is the area of the region enclosed by y = x^3 and y = x?", choices=[
   "0",
   "1/4",
   "1/2",
   "1"], ans=2,
   why="They cross at -1, 0, and 1, and each of the two pieces has area 1/4."),
 dict(q="What is the area of the region between y = x^3 - x and the x-axis?", choices=[
   "0",
   "1/4",
   "1/2",
   "2"], ans=2,
   why="The zeros are -1, 0, and 1, and each piece contributes 1/4."),
 dict(q="What is the area of the region enclosed by y = x^3 and y = 4x?", choices=[
   "0",
   "4",
   "8",
   "16"], ans=2,
   why="They cross at -2, 0, and 2, and each piece has area 4."),
 dict(q="What is the area of the region enclosed by y = x^2 and y = x^4?", choices=[
   "2/15",
   "4/15",
   "1/3",
   "8/15"], ans=1,
   why="They cross at -1, 0, and 1, and each piece contributes 1/3 - 1/5 = 2/15."),
 dict(q="What is the area of the region enclosed by y = x and y = x^5?", choices=[
   "1/3",
   "1/2",
   "2/3",
   "4/3"], ans=2,
   why="They cross at -1, 0, and 1, and each piece contributes 1/2 - 1/6 = 1/3."),
 dict(q="What is the area of the region between y = sin(x) and y = cos(x) from x = 0 to x = pi?", choices=[
   "2*sqrt(2)",
   "sqrt(2)",
   "sqrt(2) - 1",
   "2"], ans=0,
   why="They cross at x = pi/4, and the two pieces contribute sqrt(2) - 1 and 1 + sqrt(2)."),
 dict(q="What is the area of the region between y = x^3 - 9x and the x-axis?", choices=[
   "0",
   "81/4",
   "81/2",
   "243/4"], ans=2,
   why="The zeros are -3, 0, and 3, and each of the two pieces contributes 81/4."),
 dict(q="What is the area of the region between y = cos(x) and the x-axis from x = 0 to x = 2pi?", choices=[
   "0",
   "1",
   "2",
   "4"], ans=3,
   why="Cosine changes sign at pi/2 and at 3pi/2, and the three pieces contribute 1, 2, and 1."),
 dict(q="What is the area of the region between y = x^3 - 4x and the x-axis from x = -2 to x = 2?", choices=[
   "0",
   "4",
   "8",
   "16"], ans=2,
   why="The zeros are -2, 0, and 2, and each of the two pieces has area 4."),
 dict(q="What is the area of the region enclosed by y = |x| and y = x^2?", choices=[
   "1/6",
   "1/3",
   "1/2",
   "2/3"], ans=1,
   why="They cross at -1, 0, and 1, and each piece contributes 1/2 - 1/3 = 1/6."),
 dict(q="What is the area of the region between y = sin(2x) and the x-axis from x = 0 to x = pi?", choices=[
   "0",
   "1",
   "2",
   "4"], ans=2,
   why="The zeros are 0, pi/2, and pi, and each piece contributes 1."),
 dict(q="What is the area of the region between y = x^4 - 4x^2 and the x-axis?", choices=[
   "64/15",
   "32/5",
   "128/15",
   "32/3"], ans=2,
   why="The zeros are -2, 0, and 2, and each piece contributes 64/15."),
 dict(q="What is the area of the region between y = x^3 and y = x^2 from x = -1 to x = 2?", choices=[
   "7/12",
   "2/3",
   "17/12",
   "25/12"], ans=3,
   why="The two curves swap order only at x = 1, so the area is 2/3 from [-1, 1] plus 17/12 from [1, 2]."),
 dict(q="What is the area of the region enclosed by y = 2x and y = x^3 + x^2?", choices=[
   "5/12",
   "8/3",
   "3",
   "37/12"], ans=3,
   why="They cross at -2, 0, and 1, and the pieces contribute 8/3 and 5/12."),
 dict(q="A student computes the area between y = x^3 and y = x on [-1, 1] as int from -1 to 1 of (x - x^3) dx and gets 0. What went wrong?", choices=[
   "the curves cross at x = 0, so the two halves cancel; each piece must be integrated with the correct order and the results added",
   "the antiderivative of x^3 is wrong",
   "the limits should be 0 to 1",
   "nothing; the enclosed area really is 0"], ans=0,
   why="Integrating a difference that changes sign lets the pieces cancel, which is why the region must be split at the crossing."),
 dict(q="For the region enclosed by y = x^3 and y = x, why is the total area twice the area of the piece on [0, 1]?", choices=[
   "both x^3 and x are odd, so the two pieces are congruent reflections through the origin",
   "the pieces happen to be equal only for these particular functions and there is no reason for it",
   "the interval [-1, 0] is the same length as [0, 1], which always forces equal areas",
   "the curves are symmetric about the y-axis"], ans=0,
   why="Odd symmetry maps the piece on [-1, 0] onto the piece on [0, 1] through the origin, preserving area."),
 dict(q="Does the area between y = x^2 - 1 and y = 1 - x^2 require splitting the integral?", choices=[
   "no, because the curves meet only at x = -1 and x = 1, with no crossing in between",
   "yes, because they cross at x = 0",
   "yes, because both are parabolas",
   "no, because the curves never meet"], ans=0,
   why="Setting the two equal gives 2x^2 = 2, so the only meeting points are the endpoints of the region."),
 dict(q="What is the area of the region between y = sin(x) and y = sin(2x) from x = 0 to x = pi?", choices=[
   "0",
   "1/4",
   "9/4",
   "5/2"], ans=3,
   why="They cross at x = pi/3 inside the interval, and the two pieces contribute 1/4 and 9/4."),
 dict(q="Which expression gives the area enclosed by y = x^3 and y = x?", choices=[
   "int from -1 to 0 of (x^3 - x) dx + int from 0 to 1 of (x - x^3) dx",
   "int from -1 to 1 of (x - x^3) dx",
   "int from -1 to 1 of (x^3 - x) dx",
   "int from 0 to 1 of (x - x^3) dx"], ans=0,
   why="On [-1, 0] the cubic is above the line and on [0, 1] the line is above the cubic."),
 dict(q="The line y = 2x - 1 meets y = x^2 only at x = 1, where it is tangent. What is the area enclosed by the two graphs?", choices=[
   "0, because a single point of tangency encloses no region",
   "1/3",
   "1/6",
   "the area is infinite"], ans=0,
   why="Two crossings are needed to bound a region; touching at one point leaves nothing enclosed."),
]
