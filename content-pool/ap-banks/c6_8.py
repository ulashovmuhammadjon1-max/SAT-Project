# CALC 6.8 Finding Antiderivatives and Indefinite Integrals: Basic Rules and Notation — 25 questions
# Answers verified with sympy; see verify_c6_8.py, which differentiates the
# keyed antiderivative back to the integrand and confirms that no distractor
# differentiates to the same thing (two antiderivatives of one function differ
# by a constant, so the check compares derivatives, not expressions).
# Questions 12, 20, 25 are conceptual (why the power rule excludes n = -1, why
# + C is required, and indefinite versus definite notation).
TOPIC = ("6.8", "Finding Antiderivatives and Indefinite Integrals: Basic Rules and Notation", 6)
QUESTIONS = [
 dict(q="What is int x^5 dx?", choices=[
   "x^6/6 + C",
   "5x^4 + C",
   "x^6 + C",
   "x^4/4 + C"], ans=0,
   why="The power rule raises the exponent by one and divides by the new exponent."),
 dict(q="What is int 3x^2 dx?", choices=[
   "x^3 + C",
   "3x^3 + C",
   "6x + C",
   "x^3/3 + C"], ans=0,
   why="Antidifferentiating x^2 gives x^3/3, and the factor 3 cancels the 1/3."),
 dict(q="What is int (1/x) dx?", choices=[
   "ln|x| + C",
   "-1/x^2 + C",
   "x^0/0 + C",
   "1/(2x^2) + C"], ans=0,
   why="The power rule cannot be used when the exponent is -1; the antiderivative is the natural logarithm of the absolute value of x."),
 dict(q="What is int e^x dx?", choices=[
   "e^x + C",
   "e^x/x + C",
   "x e^(x-1) + C",
   "e^(x+1)/(x + 1) + C"], ans=0,
   why="The exponential function is its own derivative, so it is also its own antiderivative."),
 dict(q="What is int cos(x) dx?", choices=[
   "sin(x) + C",
   "-sin(x) + C",
   "-cos(x) + C",
   "tan(x) + C"], ans=0,
   why="The derivative of sin(x) is cos(x)."),
 dict(q="What is int sin(x) dx?", choices=[
   "-cos(x) + C",
   "cos(x) + C",
   "-sin(x) + C",
   "sec(x) + C"], ans=0,
   why="The derivative of -cos(x) is +sin(x); dropping that minus sign is the most common antiderivative error in trigonometry."),
 dict(q="What is int sec^2(x) dx?", choices=[
   "tan(x) + C",
   "sec(x) tan(x) + C",
   "sec^3(x)/3 + C",
   "2 sec(x) + C"], ans=0,
   why="The derivative of tan(x) is sec^2(x)."),
 dict(q="What is int x^(-2) dx?", choices=[
   "-1/x + C",
   "-2/x^3 + C",
   "x^(-1) + C",
   "ln|x^2| + C"], ans=0,
   why="The power rule gives x^(-1)/(-1) = -1/x, and its derivative is indeed x^(-2)."),
 dict(q="What is int sqrt(x) dx?", choices=[
   "(2/3) x^(3/2) + C",
   "(3/2) x^(3/2) + C",
   "(1/2) x^(-1/2) + C",
   "x^(3/2) + C"], ans=0,
   why="Writing sqrt(x) as x^(1/2), the power rule gives x^(3/2) divided by 3/2, which is (2/3)x^(3/2)."),
 dict(q="What is int (4x^3 - 6x + 5) dx?", choices=[
   "x^4 - 3x^2 + 5x + C",
   "x^4 - 6x^2 + 5x + C",
   "12x^2 - 6 + C",
   "4x^4 - 3x^2 + 5x + C"], ans=0,
   why="Antidifferentiate term by term: 4x^3 gives x^4, -6x gives -3x^2, and 5 gives 5x."),
 dict(q="What is int 1/(1 + x^2) dx?", choices=[
   "arctan(x) + C",
   "ln(1 + x^2) + C",
   "-1/(1 + x^2)^2 + C",
   "arcsin(x) + C"], ans=0,
   why="The derivative of arctan(x) is 1/(1 + x^2); ln(1 + x^2) would require a factor of 2x in the numerator."),
 dict(q="The power rule for antiderivatives, int x^n dx = x^(n+1)/(n + 1) + C, requires n to be different from -1 because", choices=[
   "for n = -1 the formula would divide by zero, and the antiderivative is ln|x| instead",
   "x^(-1) has no antiderivative",
   "the rule only holds for positive integers n",
   "for n = -1 the antiderivative is x^0 + C"], ans=0,
   why="Substituting n = -1 makes the denominator n + 1 equal to zero, which is why that case has its own logarithmic antiderivative."),
 dict(q="What is int 5 dx?", choices=[
   "5x + C",
   "5 + C",
   "x + C",
   "5x^2/2 + C"], ans=0,
   why="The derivative of 5x is the constant 5."),
 dict(q="What is int (2/x) dx?", choices=[
   "2 ln|x| + C",
   "ln|2x| + 2C",
   "-2/x^2 + C",
   "2/(x^2) + C"], ans=0,
   why="A constant multiple passes through the integral, giving 2 ln|x| + C."),
 dict(q="What is int e^(3x) dx?", choices=[
   "e^(3x)/3 + C",
   "e^(3x) + C",
   "3 e^(3x) + C",
   "e^(3x)/x + C"], ans=0,
   why="Differentiating e^(3x)/3 returns e^(3x); leaving out the 1/3 is the standard slip."),
 dict(q="If F'(x) = 2x and F(1) = 5, what is F(x)?", choices=[
   "x^2 + 4",
   "x^2 + 5",
   "x^2 - 4",
   "2x^2 + 3"], ans=0,
   why="F(x) = x^2 + C, and F(1) = 1 + C = 5 forces C = 4."),
 dict(q="If f'(x) = 6x^2 and f(0) = -2, what is f(x)?", choices=[
   "2x^3 - 2",
   "2x^3 + 2",
   "6x^3 - 2",
   "12x - 2"], ans=0,
   why="Antidifferentiating gives 2x^3 + C, and f(0) = C = -2."),
 dict(q="What is int x(x + 2) dx?", choices=[
   "x^3/3 + x^2 + C",
   "x^3/3 + 2x^2 + C",
   "x^2(x^2/2 + 2x)/2 + C",
   "(x^2/2)(x^2/2 + 2x) + C"], ans=0,
   why="Expand first to x^2 + 2x, then antidifferentiate term by term; there is no product rule for integrals."),
 dict(q="What is int sec(x) tan(x) dx?", choices=[
   "sec(x) + C",
   "tan(x) + C",
   "sec^2(x)/2 + C",
   "sec(x) tan(x) + C"], ans=0,
   why="The derivative of sec(x) is sec(x)tan(x)."),
 dict(q="Why must an indefinite integral include the constant C?", choices=[
   "Because any two antiderivatives of the same function differ by a constant, so C describes the whole family",
   "Because the integral is only an approximation",
   "Because C accounts for the lower limit of integration",
   "Because without C the answer would not be differentiable"], ans=0,
   why="Adding a constant does not change a derivative, so every antiderivative of f has the form F(x) + C and the notation must say so."),
 dict(q="What is int (1/sqrt(x)) dx?", choices=[
   "2 sqrt(x) + C",
   "sqrt(x)/2 + C",
   "-1/(2 x^(3/2)) + C",
   "ln|sqrt(x)| + C"], ans=0,
   why="Write the integrand as x^(-1/2); the power rule gives x^(1/2) divided by 1/2, which is 2 sqrt(x)."),
 dict(q="A particle has velocity v(t) = 4t + 1 and position s(0) = 3. What is s(t)?", choices=[
   "2t^2 + t + 3",
   "2t^2 + t",
   "4t^2 + t + 3",
   "2t^2 + 3t + 1"], ans=0,
   why="Antidifferentiating the velocity gives 2t^2 + t + C, and s(0) = C = 3."),
 dict(q="What is int (3/x^4) dx?", choices=[
   "-1/x^3 + C",
   "-3/x^3 + C",
   "3/x^3 + C",
   "-12/x^5 + C"], ans=0,
   why="Write the integrand as 3x^(-4); the power rule gives 3x^(-3)/(-3) = -x^(-3)."),
 dict(q="Which function is an antiderivative of f(x) = 2 cos(x) - 3 sin(x)?", choices=[
   "2 sin(x) + 3 cos(x)",
   "2 sin(x) - 3 cos(x)",
   "-2 sin(x) + 3 cos(x)",
   "-2 sin(x) - 3 cos(x)"], ans=0,
   why="Differentiating 2 sin(x) + 3 cos(x) gives 2 cos(x) - 3 sin(x), the two sign changes landing correctly."),
 dict(q="Which statement correctly distinguishes int f(x) dx from int from a to b of f(x) dx?", choices=[
   "The first is a family of functions and the second is a number",
   "The first is a number and the second is a family of functions",
   "Both are numbers, but the second one depends on x",
   "They are two notations for the same thing"], ans=0,
   why="An indefinite integral names all antiderivatives of f, while a definite integral evaluates to a single value."),
]
