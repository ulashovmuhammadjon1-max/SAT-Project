# CALC 6.9 Integrating Using Substitution — 25 questions
# Answers verified with sympy; see verify_c6_9.py, which differentiates every
# keyed antiderivative back to the integrand and evaluates every definite
# integral both ways -- in x and in u with converted limits -- so the
# limit-changing questions are checked by the method they are testing.
# Questions 3, 14, 25 are conceptual (choosing u, the forgotten limit change,
# and setting up du).
TOPIC = ("6.9", "Integrating Using Substitution", 6)
QUESTIONS = [
 dict(q="What is int 2x (x^2 + 1)^3 dx?", choices=[
   "(x^2 + 1)^4/4 + C",
   "(x^2 + 1)^4/8 + C",
   "(x^2 + 1)^4 + C",
   "6x^2 (x^2 + 1)^2 + C"], ans=0,
   why="With u = x^2 + 1 the factor 2x dx is exactly du, so the integral is u^3 du = u^4/4."),
 dict(q="What is int x (x^2 + 1)^3 dx?", choices=[
   "(x^2 + 1)^4/8 + C",
   "(x^2 + 1)^4/4 + C",
   "(x^2 + 1)^4/2 + C",
   "x^2 (x^2 + 1)^4/8 + C"], ans=0,
   why="Here x dx = du/2, so the integral is (1/2)u^3 du = u^4/8."),
 dict(q="Which substitution turns int x sqrt(x^2 + 9) dx into an integral in u alone?", choices=[
   "u = x^2 + 9",
   "u = sqrt(x^2 + 9)",
   "u = x",
   "u = 9"], ans=0,
   why="With u = x^2 + 9, du = 2x dx matches the leftover factor x dx up to the constant 1/2."),
 dict(q="What is int cos(3x) dx?", choices=[
   "sin(3x)/3 + C",
   "3 sin(3x) + C",
   "sin(3x) + C",
   "-sin(3x)/3 + C"], ans=0,
   why="With u = 3x, dx = du/3, so the antiderivative carries the factor 1/3."),
 dict(q="What is int sin(x) cos(x) dx?", choices=[
   "sin^2(x)/2 + C",
   "sin^2(x) + C",
   "cos^2(x)/2 + C",
   "sin(x) cos(x) + C"], ans=0,
   why="With u = sin(x), du = cos(x) dx, so the integral is u du = u^2/2; differentiating cos^2(x)/2 gives -sin(x)cos(x), the wrong sign."),
 dict(q="What is int 2x e^(x^2) dx?", choices=[
   "e^(x^2) + C",
   "e^(x^2)/2 + C",
   "2x e^(x^2) + C",
   "x^2 e^(x^2) + C"], ans=0,
   why="With u = x^2 the factor 2x dx is du, so the integral is e^u du = e^u."),
 dict(q="What is int (2x + 1)^5 dx?", choices=[
   "(2x + 1)^6/12 + C",
   "(2x + 1)^6/6 + C",
   "(2x + 1)^6/2 + C",
   "10 (2x + 1)^4 + C"], ans=0,
   why="With u = 2x + 1, dx = du/2, giving u^6/12."),
 dict(q="What is int 1/(3x + 2) dx?", choices=[
   "(1/3) ln|3x + 2| + C",
   "ln|3x + 2| + C",
   "3 ln|3x + 2| + C",
   "-1/(3(3x + 2)^2) + C"], ans=0,
   why="With u = 3x + 2, dx = du/3, so the antiderivative is (1/3)ln|u|."),
 dict(q="What is the value of int from 0 to 2 of 2x (x^2 + 1)^3 dx?", choices=[
   "4",
   "39",
   "156",
   "625/4"], ans=2,
   why="With u = x^2 + 1 the limits become u = 1 and u = 5, giving (5^4 - 1^4)/4 = 624/4 = 156."),
 dict(q="If the substitution u = x^2 + 1 is used in int from 0 to 2 of x sqrt(x^2 + 1) dx, what are the new limits of integration?", choices=[
   "from u = 1 to u = 5",
   "from u = 0 to u = 2",
   "from u = 1 to u = 4",
   "from u = 0 to u = 5"], ans=0,
   why="The limits are values of x and must be run through u = x^2 + 1: x = 0 gives u = 1 and x = 2 gives u = 5."),
 dict(q="Evaluate int from 0 to pi/2 of sin^2(x) cos(x) dx by substituting u = sin(x) and then converting back to x.", choices=[
   "1/3",
   "1/2",
   "2/3",
   "1"], ans=0,
   why="The antiderivative in u is u^3/3, so in x it is sin^3(x)/3, which runs from 0 to 1/3."),
 dict(q="What is the value of int from 0 to 1 of x e^(x^2) dx?", choices=[
   "(e - 1)/2",
   "e - 1",
   "e/2",
   "2(e - 1)"], ans=0,
   why="With u = x^2 the limits become 0 and 1 and the integral is (1/2) e^u du, giving (e - 1)/2."),
 dict(q="What is the value of int from 0 to 1 of (3x + 1)^4 dx?", choices=[
   "341/5",
   "1023/5",
   "341/15",
   "1024/15"], ans=0,
   why="With u = 3x + 1 the limits become 1 and 4, giving (4^5 - 1^5)/15 = 1023/15 = 341/5."),
 dict(q="A student substitutes u = x^2 + 1 into int from 0 to 2 of 2x (x^2 + 1)^3 dx and writes int from 0 to 2 of u^3 du = 4. What is the error?", choices=[
   "The limits 0 and 2 are values of x and must be converted to u = 1 and u = 5.",
   "The substitution should have been u = 2x.",
   "The differential du should be 2 dx.",
   "There is no error."], ans=0,
   why="After a substitution the limits must either be converted to values of u or the antiderivative must be written back in terms of x before the original limits are used."),
 dict(q="What is int tan(x) dx?", choices=[
   "-ln|cos(x)| + C",
   "ln|cos(x)| + C",
   "sec^2(x) + C",
   "tan^2(x)/2 + C"], ans=0,
   why="Write tan(x) as sin(x)/cos(x) and let u = cos(x), so du = -sin(x) dx and the integral is -ln|u|."),
 dict(q="What is int (ln(x))/x dx for x > 0?", choices=[
   "(ln(x))^2/2 + C",
   "ln(x)^2 + C",
   "1/(2x^2) + C",
   "ln|ln(x)| + C"], ans=0,
   why="With u = ln(x), du = dx/x, so the integral is u du = u^2/2."),
 dict(q="What is int x/(x^2 + 4) dx?", choices=[
   "(1/2) ln(x^2 + 4) + C",
   "ln(x^2 + 4) + C",
   "arctan(x/2)/2 + C",
   "x^2/(2 ln(x^2 + 4)) + C"], ans=0,
   why="With u = x^2 + 4, x dx = du/2, giving (1/2)ln|u|, and u is always positive here."),
 dict(q="What is int sec^2(5x) dx?", choices=[
   "tan(5x)/5 + C",
   "5 tan(5x) + C",
   "tan(5x) + C",
   "sec^3(5x)/15 + C"], ans=0,
   why="With u = 5x, dx = du/5, so the antiderivative is tan(u)/5."),
 dict(q="What is the value of int from 0 to pi of sin(2x) dx?", choices=[
   "0",
   "1",
   "2",
   "1/2"], ans=0,
   why="An antiderivative is -cos(2x)/2, and cos(2pi) = cos(0), so the two halves of the interval cancel exactly."),
 dict(q="What is int x sqrt(x - 1) dx?", choices=[
   "(2/5)(x - 1)^(5/2) + (2/3)(x - 1)^(3/2) + C",
   "(2/3) x (x - 1)^(3/2) + C",
   "(2/5)(x - 1)^(5/2) + C",
   "(2/3)(x - 1)^(3/2) + (2/5)(x - 1)^(5/2) x + C"], ans=0,
   why="With u = x - 1 the leftover x becomes u + 1, so the integrand is (u + 1)sqrt(u) = u^(3/2) + u^(1/2)."),
 dict(q="What is the value of int from 1 to 5 of x sqrt(x - 1) dx?", choices=[
   "272/15",
   "64/5",
   "16/3",
   "128/15"], ans=0,
   why="With u = x - 1 the limits become 0 and 4, and (2/5)(32) + (2/3)(8) = 64/5 + 16/3 = 272/15."),
 dict(q="What is the value of int from 0 to 1 of x/(x^2 + 1)^2 dx?", choices=[
   "1/4",
   "1/2",
   "1/8",
   "ln(2)/2"], ans=0,
   why="With u = x^2 + 1 the integral is (1/2) u^(-2) du from 1 to 2, which is -1/(2u) evaluated there: -1/4 + 1/2 = 1/4."),
 dict(q="What is int e^(sin(x)) cos(x) dx?", choices=[
   "e^(sin(x)) + C",
   "e^(sin(x)) sin(x) + C",
   "e^(cos(x)) + C",
   "e^(sin(x))/cos(x) + C"], ans=0,
   why="With u = sin(x), du = cos(x) dx, so the integral is e^u du = e^u."),
 dict(q="What is the value of int from 0 to ln(3) of e^x/(1 + e^x) dx?", choices=[
   "ln(2)",
   "ln(3)",
   "ln(4)",
   "1/2"], ans=0,
   why="With u = 1 + e^x the limits become 2 and 4, giving ln(4) - ln(2) = ln(2)."),
 dict(q="For int 3x^2 cos(x^3) dx with the substitution u = x^3, which integral in u is correct?", choices=[
   "int cos(u) du",
   "int 3x^2 cos(u) du",
   "int (1/3) cos(u) du",
   "int u^2 cos(u) du"], ans=0,
   why="Since du = 3x^2 dx, the whole factor 3x^2 dx is replaced by du and no x may remain."),
]
