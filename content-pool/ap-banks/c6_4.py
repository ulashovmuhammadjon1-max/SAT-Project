# CALC 6.4 The Fundamental Theorem of Calculus and Accumulation Functions — 25 questions
# Answers verified with sympy; see verify_c6_4.py, which differentiates each
# accumulation function directly with sp.diff on sp.Integral so the chain-rule
# factor on the upper limit is checked by the computer, not by hand.
# Questions 1, 13, 17, 18, 22, 25 are conceptual (statement of the theorem, its
# hypotheses, and the classic missing-chain-rule error).
TOPIC = ("6.4", "The Fundamental Theorem of Calculus and Accumulation Functions", 6)
QUESTIONS = [
 dict(q="Let f be continuous and let F(x) = int from 1 to x of f(t) dt. What is F'(x)?", choices=[
   "f(x)",
   "f(x) - f(1)",
   "f'(x)",
   "F(x) - F(1)"], ans=0,
   why="The Fundamental Theorem of Calculus says that differentiating an accumulation function returns the integrand evaluated at the upper limit."),
 dict(q="If F(x) = int from 0 to x of (t^2 + 1) dt, what is F'(x)?", choices=[
   "x^2 + 1",
   "2x",
   "x^3/3 + x",
   "(x^2 + 1)/3"], ans=0,
   why="F'(x) is the integrand with t replaced by the upper limit x, so F'(x) = x^2 + 1."),
 dict(q="If F(x) = int from 2 to x of sqrt(t^3 + 1) dt, what is F'(3)?", choices=[
   "3",
   "sqrt(28)",
   "sqrt(28) - 3",
   "28"], ans=1,
   why="F'(x) = sqrt(x^3 + 1), so F'(3) = sqrt(27 + 1) = sqrt(28)."),
 dict(q="What is d/dx of int from 0 to x^2 of sin(t) dt?", choices=[
   "sin(x^2)",
   "2x sin(x^2)",
   "2x cos(x^2)",
   "cos(x^2) - 1"], ans=1,
   why="The upper limit is a function of x, so the chain rule contributes its derivative: sin(x^2) times 2x."),
 dict(q="What is d/dx of int from 1 to x^3 of ln(t) dt?", choices=[
   "ln(x^3)",
   "3x^2 ln(x^3)",
   "3x^2/x^3",
   "x^3 ln(x^3) - x^3"], ans=1,
   why="By the chain rule the derivative is ln(x^3) times the derivative of the upper limit, which is 3x^2."),
 dict(q="What is d/dx of int from x to 5 of e^(t^2) dt?", choices=[
   "e^(x^2)",
   "-e^(x^2)",
   "-2x e^(x^2)",
   "e^25 - e^(x^2)"], ans=1,
   why="The variable is the lower limit, so reversing the limits introduces a factor of -1: the derivative is -e^(x^2)."),
 dict(q="If G(x) = int from 0 to x of 1/(1 + t^2) dt, what is G'(x)?", choices=[
   "1/(1 + x^2)",
   "arctan(x)",
   "-2x/(1 + x^2)^2",
   "2x/(1 + x^2)"], ans=0,
   why="The derivative of an accumulation function is the integrand at the upper limit; differentiating the integrand itself is a different, incorrect operation."),
 dict(q="Let F(x) = int from 3 to x of f(t) dt, where f is continuous. What is F(3)?", choices=[
   "0",
   "3",
   "f(3)",
   "It cannot be determined without knowing f."], ans=0,
   why="An integral whose two limits are equal has value 0, no matter what the integrand is."),
 dict(q="What is d/dx of int from 2x to 5 of cos(t) dt?", choices=[
   "-2 cos(2x)",
   "2 cos(2x)",
   "-cos(2x)",
   "-2 sin(2x)"], ans=0,
   why="With the variable in the lower limit the sign flips, and the chain rule contributes the factor 2: the derivative is -2cos(2x)."),
 dict(q="For x > 0, what is d/dx of int from x^2 to x^3 of (1/t) dt?", choices=[
   "1/x",
   "3/x",
   "5/x",
   "ln(x^3) - ln(x^2)"], ans=0,
   why="The derivative is (1/x^3)(3x^2) - (1/x^2)(2x) = 3/x - 2/x = 1/x."),
 dict(q="Let g(x) = int from 0 to x of f(t) dt, where f is continuous and f(2) = 5. What is g'(2)?", choices=[
   "0",
   "2",
   "5",
   "10"], ans=2,
   why="g'(x) = f(x) by the Fundamental Theorem, so g'(2) = f(2) = 5."),
 dict(q="If F(x) = int from 0 to x of (t^2 - 4) dt, what is F''(x)?", choices=[
   "2",
   "2x",
   "x^2 - 4",
   "x^3/3 - 4x"], ans=1,
   why="F'(x) = x^2 - 4, so differentiating once more gives F''(x) = 2x."),
 dict(q="A student computes d/dx of int from 0 to x^2 of cos(t) dt and writes cos(x^2). What is the error?", choices=[
   "The student omitted the factor 2x from the chain rule.",
   "The student should have written sin(x^2).",
   "The student should have subtracted cos(0).",
   "There is no error."], ans=0,
   why="The upper limit x^2 is a function of x, so the derivative is cos(x^2) times the derivative of x^2, which is 2x."),
 dict(q="What is d/dx of int from 0 to sin(x) of t^2 dt?", choices=[
   "sin^2(x) cos(x)",
   "sin^2(x)",
   "sin^3(x)/3",
   "2 sin(x) cos(x)"], ans=0,
   why="The integrand at the upper limit is (sin x)^2, multiplied by the derivative of sin x, which is cos x."),
 dict(q="Let F(x) = int from 1 to x of 2t dt. What is F(3)?", choices=[
   "6",
   "8",
   "9",
   "10"], ans=1,
   why="F(x) = x^2 - 1, so F(3) = 9 - 1 = 8; the lower limit contributes the -1 that the common answer 9 forgets."),
 dict(q="If H(x) = int from 0 to x of (3t - 1) dt, what is H'(4)?", choices=[
   "3",
   "11",
   "12",
   "20"], ans=1,
   why="H'(x) = 3x - 1, so H'(4) = 11; the value 20 is H(4), the integral itself rather than its derivative."),
 dict(q="The Fundamental Theorem of Calculus guarantees that F(x) = int from a to x of f(t) dt satisfies F'(x) = f(x) provided that", choices=[
   "f is continuous on an interval containing a and x",
   "f is increasing on [a, x]",
   "f is positive on [a, x]",
   "f is differentiable on [a, x]"], ans=0,
   why="Continuity of the integrand is the hypothesis; f need not be positive, monotonic, or differentiable."),
 dict(q="If f is continuous on the real numbers and F(x) = int from 0 to x of f(t) dt, which statement must be true?", choices=[
   "F is differentiable, and therefore continuous, everywhere",
   "F is continuous but need not be differentiable",
   "F is increasing everywhere",
   "F has the same graph as f"], ans=0,
   why="The Fundamental Theorem makes F differentiable with F' = f, and differentiability implies continuity; F increases only where f is positive."),
 dict(q="Let F(x) = int from 1 to x^2 of 1/(1 + t^2) dt. What is F'(1)?", choices=[
   "0",
   "1/2",
   "1",
   "2"], ans=2,
   why="F'(x) = 2x/(1 + x^4), so F'(1) = 2/2 = 1."),
 dict(q="Let F(x) = int from 0 to 2x of sqrt(1 + t^2) dt. What is F'(1)?", choices=[
   "sqrt(5)/2",
   "sqrt(5)",
   "2 sqrt(5)",
   "4 sqrt(5)"], ans=2,
   why="F'(x) = 2 sqrt(1 + 4x^2), so F'(1) = 2 sqrt(5)."),
 dict(q="What is d/dx of int from x to x^2 of e^t dt?", choices=[
   "e^(x^2) - e^x",
   "2x e^(x^2) - e^x",
   "2x e^(x^2) - 1",
   "e^(x^2) - 1"], ans=1,
   why="Both limits vary, so the derivative is e^(x^2) times 2x for the upper limit minus e^x times 1 for the lower limit."),
 dict(q="Let h(x) = int from 4 to x of f(t) dt, where f is continuous and f(t) > 0 for all t. Which statement must be true?", choices=[
   "h is increasing on the real numbers",
   "h is positive on the real numbers",
   "h is concave up on the real numbers",
   "h has a minimum at x = 4"], ans=0,
   why="h'(x) = f(x) > 0 makes h increasing; h itself is negative for x < 4, and concavity depends on f', which is unknown."),
 dict(q="Let F(x) = int from 2 to x of f(t) dt, and suppose int from 2 to 6 of f(t) dt = 9. What is F(6)?", choices=[
   "0",
   "4.5",
   "9",
   "18"], ans=2,
   why="F(6) is by definition the integral of f from 2 to 6, which is given as 9."),
 dict(q="Let G(x) = int from 0 to x^2 of t dt for x > 0. Which of the following is correct?", choices=[
   "G(x) = x^4/2 and G'(x) = 2x^3",
   "G(x) = x^2/2 and G'(x) = x",
   "G(x) = x^4/2 and G'(x) = x^2",
   "G(x) = x^4/4 and G'(x) = x^3"], ans=0,
   why="Evaluating gives G(x) = (x^2)^2/2 = x^4/2, whose derivative 2x^3 agrees with the chain-rule form x^2 times 2x."),
 dict(q="For a continuous f and a constant a, which expression equals d/dx of int from a to x of f(t) dt?", choices=[
   "f(x)",
   "f(x) - f(a)",
   "f(t)",
   "int from a to x of f'(t) dt"], ans=0,
   why="The derivative is the integrand at the upper limit; the answer cannot contain t, which is only a variable of integration, and the constant lower limit contributes nothing."),
]
