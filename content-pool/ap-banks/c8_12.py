# CALC 8.12 Volume with Washer Method: Revolving Around Other Axes
# — 25 questions
# Both radii shift by the same constant: about y = k below the region,
# R = f(x) - k and r = g(x) - k; about y = k above it, the LOWER curve gives
# the outer radius. All volumes recomputed by sympy; see verify_c8_12.py.
TOPIC = ("8.12", "Volume with Washer Method: Revolving Around Other Axes", 8)
QUESTIONS = [
 dict(q="A region bounded above by y = f(x) and below by y = g(x) is revolved about the line y = k, which lies BELOW the region. The radii are", choices=[
   "R = f(x) - k and r = g(x) - k",
   "R = f(x) and r = g(x)",
   "R = f(x) - k and r = g(x)",
   "R = k - f(x) and r = k - g(x)"], ans=0,
   why="Every distance is measured from the line y = k, so both radii shift by the same k."),
 dict(q="A region bounded above by y = f(x) and below by y = g(x) is revolved about the line y = k, which lies ABOVE the region. Which curve gives the outer radius?", choices=[
   "the lower curve g, because it is farther from the axis, giving R = k - g(x)",
   "the upper curve f, because it is always the outer one",
   "whichever curve has the larger values",
   "neither; the radii are equal"], ans=0,
   why="Outer means farther from the axis, and when the axis is above the region the bottom of the region is the farther boundary."),
 dict(q="A student revolves the region between y = f(x) and y = g(x) about y = -1 and uses R = f(x) + 1 and r = g(x). What is the error?", choices=[
   "both radii must shift by the same amount, so r should be g(x) + 1",
   "the outer radius should be f(x) - 1",
   "the radii should not be shifted at all",
   "there is no error"], ans=0,
   why="Both distances are measured from the same line, so the shift applies to both boundaries."),
 dict(q="The region between y = x and y = x^2 is revolved about the line y = -1. What is the volume?", choices=[
   "7*pi/15",
   "8*pi/15",
   "2*pi/15",
   "pi/6"], ans=0,
   why="The radii are x + 1 and x^2 + 1, and the integral of the difference of their squares on [0, 1] is 7/15."),
 dict(q="The region between y = x and y = x^2 is revolved about the line y = 2. What is the volume?", choices=[
   "8*pi/15",
   "7*pi/15",
   "2*pi/15",
   "16*pi/15"], ans=0,
   why="The axis is above the region, so R = 2 - x^2 and r = 2 - x, and the integral gives 8/15."),
 dict(q="The region between y = sqrt(x) and y = x is revolved about the line y = 1. What is the volume?", choices=[
   "pi/6",
   "pi/3",
   "2*pi/15",
   "pi/2"], ans=0,
   why="The axis is above the region, so R = 1 - x and r = 1 - sqrt(x), and the integral of the difference of squares is 1/6."),
 dict(q="The region bounded by y = x^2 and y = 4 is revolved about the line y = 5. What is the volume?", choices=[
   "832*pi/15",
   "512*pi/15",
   "416*pi/15",
   "1088*pi/15"], ans=0,
   why="The axis is above the region, so R = 5 - x^2 and r = 1, and the integral over [-2, 2] gives 832/15."),
 dict(q="The region bounded by y = x^2 and y = 4 is revolved about the line y = -1. What is the volume?", choices=[
   "1088*pi/15",
   "832*pi/15",
   "512*pi/15",
   "544*pi/15"], ans=0,
   why="The radii are 5 and x^2 + 1, and the integral of the difference of their squares over [-2, 2] is 1088/15."),
 dict(q="The region between x = y and x = y^2 is revolved about the line x = -1. What is the volume?", choices=[
   "7*pi/15",
   "8*pi/15",
   "2*pi/15",
   "pi/6"], ans=0,
   why="The radii are y + 1 and y^2 + 1, and the integral of the difference of their squares on [0, 1] is 7/15."),
 dict(q="The region between x = y and x = y^2 is revolved about the line x = 2. What is the volume?", choices=[
   "8*pi/15",
   "7*pi/15",
   "2*pi/15",
   "16*pi/15"], ans=0,
   why="The axis is to the right of the region, so R = 2 - y^2 and r = 2 - y, and the integral gives 8/15."),
 dict(q="The region bounded by y = x, y = 0, and x = 2 is revolved about the line y = 3. What is the volume?", choices=[
   "28*pi/3",
   "14*pi/3",
   "8*pi/3",
   "56*pi/3"], ans=0,
   why="The axis is above the region, so R = 3 and r = 3 - x, and the integral of 6x - x^2 on [0, 2] is 28/3."),
 dict(q="The region bounded by y = sqrt(x), y = 0, and x = 4 is revolved about the line y = 2. What is the volume?", choices=[
   "40*pi/3",
   "20*pi/3",
   "8*pi/3",
   "16*pi/3"], ans=0,
   why="The axis is above the region, so R = 2 and r = 2 - sqrt(x), and the integral of 4*sqrt(x) - x on [0, 4] is 40/3."),
 dict(q="The region bounded by y = x^2, y = 0, and x = 1 is revolved about the line x = 2. What is the volume?", choices=[
   "5*pi/6",
   "5*pi/3",
   "pi/6",
   "7*pi/6"], ans=0,
   why="Slicing horizontally, R = 2 - sqrt(y) and r = 1, and the integral on [0, 1] gives 5/6."),
 dict(q="Which integral gives the volume when the region bounded by y = x^2 and y = 4 is revolved about the line y = 5?", choices=[
   "pi * int from -2 to 2 of ((5 - x^2)^2 - 1) dx",
   "pi * int from -2 to 2 of ((5 - x^2)^2 - 5^2) dx",
   "pi * int from -2 to 2 of ((x^2 - 5)^2 - 4^2) dx",
   "pi * int from -2 to 2 of (5 - x^2 - 1)^2 dx"], ans=0,
   why="The outer radius reaches from y = 5 down to the parabola and the inner radius reaches down to y = 4, a distance of 1."),
 dict(q="The region between y = x and y = x^2 on [0, 1] is revolved about y = -1. What is the OUTER radius?", choices=[
   "x + 1",
   "x^2 + 1",
   "x - 1",
   "1 - x"], ans=0,
   why="The upper curve y = x is farther from the line y = -1, and its distance from that line is x - (-1)."),
 dict(q="The region between y = x and y = x^2 on [0, 1] is revolved about y = -1. What is the INNER radius?", choices=[
   "x^2 + 1",
   "x + 1",
   "x^2 - 1",
   "1 - x^2"], ans=0,
   why="The nearer boundary is y = x^2, whose distance from y = -1 is x^2 + 1."),
 dict(q="The region between y = x and y = x^2 on [0, 1] is revolved about y = 3. What is the OUTER radius?", choices=[
   "3 - x^2",
   "3 - x",
   "x^2 + 3",
   "x + 3"], ans=0,
   why="With the axis above the region, the lower curve y = x^2 is farther away, at distance 3 - x^2."),
 dict(q="Why does moving the axis of revolution from y = 0 to y = -1 change the volume of the solid?", choices=[
   "every radius grows by 1, and squaring makes that change unequal across the region",
   "it does not change the volume",
   "the region itself changes",
   "the limits of integration change"], ans=0,
   why="The integrand involves squares of the radii, so adding a constant to both does not cancel."),
 dict(q="The region between y = x and y = x^2 on [0, 1] is revolved about the x-axis. Is the solid a disc solid or a washer solid?", choices=[
   "a washer solid, because the region does not touch the x-axis except at the endpoints",
   "a disc solid, because the region touches the axis at x = 0",
   "a washer solid, because both curves are increasing",
   "a disc solid, because the axis is a coordinate axis"], ans=0,
   why="Between the endpoints the region is separated from the axis by the curve y = x^2, so each slice has a hole."),
 dict(q="The region between y = 4 - x^2 and the x-axis is revolved about the line y = -2. What is the volume?", choices=[
   "384*pi/5",
   "192*pi/5",
   "768*pi/5",
   "128*pi/5"], ans=0,
   why="The radii are 6 - x^2 and 2, and the integral of the difference of their squares over [-2, 2] is 384/5."),
 dict(q="The region bounded by y = 1/x, y = 0, x = 1, and x = 2 is revolved about the line y = -1. What is the volume?", choices=[
   "pi/2 + 2*pi*ln(2)",
   "pi/2 - 2*pi*ln(2)",
   "2*pi*ln(2)",
   "pi/2"], ans=0,
   why="The radii are 1/x + 1 and 1, and the integrand 1/x^2 + 2/x integrates to 1/2 + 2ln(2)."),
 dict(q="The region bounded by y = x^3, y = 0, and x = 1 is revolved about the line y = 1. What is the volume?", choices=[
   "5*pi/14",
   "5*pi/7",
   "pi/7",
   "9*pi/14"], ans=0,
   why="The axis is above the region, so R = 1 and r = 1 - x^3, and the integrand 2x^3 - x^6 integrates to 5/14."),
 dict(q="When revolving about a line other than a coordinate axis, the volume formula", choices=[
   "is still pi times the integral of R^2 - r^2, with both radii measured from that line",
   "changes to 2pi times the integral of R - r",
   "requires the region to be in the first quadrant",
   "no longer involves pi"], ans=0,
   why="Only the expressions for the radii change; the washer formula itself is unchanged."),
 dict(q="A region lies entirely above the line y = k. Revolving it about y = k gives radii that are", choices=[
   "both nonnegative, since every point of the region is at or above the axis",
   "both negative",
   "one positive and one negative",
   "undefined"], ans=0,
   why="Distances from the axis to points of the region are nonnegative when the region lies on one side of it."),
 dict(q="The region bounded by y = x^2 and y = 4 is revolved first about y = 4 and then about y = 5. Which volume is larger?", choices=[
   "the one about y = 5, which is 832pi/15 against 512pi/15",
   "the one about y = 4, which is 832pi/15 against 512pi/15",
   "they are equal",
   "the comparison depends on the units"], ans=0,
   why="Pushing the axis farther away enlarges every outer radius more than it enlarges the hole."),
]
