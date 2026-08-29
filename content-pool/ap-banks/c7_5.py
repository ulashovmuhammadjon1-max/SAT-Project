# CALC 7.5 Approximating Solutions Using Euler's Method — 25 questions
# BC only. Every numeric approximation is recomputed by a generic Euler
# routine in verify_c7_5.py, so both the arithmetic and the keyed string are
# checked.
TOPIC = ("7.5", "Approximating Solutions Using Euler's Method", 7)
QUESTIONS = [
 dict(q="Let dy/dx = x + y with y(0) = 1. Using Euler's method with one step of size h = 0.5, what is the approximation of y(0.5)?", choices=[
   "1.25",
   "1.5",
   "2",
   "2.5"], ans=1,
   why="One step gives 1 + 0.5*(0 + 1) = 1.5."),
 dict(q="Let dy/dx = x + y with y(0) = 1. Using Euler's method with two steps of size h = 0.5, what is the approximation of y(1)?", choices=[
   "2",
   "2.5",
   "3",
   "3.5"], ans=1,
   why="The first step gives 1.5 at x = 0.5, and the second gives 1.5 + 0.5*(0.5 + 1.5) = 2.5."),
 dict(q="Let dy/dx = 2x with y(1) = 3. Using Euler's method with one step of size h = 0.1, what is the approximation of y(1.1)?", choices=[
   "3.02",
   "3.1",
   "3.2",
   "3.21"], ans=2,
   why="One step gives 3 + 0.1*(2*1) = 3.2."),
 dict(q="Let dy/dx = y with y(0) = 2. Using Euler's method with two steps of size h = 0.25, what is the approximation of y(0.5)?", choices=[
   "2.5",
   "2.75",
   "3",
   "3.125"], ans=3,
   why="Each step multiplies by 1.25, so the estimate is 2*(1.25)^2 = 3.125."),
 dict(q="Let dy/dx = x - y with y(0) = 4. Using Euler's method with one step of size h = 1, what is the approximation of y(1)?", choices=[
   "0",
   "1",
   "3",
   "4"], ans=0,
   why="One step gives 4 + 1*(0 - 4) = 0."),
 dict(q="Let dy/dx = x - y with y(0) = 4. Using Euler's method with two steps of size h = 1, what is the approximation of y(2)?", choices=[
   "-1",
   "0",
   "1",
   "2"], ans=2,
   why="After the first step y is 0 at x = 1, and the second step gives 0 + 1*(1 - 0) = 1."),
 dict(q="Let dy/dx = xy with y(1) = 2. Using Euler's method with one step of size h = 0.5, what is the approximation of y(1.5)?", choices=[
   "2.5",
   "3",
   "3.5",
   "4"], ans=1,
   why="One step gives 2 + 0.5*(1*2) = 3."),
 dict(q="Let dy/dx = xy with y(1) = 2. Using Euler's method with two steps of size h = 0.5, what is the approximation of y(2)?", choices=[
   "3",
   "4",
   "4.5",
   "5.25"], ans=3,
   why="After one step y is 3 at x = 1.5, and the second step gives 3 + 0.5*(1.5*3) = 5.25."),
 dict(q="Euler's method is to be used to approximate y(2) starting from x = 0 using four steps of equal size. What step size h should be used?", choices=[
   "0.25",
   "0.5",
   "2",
   "4"], ans=1,
   why="The interval has length 2, and dividing it into four equal steps gives h = 2/4 = 0.5."),
 dict(q="Euler's method approximates a solution by", choices=[
   "following the tangent line at each point for one step of length h and then recomputing the slope",
   "computing an exact antiderivative and evaluating it",
   "averaging the slopes at the two endpoints of each step",
   "using a Riemann sum of the solution values"], ans=0,
   why="Each Euler step is a straight move along the tangent line determined by the differential equation at the current point."),
 dict(q="Which formula is Euler's method?", choices=[
   "y_(n+1) = y_n + h*f(x_n, y_n)",
   "y_(n+1) = y_n + f(x_n, y_n)",
   "y_(n+1) = y_n*h*f(x_n, y_n)",
   "y_(n+1) = y_n + h*f(x_(n+1), y_(n+1))"], ans=0,
   why="The new value is the old value plus the step size times the slope evaluated at the old point."),
 dict(q="A solution curve is concave up on the interval used. An Euler's method approximation of the solution value at the right endpoint is", choices=[
   "an underestimate, because each tangent line lies below the curve",
   "an overestimate, because each tangent line lies above the curve",
   "exact, because tangent lines meet the curve",
   "an underestimate only if the solution is also increasing"], ans=0,
   why="For a concave up function every tangent line lies below the graph, so stepping along tangent lines falls short."),
 dict(q="A solution curve is concave down on the interval used. An Euler's method approximation of the solution value at the right endpoint is", choices=[
   "an overestimate",
   "an underestimate",
   "exact",
   "an overestimate only if the solution is decreasing"], ans=0,
   why="For a concave down function every tangent line lies above the graph, so the stepping overshoots."),
 dict(q="Let dy/dx = y^2 with y(0) = 1. Using Euler's method with two steps of size h = 0.1, what is the approximation of y(0.2)?", choices=[
   "1.2",
   "1.21",
   "1.221",
   "1.331"], ans=2,
   why="The first step gives 1.1, and the second gives 1.1 + 0.1*(1.1)^2 = 1.221."),
 dict(q="Let dy/dx = x + y with y(1) = 2. Using Euler's method with two steps of size h = -0.5, what is the approximation of y(0)?", choices=[
   "-0.5",
   "0",
   "0.5",
   "1"], ans=1,
   why="Stepping backward gives 2 + (-0.5)(1 + 2) = 0.5 at x = 0.5, then 0.5 + (-0.5)(0.5 + 0.5) = 0."),
 dict(q="Let dy/dx = 2x with y(0) = 1, whose exact solution is y = x^2 + 1. Using Euler's method with two steps of size h = 0.5, the approximation of y(1) is 1.5. By how much does this differ from the exact value?", choices=[
   "0",
   "0.25",
   "0.5",
   "1"], ans=2,
   why="The exact value is 1 + 1 = 2, and 2 - 1.5 = 0.5."),
 dict(q="Let dy/dx = 3 - y with y(0) = 1. Using Euler's method with two steps of size h = 0.2, what is the approximation of y(0.4)?", choices=[
   "1.4",
   "1.6",
   "1.72",
   "1.8"], ans=2,
   why="The first step gives 1 + 0.2*2 = 1.4, and the second gives 1.4 + 0.2*(3 - 1.4) = 1.72."),
 dict(q="Let dy/dx = 1/x with y(1) = 0. Using Euler's method with two steps of size h = 0.5, what is the approximation of y(2)?", choices=[
   "1/2",
   "5/6",
   "1",
   "7/6"], ans=1,
   why="The first step gives 0 + 0.5*(1/1) = 1/2, and the second gives 1/2 + 0.5*(1/1.5) = 5/6."),
 dict(q="Let dy/dx = 2y - 4 with y(0) = 3. Using Euler's method with two steps of size h = 0.5, what is the approximation of y(1)?", choices=[
   "4",
   "5",
   "6",
   "7"], ans=2,
   why="The first step gives 3 + 0.5*2 = 4, and the second gives 4 + 0.5*(2*4 - 4) = 6."),
 dict(q="Let dy/dx = x^2 - y with y(2) = 1. Using Euler's method with one step of size h = 0.1, what is the approximation of y(2.1)?", choices=[
   "0.7",
   "1.03",
   "1.3",
   "1.4"], ans=2,
   why="One step gives 1 + 0.1*(4 - 1) = 1.3."),
 dict(q="Let dy/dx = y/2 with y(0) = 4. Using Euler's method with three steps of size h = 1, what is the approximation of y(3)?", choices=[
   "6",
   "9",
   "12",
   "13.5"], ans=3,
   why="The successive values are 4, 6, 9, and 13.5."),
 dict(q="Let dy/dx = x + 2 with y(1) = 5. Using Euler's method with one step of size h = 0.25, what is the approximation of y(1.25)?", choices=[
   "5.25",
   "5.5",
   "5.75",
   "8"], ans=2,
   why="One step gives 5 + 0.25*(1 + 2) = 5.75."),
 dict(q="Let dy/dx = -2xy with y(0) = 1. Using Euler's method with two steps of size h = 0.5, what is the approximation of y(1)?", choices=[
   "-0.5",
   "0",
   "0.25",
   "0.5"], ans=3,
   why="The first step gives 1 + 0.5*0 = 1 at x = 0.5, and the second gives 1 + 0.5*(-2*0.5*1) = 0.5."),
 dict(q="If the step size in an Euler's method approximation is halved while the interval stays the same, what generally happens to the error?", choices=[
   "it is roughly halved, since Euler's method has error proportional to h",
   "it is roughly quartered",
   "it is unchanged",
   "it roughly doubles"], ans=0,
   why="Euler's method is a first-order method, so the accumulated error over a fixed interval scales like the first power of h."),
 dict(q="Let dy/dx = x + y with y(0) = 1. A student computes one step of size h = 1 and gets y(1) is about 2, then uses two steps of size h = 0.5 and gets 2.5. Which statement is best supported?", choices=[
   "the solution is concave up here, so both are underestimates and 2.5 is the better one",
   "the solution is concave down here, so both are overestimates",
   "the two answers should have agreed, so one of them is an arithmetic error",
   "the smaller step size always makes the estimate smaller"], ans=0,
   why="d^2y/dx^2 = 1 + x + y is positive here, so tangent lines lie below the curve and the finer stepping climbs closer to the true value."),
]
