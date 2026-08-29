# CALC 6.14 Selecting Techniques for Antidifferentiation — 25 questions
# Mixed problems: the student must decide which technique applies before
# computing.  Answers verified with sympy; see verify_c6_14.py, which
# differentiates every keyed antiderivative back to the integrand, evaluates
# the definite ones, and for each "which technique" question carries out the
# named technique and checks that it really produces the antiderivative.
# Question 24 is conceptual (recognizing which integrand resists substitution).
TOPIC = ("6.14", "Selecting Techniques for Antidifferentiation", 6)
QUESTIONS = [
 dict(q="Which technique is the appropriate first step for int x cos(x^2) dx?", choices=[
   "substitution with u = x^2",
   "integration by parts with u = x",
   "partial fractions",
   "long division"], ans=0,
   why="The factor x is, up to the constant 1/2, the derivative of the inside function x^2, which is exactly what substitution needs."),
 dict(q="Which technique is the appropriate first step for int x cos(x) dx?", choices=[
   "integration by parts with u = x",
   "substitution with u = cos(x)",
   "partial fractions",
   "completing the square"], ans=0,
   why="Here x is not the derivative of anything inside the cosine, so the product must be handled by parts."),
 dict(q="Which technique is the appropriate first step for int (x + 2)/(x^2 - 9) dx?", choices=[
   "partial fractions, since the denominator factors as (x - 3)(x + 3)",
   "completing the square",
   "integration by parts",
   "long division"], ans=0,
   why="The fraction is proper and the denominator splits into distinct linear factors."),
 dict(q="Which technique is the appropriate first step for int (x^2 + 3)/(x + 1) dx?", choices=[
   "long division, since the numerator has the higher degree",
   "partial fractions applied directly",
   "substitution with u = x + 1 alone",
   "integration by parts"], ans=0,
   why="An improper rational function must be divided before any of the logarithm forms apply."),
 dict(q="Which technique is the appropriate first step for int 1/(x^2 + 6x + 10) dx?", choices=[
   "completing the square, since the denominator has no real roots",
   "partial fractions",
   "long division",
   "integration by parts"], ans=0,
   why="The discriminant 36 - 40 is negative, so the quadratic is irreducible and the integral is an arctangent form."),
 dict(q="Which technique is the appropriate first step for int 2x/(x^2 + 1) dx?", choices=[
   "substitution with u = x^2 + 1",
   "partial fractions",
   "integration by parts with u = 2x",
   "completing the square"], ans=0,
   why="The numerator is exactly the derivative of the denominator, so the integral is a logarithm by substitution."),
 dict(q="What is int x^2 sin(x^3) dx?", choices=[
   "-cos(x^3)/3 + C",
   "cos(x^3)/3 + C",
   "-cos(x^3) + C",
   "-x^3 cos(x^3)/3 + C"], ans=0,
   why="With u = x^3, x^2 dx = du/3, so the integral is -(1/3)cos(u)."),
 dict(q="What is int x^2 sin(x) dx?", choices=[
   "-x^2 cos(x) + 2x sin(x) + 2 cos(x) + C",
   "-x^2 cos(x) + 2x sin(x) - 2 cos(x) + C",
   "-x^2 cos(x) - 2x sin(x) - 2 cos(x) + C",
   "-cos(x^3)/3 + C"], ans=0,
   why="Integration by parts applied twice, starting from u = x^2, gives -x^2 cos(x) + 2(x sin(x) + cos(x))."),
 dict(q="What is int (x^3 - 1)/x^2 dx?", choices=[
   "x^2/2 + 1/x + C",
   "x^2/2 - 1/x + C",
   "x^2/2 - ln|x| + C",
   "(x^4/4 - x)/(x^3/3) + C"], ans=0,
   why="Dividing term by term gives x - x^(-2), whose antiderivative is x^2/2 + 1/x."),
 dict(q="What is int 1/(x^2 + 9) dx?", choices=[
   "(1/3) arctan(x/3) + C",
   "arctan(x/3) + C",
   "(1/9) arctan(x/3) + C",
   "(1/3) ln(x^2 + 9) + C"], ans=0,
   why="With a = 3 the standard form int du/(u^2 + a^2) = (1/a) arctan(u/a) applies."),
 dict(q="What is int e^(3x + 1) dx?", choices=[
   "e^(3x + 1)/3 + C",
   "e^(3x + 1) + C",
   "3 e^(3x + 1) + C",
   "e^(3x + 1)/(3x + 1) + C"], ans=0,
   why="With u = 3x + 1, dx = du/3."),
 dict(q="What is int sin^3(x) cos(x) dx?", choices=[
   "sin^4(x)/4 + C",
   "sin^4(x) + C",
   "cos^4(x)/4 + C",
   "-sin^4(x)/4 + C"], ans=0,
   why="With u = sin(x), du = cos(x) dx, so the integral is u^3 du = u^4/4."),
 dict(q="What is int 1/(x^2 - 9) dx?", choices=[
   "(1/6) ln|x - 3| - (1/6) ln|x + 3| + C",
   "(1/6) ln|x - 3| + (1/6) ln|x + 3| + C",
   "(1/3) arctan(x/3) + C",
   "(1/6) ln|x^2 - 9| + C"], ans=0,
   why="The denominator factors, so partial fractions give (1/6)/(x - 3) - (1/6)/(x + 3)."),
 dict(q="What is int (2x + 3)/(x^2 + 3x + 1) dx?", choices=[
   "ln|x^2 + 3x + 1| + C",
   "(1/2) ln|x^2 + 3x + 1| + C",
   "2 ln|x^2 + 3x + 1| + C",
   "arctan(x^2 + 3x + 1) + C"], ans=0,
   why="The numerator is exactly the derivative of the denominator, so the substitution u = x^2 + 3x + 1 gives ln|u| with no extra factor."),
 dict(q="What is int x/(x^2 + 1)^3 dx?", choices=[
   "-1/(4(x^2 + 1)^2) + C",
   "-1/(2(x^2 + 1)^2) + C",
   "1/(4(x^2 + 1)^2) + C",
   "(1/2) ln((x^2 + 1)^3) + C"], ans=0,
   why="With u = x^2 + 1 the integral is (1/2) u^(-3) du = -1/(4u^2)."),
 dict(q="What is int sqrt(x)(x + 1) dx?", choices=[
   "(2/5) x^(5/2) + (2/3) x^(3/2) + C",
   "(2/3) x^(3/2) (x^2/2 + x) + C",
   "(2/5) x^(5/2) + (2/3) x^(1/2) + C",
   "(2/7) x^(7/2) + (2/3) x^(3/2) + C"], ans=0,
   why="Distribute first to x^(3/2) + x^(1/2), then apply the power rule to each term."),
 dict(q="What is int ln(2x) dx for x > 0?", choices=[
   "x ln(2x) - x + C",
   "x ln(2x) + x + C",
   "ln(2x)/x + C",
   "(1/2) x ln(2x) - x + C"], ans=0,
   why="Integration by parts with u = ln(2x) and dv = dx gives x ln(2x) - int x (1/x) dx."),
 dict(q="What is int cos^2(x) dx?", choices=[
   "x/2 + sin(2x)/4 + C",
   "cos^3(x)/3 + C",
   "x/2 - sin(2x)/4 + C",
   "sin^2(x)/2 + C"], ans=0,
   why="No substitution or parts is needed first: the identity cos^2(x) = (1 + cos(2x))/2 turns it into a routine antiderivative."),
 dict(q="What is the value of int from 0 to 1 of x/(x + 1) dx?", choices=[
   "1 - ln(2)",
   "1 + ln(2)",
   "ln(2)",
   "1/2"], ans=0,
   why="Dividing gives 1 - 1/(x + 1), whose antiderivative x - ln|x + 1| runs from 0 to 1 - ln 2."),
 dict(q="What is int (3x^2 + 2x)/(x^3 + x^2) dx?", choices=[
   "ln|x^3 + x^2| + C",
   "(1/3) ln|x^3 + x^2| + C",
   "3 ln|x^3 + x^2| + C",
   "ln|3x^2 + 2x| + C"], ans=0,
   why="The numerator is the derivative of the denominator, so no partial fractions are needed at all."),
 dict(q="What is int x/sqrt(x + 4) dx?", choices=[
   "(2/3)(x + 4)^(3/2) - 8 sqrt(x + 4) + C",
   "(2/3)(x + 4)^(3/2) + 8 sqrt(x + 4) + C",
   "2 x sqrt(x + 4) + C",
   "(2/3)(x + 4)^(3/2) + C"], ans=0,
   why="With u = x + 4 the leftover x becomes u - 4, giving int (u^(1/2) - 4u^(-1/2)) du."),
 dict(q="What is int x/(1 + x^4) dx?", choices=[
   "(1/2) arctan(x^2) + C",
   "arctan(x^2) + C",
   "(1/2) ln(1 + x^4) + C",
   "arctan(x)/2 + C"], ans=0,
   why="With u = x^2, x dx = du/2 and the integral becomes (1/2) int du/(1 + u^2)."),
 dict(q="What is the value of int from 0 to pi/2 of sin(x) e^(cos(x)) dx?", choices=[
   "e - 1",
   "1 - e",
   "e",
   "1"], ans=0,
   why="With u = cos(x) the limits become 1 and 0 and the minus sign flips them back, leaving int from 0 to 1 of e^u du = e - 1."),
 dict(q="Which of these integrals CANNOT be evaluated by a substitution and requires integration by parts?", choices=[
   "int x e^x dx",
   "int x e^(x^2) dx",
   "int (2x + 1)/(x^2 + x) dx",
   "int cos(x) sin(x) dx"], ans=0,
   why="In the other three, one factor is the derivative of the inside of another factor; in int x e^x dx the factors are unrelated in that way."),
 dict(q="What is int x^2/(x^3 + 1) dx?", choices=[
   "(1/3) ln|x^3 + 1| + C",
   "ln|x^3 + 1| + C",
   "3 ln|x^3 + 1| + C",
   "x^3/(3(x^3 + 1)) + C"], ans=0,
   why="With u = x^3 + 1, x^2 dx = du/3, so the integral is (1/3)ln|u|."),
]
