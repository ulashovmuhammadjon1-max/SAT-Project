# CALC 6.11 Integrating Using Integration by Parts — 25 questions  [BC only]
# Answers verified with sympy; see verify_c6_11.py, which differentiates every
# keyed antiderivative back to the integrand and, for each by-parts question,
# also carries out u*v - int v du symbolically and checks it agrees.
# Questions 1, 12, 24 are conceptual (the formula, the LIATE guideline, and why
# substitution fails on a product of unrelated factors).
TOPIC = ("6.11", "Integrating Using Integration by Parts", 6)
QUESTIONS = [
 dict(q="The integration by parts formula states that int u dv equals", choices=[
   "uv - int v du",
   "uv + int v du",
   "int v du - uv",
   "uv - int u dv"], ans=0,
   why="The formula comes from integrating the product rule, d(uv) = u dv + v du, and solving for int u dv."),
 dict(q="What is int x e^x dx?", choices=[
   "x e^x - e^x + C",
   "x e^x + e^x + C",
   "x^2 e^x/2 + C",
   "e^x + C"], ans=0,
   why="Take u = x and dv = e^x dx, so the result is x e^x - int e^x dx = x e^x - e^x."),
 dict(q="What is int x cos(x) dx?", choices=[
   "x sin(x) + cos(x) + C",
   "x sin(x) - cos(x) + C",
   "-x sin(x) + cos(x) + C",
   "x^2 sin(x)/2 + C"], ans=0,
   why="With u = x and dv = cos(x) dx, the result is x sin(x) - int sin(x) dx = x sin(x) + cos(x)."),
 dict(q="What is int x sin(x) dx?", choices=[
   "-x cos(x) + sin(x) + C",
   "x cos(x) - sin(x) + C",
   "-x cos(x) - sin(x) + C",
   "x sin(x) + cos(x) + C"], ans=0,
   why="With u = x and dv = sin(x) dx, v = -cos(x), giving -x cos(x) + int cos(x) dx."),
 dict(q="What is int ln(x) dx?", choices=[
   "x ln(x) - x + C",
   "x ln(x) + x + C",
   "1/x + C",
   "ln(x)^2/2 + C"], ans=0,
   why="Take u = ln(x) and dv = dx, so the result is x ln(x) - int x (1/x) dx = x ln(x) - x."),
 dict(q="In int x ln(x) dx, which choice of u makes the resulting integral easier?", choices=[
   "u = ln(x), dv = x dx",
   "u = x, dv = ln(x) dx",
   "u = x ln(x), dv = dx",
   "u = 1, dv = x ln(x) dx"], ans=0,
   why="Differentiating ln(x) removes the logarithm, while antidifferentiating ln(x) is the harder problem one is trying to avoid."),
 dict(q="What is int x ln(x) dx?", choices=[
   "x^2 ln(x)/2 - x^2/4 + C",
   "x^2 ln(x)/2 - x^2/2 + C",
   "x^2 ln(x)/2 + x^2/4 + C",
   "x ln(x) - x + C"], ans=0,
   why="With u = ln(x) and v = x^2/2, the leftover integral is int (x/2) dx = x^2/4, which is subtracted."),
 dict(q="What is int x e^(2x) dx?", choices=[
   "x e^(2x)/2 - e^(2x)/4 + C",
   "x e^(2x)/2 - e^(2x)/2 + C",
   "x e^(2x)/2 + e^(2x)/4 + C",
   "x e^(2x) - e^(2x)/2 + C"], ans=0,
   why="With u = x and v = e^(2x)/2, the leftover integral is int e^(2x)/2 dx = e^(2x)/4."),
 dict(q="What is int x^2 e^x dx?", choices=[
   "x^2 e^x - 2x e^x + 2 e^x + C",
   "x^2 e^x - 2x e^x - 2 e^x + C",
   "x^2 e^x + 2x e^x + 2 e^x + C",
   "x^3 e^x/3 + C"], ans=0,
   why="Integration by parts must be applied twice, and the signs alternate: x^2 e^x - 2(x e^x - e^x)."),
 dict(q="What is the value of int from 0 to 1 of x e^x dx?", choices=[
   "1",
   "e - 1",
   "e",
   "2e - 1"], ans=0,
   why="The antiderivative is x e^x - e^x, which is 0 at x = 1 minus (-1) at x = 0, giving 1."),
 dict(q="What is the value of int from 0 to pi of x sin(x) dx?", choices=[
   "pi",
   "2pi",
   "0",
   "pi/2"], ans=0,
   why="The antiderivative is -x cos(x) + sin(x), which is pi at x = pi and 0 at x = 0."),
 dict(q="When integrating a product by parts, the LIATE guideline suggests choosing u to be", choices=[
   "the factor that appears earliest in the list logarithmic, inverse trigonometric, algebraic, trigonometric, exponential",
   "the factor that is easiest to antidifferentiate",
   "always the exponential factor",
   "always the factor containing the highest power of x"], ans=0,
   why="LIATE ranks the factors by how much simpler they become when differentiated, and u is the one that improves the most."),
 dict(q="What is int arctan(x) dx?", choices=[
   "x arctan(x) - (1/2) ln(1 + x^2) + C",
   "x arctan(x) + (1/2) ln(1 + x^2) + C",
   "arctan(x)^2/2 + C",
   "1/(1 + x^2) + C"], ans=0,
   why="With u = arctan(x) and dv = dx, the leftover integral is int x/(1 + x^2) dx = (1/2)ln(1 + x^2)."),
 dict(q="What is int x sec^2(x) dx?", choices=[
   "x tan(x) + ln|cos(x)| + C",
   "x tan(x) - ln|cos(x)| + C",
   "x tan(x) - tan^2(x)/2 + C",
   "x^2 tan(x)/2 + C"], ans=0,
   why="With u = x and v = tan(x), the leftover integral is int tan(x) dx = -ln|cos(x)|, which is subtracted."),
 dict(q="What is int x^2 ln(x) dx?", choices=[
   "x^3 ln(x)/3 - x^3/9 + C",
   "x^3 ln(x)/3 - x^3/3 + C",
   "x^3 ln(x)/3 + x^3/9 + C",
   "x^3/(3 ln(x)) + C"], ans=0,
   why="With u = ln(x) and v = x^3/3, the leftover integral is int x^2/3 dx = x^3/9."),
 dict(q="What is int e^x sin(x) dx?", choices=[
   "e^x (sin(x) - cos(x))/2 + C",
   "e^x (sin(x) + cos(x))/2 + C",
   "e^x sin(x) - e^x cos(x) + C",
   "-e^x cos(x) + C"], ans=0,
   why="Applying parts twice returns the original integral, and solving the resulting equation for it gives half the sum."),
 dict(q="What is the value of int from 1 to e of ln(x) dx?", choices=[
   "1",
   "e - 1",
   "e",
   "e - 2"], ans=0,
   why="The antiderivative x ln(x) - x equals 0 at x = e and -1 at x = 1, so the value is 1."),
 dict(q="For int x^2 e^x dx, which choice of u and dv should be made first?", choices=[
   "u = x^2 and dv = e^x dx",
   "u = e^x and dv = x^2 dx",
   "u = x and dv = x e^x dx",
   "u = x^2 e^x and dv = dx"], ans=0,
   why="Differentiating x^2 lowers its degree, so repeating the process eventually clears the polynomial; differentiating e^x never simplifies anything."),
 dict(q="What is int (x + 1) e^x dx?", choices=[
   "x e^x + C",
   "(x + 1) e^x + C",
   "(x + 2) e^x + C",
   "x^2 e^x/2 + x e^x + C"], ans=0,
   why="By parts the answer is (x + 1)e^x - e^x = x e^x, which can be checked instantly by the product rule."),
 dict(q="What is int x sqrt(x + 1) dx?", choices=[
   "(2/3) x (x + 1)^(3/2) - (4/15)(x + 1)^(5/2) + C",
   "(2/3) x (x + 1)^(3/2) + (4/15)(x + 1)^(5/2) + C",
   "(2/3)(x + 1)^(3/2) + C",
   "x^2 (x + 1)^(3/2)/3 + C"], ans=0,
   why="With u = x and v = (2/3)(x + 1)^(3/2), the leftover integral is (2/3) int (x + 1)^(3/2) dx = (4/15)(x + 1)^(5/2)."),
 dict(q="What is the value of int from 0 to 1 of arctan(x) dx?", choices=[
   "pi/4 - ln(2)/2",
   "pi/4 + ln(2)/2",
   "pi/4",
   "ln(2)/2"], ans=0,
   why="The antiderivative x arctan(x) - (1/2)ln(1 + x^2) equals pi/4 - (1/2)ln 2 at x = 1 and 0 at x = 0."),
 dict(q="What is int x^3 e^(x^2) dx?", choices=[
   "(x^2 - 1) e^(x^2)/2 + C",
   "(x^2 + 1) e^(x^2)/2 + C",
   "x^2 e^(x^2)/2 + C",
   "x^4 e^(x^2)/4 + C"], ans=0,
   why="Substituting w = x^2 turns the integral into (1/2) int w e^w dw, which parts evaluates as (1/2)(w - 1)e^w."),
 dict(q="What is int (ln(x))/x^2 dx?", choices=[
   "-ln(x)/x - 1/x + C",
   "-ln(x)/x + 1/x + C",
   "ln(x)/x + 1/x + C",
   "(ln(x))^2/(2x) + C"], ans=0,
   why="With u = ln(x) and v = -1/x, the result is -ln(x)/x + int (-1/x^2) dx = -ln(x)/x - 1/x."),
 dict(q="Why is substitution not a workable first approach for int x e^x dx?", choices=[
   "No factor of the integrand is the derivative of the inside of another factor, so no substitution simplifies it",
   "The integrand is discontinuous",
   "Substitution never applies to products",
   "The integrand has no antiderivative"], ans=0,
   why="Substitution needs a function together with its own derivative; here the factors x and e^x are unrelated in that way, which is exactly the situation integration by parts is designed for."),
 dict(q="What is int e^x cos(x) dx?", choices=[
   "e^x (sin(x) + cos(x))/2 + C",
   "e^x (sin(x) - cos(x))/2 + C",
   "e^x sin(x) + C",
   "e^x cos(x)/2 + C"], ans=0,
   why="Two applications of parts return the original integral with a minus sign, and solving for it gives half the sum."),
]
