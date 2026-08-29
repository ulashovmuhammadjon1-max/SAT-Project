# CALC 6.10 Integrating Functions Using Long Division and Completing the Square — 25 questions
# Answers verified with sympy; see verify_c6_10.py, which differentiates every
# keyed antiderivative back to the integrand, confirms each long division with
# sp.div, and confirms each completed square as an identity.
# Questions 1 and 24 are conceptual (when division is needed, and when a
# quadratic denominator calls for completing the square rather than factoring).
TOPIC = ("6.10", "Integrating Functions Using Long Division and Completing the Square", 6)
QUESTIONS = [
 dict(q="Polynomial long division should be performed before integrating a rational function when", choices=[
   "the degree of the numerator is greater than or equal to the degree of the denominator",
   "the degree of the numerator is less than the degree of the denominator",
   "the denominator has no real roots",
   "the numerator is a constant"], ans=0,
   why="Only a proper rational function, with numerator degree strictly smaller, is ready for the logarithm or arctangent forms; otherwise divide first."),
 dict(q="What is int (x + 3)/x dx?", choices=[
   "x + 3 ln|x| + C",
   "1 + 3 ln|x| + C",
   "ln|x| + 3x + C",
   "(x^2/2 + 3x)/(x^2/2) + C"], ans=0,
   why="Dividing gives 1 + 3/x, whose antiderivative is x + 3 ln|x|."),
 dict(q="What is int (2x + 1)/x dx?", choices=[
   "2x + ln|x| + C",
   "2 + ln|x| + C",
   "2x + 1/x + C",
   "x^2 + ln|x| + C"], ans=0,
   why="Dividing gives 2 + 1/x, whose antiderivative is 2x + ln|x|."),
 dict(q="What is int x/(x + 2) dx?", choices=[
   "x - 2 ln|x + 2| + C",
   "x + 2 ln|x + 2| + C",
   "ln|x + 2| + C",
   "x^2/(2 ln|x + 2|) + C"], ans=0,
   why="Since x/(x + 2) = 1 - 2/(x + 2), the antiderivative is x - 2 ln|x + 2|."),
 dict(q="What is int 3x/(x - 1) dx?", choices=[
   "3x + 3 ln|x - 1| + C",
   "3x - 3 ln|x - 1| + C",
   "3 ln|x - 1| + C",
   "3x^2/2 + ln|x - 1| + C"], ans=0,
   why="Dividing gives 3 + 3/(x - 1), so the antiderivative is 3x + 3 ln|x - 1|."),
 dict(q="What is int (4x + 5)/(x + 2) dx?", choices=[
   "4x - 3 ln|x + 2| + C",
   "4x + 3 ln|x + 2| + C",
   "4x + 5 ln|x + 2| + C",
   "4 - 3/(x + 2)^2 + C"], ans=0,
   why="Dividing gives 4 - 3/(x + 2), since 4(x + 2) = 4x + 8 overshoots 4x + 5 by 3."),
 dict(q="What is int x^2/(x + 1) dx?", choices=[
   "x^2/2 - x + ln|x + 1| + C",
   "x^2/2 + x + ln|x + 1| + C",
   "x^2/2 - x - ln|x + 1| + C",
   "x^3/(3 ln|x + 1|) + C"], ans=0,
   why="Long division gives x - 1 + 1/(x + 1)."),
 dict(q="What is int (x^2 - 4)/(x - 2) dx?", choices=[
   "x^2/2 + 2x + C",
   "x^2/2 - 2x + C",
   "ln|x - 2| + C",
   "(x^3/3 - 4x)/(x^2/2 - 2x) + C"], ans=0,
   why="The numerator factors as (x - 2)(x + 2), so the integrand is simply x + 2 for x not equal to 2."),
 dict(q="What is int x^2/(x^2 + 1) dx?", choices=[
   "x - arctan(x) + C",
   "x + arctan(x) + C",
   "arctan(x) + C",
   "x^3/(3(x^3/3 + x)) + C"], ans=0,
   why="Dividing gives 1 - 1/(x^2 + 1), whose antiderivative is x - arctan(x)."),
 dict(q="What is int (2x^2 + 3)/(x^2 + 1) dx?", choices=[
   "2x + arctan(x) + C",
   "2x - arctan(x) + C",
   "2x + 3 arctan(x) + C",
   "2 + arctan(x) + C"], ans=0,
   why="Dividing gives 2 + 1/(x^2 + 1), since 2(x^2 + 1) = 2x^2 + 2 leaves a remainder of 1."),
 dict(q="For x not equal to -1, the expression (x^2 + 3x + 2)/(x + 1) simplifies to", choices=[
   "x + 2",
   "x + 3",
   "x^2 + 2",
   "x - 2"], ans=0,
   why="The numerator factors as (x + 1)(x + 2), and the common factor cancels."),
 dict(q="Completing the square, x^2 + 6x + 13 can be written as", choices=[
   "(x + 3)^2 + 4",
   "(x + 3)^2 + 13",
   "(x + 6)^2 - 23",
   "(x - 3)^2 + 4"], ans=0,
   why="Half of 6 is 3, and (x + 3)^2 = x^2 + 6x + 9 leaves 13 - 9 = 4."),
 dict(q="What is int 1/(x^2 + 4x + 5) dx?", choices=[
   "arctan(x + 2) + C",
   "arctan(x + 4) + C",
   "ln|x^2 + 4x + 5| + C",
   "(1/2) arctan((x + 2)/2) + C"], ans=0,
   why="The denominator is (x + 2)^2 + 1, so the antiderivative is arctan(x + 2)."),
 dict(q="What is int 1/(x^2 - 6x + 13) dx?", choices=[
   "(1/2) arctan((x - 3)/2) + C",
   "arctan(x - 3) + C",
   "2 arctan((x - 3)/2) + C",
   "(1/2) ln|x^2 - 6x + 13| + C"], ans=0,
   why="The denominator is (x - 3)^2 + 4, and int du/(u^2 + a^2) = (1/a) arctan(u/a) with a = 2."),
 dict(q="What is int 1/(x^2 + 2x + 5) dx?", choices=[
   "(1/2) arctan((x + 1)/2) + C",
   "arctan(x + 1) + C",
   "(1/2) arctan(x + 1) + C",
   "(1/4) arctan((x + 1)/2) + C"], ans=0,
   why="The denominator is (x + 1)^2 + 4, so a = 2 and the answer carries the factor 1/2."),
 dict(q="What is int 1/(x^2 - 2x + 10) dx?", choices=[
   "(1/3) arctan((x - 1)/3) + C",
   "(1/3) arctan((x - 1)/9) + C",
   "3 arctan((x - 1)/3) + C",
   "arctan((x - 1)/3) + C"], ans=0,
   why="The denominator is (x - 1)^2 + 9, so a = 3 and both the factor and the argument carry a 3."),
 dict(q="What is int 1/sqrt(8 + 2x - x^2) dx?", choices=[
   "arcsin((x - 1)/3) + C",
   "arcsin((x + 1)/3) + C",
   "(1/3) arcsin((x - 1)/3) + C",
   "arctan((x - 1)/3) + C"], ans=0,
   why="Completing the square gives 9 - (x - 1)^2, which is the arcsine form with a = 3."),
 dict(q="What is the value of int from 1 to 2 of (x + 1)/x dx?", choices=[
   "1 + ln(2)",
   "ln(2)",
   "1 + 2 ln(2)",
   "3/2"], ans=0,
   why="Dividing gives 1 + 1/x, so the antiderivative x + ln|x| runs from 1 to 2 + ln(2)."),
 dict(q="What is the value of int from 0 to 1 of 1/(x^2 + 2x + 2) dx?", choices=[
   "arctan(2) - pi/4",
   "arctan(2)",
   "pi/4",
   "ln(5)/2"], ans=0,
   why="The denominator is (x + 1)^2 + 1, so the antiderivative is arctan(x + 1), evaluated from arctan(1) = pi/4 to arctan(2)."),
 dict(q="What is the value of int from 0 to 2 of x/(x + 2) dx?", choices=[
   "2 - 2 ln(2)",
   "2 + 2 ln(2)",
   "2 ln(2)",
   "1/2"], ans=0,
   why="The antiderivative is x - 2 ln|x + 2|, giving (2 - 2 ln 4) - (0 - 2 ln 2) = 2 - 2 ln 2."),
 dict(q="What is int (x + 3)/(x^2 + 2x + 5) dx?", choices=[
   "(1/2) ln(x^2 + 2x + 5) + arctan((x + 1)/2) + C",
   "(1/2) ln(x^2 + 2x + 5) + C",
   "ln(x^2 + 2x + 5) + arctan((x + 1)/2) + C",
   "(1/2) ln(x^2 + 2x + 5) + (1/2) arctan((x + 1)/2) + C"], ans=0,
   why="Split the numerator as (1/2)(2x + 2) + 2: the first piece is a logarithm, and the second gives 2 times (1/2)arctan((x + 1)/2)."),
 dict(q="What is int (x^2 + 2x)/(x + 1) dx?", choices=[
   "x^2/2 + x - ln|x + 1| + C",
   "x^2/2 + x + ln|x + 1| + C",
   "x^2/2 + 2x - ln|x + 1| + C",
   "x + 1 - ln|x + 1| + C"], ans=0,
   why="Long division gives x + 1 - 1/(x + 1)."),
 dict(q="What is int (x^3 + 2)/x^2 dx?", choices=[
   "x^2/2 - 2/x + C",
   "x^2/2 + 2/x + C",
   "x^2/2 - 2 ln|x| + C",
   "(x^4/4 + 2x)/(x^3/3) + C"], ans=0,
   why="Dividing term by term gives x + 2x^(-2), whose antiderivative is x^2/2 - 2/x."),
 dict(q="For int 1/(x^2 - 5x + 6) dx, why is completing the square NOT the appropriate first step?", choices=[
   "The denominator factors over the real numbers, so partial fractions apply instead",
   "The numerator has a higher degree than the denominator",
   "The denominator is irreducible",
   "The integrand is not continuous anywhere"], ans=0,
   why="x^2 - 5x + 6 = (x - 2)(x - 3), and completing the square would lead to a logarithm of an absolute-value difference rather than the clean arctangent form; the factored denominator is a partial-fractions problem."),
 dict(q="What is int (x^2 + 1)/(x - 1) dx?", choices=[
   "x^2/2 + x + 2 ln|x - 1| + C",
   "x^2/2 + x - 2 ln|x - 1| + C",
   "x^2/2 - x + 2 ln|x - 1| + C",
   "x^2/2 + x + ln|x - 1| + C"], ans=0,
   why="Long division gives x + 1 + 2/(x - 1), since (x - 1)(x + 1) = x^2 - 1 leaves a remainder of 2."),
]
