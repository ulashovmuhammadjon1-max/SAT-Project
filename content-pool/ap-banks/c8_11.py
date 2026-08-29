# CALC 8.11 Volume with Washer Method: Revolving Around the x- or y-Axis
# — 25 questions
# V = pi * int (R^2 - r^2). The squares are subtracted, never the radii.
# All volumes recomputed by sympy; see verify_c8_11.py.
TOPIC = ("8.11", "Volume with Washer Method: Revolving Around the x- or y-Axis", 8)
QUESTIONS = [
 dict(q="A region is revolved about the x-axis, producing a solid with a hole. If R(x) is the outer radius and r(x) the inner radius, the volume is", choices=[
   "pi * int of (R(x)^2 - r(x)^2) dx",
   "pi * int of (R(x) - r(x))^2 dx",
   "pi * int of (R(x) - r(x)) dx",
   "2*pi * int of (R(x) - r(x)) dx"], ans=0,
   why="The area of a washer is the outer circle's area minus the inner circle's area, which subtracts the squares."),
 dict(q="A student computes a washer volume as pi times the integral of (R - r)^2. Why is this wrong?", choices=[
   "the area of a washer is pi*R^2 - pi*r^2, and (R - r)^2 is not equal to R^2 - r^2",
   "the constant should be 2pi",
   "the radii should not be squared at all",
   "it is not wrong"], ans=0,
   why="Expanding (R - r)^2 gives R^2 - 2Rr + r^2, which is a different quantity entirely."),
 dict(q="The region between y = x and y = x^2 is revolved about the x-axis. What is the volume?", choices=[
   "2*pi/15",
   "pi/6",
   "pi/15",
   "4*pi/15"], ans=0,
   why="On [0, 1] the outer radius is x and the inner is x^2, and pi(1/3 - 1/5) = 2pi/15."),
 dict(q="The region between y = sqrt(x) and y = x is revolved about the x-axis. What is the volume?", choices=[
   "pi/6",
   "pi/3",
   "2*pi/15",
   "pi/2"], ans=0,
   why="On [0, 1] the outer radius is sqrt(x) and the inner is x, and pi(1/2 - 1/3) = pi/6."),
 dict(q="The region bounded by y = 4 and y = x^2 is revolved about the x-axis. What is the volume?", choices=[
   "256*pi/5",
   "128*pi/5",
   "512*pi/15",
   "64*pi/5"], ans=0,
   why="The outer radius is 4 and the inner is x^2 for -2 <= x <= 2, and pi(64 - 64/5) = 256pi/5."),
 dict(q="The region bounded by y = 2, y = 1/x, x = 1, and x = 2 is revolved about the x-axis. What is the volume?", choices=[
   "7*pi/2",
   "5*pi/2",
   "7*pi/4",
   "4*pi"], ans=0,
   why="The outer radius is 2 and the inner is 1/x, and pi(4 - 1/2) = 7pi/2."),
 dict(q="The region between y = x^2 and y = x^3 is revolved about the x-axis. What is the volume?", choices=[
   "2*pi/35",
   "pi/35",
   "4*pi/35",
   "2*pi/15"], ans=0,
   why="On [0, 1] the outer radius is x^2 and the inner is x^3, and pi(1/5 - 1/7) = 2pi/35."),
 dict(q="The region between x = y and x = y^2 is revolved about the y-axis. What is the volume?", choices=[
   "2*pi/15",
   "pi/6",
   "pi/15",
   "4*pi/15"], ans=0,
   why="On [0, 1] the outer radius is y and the inner is y^2, and pi(1/3 - 1/5) = 2pi/15."),
 dict(q="The region between y = x and y = x^2 is revolved about the y-axis. What is the volume?", choices=[
   "pi/6",
   "2*pi/15",
   "pi/3",
   "pi/2"], ans=0,
   why="In terms of y the outer radius is sqrt(y) and the inner is y, and pi(1/2 - 1/3) = pi/6."),
 dict(q="In a washer set-up, the outer radius R is", choices=[
   "the distance from the axis of revolution to the farther boundary curve",
   "always the larger function value, regardless of the axis",
   "the distance between the two curves",
   "the same as the inner radius plus 1"], ans=0,
   why="Both radii are distances measured from the axis, and the farther boundary gives the outer one."),
 dict(q="The region bounded by y = e^x, y = 1, x = 0, and x = 1 is revolved about the x-axis. What is the volume?", choices=[
   "pi*(e^2 - 3)/2",
   "pi*(e^2 - 1)/2",
   "pi*(e^2 - 4e + 5)/2",
   "pi*(e - 1)^2"], ans=0,
   why="The outer radius is e^x and the inner is 1, so the volume is pi[(e^2 - 1)/2 - 1]."),
 dict(q="The region bounded by y = 4 - x^2 and y = 3 is revolved about the x-axis. What is the volume?", choices=[
   "136*pi/15",
   "68*pi/15",
   "16*pi/15",
   "272*pi/15"], ans=0,
   why="For -1 <= x <= 1 the outer radius is 4 - x^2 and the inner is 3, and the integral of the difference of squares is 136/15."),
 dict(q="Which integral gives the volume when the region between y = x and y = x^2 is revolved about the x-axis?", choices=[
   "pi * int from 0 to 1 of (x^2 - x^4) dx",
   "pi * int from 0 to 1 of (x - x^2)^2 dx",
   "pi * int from 0 to 1 of (x^4 - x^2) dx",
   "pi * int from 0 to 1 of (x - x^2) dx"], ans=0,
   why="The squares of the two radii are x^2 and x^4, and the outer one comes first."),
 dict(q="The region between y = 2x and y = x^2 is revolved about the x-axis. What is the volume?", choices=[
   "64*pi/15",
   "32*pi/15",
   "128*pi/15",
   "16*pi/3"], ans=0,
   why="On [0, 2] the outer radius is 2x and the inner is x^2, and pi(32/3 - 32/5) = 64pi/15."),
 dict(q="The region bounded by x = 4 and x = y^2 is revolved about the y-axis. What is the volume?", choices=[
   "256*pi/5",
   "128*pi/5",
   "512*pi/15",
   "64*pi/5"], ans=0,
   why="The outer radius is 4 and the inner is y^2 for -2 <= y <= 2, and pi(64 - 64/5) = 256pi/5."),
 dict(q="The region bounded by y = 1, y = 1/x, x = 1, and x = 3 is revolved about the x-axis. What is the volume?", choices=[
   "4*pi/3",
   "2*pi/3",
   "8*pi/3",
   "2*pi"], ans=0,
   why="The outer radius is 1 and the inner is 1/x, and pi(2 - 2/3) = 4pi/3."),
 dict(q="The washer method reduces to the disc method exactly when", choices=[
   "the inner radius is 0, meaning the region touches the axis of revolution",
   "the outer radius is constant",
   "the region is symmetric",
   "the axis is the y-axis"], ans=0,
   why="With r = 0 the formula pi(R^2 - r^2) collapses to pi*R^2."),
 dict(q="The region bounded by y = 1, y = sin(x), x = 0, and x = pi/2 is revolved about the x-axis. What is the volume?", choices=[
   "pi^2/4",
   "pi^2/2",
   "pi/4",
   "pi^2"], ans=0,
   why="The integrand is 1 - sin^2(x) = cos^2(x), whose integral on [0, pi/2] is pi/4."),
 dict(q="The region between y = x and y = x^3 for 0 <= x <= 1 is revolved about the x-axis. What is the volume?", choices=[
   "4*pi/21",
   "2*pi/21",
   "8*pi/21",
   "pi/7"], ans=0,
   why="The outer radius is x and the inner is x^3, and pi(1/3 - 1/7) = 4pi/21."),
 dict(q="The region between y = sqrt(x) and y = x^2 is revolved about the x-axis. What is the volume?", choices=[
   "3*pi/10",
   "3*pi/5",
   "pi/10",
   "7*pi/10"], ans=0,
   why="On [0, 1] the outer radius is sqrt(x) and the inner is x^2, and pi(1/2 - 1/5) = 3pi/10."),
 dict(q="The region bounded by y = 2, y = x, x = 0, and x = 2 is revolved about the x-axis. What is the volume?", choices=[
   "16*pi/3",
   "8*pi/3",
   "32*pi/3",
   "8*pi"], ans=0,
   why="The outer radius is 2 and the inner is x, and pi(8 - 8/3) = 16pi/3."),
 dict(q="In a washer problem, why must both R and r be measured from the same line?", choices=[
   "the two circles that form a washer are concentric about the axis of revolution",
   "otherwise the integral diverges",
   "so that R is always larger than r",
   "so the units work out"], ans=0,
   why="A washer is the region between two circles sharing a center on the axis, so both radii start at that axis."),
 dict(q="A student writes the washer integrand as r^2 - R^2 instead of R^2 - r^2. What is the result?", choices=[
   "the computed volume is the negative of the correct one",
   "the answer is unchanged, since the radii are squared",
   "the answer is doubled",
   "the integral becomes undefined"], ans=0,
   why="Reversing the subtraction changes the sign of the whole integrand, and volume must be positive."),
 dict(q="If x and y are in inches, the washer method produces a result in", choices=[
   "cubic inches",
   "square inches",
   "inches",
   "inches to the fourth power"], ans=0,
   why="The washer's area in square inches is multiplied by a thickness in inches."),
 dict(q="The region between y = x and y = x^2 is revolved first about the x-axis and then about the y-axis. Which solid has the greater volume?", choices=[
   "the one from revolving about the y-axis, since pi/6 is greater than 2pi/15",
   "the one from revolving about the x-axis, since 2pi/15 is greater than pi/6",
   "they are equal",
   "the comparison cannot be made without more information"], ans=0,
   why="The two volumes are 2pi/15 and pi/6, and pi/6 is about 0.524 while 2pi/15 is about 0.419."),
]
