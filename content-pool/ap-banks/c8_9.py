# CALC 8.9 Volume with Disc Method: Revolving Around the x- or y-Axis
# — 25 questions
# V = pi * int R^2, where R is the distance from the axis of revolution to the
# curve. Every volume is recomputed by sympy; see verify_c8_9.py.
TOPIC = ("8.9", "Volume with Disc Method: Revolving Around the x- or y-Axis", 8)
QUESTIONS = [
 dict(q="The region under y = f(x) from x = a to x = b is revolved about the x-axis. The volume of the resulting solid is", choices=[
   "pi * int from a to b of f(x)^2 dx",
   "pi * int from a to b of f(x) dx",
   "2*pi * int from a to b of f(x)^2 dx",
   "int from a to b of f(x)^2 dx"], ans=0,
   why="Each disc has radius f(x) and area pi*f(x)^2, and the thickness is dx."),
 dict(q="A region is revolved about the y-axis using discs. The volume is", choices=[
   "pi * int of (the radius as a function of y)^2 dy",
   "pi * int of (the radius as a function of x)^2 dx",
   "2*pi * int of x dy",
   "pi * int of y^2 dx"], ans=0,
   why="Discs perpendicular to the y-axis are indexed by y, so both the radius and the thickness must be expressed in y."),
 dict(q="When a region is revolved about the x-axis, the radius of a disc at position x is", choices=[
   "the distance from the x-axis to the curve, which is |f(x)|",
   "the value of x",
   "the width of the region",
   "f(x) - x"], ans=0,
   why="The radius of the circular slice is measured from the axis of revolution out to the boundary curve."),
 dict(q="The region bounded by y = x, y = 0, and x = 3 is revolved about the x-axis. What is the volume?", choices=[
   "9*pi",
   "3*pi",
   "27*pi",
   "18*pi"], ans=0,
   why="The volume is pi times the integral of x^2 from 0 to 3, which is 9pi."),
 dict(q="The region bounded by y = sqrt(x), y = 0, and x = 4 is revolved about the x-axis. What is the volume?", choices=[
   "8*pi",
   "16*pi",
   "4*pi",
   "32*pi/3"], ans=0,
   why="The volume is pi times the integral of x from 0 to 4, which is 8pi."),
 dict(q="The region bounded by y = x^2, y = 0, and x = 2 is revolved about the x-axis. What is the volume?", choices=[
   "32*pi/5",
   "8*pi/3",
   "32*pi/3",
   "16*pi/5"], ans=0,
   why="The volume is pi times the integral of x^4 from 0 to 2, which is 32pi/5."),
 dict(q="The region bounded by y = 1/x, y = 0, x = 1, and x = 3 is revolved about the x-axis. What is the volume?", choices=[
   "2*pi/3",
   "pi*ln(3)",
   "pi/3",
   "8*pi/9"], ans=0,
   why="The volume is pi times the integral of 1/x^2 from 1 to 3, which is pi(1 - 1/3) = 2pi/3."),
 dict(q="The region bounded by y = e^x, y = 0, x = 0, and x = 1 is revolved about the x-axis. What is the volume?", choices=[
   "pi*(e^2 - 1)/2",
   "pi*(e - 1)",
   "pi*(e^2 - 1)",
   "pi*(e - 1)^2"], ans=0,
   why="The volume is pi times the integral of e^(2x) from 0 to 1, which is pi(e^2 - 1)/2."),
 dict(q="The region bounded by y = sin(x) and the x-axis for 0 <= x <= pi is revolved about the x-axis. What is the volume?", choices=[
   "pi^2/2",
   "pi^2",
   "2*pi",
   "pi/2"], ans=0,
   why="The integral of sin^2(x) on [0, pi] is pi/2, and multiplying by pi gives pi^2/2."),
 dict(q="The region bounded by x = y^2, the y-axis, y = 0, and y = 2 is revolved about the y-axis. What is the volume?", choices=[
   "32*pi/5",
   "8*pi/3",
   "16*pi/5",
   "4*pi"], ans=0,
   why="The radius is y^2, so the volume is pi times the integral of y^4 from 0 to 2, which is 32pi/5."),
 dict(q="The region in the first quadrant bounded by y = x^2, y = 4, and the y-axis is revolved about the y-axis. What is the volume?", choices=[
   "8*pi",
   "16*pi",
   "32*pi/5",
   "4*pi"], ans=0,
   why="The radius is x = sqrt(y), so the volume is pi times the integral of y from 0 to 4, which is 8pi."),
 dict(q="The region bounded by y = 2x + 1, y = 0, x = 0, and x = 2 is revolved about the x-axis. What is the volume?", choices=[
   "62*pi/3",
   "31*pi/3",
   "125*pi/6",
   "25*pi"], ans=0,
   why="An antiderivative of (2x + 1)^2 is (2x + 1)^3/6, giving pi(125 - 1)/6 = 62pi/3."),
 dict(q="The region under y = sqrt(9 - x^2) from x = -3 to x = 3 is revolved about the x-axis. What is the volume, and what solid is it?", choices=[
   "36*pi, a sphere of radius 3",
   "18*pi, a hemisphere of radius 3",
   "9*pi, a cone",
   "27*pi, a cylinder"], ans=0,
   why="The integral of 9 - x^2 from -3 to 3 is 36, and 36pi agrees with (4/3)pi*3^3."),
 dict(q="The region bounded by y = 2x, y = 0, and x = 3 is revolved about the x-axis. What is the volume, and what solid is it?", choices=[
   "36*pi, a cone of radius 6 and height 3",
   "12*pi, a cone of radius 6 and height 3",
   "36*pi, a cylinder of radius 6",
   "108*pi, a cone of radius 6 and height 3"], ans=0,
   why="pi times the integral of 4x^2 from 0 to 3 is 36pi, which matches (1/3)pi(6^2)(3)."),
 dict(q="Which integral gives the volume of the solid formed by revolving the region under y = sqrt(x) from x = 0 to x = 4 about the x-axis?", choices=[
   "pi * int from 0 to 4 of x dx",
   "pi * int from 0 to 4 of sqrt(x) dx",
   "pi * int from 0 to 2 of y^4 dy",
   "int from 0 to 4 of pi*x^2 dx"], ans=0,
   why="Squaring the radius sqrt(x) gives x, and the region runs from x = 0 to x = 4."),
 dict(q="A student finds the volume of a solid of revolution as pi times the integral of f(x) rather than f(x)^2. What is the error?", choices=[
   "the area of a disc is pi times the radius SQUARED, so the integrand must be f(x)^2",
   "the constant should be 2pi",
   "the limits are wrong",
   "there is no error"], ans=0,
   why="Leaving the radius unsquared computes pi times an area, not a volume."),
 dict(q="The region bounded by y = x^3, y = 0, and x = 1 is revolved about the x-axis. What is the volume?", choices=[
   "pi/7",
   "pi/4",
   "pi/3",
   "pi/6"], ans=0,
   why="The volume is pi times the integral of x^6 from 0 to 1, which is pi/7."),
 dict(q="The region between y = 4 - x^2 and the x-axis is revolved about the x-axis. What is the volume?", choices=[
   "512*pi/15",
   "256*pi/15",
   "32*pi/3",
   "64*pi/3"], ans=0,
   why="The volume is pi times the integral of (4 - x^2)^2 from -2 to 2, which is 512pi/15."),
 dict(q="The region bounded by y = cos(x), y = 0, x = 0, and x = pi/2 is revolved about the x-axis. What is the volume?", choices=[
   "pi^2/4",
   "pi^2/2",
   "pi/2",
   "pi^2"], ans=0,
   why="The integral of cos^2(x) on [0, pi/2] is pi/4, and multiplying by pi gives pi^2/4."),
 dict(q="The region bounded by x = 1 - y^2 and the y-axis is revolved about the y-axis. What is the volume?", choices=[
   "16*pi/15",
   "8*pi/15",
   "4*pi/3",
   "32*pi/15"], ans=0,
   why="The radius is 1 - y^2 for -1 <= y <= 1, and pi times the integral of its square is 16pi/15."),
 dict(q="The region bounded by y = 2, y = 0, x = 0, and x = 5 is revolved about the x-axis. What is the volume?", choices=[
   "20*pi",
   "10*pi",
   "40*pi",
   "4*pi"], ans=0,
   why="The solid is a cylinder of radius 2 and height 5, and pi(4)(5) = 20pi."),
 dict(q="If x and y are in meters, a volume computed by the disc method has units of", choices=[
   "cubic meters",
   "square meters",
   "meters",
   "pi cubic meters"], ans=0,
   why="An area in square meters times a thickness in meters gives cubic meters, and pi is dimensionless."),
 dict(q="The region bounded by y = x^(1/3), y = 0, and x = 8 is revolved about the x-axis. What is the volume?", choices=[
   "96*pi/5",
   "48*pi/5",
   "32*pi/5",
   "24*pi"], ans=0,
   why="The volume is pi times the integral of x^(2/3) from 0 to 8, which is pi(3/5)(32) = 96pi/5."),
 dict(q="The region in the first quadrant bounded by y = x^2, y = 1, and the y-axis is revolved about the y-axis. What is the volume?", choices=[
   "pi/2",
   "pi/3",
   "pi/5",
   "2*pi/5"], ans=0,
   why="The radius is sqrt(y), so the volume is pi times the integral of y from 0 to 1, which is pi/2."),
 dict(q="A region is revolved about the x-axis, and a student writes the volume as pi times an integral with respect to y. What is wrong?", choices=[
   "discs perpendicular to the x-axis have thickness dx, so the integral must be taken in x with x-limits",
   "the constant should be 2pi",
   "the radius should not be squared",
   "nothing; either variable may be used with the same limits"], ans=0,
   why="The variable of integration has to match the direction in which the discs are stacked."),
]
