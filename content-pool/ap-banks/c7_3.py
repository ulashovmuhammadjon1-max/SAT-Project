# CALC 7.3 Sketching Slope Fields — 25 questions
# No figures exist in this bank, so slope fields are handled numerically
# (slopes computed at named points) and verbally (a field described in words).
# Slope computations verified with sympy; see verify_c7_3.py.
TOPIC = ("7.3", "Sketching Slope Fields", 7)
QUESTIONS = [
 dict(q="In the slope field for dy/dx = 2x - y, what is the slope of the segment drawn at the point (1, 3)?", choices=[
   "-1",
   "1",
   "2",
   "5"], ans=0,
   why="Substituting gives 2(1) - 3 = -1."),
 dict(q="In the slope field for dy/dx = x + y, what is the slope of the segment drawn at the point (-2, 5)?", choices=[
   "-7",
   "-3",
   "3",
   "7"], ans=2,
   why="Substituting gives -2 + 5 = 3."),
 dict(q="In the slope field for dy/dx = xy, what is the slope of the segment drawn at the point (3, -2)?", choices=[
   "-6",
   "-1",
   "1",
   "6"], ans=0,
   why="Substituting gives (3)(-2) = -6."),
 dict(q="In the slope field for dy/dx = y - 1, along which set of points are the segments horizontal?", choices=[
   "the horizontal line y = 1",
   "the vertical line x = 1",
   "the line y = x",
   "the x-axis"], ans=0,
   why="A segment is horizontal where dy/dx = 0, and y - 1 = 0 exactly on the line y = 1."),
 dict(q="In the slope field for dy/dx = x^2 - 4, along which set of points are the segments horizontal?", choices=[
   "the vertical lines x = -2 and x = 2",
   "the horizontal lines y = -2 and y = 2",
   "the single vertical line x = 4",
   "the x-axis only"], ans=0,
   why="x^2 - 4 = 0 when x = 2 or x = -2, and those are vertical lines in the plane."),
 dict(q="For which points is no segment drawn in the slope field for dy/dx = y/x?", choices=[
   "points on the y-axis, where x = 0",
   "points on the x-axis, where y = 0",
   "points where y = x",
   "points in the third quadrant"], ans=0,
   why="The expression y/x is undefined when x = 0, so the field has no segment along the y-axis."),
 dict(q="A slope field has the property that all segments lying on any single vertical line are parallel. Which differential equation is consistent with this?", choices=[
   "dy/dx = x^2 + 1",
   "dy/dx = y^2 + 1",
   "dy/dx = x + y",
   "dy/dx = xy"], ans=0,
   why="If dy/dx depends only on x, then every point with the same x-coordinate gets the same slope."),
 dict(q="A slope field has the property that all segments lying on any single horizontal line are parallel. Which differential equation is consistent with this?", choices=[
   "dy/dx = y^2 - 1",
   "dy/dx = x^2 - 1",
   "dy/dx = x - y",
   "dy/dx = x/y"], ans=0,
   why="If dy/dx depends only on y, then every point with the same y-coordinate gets the same slope."),
 dict(q="In the slope field for dy/dx = x - y, the segments are horizontal at exactly which points?", choices=[
   "the points on the line y = x",
   "the points on the line y = -x",
   "the points on the x-axis",
   "the origin only"], ans=0,
   why="x - y = 0 precisely when y = x."),
 dict(q="Every segment in a certain slope field has slope 4. Which differential equation produced it?", choices=[
   "dy/dx = 4",
   "dy/dx = 4x",
   "dy/dx = 4y",
   "dy/dx = x + 4"], ans=0,
   why="Only a constant right-hand side gives the same slope at every point of the plane."),
 dict(q="In the slope field for dy/dx = xy, in which quadrants do the segments have positive slope?", choices=[
   "the first and third quadrants",
   "the second and fourth quadrants",
   "the first and second quadrants",
   "all four quadrants"], ans=0,
   why="The product xy is positive when x and y have the same sign, which happens in quadrants I and III."),
 dict(q="In the slope field for dy/dx = -x/y, what is the slope of the segment drawn at the point (3, 4)?", choices=[
   "-4/3",
   "-3/4",
   "3/4",
   "4/3"], ans=1,
   why="Substituting gives -3/4."),
 dict(q="A slope field has horizontal segments everywhere on the x-axis, segments of positive slope above the x-axis that steepen as y increases, and segments of negative slope below it. The slope does not depend on x. Which differential equation produced it?", choices=[
   "dy/dx = y",
   "dy/dx = x",
   "dy/dx = -y",
   "dy/dx = y^2"], ans=0,
   why="The slope equals the y-coordinate: zero on the x-axis, positive and growing above it, negative below."),
 dict(q="A slope field has horizontal segments on the x-axis, negative slopes above the x-axis, and positive slopes below it, with steepness independent of x. Which differential equation produced it?", choices=[
   "dy/dx = -y",
   "dy/dx = y",
   "dy/dx = -x",
   "dy/dx = -xy"], ans=0,
   why="The slope is the negative of the y-coordinate, so it is negative when y > 0 and positive when y < 0."),
 dict(q="In the slope field for dy/dx = sin(x), the segments are horizontal along which lines?", choices=[
   "the vertical lines x = n*pi for every integer n",
   "the horizontal lines y = n*pi for every integer n",
   "the vertical lines x = pi/2 + n*pi for every integer n",
   "the x-axis only"], ans=0,
   why="sin(x) = 0 exactly when x is an integer multiple of pi, and that condition describes vertical lines."),
 dict(q="In the slope field for dy/dx = x(y - 2), the segments are horizontal at exactly which points?", choices=[
   "the points on the line y = 2 together with the points on the y-axis",
   "the points on the line y = 2 only",
   "the points on the y-axis only",
   "the point (0, 2) only"], ans=0,
   why="A product is zero when either factor is zero, so x = 0 or y = 2."),
 dict(q="In the slope field for dy/dx = x + 2y, what is the slope of the segment drawn at the point (2, -3)?", choices=[
   "-4",
   "-1",
   "1",
   "8"], ans=0,
   why="Substituting gives 2 + 2(-3) = -4."),
 dict(q="For which differential equation does the slope field assign the same slope at (1, 2) as at (1, -2)?", choices=[
   "dy/dx = x + y^2",
   "dy/dx = x + y",
   "dy/dx = xy",
   "dy/dx = y/x"], ans=0,
   why="Only y^2 is unchanged when y is replaced by -y, giving 5 at both points."),
 dict(q="On which part of the plane does the slope field for dy/dx = ln(y) exist?", choices=[
   "only where y > 0",
   "only where y is not 0",
   "only where x > 0",
   "the entire plane"], ans=0,
   why="The natural logarithm is defined only for positive inputs, so no segments are drawn where y is 0 or negative."),
 dict(q="In the slope field for dy/dx = sqrt(x), what is the slope of the segment drawn at (9, -4), and where does the field exist?", choices=[
   "slope 3, and the field exists only where x is greater than or equal to 0",
   "slope 3, and the field exists on the whole plane",
   "slope 81, and the field exists only where x is greater than or equal to 0",
   "slope -3, and the field exists only where x is greater than or equal to 0"], ans=0,
   why="sqrt(9) = 3, and the square root requires a nonnegative input, so the field is empty for x < 0."),
 dict(q="A slope field has exactly one horizontal segment, at the origin, and its segments grow steeper the farther a point lies from the origin, always with positive slope elsewhere. Which differential equation produced it?", choices=[
   "dy/dx = x^2 + y^2",
   "dy/dx = x + y",
   "dy/dx = xy",
   "dy/dx = x^2 - y^2"], ans=0,
   why="A sum of squares is zero only at the origin and grows with distance from it, and it is never negative."),
 dict(q="For which differential equation does no segment in the slope field have a negative slope?", choices=[
   "dy/dx = y^2",
   "dy/dx = y",
   "dy/dx = x",
   "dy/dx = x - y"], ans=0,
   why="A square is never negative, so every segment is horizontal or rising."),
 dict(q="In the slope field for dy/dx = x - 1, which description is correct?", choices=[
   "segments are horizontal along the vertical line x = 1, fall to the left of it, and rise to the right of it",
   "segments are horizontal along the horizontal line y = 1, fall below it, and rise above it",
   "segments have slope 1 everywhere",
   "segments are horizontal only at the point (1, 1)"], ans=0,
   why="x - 1 is zero at x = 1, negative for x < 1, and positive for x > 1, and each of those conditions describes a vertical strip."),
 dict(q="A student claims that the segments in the slope field for dy/dx = 2 get steeper as x increases. What is wrong with this claim?", choices=[
   "The right side does not depend on x, so every segment in the whole plane has slope 2",
   "Nothing is wrong; the slope is 2x",
   "The segments actually get steeper as y increases",
   "The field has no segments at all"], ans=0,
   why="A constant derivative gives one common slope everywhere; steepness cannot change."),
 dict(q="In the slope field for dy/dx = e^(-x^2), which statement is true?", choices=[
   "every segment has positive slope, and the segments flatten as |x| grows",
   "every segment has positive slope, and the segments steepen as |x| grows",
   "the segments are horizontal along the y-axis",
   "the segments have negative slope when x is negative"], ans=0,
   why="An exponential is always positive, and e^(-x^2) decreases toward 0 as |x| increases, so the segments flatten."),
]
