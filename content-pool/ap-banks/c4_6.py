# CALC 4.6 Approximating Values of a Function Using Local Linearity and Linearization — 25 questions
# Every linearization, estimate, and comparison with the true value is recomputed in
# verify_c4_6.py with sympy, including the sign of f'' that decides whether the tangent
# line estimate is an overestimate or an underestimate.
TOPIC = ("4.6", "Approximating Values of a Function Using Local Linearity and Linearization", 4)
QUESTIONS = [
 dict(q="If f is differentiable at a, the linearization of f at a is",
   choices=[
     "L(x) = f(a) + f'(a)(x - a)",
     "L(x) = f'(a) + f(a)(x - a)",
     "L(x) = f(a) + f'(x)(x - a)",
     "L(x) = f(a)(x - a) + f'(a)"], ans=0,
   why="The linearization is the tangent line at x = a: it passes through (a, f(a)) with slope f'(a)."),

 dict(q="The linearization of f(x) = sqrt(x) at a = 9 is",
   choices=[
     "L(x) = 3 + (1/6)(x - 9)",
     "L(x) = 3 + (1/3)(x - 9)",
     "L(x) = 9 + (1/6)(x - 9)",
     "L(x) = 3 + 6(x - 9)"], ans=0,
   why="f(9) = 3 and f'(x) = 1/(2sqrt(x)) gives f'(9) = 1/6."),

 dict(q="Using the tangent line to f(x) = sqrt(x) at x = 9, the approximation of sqrt(9.1) is",
   choices=[
     "about 3.0167",
     "about 3.0333",
     "about 3.6000",
     "about 3.0000"], ans=0,
   why="L(9.1) = 3 + (0.1)/6 = 3.01667, close to the true value 3.01662."),

 dict(q="The tangent line approximation of sqrt(9.1) at a = 9 is",
   choices=[
     "an overestimate, because f(x) = sqrt(x) is concave down",
     "an underestimate, because f(x) = sqrt(x) is increasing",
     "an underestimate, because f(x) = sqrt(x) is concave down",
     "exactly equal to the true value"], ans=0,
   why="f''(x) = -1/(4x^(3/2)) < 0, so the curve bends below its tangent line and the tangent value is too large."),

 dict(q="Using the tangent line to f(x) = x^(1/3) at a = 8, the approximation of (8.6)^(1/3) is",
   choices=[
     "2.05, an overestimate",
     "2.05, an underestimate",
     "2.15, an overestimate",
     "2.60, an overestimate"], ans=0,
   why="f'(8) = 1/12 gives L(8.6) = 2 + 0.6/12 = 2.05, and f'' < 0 for x > 0 makes the tangent line lie above the curve."),

 dict(q="Using the linearization of f(x) = e^x at a = 0, the approximation of e^(0.1) is",
   choices=[
     "1.1, an underestimate",
     "1.1, an overestimate",
     "0.1, an underestimate",
     "1.0, an underestimate"], ans=0,
   why="L(x) = 1 + x gives 1.1, and since e^x is concave up the tangent line lies below the curve, so 1.1 < e^(0.1) = 1.10517."),

 dict(q="Using the linearization of f(x) = ln(x) at a = 1, the approximation of ln(1.05) is",
   choices=[
     "0.05, an overestimate",
     "0.05, an underestimate",
     "1.05, an overestimate",
     "0.0488, an overestimate"], ans=0,
   why="L(x) = x - 1 gives 0.05, and ln is concave down, so the tangent estimate exceeds the true value 0.04879."),

 dict(q="Using the linearization of f(x) = sin(x) at a = 0, the approximation of sin(0.1) is",
   choices=[
     "0.1, an overestimate",
     "0.1, an underestimate",
     "0, an underestimate",
     "0.0998, an underestimate"], ans=0,
   why="L(x) = x gives 0.1, and f''(x) = -sin(x) is negative just to the right of 0, so the tangent line lies above the curve."),

 dict(q="A differentiable function satisfies f(2) = 5 and f'(2) = -3. The tangent line approximation of f(2.1) is",
   choices=[
     "4.7",
     "5.3",
     "2",
     "4.4"], ans=0,
   why="f(2.1) is about f(2) + f'(2)(0.1) = 5 - 0.3 = 4.7."),

 dict(q="A function satisfies f(3) = 10, f'(3) = 4, and f''(x) < 0 for all x. The tangent line approximation of f(3.2) is",
   choices=[
     "10.8, an overestimate",
     "10.8, an underestimate",
     "10.4, an overestimate",
     "13.2, an overestimate"], ans=0,
   why="L(3.2) = 10 + 4(0.2) = 10.8, and a concave-down function lies below its tangent line, so the estimate is too big."),

 dict(q="For y = x^2, the differential dy at x = 3 with dx = 0.01 is",
   choices=[
     "0.06",
     "0.09",
     "0.0601",
     "0.6"], ans=0,
   why="dy = f'(x)dx = 2(3)(0.01) = 0.06; the exact change is 0.0601, and the differential is the linear part of it."),

 dict(q="The edge of a cube is measured as 10 centimeters with a possible error of at most 0.1 centimeter. Using differentials, the greatest possible error in the computed volume is about",
   choices=[
     "30 cubic centimeters",
     "3 cubic centimeters",
     "100 cubic centimeters",
     "0.1 cubic centimeter"], ans=0,
   why="dV = 3s^2*ds = 3(100)(0.1) = 30 cubic centimeters."),

 dict(q="A circle's radius is measured as 5 meters with a possible error of at most 0.05 meter. Using differentials, the greatest possible error in the computed area is about",
   choices=[
     "0.5pi square meters",
     "0.05pi square meters",
     "25pi square meters",
     "10pi square meters"], ans=0,
   why="dA = 2pi*r*dr = 2pi(5)(0.05) = 0.5pi, about 1.57 square meters."),

 dict(q="A tangent line approximation of f near x = a is an underestimate when",
   choices=[
     "f is concave up near a",
     "f is concave down near a",
     "f is increasing near a",
     "f is decreasing near a"], ans=0,
   why="A concave-up curve lies above its tangent lines, so the tangent value falls short of the true value."),

 dict(q="Why does a tangent line approximation of f(x) generally get worse as x moves farther from a?",
   choices=[
     "Local linearity only guarantees that the curve resembles its tangent line near the point of tangency",
     "The derivative f'(a) becomes incorrect for larger x",
     "The tangent line's slope changes as x moves away",
     "The approximation is exact for all x if f is differentiable"], ans=0,
   why="Differentiability says the graph looks linear under sufficient magnification at the point, and the curvature ignored by the tangent line accumulates as the distance grows."),

 dict(q="Using the tangent line to f(x) = sqrt(x) at a = 25, the approximation of sqrt(24) is",
   choices=[
     "4.9, an overestimate",
     "4.9, an underestimate",
     "4.8, an overestimate",
     "5.1, an overestimate"], ans=0,
   why="L(24) = 5 + (1/10)(-1) = 4.9, and since sqrt is concave down the tangent line sits above the curve, so 4.9 > 4.89898."),

 dict(q="Using the tangent line to f(x) = 1/x at a = 2, the approximation of 1/2.1 is",
   choices=[
     "0.475, an underestimate",
     "0.475, an overestimate",
     "0.525, an overestimate",
     "0.476, an underestimate"], ans=0,
   why="f'(2) = -1/4 gives L(2.1) = 0.5 - 0.025 = 0.475, and 1/x is concave up for x > 0, so the tangent line lies below the curve."),

 dict(q="The linearization of f(x) = tan(x) at a = pi/4 is",
   choices=[
     "L(x) = 1 + 2(x - pi/4)",
     "L(x) = 1 + (x - pi/4)",
     "L(x) = 1 + sqrt(2)(x - pi/4)",
     "L(x) = (x - pi/4)"], ans=0,
   why="tan(pi/4) = 1 and f'(x) = sec^2(x) gives f'(pi/4) = 2."),

 dict(q="Using the linearization of f(x) = x^10 at a = 1, the approximation of (1.02)^10 is",
   choices=[
     "1.2, an underestimate",
     "1.2, an overestimate",
     "1.02, an underestimate",
     "10.2, an underestimate"], ans=0,
   why="L(x) = 1 + 10(x - 1) gives 1.2, and x^10 is concave up at x = 1, so the true value 1.21899 is larger."),

 dict(q="The linearization of f(x) = x^3 - 2x at a = 1 is",
   choices=[
     "L(x) = x - 2",
     "L(x) = x + 2",
     "L(x) = 3x - 4",
     "L(x) = -x"], ans=0,
   why="f(1) = -1 and f'(1) = 3(1) - 2 = 1, so L(x) = -1 + 1(x - 1) = x - 2."),

 dict(q="To say that a differentiable function is locally linear at x = a means that",
   choices=[
     "zooming in far enough near (a, f(a)) makes the graph nearly indistinguishable from its tangent line",
     "the function is a linear function on some interval containing a",
     "the graph of f is a straight line",
     "f'(a) = 0"], ans=0,
   why="Local linearity is the geometric content of differentiability, and it is what licenses the tangent line as an approximation."),

 dict(q="A function has f(4) = 12, f'(4) = -2, and f''(x) > 0 for all x. The tangent line estimate of f(4.3) is",
   choices=[
     "11.4, an underestimate",
     "11.4, an overestimate",
     "12.6, an underestimate",
     "10.0, an underestimate"], ans=0,
   why="L(4.3) = 12 - 2(0.3) = 11.4, and concave up means the curve lies above its tangent line, so the true value exceeds 11.4."),

 dict(q="The linearization of f at a = 3 predicts f(3.1) = 8.6, but the true value is f(3.1) = 8.5. This is consistent with",
   choices=[
     "f being concave down on the interval from 3 to 3.1",
     "f being concave up on the interval from 3 to 3.1",
     "f being increasing on the interval from 3 to 3.1",
     "f'(3) being negative"], ans=0,
   why="The tangent line overshot the true value, and a tangent line lies above a curve exactly where the curve is concave down."),

 dict(q="Using differentials, the approximate change in the volume of a sphere when its radius increases from 5 to 5.1 centimeters is",
   choices=[
     "10pi cubic centimeters",
     "pi cubic centimeters",
     "100pi cubic centimeters",
     "(4/3)pi(0.1)^3 cubic centimeters"], ans=0,
   why="dV = 4pi*r^2*dr = 4pi(25)(0.1) = 10pi, about 31.4 cubic centimeters."),

 dict(q="The tangent line to f at a = 2 is L(x) = 7 - 3(x - 2), and f''(x) < 0 for all x. Which conclusion about f(2.5) is correct?",
   choices=[
     "f(2.5) < 5.5",
     "f(2.5) > 5.5",
     "f(2.5) = 5.5",
     "f(2.5) > 7"], ans=0,
   why="L(2.5) = 5.5, and a concave-down graph lies strictly below its tangent line away from the point of tangency."),
]
