# CALC 6.7 The Fundamental Theorem of Calculus and Definite Integrals — 25 questions
# Answers verified with sympy; see verify_c6_7.py, which evaluates every
# definite integral with sp.integrate and separately confirms the antiderivative
# by differentiating it back to the integrand.
# Questions 1, 11, 16, 25 are conceptual (the statement of the theorem, the
# F(a) - F(b) reversal error, the net change theorem, and the continuity
# hypothesis).
TOPIC = ("6.7", "The Fundamental Theorem of Calculus and Definite Integrals", 6)
QUESTIONS = [
 dict(q="If f is continuous on [a, b] and F is any antiderivative of f, then int from a to b of f(x) dx equals", choices=[
   "F(b) - F(a)",
   "F(a) - F(b)",
   "f(b) - f(a)",
   "F'(b) - F'(a)"], ans=0,
   why="The Fundamental Theorem evaluates the integral as the antiderivative at the upper limit minus the antiderivative at the lower limit."),
 dict(q="What is the value of int from 0 to 3 of 2x dx?", choices=[
   "3",
   "6",
   "9",
   "18"], ans=2,
   why="An antiderivative is x^2, so the value is 9 - 0 = 9."),
 dict(q="What is the value of int from 1 to 4 of 3x^2 dx?", choices=[
   "21",
   "45",
   "63",
   "64"], ans=2,
   why="An antiderivative is x^3, so the value is 64 - 1 = 63; forgetting the lower limit gives 64."),
 dict(q="What is the value of int from 0 to 2 of (x^2 + 1) dx?", choices=[
   "8/3",
   "4",
   "14/3",
   "20/3"], ans=2,
   why="An antiderivative is x^3/3 + x, giving 8/3 + 2 = 14/3."),
 dict(q="What is the value of int from 1 to e of (1/x) dx?", choices=[
   "0",
   "1",
   "e - 1",
   "e"], ans=1,
   why="An antiderivative is ln(x), so the value is ln(e) - ln(1) = 1 - 0 = 1."),
 dict(q="What is the value of int from 0 to pi/2 of cos(x) dx?", choices=[
   "-1",
   "0",
   "1",
   "pi/2"], ans=2,
   why="An antiderivative is sin(x), giving sin(pi/2) - sin(0) = 1."),
 dict(q="What is the value of int from 0 to 1 of e^x dx?", choices=[
   "1",
   "e - 1",
   "e",
   "e + 1"], ans=1,
   why="An antiderivative is e^x, so the value is e^1 - e^0 = e - 1; dropping the lower limit is the common slip."),
 dict(q="What is the value of int from -1 to 2 of (2x - 3) dx?", choices=[
   "-6",
   "-2",
   "2",
   "6"], ans=0,
   why="An antiderivative is x^2 - 3x, giving (4 - 6) - (1 + 3) = -2 - 4 = -6."),
 dict(q="What is the value of int from 1 to 9 of sqrt(x) dx?", choices=[
   "16/3",
   "26/3",
   "52/3",
   "18"], ans=2,
   why="An antiderivative is (2/3)x^(3/2), giving (2/3)(27) - (2/3)(1) = 52/3."),
 dict(q="What is the value of int from 0 to 4 of (x - 2) dx?", choices=[
   "-4",
   "0",
   "4",
   "8"], ans=1,
   why="An antiderivative is x^2/2 - 2x, giving (8 - 8) - 0 = 0: the negative area on [0, 2] cancels the positive area on [2, 4]."),
 dict(q="A student evaluates int from 1 to 3 of x^2 dx by computing F(1) - F(3), where F(x) = x^3/3, and reports -26/3. What is the student's error, and what is the correct value?", choices=[
   "The limits were subtracted in the wrong order; the correct value is 26/3.",
   "The antiderivative should have been 3x^2; the correct value is 78.",
   "The student forgot the constant of integration; the correct value is -26/3 + C.",
   "There is no error."], ans=0,
   why="The Fundamental Theorem calls for F(upper) - F(lower), and reversing the order only changes the sign."),
 dict(q="What is the value of int from 0 to pi of sin(x) dx?", choices=[
   "-2",
   "0",
   "1",
   "2"], ans=3,
   why="An antiderivative is -cos(x), giving -cos(pi) + cos(0) = 1 + 1 = 2."),
 dict(q="What is the value of int from 2 to 5 of 4 dx?", choices=[
   "4",
   "12",
   "20",
   "28"], ans=1,
   why="An antiderivative is 4x, giving 20 - 8 = 12, which is the area of a rectangle of height 4 and width 3."),
 dict(q="What is the value of int from 1 to 2 of (1/x^2) dx?", choices=[
   "-1/2",
   "1/2",
   "ln(2)",
   "7/3"], ans=1,
   why="An antiderivative is -1/x, giving -1/2 - (-1) = 1/2; the answer ln(2) comes from mistaking 1/x^2 for 1/x."),
 dict(q="A particle moves with velocity v(t) = 3t^2 feet per second. What is its change in position from t = 0 to t = 2 seconds?", choices=[
   "4 feet",
   "6 feet",
   "8 feet",
   "12 feet"], ans=2,
   why="The change in position is int from 0 to 2 of 3t^2 dt = t^3 evaluated from 0 to 2, which is 8 feet."),
 dict(q="The net change theorem states that int from a to b of f'(x) dx equals", choices=[
   "f(b) - f(a)",
   "f'(b) - f'(a)",
   "the average rate of change of f on [a, b]",
   "f(b) + f(a)"], ans=0,
   why="Integrating a rate of change over [a, b] recovers the net change in the function itself."),
 dict(q="If f(0) = 5 and int from 0 to 4 of f'(x) dx = 7, what is f(4)?", choices=[
   "2",
   "7",
   "12",
   "35"], ans=2,
   why="The integral of f' gives f(4) - f(0) = 7, so f(4) = 5 + 7 = 12."),
 dict(q="What is the value of int from -2 to 2 of x^2 dx?", choices=[
   "0",
   "8/3",
   "16/3",
   "32/3"], ans=2,
   why="An antiderivative is x^3/3, giving 8/3 - (-8/3) = 16/3; the integrand is even, not odd, so the halves add rather than cancel."),
 dict(q="What is the value of int from 0 to 1 of (4x^3 - 2x) dx?", choices=[
   "-1",
   "0",
   "1",
   "2"], ans=1,
   why="An antiderivative is x^4 - x^2, giving (1 - 1) - 0 = 0."),
 dict(q="What is the value of int from 0 to pi/4 of sec^2(x) dx?", choices=[
   "0",
   "1/2",
   "1",
   "sqrt(2)"], ans=2,
   why="An antiderivative is tan(x), giving tan(pi/4) - tan(0) = 1."),
 dict(q="What is the value of int from 1 to 8 of x^(-2/3) dx?", choices=[
   "3",
   "6",
   "9/2",
   "21/2"], ans=0,
   why="An antiderivative is 3x^(1/3), giving 3(2) - 3(1) = 3."),
 dict(q="What is the value of int from 0 to ln(2) of e^(2x) dx?", choices=[
   "1",
   "3/2",
   "2",
   "3"], ans=1,
   why="An antiderivative is e^(2x)/2, giving 4/2 - 1/2 = 3/2; forgetting the factor 1/2 gives 3."),
 dict(q="What is the value of int from -1 to 1 of |x| dx?", choices=[
   "0",
   "1/2",
   "1",
   "2"], ans=2,
   why="The graph is two triangles of area 1/2 each, and both lie above the axis, so the total is 1."),
 dict(q="A particle moves along a line with velocity v(t) = t^2 - 4 meters per second. What is its displacement from t = 0 to t = 3 seconds?", choices=[
   "-3 meters",
   "3 meters",
   "5 meters",
   "9 meters"], ans=0,
   why="Displacement is int from 0 to 3 of (t^2 - 4) dt = 9 - 12 = -3 meters; the particle ends up left of where it started."),
 dict(q="Why is it wrong to evaluate int from -1 to 1 of (1/x^2) dx as -1/x evaluated from -1 to 1, giving -2?", choices=[
   "The integrand is not continuous on [-1, 1], so the Fundamental Theorem does not apply.",
   "The antiderivative of 1/x^2 is ln|x|.",
   "The limits must be subtracted in the other order.",
   "Nothing is wrong; the value is -2."], ans=0,
   why="The integrand blows up at x = 0, which lies inside the interval, so the hypothesis of the theorem fails; a positive integrand could never give a negative value anyway."),
]
