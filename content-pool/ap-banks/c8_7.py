# CALC 8.7 Volumes with Cross Sections: Squares and Rectangles — 25 questions
# V = int A(x) dx, where A is the area of the cross section and the side of the
# square is the length of the segment cut from the base region. Every volume is
# recomputed by sympy; see verify_c8_7.py.
TOPIC = ("8.7", "Volumes with Cross Sections: Squares and Rectangles", 8)
QUESTIONS = [
 dict(q="A solid has known cross-sectional area A(x) for a <= x <= b. Its volume is", choices=[
   "int from a to b of A(x) dx",
   "int from a to b of A(x)^2 dx",
   "pi * int from a to b of A(x) dx",
   "A(b) - A(a)"], ans=0,
   why="Each slab has volume A(x) dx, and integrating adds up the slabs."),
 dict(q="If the cross sections of a solid are taken perpendicular to the x-axis, the volume integral is taken", choices=[
   "with respect to x, with limits that are x-values",
   "with respect to y, with limits that are y-values",
   "with respect to either variable, with the same limits",
   "with respect to the cross-sectional area"], ans=0,
   why="Slices perpendicular to the x-axis are indexed by x, so the thickness is dx."),
 dict(q="A solid has square cross sections perpendicular to the x-axis, and its base is the region between y = f(x) and y = g(x) with f above g. The area of a cross section is", choices=[
   "(f(x) - g(x))^2",
   "f(x)^2 - g(x)^2",
   "pi*(f(x) - g(x))^2",
   "4*(f(x) - g(x))"], ans=0,
   why="The side of the square is the length of the segment, and a square's area is the side squared."),
 dict(q="The base of a solid is the region bounded by y = x, y = 0, and x = 4. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "32/3",
   "16",
   "64/3",
   "64"], ans=2,
   why="The side is x, so the volume is the integral of x^2 from 0 to 4, which is 64/3."),
 dict(q="The base of a solid is the region bounded by y = sqrt(x), y = 0, and x = 4. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "4",
   "16/3",
   "8",
   "16"], ans=2,
   why="The side is sqrt(x), so the volume is the integral of x from 0 to 4, which is 8."),
 dict(q="The base of a solid is the region between y = 4 - x^2 and the x-axis. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "32/3",
   "256/15",
   "64/3",
   "512/15"], ans=3,
   why="The side is 4 - x^2, and the integral of (4 - x^2)^2 from -2 to 2 is 512/15."),
 dict(q="The base of a solid is the region between y = x and y = x^2. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "1/30",
   "1/15",
   "1/6",
   "1/5"], ans=0,
   why="The side is x - x^2, and the integral of (x - x^2)^2 from 0 to 1 is 1/30."),
 dict(q="The base of a solid is the region between y = x and y = x^2. Cross sections perpendicular to the x-axis are rectangles whose height is twice the base. What is the volume?", choices=[
   "1/30",
   "1/15",
   "2/15",
   "1/6"], ans=1,
   why="The area is 2 times the base squared, so the volume is twice the 1/30 obtained with squares."),
 dict(q="The base of a solid is the disk x^2 + y^2 = 4. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "32/3",
   "64/3",
   "128/3",
   "256/3"], ans=2,
   why="The side is 2*sqrt(4 - x^2), so the area is 4(4 - x^2) and the integral from -2 to 2 is 128/3."),
 dict(q="The base of a solid is the region bounded by y = e^x, y = 0, x = 0, and x = 1. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "(e^2 - 1)/2",
   "e^2 - 1",
   "e - 1",
   "(e - 1)^2"], ans=0,
   why="The side is e^x, and the integral of e^(2x) from 0 to 1 is (e^2 - 1)/2."),
 dict(q="The base of a solid is the region bounded by x = y, x = 0, and y = 3. Cross sections perpendicular to the y-axis are squares. What is the volume?", choices=[
   "3",
   "9",
   "27/2",
   "27"], ans=1,
   why="The side is y, and the integral of y^2 from 0 to 3 is 9."),
 dict(q="The base of a solid is the region bounded by y = x, y = 0, and x = 2. Cross sections perpendicular to the x-axis are rectangles whose height is three times the base. What is the volume?", choices=[
   "8/3",
   "4",
   "8",
   "12"], ans=2,
   why="The area is 3x^2, and the integral from 0 to 2 is 8."),
 dict(q="The base of a solid is the region bounded by y = x, y = 0, and x = 2. Cross sections perpendicular to the x-axis are squares whose DIAGONAL lies in the base. What is the volume?", choices=[
   "2/3",
   "4/3",
   "8/3",
   "8"], ans=1,
   why="A square of diagonal d has area d^2/2, so the integrand is x^2/2 and the integral from 0 to 2 is 4/3."),
 dict(q="Which integral gives the volume of the solid whose base is the region between y = 4 - x^2 and the x-axis, with square cross sections perpendicular to the x-axis?", choices=[
   "int from -2 to 2 of (4 - x^2)^2 dx",
   "int from -2 to 2 of (4 - x^2) dx",
   "pi * int from -2 to 2 of (4 - x^2)^2 dx",
   "int from 0 to 2 of (4 - x^2)^2 dx"], ans=0,
   why="The side of each square is the vertical extent 4 - x^2, and the base spans x = -2 to x = 2."),
 dict(q="The base of a solid is the triangle bounded by y = 2 - x, the x-axis, and the y-axis. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "4/3",
   "2",
   "8/3",
   "4"], ans=2,
   why="The side is 2 - x, and the integral of (2 - x)^2 from 0 to 2 is 8/3."),
 dict(q="The base of a solid is the region between y = sin(x) and the x-axis for 0 <= x <= pi. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "pi/2",
   "2",
   "pi",
   "4"], ans=0,
   why="The side is sin(x), and the integral of sin^2(x) over a half period is pi/2."),
 dict(q="The base of a solid is the region between y = 4 - x^2 and the x-axis. Cross sections perpendicular to the x-axis are rectangles of constant height 5. What is the volume?", choices=[
   "32/3",
   "80/3",
   "512/15",
   "160/3"], ans=3,
   why="The area is 5(4 - x^2), and 5 times the area 32/3 of the base region is 160/3."),
 dict(q="If x and y are measured in centimeters, the volume computed from square cross sections has units of", choices=[
   "cubic centimeters",
   "square centimeters",
   "centimeters",
   "centimeters to the fourth power"], ans=0,
   why="An area in square centimeters multiplied by a thickness in centimeters gives cubic centimeters."),
 dict(q="A student computes the volume of a solid with square cross sections using pi times the side squared. What is the error?", choices=[
   "pi belongs to circular cross sections; a square of side s has area s^2, with no pi",
   "the side should be squared twice",
   "the limits of integration are wrong",
   "there is no error"], ans=0,
   why="The factor pi comes from the area of a circle and has no place in the area of a square."),
 dict(q="The base of a solid is the region between y = x and y = x^2. Cross sections perpendicular to the x-axis are rectangles of constant height 2. What is the volume?", choices=[
   "1/15",
   "1/6",
   "1/3",
   "2/3"], ans=2,
   why="The area is 2(x - x^2), and twice the base area 1/6 is 1/3."),
 dict(q="The base of a solid is the region bounded by y = 1/x, y = 0, x = 1, and x = 3. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "2/3",
   "ln(3)",
   "1/3",
   "8/9"], ans=0,
   why="The side is 1/x, and the integral of 1/x^2 from 1 to 3 is 1 - 1/3 = 2/3."),
 dict(q="The base of a solid is the region between y = 2x and y = x^2. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "8/15",
   "16/15",
   "4/3",
   "32/15"], ans=1,
   why="The side is 2x - x^2 on [0, 2], and the integral of its square is 16/15."),
 dict(q="The base of a solid is the region in the first quadrant bounded by y = x^2, y = 4, and the y-axis. Cross sections perpendicular to the y-axis are squares. What is the volume?", choices=[
   "8",
   "32/3",
   "64/5",
   "16"], ans=0,
   why="At height y the segment runs from x = 0 to x = sqrt(y), so the area is y and the integral from 0 to 4 is 8."),
 dict(q="The base of a solid is the triangle bounded by y = 6 - 2x and the two axes. Cross sections perpendicular to the x-axis are squares. What is the volume?", choices=[
   "12",
   "18",
   "27",
   "36"], ans=3,
   why="The side is 6 - 2x on [0, 3], and the integral of (6 - 2x)^2 there is 36."),
 dict(q="If the segment cut from the base region is the DIAGONAL of a square cross section rather than a side, the cross-sectional area is", choices=[
   "half the square of the segment length",
   "the square of the segment length",
   "twice the square of the segment length",
   "the segment length times sqrt(2)"], ans=0,
   why="A square with diagonal d has side d/sqrt(2), so its area is d^2/2."),
]
