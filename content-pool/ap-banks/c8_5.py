# CALC 8.5 Finding the Area Between Curves Expressed as Functions of y
# — 25 questions
# Horizontal rectangles: width is (right minus left), integrated with respect to
# y. Every area is recomputed by sympy; see verify_c8_5.py.
TOPIC = ("8.5", "Finding the Area Between Curves Expressed as Functions of y", 8)
QUESTIONS = [
 dict(q="If the curve x = f(y) lies to the right of x = g(y) for c <= y <= d, the area between them is", choices=[
   "int from c to d of (f(y) - g(y)) dy",
   "int from c to d of (g(y) - f(y)) dy",
   "int from c to d of (f(y) - g(y)) dx",
   "int from g(y) to f(y) of (d - c) dy"], ans=0,
   why="A horizontal rectangle has width equal to the right boundary minus the left boundary."),
 dict(q="When a region is sliced with horizontal rectangles, the width of a representative rectangle is", choices=[
   "the right-hand x-value minus the left-hand x-value at that y",
   "the top y-value minus the bottom y-value",
   "the height of the region",
   "the sum of the two x-values"], ans=0,
   why="A horizontal strip stretches from the left boundary curve across to the right boundary curve."),
 dict(q="Integrating with respect to y is usually the better choice when", choices=[
   "the left and right boundaries of the region are each a single function of y",
   "the region is symmetric about the y-axis",
   "the curves are given as y = f(x)",
   "the region lies in the first quadrant"], ans=0,
   why="Horizontal slices avoid splitting the region when the boundaries are naturally expressed as x in terms of y."),
 dict(q="What is the area of the region bounded by x = y^2 and x = 4?", choices=[
   "16/3",
   "8",
   "32/3",
   "16"], ans=2,
   why="The curves meet at y = -2 and y = 2, and the integral of 4 - y^2 there is 32/3."),
 dict(q="What is the area of the region bounded by x = y^2 and x = y?", choices=[
   "1/6",
   "1/3",
   "1/2",
   "2/3"], ans=0,
   why="They meet at y = 0 and y = 1, and on that interval y is to the right of y^2, giving 1/2 - 1/3 = 1/6."),
 dict(q="What is the area of the region between x = y and x = y^3 for 0 <= y <= 1?", choices=[
   "1/4",
   "1/3",
   "1/2",
   "3/4"], ans=0,
   why="On [0, 1] the curve x = y is to the right, and 1/2 - 1/4 = 1/4."),
 dict(q="The region under y = sqrt(x) from x = 0 to x = 4 and above the x-axis is integrated with respect to y. What is its area?", choices=[
   "8/3",
   "16/3",
   "8",
   "32/3"], ans=1,
   why="Horizontal strips run from x = y^2 to x = 4 for 0 <= y <= 2, and the integral of 4 - y^2 there is 16/3."),
 dict(q="What is the area of the region between x = sqrt(y) and x = y/2 for 0 <= y <= 4?", choices=[
   "2/3",
   "4/3",
   "8/3",
   "16/3"], ans=1,
   why="On [0, 4] the curve x = sqrt(y) is to the right, and 16/3 - 4 = 4/3."),
 dict(q="What is the area of the region bounded by x = y^2 and x = y + 2?", choices=[
   "5/2",
   "7/2",
   "9/2",
   "9"], ans=2,
   why="They meet at y = -1 and y = 2, and the integral of y + 2 - y^2 over that interval is 9/2."),
 dict(q="What is the area of the region bounded by x = y^2 and x = 2 - y^2?", choices=[
   "4/3",
   "8/3",
   "4",
   "16/3"], ans=1,
   why="They meet at y = -1 and y = 1, and the integral of 2 - 2y^2 there is 4 - 4/3 = 8/3."),
 dict(q="What is the area of the region bounded by x = 4y - y^2 and the y-axis?", choices=[
   "16/3",
   "32/3",
   "16",
   "64/3"], ans=1,
   why="The curve meets x = 0 at y = 0 and y = 4, and the integral of 4y - y^2 there is 32 - 64/3 = 32/3."),
 dict(q="What is the area of the region bounded by x = e^y, the y-axis, y = 0, and y = 1?", choices=[
   "e - 1",
   "e",
   "e + 1",
   "1"], ans=0,
   why="Horizontal strips have width e^y, and the integral from 0 to 1 is e - 1."),
 dict(q="What is the area of the region bounded by x = sin(y), the y-axis, y = 0, and y = pi?", choices=[
   "2",
   "1",
   "0",
   "pi"], ans=0,
   why="The strips have width sin(y), which is nonnegative on [0, pi], and its integral is 2."),
 dict(q="What is the area of the region bounded by x = y^2 and x = 8 - y^2?", choices=[
   "32/3",
   "16",
   "64/3",
   "32"], ans=2,
   why="They meet at y = -2 and y = 2, and the integral of 8 - 2y^2 there is 32 - 32/3 = 64/3."),
 dict(q="Solved for x, the line y = 2x + 1 becomes", choices=[
   "x = (y - 1)/2",
   "x = 2y - 1",
   "x = (y + 1)/2",
   "x = y/2 - 1"], ans=0,
   why="Subtracting 1 and dividing by 2 isolates x."),
 dict(q="For x greater than or equal to 0, the curve y = x^2 solved for x is", choices=[
   "x = sqrt(y)",
   "x = -sqrt(y)",
   "x = y^2",
   "x = y/2"], ans=0,
   why="Taking the nonnegative square root inverts the relation on that branch."),
 dict(q="The region bounded by y = x^2, y = 0, and x = 2 is sliced horizontally. What is its area?", choices=[
   "4/3",
   "8/3",
   "4",
   "16/3"], ans=1,
   why="Strips run from x = sqrt(y) to x = 2 for 0 <= y <= 4, and the integral of 2 - sqrt(y) is 8 - 16/3 = 8/3."),
 dict(q="Which integral gives the area of the region bounded by x = y^2 - 4 and the y-axis?", choices=[
   "int from -2 to 2 of (4 - y^2) dy",
   "int from -2 to 2 of (y^2 - 4) dy",
   "int from 0 to 2 of (4 - y^2) dy",
   "int from -4 to 0 of (4 - y^2) dy"], ans=0,
   why="The parabola lies to the left of the y-axis between y = -2 and y = 2, so the width is 0 - (y^2 - 4)."),
 dict(q="A student computes the area of a region sliced horizontally as int of (top - bottom) dy. What is the error?", choices=[
   "with horizontal slices the integrand must be right minus left, expressed as functions of y",
   "the limits should be x-values",
   "there is no error",
   "horizontal slices require an integral with respect to x"], ans=0,
   why="Top-minus-bottom belongs to vertical slices; a horizontal strip's dimension across is right minus left."),
 dict(q="What is the area of the region bounded by x = 2y and x = y^2?", choices=[
   "2/3",
   "4/3",
   "8/3",
   "4"], ans=1,
   why="They meet at y = 0 and y = 2, and the integral of 2y - y^2 there is 4 - 8/3 = 4/3."),
 dict(q="What is the area of the region bounded by x = 1/y, the y-axis, y = 1, and y = 2?", choices=[
   "ln(2)",
   "1/2",
   "ln(2) - 1",
   "2"], ans=0,
   why="The strips have width 1/y, and the integral from 1 to 2 is ln(2) - ln(1) = ln(2)."),
 dict(q="What is the area of the region between x = y^2 and x = y^4 for 0 <= y <= 1?", choices=[
   "1/15",
   "2/15",
   "1/3",
   "8/15"], ans=1,
   why="On [0, 1] the curve x = y^2 is to the right, and 1/3 - 1/5 = 2/15."),
 dict(q="What are the limits of integration for the area of the region bounded by x = y^2 and x = y + 6, integrating with respect to y?", choices=[
   "from y = -2 to y = 3",
   "from y = -3 to y = 2",
   "from y = 0 to y = 3",
   "from x = -2 to x = 3"], ans=0,
   why="Setting y^2 = y + 6 gives y^2 - y - 6 = 0, whose roots are y = -2 and y = 3."),
 dict(q="What is the area of the region bounded by x = y^2 and x = y + 6?", choices=[
   "25/6",
   "20",
   "125/6",
   "125/3"], ans=2,
   why="Integrating y + 6 - y^2 from y = -2 to y = 3 gives 125/6."),
 dict(q="For the region enclosed by y = x and y = x^2, which statement is correct?", choices=[
   "it can be computed either way, and both integrals give 1/6",
   "only an integral with respect to x can be used",
   "only an integral with respect to y can be used",
   "the two methods give different answers"], ans=0,
   why="The region is bounded above and below by single functions of x and also left and right by single functions of y, so both set-ups apply and both give 1/6."),
]
