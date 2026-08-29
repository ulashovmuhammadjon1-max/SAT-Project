# CALC 6.12 Integrating Using Linear Partial Fractions — 25 questions  [BC only]
# Answers verified with sympy; see verify_c6_12.py, which reproduces every
# decomposition with sp.apart and differentiates every keyed antiderivative
# back to the integrand.
# Questions 6, 18, 22 are conceptual (the proper-fraction requirement, which
# denominators the method covers, and dividing before decomposing).
TOPIC = ("6.12", "Integrating Using Linear Partial Fractions", 6)
QUESTIONS = [
 dict(q="The partial fraction decomposition of 1/((x - 1)(x + 2)) is", choices=[
   "(1/3)/(x - 1) - (1/3)/(x + 2)",
   "(1/3)/(x - 1) + (1/3)/(x + 2)",
   "1/(x - 1) - 1/(x + 2)",
   "(1/2)/(x - 1) - (1/2)/(x + 2)"], ans=0,
   why="Solving A(x + 2) + B(x - 1) = 1 by setting x = 1 and x = -2 gives A = 1/3 and B = -1/3."),
 dict(q="What is int 1/((x - 1)(x + 2)) dx?", choices=[
   "(1/3) ln|x - 1| - (1/3) ln|x + 2| + C",
   "(1/3) ln|x - 1| + (1/3) ln|x + 2| + C",
   "ln|(x - 1)(x + 2)| + C",
   "(1/3) ln|(x - 1)(x + 2)| + C"], ans=0,
   why="Each term of the decomposition integrates to a logarithm, and the second one carries a minus sign."),
 dict(q="The partial fraction decomposition of 5/((x - 3)(x + 2)) is", choices=[
   "1/(x - 3) - 1/(x + 2)",
   "1/(x - 3) + 1/(x + 2)",
   "5/(x - 3) - 5/(x + 2)",
   "(1/5)/(x - 3) - (1/5)/(x + 2)"], ans=0,
   why="A(x + 2) + B(x - 3) = 5 gives 5A = 5 at x = 3 and -5B = 5 at x = -2, so A = 1 and B = -1."),
 dict(q="What is int 1/(x^2 - 1) dx?", choices=[
   "(1/2) ln|x - 1| - (1/2) ln|x + 1| + C",
   "(1/2) ln|x - 1| + (1/2) ln|x + 1| + C",
   "ln|x^2 - 1| + C",
   "arctan(x) + C"], ans=0,
   why="Factor as (x - 1)(x + 1); the decomposition is (1/2)/(x - 1) - (1/2)/(x + 1)."),
 dict(q="What is int (x + 7)/((x - 1)(x + 3)) dx?", choices=[
   "2 ln|x - 1| - ln|x + 3| + C",
   "ln|x - 1| - 2 ln|x + 3| + C",
   "2 ln|x - 1| + ln|x + 3| + C",
   "ln|(x - 1)(x + 3)| + C"], ans=0,
   why="A(x + 3) + B(x - 1) = x + 7 gives 4A = 8 at x = 1 and -4B = 4 at x = -3, so A = 2 and B = -1."),
 dict(q="Before a rational function can be split into partial fractions, it must be", choices=[
   "a proper fraction, with numerator degree less than denominator degree",
   "an improper fraction",
   "continuous everywhere",
   "written with a squared denominator"], ans=0,
   why="An improper rational function must be divided first; the quotient is integrated separately and only the proper remainder is decomposed."),
 dict(q="Which is the correct setup for the partial fraction decomposition of 3x/((x - 2)(x + 5))?", choices=[
   "A/(x - 2) + B/(x + 5)",
   "A/((x - 2)(x + 5))",
   "(Ax + B)/(x - 2) + C/(x + 5)",
   "A/(x - 2) + B/(x - 2)^2"], ans=0,
   why="Each distinct linear factor contributes one term with a constant numerator."),
 dict(q="What is int 1/(x(x + 1)) dx?", choices=[
   "ln|x| - ln|x + 1| + C",
   "ln|x| + ln|x + 1| + C",
   "ln|x(x + 1)| + C",
   "-1/(x(x + 1)) + C"], ans=0,
   why="The decomposition is 1/x - 1/(x + 1), so the antiderivative is the difference of the two logarithms."),
 dict(q="What is int 1/(x^2 - 4) dx?", choices=[
   "(1/4) ln|x - 2| - (1/4) ln|x + 2| + C",
   "(1/4) ln|x - 2| + (1/4) ln|x + 2| + C",
   "(1/2) ln|x - 2| - (1/2) ln|x + 2| + C",
   "(1/2) arctan(x/2) + C"], ans=0,
   why="With A(x + 2) + B(x - 2) = 1, x = 2 gives A = 1/4 and x = -2 gives B = -1/4."),
 dict(q="What is the value of int from 2 to 3 of 1/(x(x - 1)) dx?", choices=[
   "ln(4/3)",
   "ln(3/2)",
   "ln(2)",
   "ln(3/4)"], ans=0,
   why="The decomposition is 1/(x - 1) - 1/x, so the antiderivative is ln|(x - 1)/x|, giving ln(2/3) - ln(1/2) = ln(4/3)."),
 dict(q="What is int (3x + 11)/((x - 3)(x + 2)) dx?", choices=[
   "4 ln|x - 3| - ln|x + 2| + C",
   "ln|x - 3| - 4 ln|x + 2| + C",
   "4 ln|x - 3| + ln|x + 2| + C",
   "3 ln|(x - 3)(x + 2)| + C"], ans=0,
   why="A(x + 2) + B(x - 3) = 3x + 11 gives 5A = 20 at x = 3 and -5B = 5 at x = -2."),
 dict(q="For 0 < x < 1, what is int 1/(x(1 - x)) dx?", choices=[
   "ln|x| - ln|1 - x| + C",
   "ln|x| + ln|1 - x| + C",
   "-ln|x(1 - x)| + C",
   "ln|1 - x| - ln|x| + C"], ans=0,
   why="The decomposition is 1/x + 1/(1 - x), and antidifferentiating the second term brings a minus sign from the chain rule: -ln|1 - x|."),
 dict(q="What is the value of int from 0 to 1 of 1/((x + 1)(x + 2)) dx?", choices=[
   "ln(4/3)",
   "ln(3/2)",
   "ln(2/3)",
   "ln(2)"], ans=0,
   why="The decomposition 1/(x + 1) - 1/(x + 2) integrates to ln|(x + 1)/(x + 2)|, giving ln(2/3) - ln(1/2) = ln(4/3)."),
 dict(q="What is int x^2/(x^2 - 1) dx?", choices=[
   "x + (1/2) ln|x - 1| - (1/2) ln|x + 1| + C",
   "(1/2) ln|x - 1| - (1/2) ln|x + 1| + C",
   "x + ln|x^2 - 1| + C",
   "x - (1/2) ln|x - 1| + (1/2) ln|x + 1| + C"], ans=0,
   why="The fraction is improper: dividing gives 1 + 1/(x^2 - 1), and only the remainder is decomposed."),
 dict(q="What is int 4x/(x^2 - 4) dx?", choices=[
   "2 ln|x - 2| + 2 ln|x + 2| + C",
   "2 ln|x - 2| - 2 ln|x + 2| + C",
   "4 ln|x^2 - 4| + C",
   "ln|x - 2| + ln|x + 2| + C"], ans=0,
   why="A(x + 2) + B(x - 2) = 4x gives A = 2 and B = 2, and the sum of the two logarithms is 2 ln|x^2 - 4|."),
 dict(q="In the decomposition (2x + 3)/((x + 1)(x - 4)) = A/(x + 1) + B/(x - 4), what is A?", choices=[
   "-1/5",
   "1/5",
   "11/5",
   "-11/5"], ans=0,
   why="Setting x = -1 in A(x - 4) + B(x + 1) = 2x + 3 gives -5A = 1, so A = -1/5."),
 dict(q="What is int 6/((x - 1)(x + 5)) dx?", choices=[
   "ln|x - 1| - ln|x + 5| + C",
   "ln|x - 1| + ln|x + 5| + C",
   "6 ln|x - 1| - 6 ln|x + 5| + C",
   "(1/6) ln|(x - 1)/(x + 5)| + C"], ans=0,
   why="A(x + 5) + B(x - 1) = 6 gives 6A = 6 at x = 1 and -6B = 6 at x = -5, so A = 1 and B = -1."),
 dict(q="The linear partial fraction method as tested on the AP exam applies to a proper rational function whose denominator", choices=[
   "factors into distinct linear factors",
   "is an irreducible quadratic",
   "has a repeated linear factor",
   "has degree lower than the numerator's"], ans=0,
   why="Each distinct linear factor contributes one constant over that factor; irreducible quadratics call for completing the square instead."),
 dict(q="What is the value of int from 3 to 4 of 1/(x^2 - 4) dx?", choices=[
   "(1/4) ln(5/3)",
   "(1/4) ln(3/5)",
   "(1/2) ln(5/3)",
   "ln(5/3)"], ans=0,
   why="The antiderivative is (1/4)ln|(x - 2)/(x + 2)|, giving (1/4)(ln(1/3) - ln(1/5)) = (1/4)ln(5/3)."),
 dict(q="What is int (x + 1)/(x^2 - x - 6) dx?", choices=[
   "(4/5) ln|x - 3| + (1/5) ln|x + 2| + C",
   "(1/5) ln|x - 3| + (4/5) ln|x + 2| + C",
   "(4/5) ln|x - 3| - (1/5) ln|x + 2| + C",
   "ln|x^2 - x - 6| + C"], ans=0,
   why="The denominator factors as (x - 3)(x + 2), and A(x + 2) + B(x - 3) = x + 1 gives 5A = 4 and -5B = -1."),
 dict(q="What is int 2/(x^2 + x) dx?", choices=[
   "2 ln|x| - 2 ln|x + 1| + C",
   "2 ln|x| + 2 ln|x + 1| + C",
   "ln|x| - ln|x + 1| + C",
   "2 ln|x^2 + x| + C"], ans=0,
   why="Factoring gives x(x + 1) and the decomposition 2/x - 2/(x + 1)."),
 dict(q="What must be done first to integrate x^3/(x^2 - 1)?", choices=[
   "Divide, since the numerator has the higher degree",
   "Decompose directly into A/(x - 1) + B/(x + 1)",
   "Complete the square in the denominator",
   "Substitute u = x^2 - 1"], ans=0,
   why="Partial fractions applies only to a proper fraction, so long division must come first, leaving x + x/(x^2 - 1)."),
 dict(q="What is the value of int from 1 to 2 of 1/(x(x + 2)) dx?", choices=[
   "(1/2) ln(3/2)",
   "(1/2) ln(2/3)",
   "ln(3/2)",
   "(1/2) ln(4/3)"], ans=0,
   why="The antiderivative is (1/2)ln|x/(x + 2)|, giving (1/2)(ln(1/2) - ln(1/3)) = (1/2)ln(3/2)."),
 dict(q="In the decomposition 7/((x - 2)(x + 5)) = A/(x - 2) + B/(x + 5), what are A and B?", choices=[
   "A = 1 and B = -1",
   "A = -1 and B = 1",
   "A = 7 and B = -7",
   "A = 1/7 and B = -1/7"], ans=0,
   why="A(x + 5) + B(x - 2) = 7 gives 7A = 7 at x = 2 and -7B = 7 at x = -5."),
 dict(q="What is int (5x - 2)/(x^2 - 4) dx?", choices=[
   "2 ln|x - 2| + 3 ln|x + 2| + C",
   "3 ln|x - 2| + 2 ln|x + 2| + C",
   "2 ln|x - 2| - 3 ln|x + 2| + C",
   "5 ln|x^2 - 4| - 2 arctan(x/2) + C"], ans=0,
   why="A(x + 2) + B(x - 2) = 5x - 2 gives 4A = 8 at x = 2 and -4B = -12 at x = -2, so A = 2 and B = 3."),
]
