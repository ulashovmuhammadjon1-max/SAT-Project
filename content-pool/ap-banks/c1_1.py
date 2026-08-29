# CALC 1.1 Introducing Calculus: Can Change Occur at an Instant? — 25 questions
# Computational answers verified with sympy; see verify_c1_1.py.
# Questions 1-5, 19, 22 and 24 are conceptual (definitions, geometry of secant
# and tangent lines, units); their reasoning is stated in `why` and is not
# something sympy can confirm.
TOPIC = ("1.1", "Introducing Calculus: Can Change Occur at an Instant?", 1)
QUESTIONS = [
 dict(q="For a function f, the average rate of change of f over the interval [a, b] is defined as", choices=[
   "(f(b) - f(a))/(b - a)",
   "(f(b) + f(a))/(b - a)",
   "f(b) - f(a)",
   "(b - a)/(f(b) - f(a))"], ans=0,
   why="The average rate of change is the change in output divided by the change in input."),
 dict(q="The instantaneous rate of change of f at x = a is best described as", choices=[
   "the average rate of change of f over the interval [0, a]",
   "the limit of the average rates of change of f over intervals that shrink toward a",
   "the value f(a) divided by a",
   "the difference f(a + 1) - f(a)"], ans=1,
   why="An instantaneous rate is defined as a limit of average rates over ever-shorter intervals."),
 dict(q="Geometrically, the average rate of change of f over [a, b] is equal to the slope of", choices=[
   "the tangent line to the graph of f at x = a",
   "the secant line through the points (a, f(a)) and (b, f(b))",
   "the horizontal line y = f(a)",
   "the normal line to the graph of f at x = b"], ans=1,
   why="Dividing the rise f(b) - f(a) by the run b - a is exactly the slope of the secant line joining the two points."),
 dict(q="Geometrically, the instantaneous rate of change of f at x = a is equal to the slope of", choices=[
   "the secant line through (a, f(a)) and (a + 1, f(a + 1))",
   "the tangent line to the graph of f at the point (a, f(a))",
   "any chord of the graph of f",
   "the x-axis"], ans=1,
   why="Secant slopes approach the tangent slope as the second point slides toward (a, f(a))."),
 dict(q="Why can the velocity of an object at a single instant not be found simply by dividing a change in position by a change in time?", choices=[
   "Because position is always zero at an instant",
   "Because at a single instant both the change in position and the change in time are 0, so the quotient has the indeterminate form 0/0 and a limit is required",
   "Because velocity is not defined for moving objects",
   "Because time cannot be measured precisely enough"], ans=1,
   why="A single instant supplies no interval, so the difference quotient collapses to 0/0 and only a limiting process gives a value."),
 dict(q="A particle has position s(t) = t^2 + 3t meters at time t seconds. Its average velocity on the interval [1, 4] is", choices=[
   "6 meters per second", "8 meters per second", "11 meters per second", "24 meters per second"], ans=1,
   why="s(4) - s(1) = 28 - 4 = 24, and 24 divided by the elapsed time 3 is 8."),
 dict(q="For f(x) = x^2, the average rate of change of f over the interval [2, 2 + h], where h is not 0, simplifies to", choices=[
   "4", "4 + h", "4 + h^2", "2 + h"], ans=1,
   why="((2 + h)^2 - 4)/h = (4h + h^2)/h = 4 + h."),
 dict(q="For f(x) = x^2, the instantaneous rate of change of f at x = 2 is", choices=[
   "0", "2", "4", "8"], ans=2,
   why="The average rates 4 + h approach 4 as h approaches 0."),
 dict(q="For f(x) = 1/x, the average rate of change of f over [1, 3] is", choices=[
   "-2/3", "-1/2", "-1/3", "1/3"], ans=2,
   why="(1/3 - 1)/(3 - 1) = (-2/3)/2 = -1/3."),
 dict(q="An object falls so that its distance fallen is s(t) = 16t^2 feet after t seconds. Its average velocity over [1, 2] is", choices=[
   "32 feet per second", "48 feet per second", "64 feet per second", "80 feet per second"], ans=1,
   why="s(2) - s(1) = 64 - 16 = 48 feet over 1 second."),
 dict(q="For the falling object with s(t) = 16t^2 feet, the average velocity over the interval [1, 1.01] is", choices=[
   "32 feet per second", "32.16 feet per second", "32.32 feet per second", "33.6 feet per second"], ans=1,
   why="(16(1.01)^2 - 16)/0.01 = 16(2.01) = 32.16, an estimate of the instantaneous velocity 32 at t = 1."),
 dict(q="A cyclist's position along a straight road is recorded as s(0) = 2, s(2) = 10, and s(5) = 25, with s in meters and t in seconds. The cyclist's average velocity over [0, 5] is", choices=[
   "4 meters per second", "4.6 meters per second", "5 meters per second", "23 meters per second"], ans=1,
   why="(25 - 2)/(5 - 0) = 23/5 = 4.6."),
 dict(q="The average rate of change of f(x) = x^3 over the interval [-1, 2] is", choices=[
   "1", "7/3", "3", "9"], ans=2,
   why="(8 - (-1))/(2 - (-1)) = 9/3 = 3."),
 dict(q="The average rate of change of f(x) = sqrt(x) over the interval [4, 9] is", choices=[
   "1/5", "1/4", "1/2", "5"], ans=0,
   why="(3 - 2)/(9 - 4) = 1/5."),
 dict(q="The average rate of change of f(x) = 2^x over the interval [0, 3] is", choices=[
   "7/3", "8/3", "3", "7"], ans=0,
   why="(8 - 1)/(3 - 0) = 7/3."),
 dict(q="For f(x) = 3x + 5, the average rate of change of f over any interval [a, b] with a not equal to b is", choices=[
   "0", "3", "5", "8"], ans=1,
   why="For a linear function the difference quotient always equals the slope, so the interval does not matter."),
 dict(q="The average rate of change of f(x) = x^2 - 4x over the interval [0, 4] is", choices=[
   "-4", "-2", "0", "2"], ans=2,
   why="f(4) = 0 and f(0) = 0, so the numerator is 0 even though f is far from constant on the interval."),
 dict(q="For f(x) = x^2 + 1, the limit as h approaches 0 of (f(3 + h) - f(3))/h is", choices=[
   "3", "6", "9", "10"], ans=1,
   why="(f(3 + h) - f(3))/h = (6h + h^2)/h = 6 + h, which approaches 6."),
 dict(q="The expression lim as h -> 0 of ((5 + h)^3 - 125)/h represents", choices=[
   "the average rate of change of f(x) = x^3 over the interval [0, 5]",
   "the instantaneous rate of change of f(x) = x^3 at x = 5",
   "the value of 5^3",
   "the instantaneous rate of change of f(x) = x^3 at x = 3"], ans=1,
   why="It is the limit of difference quotients for f(x) = x^3 centered at the point x = 5."),
 dict(q="The value of lim as h -> 0 of ((5 + h)^3 - 125)/h is", choices=[
   "15", "25", "75", "125"], ans=2,
   why="Expanding gives (75h + 15h^2 + h^3)/h = 75 + 15h + h^2, which approaches 75."),
 dict(q="For f(x) = x^2, the difference quotients (f(2 + h) - f(2))/h take the values 4.1, 4.01, and 4.001 when h = 0.1, 0.01, and 0.001. These values most strongly suggest that", choices=[
   "f has no instantaneous rate of change at x = 2",
   "the instantaneous rate of change of f at x = 2 is 4",
   "the instantaneous rate of change of f at x = 2 is 4.001",
   "the average rate of change of f on [0, 2] is 4"], ans=1,
   why="The difference quotients are converging to 4 as the interval shrinks, which is what the instantaneous rate of change means."),
 dict(q="If s(t) gives position in meters and t is measured in seconds, then an average rate of change of s over an interval carries units of", choices=[
   "meters", "seconds", "meters per second", "meters per second per second"], ans=2,
   why="The quotient divides a change in meters by a change in seconds."),
 dict(q="The average rate of change of f(x) = x^2 - x over the interval [1, 4] is", choices=[
   "3", "4", "5", "12"], ans=1,
   why="f(4) = 12 and f(1) = 0, so the quotient is 12/3 = 4."),
 dict(q="A particle moves with position s(t) = t^3 - 6t^2 + 9t. Over which of the following intervals is the particle's average velocity equal to 0?", choices=[
   "[0, 1]", "[0, 2]", "[0, 3]", "[1, 2]"], ans=2,
   why="s(3) = 27 - 54 + 27 = 0 = s(0), so the net displacement over [0, 3] is 0 while the other intervals give nonzero displacement."),
 dict(q="For f(x) = 1/x and constants 0 < a < b, the average rate of change of f over [a, b] simplifies to", choices=[
   "-1/(ab)", "1/(ab)", "-1/(a + b)", "(b - a)/(ab)"], ans=0,
   why="(1/b - 1/a)/(b - a) = ((a - b)/(ab))/(b - a) = -1/(ab)."),
]
