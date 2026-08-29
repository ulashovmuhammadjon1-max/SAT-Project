# CALC 8.13 The Arc Length of a Smooth, Planar Curve and Distance Traveled
# — 25 questions
# BC only. L = int sqrt(1 + (dy/dx)^2) dx for y = f(x); for a parametric curve
# the integrand is the speed sqrt((dx/dt)^2 + (dy/dt)^2). Every length is
# recomputed by sympy; see verify_c8_13.py.
TOPIC = ("8.13", "The Arc Length of a Smooth, Planar Curve and Distance Traveled", 8)
QUESTIONS = [
 dict(q="The length of the curve y = f(x) from x = a to x = b is", choices=[
   "int from a to b of sqrt(1 + (f'(x))^2) dx",
   "int from a to b of sqrt(1 + f(x)^2) dx",
   "int from a to b of (1 + (f'(x))^2) dx",
   "int from a to b of f'(x) dx"], ans=0,
   why="Each small piece of the curve has length sqrt((dx)^2 + (dy)^2), which factors as sqrt(1 + (dy/dx)^2) dx."),
 dict(q="The length of the curve x = g(y) from y = c to y = d is", choices=[
   "int from c to d of sqrt(1 + (g'(y))^2) dy",
   "int from c to d of sqrt(1 + (g(y))^2) dy",
   "int from c to d of sqrt(1 + (g'(y))^2) dx",
   "int from c to d of g'(y) dy"], ans=0,
   why="The same derivation applies with the roles of the variables exchanged."),
 dict(q="For a parametric curve x = x(t), y = y(t) on a <= t <= b, the arc length is", choices=[
   "int from a to b of sqrt((dx/dt)^2 + (dy/dt)^2) dt",
   "int from a to b of sqrt(1 + (dy/dt)^2) dt",
   "int from a to b of ((dx/dt) + (dy/dt)) dt",
   "int from a to b of sqrt((dy/dx)^2) dt"], ans=0,
   why="The integrand is the speed, and integrating speed over time gives the length traced."),
 dict(q="A particle moves in the plane with position (x(t), y(t)). Its speed at time t is", choices=[
   "sqrt((dx/dt)^2 + (dy/dt)^2)",
   "(dx/dt) + (dy/dt)",
   "dy/dx",
   "sqrt((dx/dt)^2 - (dy/dt)^2)"], ans=0,
   why="Speed is the magnitude of the velocity vector, which is the square root of the sum of the squares of its components."),
 dict(q="What is the length of the curve y = 3x + 1 from x = 0 to x = 4?", choices=[
   "4*sqrt(10)",
   "4*sqrt(2)",
   "12",
   "sqrt(10)"], ans=0,
   why="The derivative is 3, so the integrand is sqrt(10) and the length is 4*sqrt(10)."),
 dict(q="What is the length of the curve y = (2/3)*x^(3/2) from x = 0 to x = 3?", choices=[
   "7/3",
   "14/3",
   "16/3",
   "28/3"], ans=1,
   why="The derivative is sqrt(x), so the integrand is sqrt(1 + x), whose integral from 0 to 3 is (2/3)(8 - 1)."),
 dict(q="What is the length of the curve y = x^3/3 + 1/(4x) from x = 1 to x = 2?", choices=[
   "17/8",
   "7/3",
   "59/24",
   "59/12"], ans=2,
   why="Here 1 + (y')^2 is the perfect square (x^2 + 1/(4x^2))^2, so the integrand is x^2 + 1/(4x^2)."),
 dict(q="What is the length of the curve y = ln(cos(x)) from x = 0 to x = pi/4?", choices=[
   "ln(1 + sqrt(2))",
   "ln(sqrt(2))",
   "sqrt(2) - 1",
   "pi/4"], ans=0,
   why="The derivative is -tan(x), so 1 + tan^2(x) = sec^2(x) and the integrand is sec(x)."),
 dict(q="What is the length of the curve y = (1/2)*(e^x + e^(-x)) from x = 0 to x = 1?", choices=[
   "(e - 1/e)/2",
   "(e + 1/e)/2",
   "e - 1",
   "(e^2 - 1)/2"], ans=0,
   why="The derivative is (e^x - e^(-x))/2, and 1 + (y')^2 is the perfect square ((e^x + e^(-x))/2)^2."),
 dict(q="What is the length of the curve y = (2/3)*(x^2 + 1)^(3/2) from x = 0 to x = 1?", choices=[
   "4/3",
   "5/3",
   "2",
   "8/3"], ans=1,
   why="The derivative is 2x*sqrt(x^2 + 1), and 1 + 4x^2(x^2 + 1) = (2x^2 + 1)^2, so the integrand is 2x^2 + 1."),
 dict(q="What is the length of the curve y = x^(3/2) from x = 0 to x = 4?", choices=[
   "(8/27)*(10*sqrt(10) - 1)",
   "(8/27)*(10*sqrt(10))",
   "(4/9)*(10*sqrt(10) - 1)",
   "(2/3)*(10*sqrt(10) - 1)"], ans=0,
   why="The integrand is sqrt(1 + 9x/4), whose antiderivative evaluated from 0 to 4 gives (8/27)(10^(3/2) - 1)."),
 dict(q="Which integral gives the length of the curve y = x^2 from x = 0 to x = 2?", choices=[
   "int from 0 to 2 of sqrt(1 + 4x^2) dx",
   "int from 0 to 2 of sqrt(1 + x^4) dx",
   "int from 0 to 2 of sqrt(1 + 2x) dx",
   "int from 0 to 2 of (1 + 4x^2) dx"], ans=0,
   why="The derivative is 2x, and squaring it gives 4x^2 under the radical."),
 dict(q="Which integral gives the length of the curve y = ln(x) from x = 1 to x = e?", choices=[
   "int from 1 to e of sqrt(1 + 1/x^2) dx",
   "int from 1 to e of sqrt(1 + ln(x)^2) dx",
   "int from 1 to e of sqrt(1 + 1/x) dx",
   "int from 1 to e of (1 + 1/x^2) dx"], ans=0,
   why="The derivative is 1/x, whose square is 1/x^2."),
 dict(q="A curve is given by x = 3cos(t), y = 3sin(t) for 0 <= t <= pi. What is its length?", choices=[
   "3*pi",
   "6*pi",
   "3",
   "9*pi"], ans=0,
   why="The speed is a constant 3, and the parameter interval has length pi."),
 dict(q="A curve is given by x = t^2, y = t^3 for 0 <= t <= 1. What is its length?", choices=[
   "(13*sqrt(13) - 8)/27",
   "(13*sqrt(13) - 8)/9",
   "(13*sqrt(13))/27",
   "(13 - 8)/27"], ans=0,
   why="The speed is t*sqrt(4 + 9t^2), and an antiderivative is (4 + 9t^2)^(3/2)/27."),
 dict(q="A particle moves in the plane with position (x(t), y(t)). The total distance it travels from t = a to t = b is", choices=[
   "int from a to b of sqrt((x'(t))^2 + (y'(t))^2) dt",
   "sqrt((x(b) - x(a))^2 + (y(b) - y(a))^2)",
   "int from a to b of (x'(t) + y'(t)) dt",
   "int from a to b of |x'(t)| dt"], ans=0,
   why="Distance travelled is the integral of the speed, which is exactly the arc length of the path."),
 dict(q="For a particle moving along a straight LINE with velocity v(t), the distance travelled from t = a to t = b is", choices=[
   "int from a to b of |v(t)| dt",
   "int from a to b of v(t) dt",
   "|int from a to b of v(t) dt|",
   "int from a to b of sqrt(1 + v(t)^2) dt"], ans=0,
   why="Motion on a line is the one-dimensional case, where the speed is |v(t)|."),
 dict(q="How does the length of a curve joining two points compare with the straight-line distance between those points?", choices=[
   "the curve is at least as long, with equality only when the curve is the straight segment",
   "the curve is always shorter",
   "they are always equal",
   "no comparison can be made"], ans=0,
   why="The straight segment is the shortest path between two points, so any other path is longer."),
 dict(q="The arc length formula requires the curve to be smooth on the interval, which means", choices=[
   "f' exists and is continuous there",
   "f is positive there",
   "f is increasing there",
   "f has no zeros there"], ans=0,
   why="A continuous derivative is what makes the integrand continuous and the integral meaningful."),
 dict(q="If x and y are in meters, an arc length computed from the formula has units of", choices=[
   "meters",
   "square meters",
   "meters per second",
   "it is dimensionless"], ans=0,
   why="The integrand is dimensionless and dx carries the length unit."),
 dict(q="What is the length of the curve y = 4 from x = 1 to x = 7?", choices=[
   "6",
   "4",
   "24",
   "sqrt(37)"], ans=0,
   why="The derivative is 0, so the integrand is 1 and the length is just the width of the interval."),
 dict(q="A student computes arc length as the integral of sqrt((f'(x))^2) instead of sqrt(1 + (f'(x))^2). What quantity has the student found?", choices=[
   "the total variation of f, that is the integral of |f'|, which is not the arc length",
   "the arc length, since the 1 is negligible",
   "the area under the curve",
   "the average value of f'"], ans=0,
   why="Dropping the 1 removes the horizontal contribution to each small piece of the curve."),
 dict(q="Which integral gives the length of the curve x = y^2 from y = 0 to y = 1?", choices=[
   "int from 0 to 1 of sqrt(1 + 4y^2) dy",
   "int from 0 to 1 of sqrt(1 + 4x^2) dx",
   "int from 0 to 1 of sqrt(1 + y^4) dy",
   "int from 0 to 1 of sqrt(1 + 2y) dy"], ans=0,
   why="With x written as a function of y, the derivative is 2y and the thickness is dy."),
 dict(q="A particle has x'(t) = 3 and y'(t) = 4 for 0 <= t <= 2. What total distance does it travel?", choices=[
   "5",
   "7",
   "10",
   "14"], ans=2,
   why="The speed is sqrt(9 + 16) = 5, and 5 times the elapsed time 2 is 10."),
 dict(q="What is the length of the curve y = (1/3)*(x^2 + 2)^(3/2) from x = 0 to x = 3?", choices=[
   "9",
   "10",
   "12",
   "15"], ans=2,
   why="The derivative is x*sqrt(x^2 + 2), and 1 + x^2(x^2 + 2) = (x^2 + 1)^2, so the integrand is x^2 + 1."),
]
