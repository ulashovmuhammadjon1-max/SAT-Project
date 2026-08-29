# CALC 8.4 Finding the Area Between Curves Expressed as Functions of x
# — 25 questions
# Vertical rectangles: height is (top minus bottom), integrated with respect to
# x. Every area is recomputed by sympy, with intersection points solved for;
# see verify_c8_4.py.
TOPIC = ("8.4", "Finding the Area Between Curves Expressed as Functions of x", 8)
QUESTIONS = [
 dict(q="If f(x) is greater than or equal to g(x) on [a, b], the area of the region between the curves is", choices=[
   "int from a to b of (f(x) - g(x)) dx",
   "int from a to b of (g(x) - f(x)) dx",
   "int from a to b of |f(x)|dx - int from a to b of |g(x)| dx",
   "int from a to b of f(x)*g(x) dx"], ans=0,
   why="A vertical rectangle has height equal to the top curve minus the bottom curve."),
 dict(q="What is the area of the region between y = x and y = x^2 from x = 0 to x = 1?", choices=[
   "1/6",
   "1/3",
   "1/2",
   "5/6"], ans=0,
   why="On this interval x is above x^2, and the integral of x - x^2 is 1/2 - 1/3 = 1/6."),
 dict(q="What is the area of the region between y = 4 - x^2 and the x-axis?", choices=[
   "16/3",
   "8",
   "32/3",
   "16"], ans=2,
   why="The curve meets the axis at x = -2 and x = 2, and the integral of 4 - x^2 there is 32/3."),
 dict(q="What is the area of the region between y = x and y = x^3 from x = 0 to x = 1?", choices=[
   "1/4",
   "1/3",
   "1/2",
   "3/4"], ans=0,
   why="On this interval x is above x^3, and 1/2 - 1/4 = 1/4."),
 dict(q="What is the area of the region enclosed by y = 2x and y = x^2?", choices=[
   "2/3",
   "4/3",
   "8/3",
   "4"], ans=1,
   why="The curves cross at x = 0 and x = 2, and the integral of 2x - x^2 there is 4 - 8/3 = 4/3."),
 dict(q="What is the area of the region between y = sqrt(x) and y = x from x = 0 to x = 1?", choices=[
   "1/6",
   "1/3",
   "1/2",
   "2/3"], ans=0,
   why="The square root is on top, and 2/3 - 1/2 = 1/6."),
 dict(q="What is the area of the region between y = e^x and y = 1 from x = 0 to x = 1?", choices=[
   "e - 2",
   "e - 1",
   "e",
   "e + 1"], ans=0,
   why="The integral of e^x - 1 from 0 to 1 is (e - 1) - 1 = e - 2."),
 dict(q="What is the area of the region between y = cos(x) and y = sin(x) from x = 0 to x = pi/4?", choices=[
   "sqrt(2) - 1",
   "1 - sqrt(2)/2",
   "sqrt(2)",
   "1"], ans=0,
   why="Cosine is on top there, and an antiderivative of cos(x) - sin(x) is sin(x) + cos(x), giving sqrt(2) - 1."),
 dict(q="To find the area between y = f(x) and y = g(x) on [a, b] using vertical rectangles, the height of a representative rectangle is", choices=[
   "the top function value minus the bottom function value at that x",
   "f(x) + g(x)",
   "the width b - a",
   "the average of f(x) and g(x)"], ans=0,
   why="Each vertical strip runs from the lower curve up to the upper curve."),
 dict(q="What is the area of the region enclosed by y = x^2 and y = 8 - x^2?", choices=[
   "32/3",
   "16",
   "64/3",
   "32"], ans=2,
   why="The curves cross at x = -2 and x = 2, and the integral of 8 - 2x^2 there is 32 - 32/3 = 64/3."),
 dict(q="What is the area of the region enclosed by y = 3x and y = x^2 + 2?", choices=[
   "1/6",
   "1/3",
   "1/2",
   "5/6"], ans=0,
   why="The curves cross at x = 1 and x = 2, and the integral of 3x - x^2 - 2 over that interval is 1/6."),
 dict(q="What is the area of the region between y = 1/x and y = 1/x^2 from x = 1 to x = 2?", choices=[
   "ln(2) - 1/2",
   "ln(2) + 1/2",
   "ln(2) - 1",
   "1/2 - ln(2)"], ans=0,
   why="On [1, 2] the curve 1/x is above 1/x^2, and the two integrals are ln(2) and 1/2."),
 dict(q="What is the area of the region between y = x^3 and y = x from x = -1 to x = 0?", choices=[
   "1/4",
   "1/3",
   "1/2",
   "3/4"], ans=0,
   why="On [-1, 0] the cube is above the line, and the integral of x^3 - x there is 1/4."),
 dict(q="What is the area of the region enclosed by y = x^2 and y = x + 2?", choices=[
   "5/2",
   "7/2",
   "9/2",
   "9"], ans=2,
   why="The curves cross at x = -1 and x = 2, and the integral of x + 2 - x^2 over that interval is 9/2."),
 dict(q="What is the area of the region between y = cos(x) and the x-axis from x = 0 to x = pi?", choices=[
   "2",
   "0",
   "1",
   "pi"], ans=0,
   why="Cosine changes sign at pi/2, and each half contributes 1 to the integral of |cos(x)|."),
 dict(q="What is the area of the region enclosed by y = x^2 and y = 9?", choices=[
   "18",
   "27",
   "36",
   "54"], ans=2,
   why="The curves cross at x = -3 and x = 3, and the integral of 9 - x^2 there is 54 - 18 = 36."),
 dict(q="What is the area of the region between y = x^2 and y = -x^2 from x = 0 to x = 1?", choices=[
   "1/6",
   "1/3",
   "2/3",
   "4/3"], ans=2,
   why="The vertical distance between the curves is 2x^2, whose integral from 0 to 1 is 2/3."),
 dict(q="What is the area of the region enclosed by y = 4x and y = x^3 for x greater than or equal to 0?", choices=[
   "2",
   "4",
   "8",
   "16"], ans=1,
   why="The curves cross at x = 0 and x = 2, and the integral of 4x - x^3 there is 8 - 4 = 4."),
 dict(q="What is the area of the region between y = ln(x) and the x-axis from x = 1 to x = e?", choices=[
   "1",
   "e - 1",
   "e",
   "1/e"], ans=0,
   why="An antiderivative of ln(x) is x*ln(x) - x, whose value is 0 at x = e and -1 at x = 1."),
 dict(q="What is the area of the region between y = x^2 - 2x and the x-axis?", choices=[
   "2/3",
   "4/3",
   "8/3",
   "4"], ans=1,
   why="The curve meets the axis at x = 0 and x = 2 and lies below it there, so the area is the absolute value of the integral, 4/3."),
 dict(q="A student sets up the area between y = x and y = x^2 on [0, 1] as int from 0 to 1 of (x^2 - x) dx and gets -1/6. What went wrong?", choices=[
   "the subtraction is backwards; on [0, 1] the line is above the parabola, so the integrand must be x - x^2",
   "the limits of integration are wrong",
   "nothing; area can be negative",
   "the antiderivative of x^2 is wrong"], ans=0,
   why="Area uses top minus bottom, and reversing the order flips the sign of the result."),
 dict(q="What is the area of the region between y = 2^x and y = x from x = 0 to x = 2?", choices=[
   "3/ln(2) - 2",
   "3/ln(2)",
   "4/ln(2) - 2",
   "3*ln(2) - 2"], ans=0,
   why="The integral of 2^x from 0 to 2 is (4 - 1)/ln(2), and the integral of x is 2."),
 dict(q="Which integral gives the area of the region enclosed by y = 6 - x^2 and y = x?", choices=[
   "int from -3 to 2 of (6 - x^2 - x) dx",
   "int from -3 to 2 of (x - 6 + x^2) dx",
   "int from -2 to 3 of (6 - x^2 - x) dx",
   "int from 0 to 2 of (6 - x^2 - x) dx"], ans=0,
   why="Setting 6 - x^2 = x gives x = -3 and x = 2, and the parabola is on top between them."),
 dict(q="What is the area of the region between y = sin(x) and the x-axis from x = 0 to x = 2pi?", choices=[
   "4",
   "0",
   "2",
   "2pi"], ans=0,
   why="The integral of sin over the full period is 0, but the area uses |sin(x)|, contributing 2 from each half."),
 dict(q="For the region enclosed by y = x^3 and y = x, why must the area be computed as two separate integrals?", choices=[
   "the curves cross at x = -1, 0, and 1, and which one is on top switches at x = 0",
   "the curves never cross",
   "one of the functions is not continuous",
   "the region is unbounded"], ans=0,
   why="On [-1, 0] the cubic is above the line and on [0, 1] the line is above the cubic, so a single top-minus-bottom expression cannot cover both."),
]
