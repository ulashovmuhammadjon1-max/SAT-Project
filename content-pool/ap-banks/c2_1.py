# CALC 2.1 Defining Average and Instantaneous Rates of Change at a Point — 25 questions
# Answers verified with sympy; see verify_c2_1.py.
# Questions 1, 6, 7, 10, 14 and 24 are conceptual (definitions, geometry, units,
# and the direction of an implication) and carry no sympy check.
TOPIC = ("2.1", "Defining Average and Instantaneous Rates of Change at a Point", 2)
QUESTIONS = [
 dict(q="The average rate of change of a function f on the interval [a, b] is given by which expression?", choices=[
   "(f(b) - f(a))/(b - a)",
   "f(b) - f(a)",
   "(f(b) + f(a))/2",
   "f'(b) - f'(a)"], ans=0,
   why="The average rate of change is the change in output divided by the change in input, which is the slope of the secant line."),
 dict(q="If f(x) = x^2, the average rate of change of f on the interval [1, 4] is", choices=[
   "2", "5", "17/2", "15"], ans=1,
   why="(f(4) - f(1))/(4 - 1) = (16 - 1)/3 = 5."),
 dict(q="If f(x) = x^3 - 2x, the average rate of change of f on the interval [0, 3] is", choices=[
   "25", "21", "7", "-2"], ans=2,
   why="(f(3) - f(0))/(3 - 0) = (21 - 0)/3 = 7; 25 is the instantaneous rate f'(3)."),
 dict(q="If f(x) = 1/x, the average rate of change of f on the interval [1, 4] is", choices=[
   "-1", "-3/4", "-1/4", "1/4"], ans=2,
   why="(1/4 - 1)/3 = (-3/4)/3 = -1/4; -3/4 is the change in f without dividing by the change in x."),
 dict(q="If f(x) = sqrt(x), the average rate of change of f on the interval [4, 9] is", choices=[
   "5", "1", "1/4", "1/5"], ans=3,
   why="(3 - 2)/(9 - 4) = 1/5; 1/4 is f'(4), the instantaneous rate at the left endpoint."),
 dict(q="The instantaneous rate of change of f at x = a is defined as", choices=[
   "lim as h -> 0 of (f(a + h) - f(a))/h",
   "(f(a + h) - f(a))/h",
   "lim as h -> 0 of (f(a + h) - f(a))",
   "lim as h -> 0 of (f(a + h) + f(a))/h"], ans=0,
   why="The instantaneous rate is the limit of the difference quotient as the interval width shrinks to zero."),
 dict(q="The average rate of change of f on [a, b] is equal to the slope of", choices=[
   "the secant line through (a, f(a)) and (b, f(b))",
   "the tangent line to the graph of f at x = a",
   "the tangent line to the graph of f at x = b",
   "the line normal to the graph of f at x = a"], ans=0,
   why="An average rate of change is a rise over a run between two points on the curve, which is exactly a secant slope."),
 dict(q="A particle moves so that its position at time t seconds is s(t) = t^2 + 3t meters. Its average velocity on the interval [1, 4] is", choices=[
   "24", "11", "8", "5"], ans=2,
   why="(s(4) - s(1))/3 = (28 - 4)/3 = 8 meters per second."),
 dict(q="A particle has position s(t) = t^2 + 3t meters at time t seconds. Its instantaneous velocity at t = 1 is", choices=[
   "2", "4", "5", "8"], ans=2,
   why="s'(t) = 2t + 3, so s'(1) = 5 meters per second; 8 is the average velocity on [1, 4]."),
 dict(q="The volume of water in a tank is V(t) liters at time t minutes. The average rate of change of V over 0 <= t <= 10 is measured in", choices=[
   "liters per minute",
   "liters",
   "minutes per liter",
   "liters per minute per minute"], ans=0,
   why="A rate of change carries the units of the output divided by the units of the input."),
 dict(q="If f(x) = e^x, the average rate of change of f on the interval [0, ln(4)] is", choices=[
   "3/ln(4)", "3/ln(2)", "3", "4/ln(4)"], ans=0,
   why="(e^(ln 4) - e^0)/(ln(4) - 0) = (4 - 1)/ln(4) = 3/ln(4)."),
 dict(q="If f(x) = sin(x), the average rate of change of f on the interval [0, pi/2] is", choices=[
   "2/pi", "1", "pi/2", "0"], ans=0,
   why="(sin(pi/2) - sin(0))/(pi/2 - 0) = 1/(pi/2) = 2/pi; the value 0 is the instantaneous rate f'(pi/2)."),
 dict(q="A differentiable function g satisfies g(2) = 5 and g(6) = 17. The average rate of change of g on [2, 6] is", choices=[
   "12", "11", "4", "3"], ans=3,
   why="(17 - 5)/(6 - 2) = 12/4 = 3; 12 is the change in g alone."),
 dict(q="Which of the following expressions represents f'(3)?", choices=[
   "lim as h -> 0 of (f(3 + h) - f(3))/h",
   "lim as h -> 0 of (f(3 + h) - f(3))",
   "lim as h -> 0 of (f(3 + h) - f(3))/3",
   "(f(3 + h) - f(3))/h"], ans=0,
   why="Only the first is a difference quotient divided by h with the limit taken as h approaches 0."),
 dict(q="If f(x) = x^2, the average rate of change of f on the interval [1, 1 + h], where h > 0, is", choices=[
   "2 + h", "2", "h", "2h + h^2"], ans=0,
   why="((1 + h)^2 - 1)/h = (2h + h^2)/h = 2 + h, which approaches f'(1) = 2 as h -> 0."),
 dict(q="For f(x) = x^2, the value of c in (1, 4) at which the instantaneous rate of change equals the average rate of change on [1, 4] is", choices=[
   "2", "5/2", "3", "5"], ans=1,
   why="The average rate is 5 and f'(c) = 2c, so 2c = 5 and c = 5/2."),
 dict(q="If f(x) = x^3, the average rate of change of f on the interval [-2, 2] is", choices=[
   "16", "12", "4", "0"], ans=2,
   why="(8 - (-8))/(2 - (-2)) = 16/4 = 4; the answer is not 0, because f(2) and f(-2) are opposites, not equal."),
 dict(q="A cost function is C(q) = 200 + 5q + 0.1q^2 dollars for q units. The average rate of change of C on [10, 20] is", choices=[
   "80", "9", "8", "7"], ans=2,
   why="(C(20) - C(10))/10 = (340 - 260)/10 = 8 dollars per unit; 9 is the marginal cost C'(20)."),
 dict(q="For the linear function f(x) = mx + b with m and b constants, the average rate of change of f on any interval [p, q] with p < q equals", choices=[
   "m", "b", "mp + b", "(m + b)/2"], ans=0,
   why="(mq + b - mp - b)/(q - p) = m(q - p)/(q - p) = m, so a line has the same rate of change on every interval."),
 dict(q="If f(x) = ln(x), the average rate of change of f on the interval [1, e^2] is", choices=[
   "2/(e^2 - 1)", "2", "2/e^2", "1/(e^2 - 1)"], ans=0,
   why="(ln(e^2) - ln(1))/(e^2 - 1) = (2 - 0)/(e^2 - 1) = 2/(e^2 - 1)."),
 dict(q="A particle has position s(t) = t^3 - 6t^2 + 9t. Its average velocity on the interval [0, 3] is", choices=[
   "-9", "0", "3", "9"], ans=1,
   why="s(3) = 0 and s(0) = 0, so the net displacement is 0 and the average velocity is 0 even though the particle moved."),
 dict(q="If f(x) = 1/x, the instantaneous rate of change of f at x = 2 is", choices=[
   "1/4", "-1/4", "-1/2", "-2"], ans=1,
   why="f'(x) = -1/x^2, so f'(2) = -1/4."),
 dict(q="The temperature in a greenhouse is H(t) degrees Fahrenheit t hours after sunrise, with H(3) = 68 and H(7) = 84. The average rate of change of H on [3, 7] is", choices=[
   "16", "8", "4", "2"], ans=2,
   why="(84 - 68)/(7 - 3) = 16/4 = 4 degrees Fahrenheit per hour."),
 dict(q="A function f is differentiable on [2, 5] and its average rate of change on that interval is 4. Which statement must be true?", choices=[
   "f(5) - f(2) = 12",
   "f'(x) = 4 for every x in [2, 5]",
   "f'(3.5) = 4",
   "f(5) = 4f(2)"], ans=0,
   why="The average rate 4 means (f(5) - f(2))/3 = 4, so the change in f is 12; the derivative equals 4 somewhere, but not necessarily at the midpoint or everywhere."),
 dict(q="If f(x) = x^2 + x, the average rate of change of f on the interval [a, a + 2] is", choices=[
   "2a + 3", "2a + 1", "2a + 5", "4a + 6"], ans=0,
   why="(f(a + 2) - f(a))/2 = (4a + 6)/2 = 2a + 3, which lies between f'(a) = 2a + 1 and f'(a + 2) = 2a + 5."),
]
