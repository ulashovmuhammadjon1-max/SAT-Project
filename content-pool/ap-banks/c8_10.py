# CALC 8.10 Volume with Disc Method: Revolving Around Other Axes — 25 questions
# The whole difficulty is the RADIUS: revolving about y = k makes it
# |f(x) - k|, and about x = h it is |g(y) - h|. Several questions turn on
# nothing else. All volumes recomputed by sympy; see verify_c8_10.py.
TOPIC = ("8.10", "Volume with Disc Method: Revolving Around Other Axes", 8)
QUESTIONS = [
 dict(q="A region bounded above by y = f(x) and below by the line y = k is revolved about the line y = k. The radius of a disc at position x is", choices=[
   "f(x) - k",
   "f(x)",
   "f(x) + k",
   "k - f(x)"], ans=0,
   why="The radius is the distance from the axis of revolution y = k out to the curve."),
 dict(q="A region bounded on the right by x = g(y) and on the left by the line x = h is revolved about the line x = h. The radius of a disc at height y is", choices=[
   "g(y) - h",
   "g(y)",
   "g(y) + h",
   "h"], ans=0,
   why="The radius is the horizontal distance from the vertical axis x = h out to the curve."),
 dict(q="When can the disc method (rather than the washer method) be used for a revolution about a line that is not a coordinate axis?", choices=[
   "when the line of revolution is itself a boundary of the region, so the solid has no hole",
   "whenever the line is horizontal",
   "whenever the region lies in the first quadrant",
   "never; a non-axis line always requires washers"], ans=0,
   why="A hole appears only when the region is separated from the axis, and touching the axis leaves the solid solid."),
 dict(q="The region bounded by y = x^2 and y = 4 is revolved about the line y = 4. What is the volume?", choices=[
   "512*pi/15",
   "256*pi/15",
   "64*pi/3",
   "32*pi/5"], ans=0,
   why="The radius is 4 - x^2 for -2 <= x <= 2, and pi times the integral of its square is 512pi/15."),
 dict(q="The region bounded by y = sqrt(x), y = 1, x = 1, and x = 4 is revolved about the line y = 1. What is the volume?", choices=[
   "7*pi/6",
   "7*pi/3",
   "5*pi/6",
   "15*pi/2"], ans=0,
   why="The radius is sqrt(x) - 1, and the integral of its square from 1 to 4 is 7/6."),
 dict(q="The region bounded by y = x, y = 3, and the y-axis is revolved about the line y = 3. What is the volume?", choices=[
   "9*pi",
   "27*pi",
   "3*pi",
   "18*pi"], ans=0,
   why="The radius is 3 - x for 0 <= x <= 3, and pi times the integral of (3 - x)^2 is 9pi."),
 dict(q="The region bounded by x = y^2 and x = 9 is revolved about the line x = 9. What is the volume?", choices=[
   "1296*pi/5",
   "648*pi/5",
   "324*pi/5",
   "1296*pi/15"], ans=0,
   why="The radius is 9 - y^2 for -3 <= y <= 3, and pi times the integral of its square is 1296pi/5."),
 dict(q="The region bounded by y = e^x, y = 1, x = 0, and x = 1 is revolved about the line y = 1. What is the volume?", choices=[
   "pi*(e^2 - 4e + 5)/2",
   "pi*(e^2 - 1)/2",
   "pi*(e - 1)^2",
   "pi*(e^2 - 2e)/2"], ans=0,
   why="The radius is e^x - 1, and expanding gives the integral (e^2 - 1)/2 - 2(e - 1) + 1."),
 dict(q="The region bounded by y = 1 - x^2 and y = 1 is revolved about the line y = 1. What is the volume?", choices=[
   "2*pi/5",
   "4*pi/5",
   "pi/5",
   "16*pi/15"], ans=0,
   why="The radius is 1 - (1 - x^2) = x^2 for -1 <= x <= 1, and pi times the integral of x^4 is 2pi/5."),
 dict(q="The region bounded by y = 4 - x^2 and y = 3 is revolved about the line y = 3. What is the volume?", choices=[
   "16*pi/15",
   "8*pi/15",
   "32*pi/15",
   "4*pi/3"], ans=0,
   why="The radius is (4 - x^2) - 3 = 1 - x^2 for -1 <= x <= 1, and pi times the integral of its square is 16pi/15."),
 dict(q="The region bounded by y = x, y = 0, and x = 2 is revolved about the line x = 2. What is the volume?", choices=[
   "8*pi/3",
   "4*pi/3",
   "16*pi/3",
   "8*pi"], ans=0,
   why="Slicing horizontally, the radius is 2 - y for 0 <= y <= 2, and pi times the integral of its square is 8pi/3."),
 dict(q="A student revolves the region bounded by y = x^2 and y = 4 about the line y = 4 and uses radius x^2. What is the error?", choices=[
   "the radius is measured from y = 4, so it is 4 - x^2, not x^2",
   "the radius should be x",
   "the limits should be 0 to 2",
   "there is no error"], ans=0,
   why="Using the function value instead of its distance from the axis measures from the wrong line."),
 dict(q="Which integral gives the volume when the region bounded by y = x^2 and y = 4 is revolved about the line y = 4?", choices=[
   "pi * int from -2 to 2 of (4 - x^2)^2 dx",
   "pi * int from -2 to 2 of (x^2 - 4) dx",
   "pi * int from -2 to 2 of (x^2)^2 dx",
   "pi * int from 0 to 4 of (4 - y)^2 dy"], ans=0,
   why="The radius 4 - x^2 is squared and integrated across the full span of the region."),
 dict(q="The region bounded by y = 2x, y = 6, and the y-axis is revolved about the line y = 6. What is the volume?", choices=[
   "36*pi",
   "18*pi",
   "72*pi",
   "12*pi"], ans=0,
   why="The radius is 6 - 2x for 0 <= x <= 3, and pi times the integral of its square is 36pi."),
 dict(q="The region bounded by x = y, x = 4, and y = 0 is revolved about the line x = 4. What is the volume?", choices=[
   "64*pi/3",
   "32*pi/3",
   "16*pi/3",
   "64*pi"], ans=0,
   why="The radius is 4 - y for 0 <= y <= 4, and pi times the integral of its square is 64pi/3."),
 dict(q="When revolving about the line y = k, why is the radius written as an absolute value |f(x) - k|?", choices=[
   "a radius is a distance and cannot be negative, though squaring it makes the sign irrelevant in the integral",
   "because f may be undefined",
   "because k may be negative",
   "because the disc may have a hole"], ans=0,
   why="The distance from the axis is nonnegative, and since the integrand uses the square, either order of subtraction gives the same volume."),
 dict(q="The region bounded by y = sqrt(x), y = 2, and the y-axis is revolved about the line y = 2. What is the volume?", choices=[
   "8*pi/3",
   "16*pi/3",
   "4*pi/3",
   "32*pi/3"], ans=0,
   why="The radius is 2 - sqrt(x) for 0 <= x <= 4, and the integral of its square is 8/3."),
 dict(q="A single region is revolved first about the x-axis and then about the line y = 1, with the line y = 1 a boundary in the second case. What is true of the two volumes?", choices=[
   "they are generally different, because the radius is measured from a different line",
   "they are always equal",
   "the second is always larger",
   "the second is always exactly pi times the first"], ans=0,
   why="Changing the axis changes every radius, so the two integrals are not the same."),
 dict(q="The region bounded by y = x^3, y = 8, and the y-axis is revolved about the line y = 8. What is the volume?", choices=[
   "576*pi/7",
   "288*pi/7",
   "64*pi",
   "128*pi/7"], ans=0,
   why="The radius is 8 - x^3 for 0 <= x <= 2, and the integral of its square is 576/7."),
 dict(q="The region bounded by x = 4 - y^2 and x = 4 is revolved about the line x = 4. What is the volume?", choices=[
   "64*pi/5",
   "32*pi/5",
   "128*pi/5",
   "16*pi/5"], ans=0,
   why="The radius is 4 - (4 - y^2) = y^2 for -2 <= y <= 2, and pi times the integral of y^4 is 64pi/5."),
 dict(q="The region bounded by y = cos(x), y = 1, x = 0, and x = pi/2 is revolved about the line y = 1. What is the volume?", choices=[
   "3*pi^2/4 - 2*pi",
   "3*pi^2/4",
   "pi^2/4 - 2*pi",
   "pi^2/2 - pi"], ans=0,
   why="The radius is 1 - cos(x), and the integral of its square on [0, pi/2] is 3pi/4 - 2."),
 dict(q="The region bounded by y = 1/x, y = 1, x = 1, and x = 2 is revolved about the line y = 1. What is the volume?", choices=[
   "3*pi/2 - 2*pi*ln(2)",
   "pi/2 - 2*pi*ln(2)",
   "3*pi/2 + 2*pi*ln(2)",
   "2*pi*ln(2)"], ans=0,
   why="The radius is 1 - 1/x, and expanding gives 1 - 2ln(2) + 1/2 for the integral."),
 dict(q="A region bounded above by y = f(x) and below by the line y = -3 is revolved about y = -3. The radius is", choices=[
   "f(x) + 3",
   "f(x) - 3",
   "3 - f(x)",
   "f(x)"], ans=0,
   why="The distance from y = -3 up to the curve is f(x) - (-3) = f(x) + 3."),
 dict(q="The region bounded by y = x^2 and y = 4 is revolved about the line y = 5. Which method is required?", choices=[
   "the washer method, because the region does not touch y = 5 and the solid has a hole",
   "the disc method, because the region is bounded by y = 4",
   "the disc method, with radius 5 - x^2",
   "neither method applies"], ans=0,
   why="A gap of 1 unit between the region and the axis of revolution is hollowed out, which is exactly what a washer accounts for."),
 dict(q="For the region bounded by y = sqrt(x) and y = 1 on 1 <= x <= 4, what is the radius of a disc when the region is revolved about the line y = 1?", choices=[
   "sqrt(x) - 1",
   "sqrt(x)",
   "1 - sqrt(x)",
   "sqrt(x) + 1"], ans=0,
   why="On this interval sqrt(x) is at least 1, so the distance from the line up to the curve is sqrt(x) - 1."),
]
