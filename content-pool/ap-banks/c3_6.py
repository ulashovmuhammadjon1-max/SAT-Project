# CALC 3.6 Calculating Higher-Order Derivatives — 25 questions
# Every derivative is confirmed with sp.diff (to the stated order) in
# verify_c3_6.py, which also checks that no distractor is equivalent to the key.
# Questions 1 and 15 are conceptual (the notation, and what f'' measures).
TOPIC = ("3.6", "Calculating Higher-Order Derivatives", 3)
QUESTIONS = [
 dict(q="The second derivative of y with respect to x is written", choices=[
   "d^2y/dx^2", "(dy/dx)^2", "d^2y/d^2x", "dy^2/dx^2"], ans=0,
   why="The 2 sits on the d in the numerator and on the x in the denominator; it is an operator applied twice, not a square."),
 dict(q="If f(x) = x^4, then f''(x) =", choices=[
   "12x^2", "4x^3", "24x", "12x^3"], ans=0,
   why="f'(x) = 4x^3 and f''(x) = 12x^2; 24x is the third derivative."),
 dict(q="If f(x) = x^5, then f'''(x) =", choices=[
   "60x^2", "20x^3", "120x", "60x^3"], ans=0,
   why="Differentiating three times gives 5x^4, then 20x^3, then 60x^2."),
 dict(q="If f(x) = sin(x), then f''(x) =", choices=[
   "-sin(x)", "sin(x)", "cos(x)", "-cos(x)"], ans=0,
   why="f'(x) = cos(x) and f''(x) = -sin(x); the minus sign comes from differentiating cosine."),
 dict(q="If f(x) = cos(x), then f''(x) =", choices=[
   "-cos(x)", "cos(x)", "sin(x)", "-sin(x)"], ans=0,
   why="f'(x) = -sin(x) and f''(x) = -cos(x)."),
 dict(q="If f(x) = e^(2x), then f''(x) =", choices=[
   "4e^(2x)", "2e^(2x)", "e^(2x)", "8e^(2x)"], ans=0,
   why="Each differentiation multiplies by 2, so two of them multiply by 4."),
 dict(q="If f(x) = ln(x), then f''(x) =", choices=[
   "-1/x^2", "1/x^2", "-1/x", "2/x^3"], ans=0,
   why="f'(x) = 1/x = x^(-1), so f''(x) = -x^(-2) = -1/x^2."),
 dict(q="If f(x) = 3x^3 - 2x^2 + x, then f''(2) =", choices=[
   "18", "29", "32", "36"], ans=2,
   why="f'(x) = 9x^2 - 4x + 1 and f''(x) = 18x - 4, so f''(2) = 32; 29 is f'(2)."),
 dict(q="If f(x) = x^3, then the fourth derivative f''''(x) =", choices=[
   "0", "6", "6x", "24"], ans=0,
   why="The third derivative is the constant 6, so the fourth is 0."),
 dict(q="If f(x) = sin(x), then the fourth derivative f''''(x) =", choices=[
   "sin(x)", "-sin(x)", "cos(x)", "-cos(x)"], ans=0,
   why="The derivatives cycle cos, -sin, -cos, sin with period 4, returning to sin(x)."),
 dict(q="If f(x) = sin(x), then the 101st derivative of f is", choices=[
   "cos(x)", "sin(x)", "-sin(x)", "-cos(x)"], ans=0,
   why="The cycle has length 4 and 101 = 4(25) + 1, so the 101st derivative matches the first, cos(x)."),
 dict(q="A particle has position s(t) = t^3 - 6t^2 + 9t. Its acceleration at t = 1 is", choices=[
   "-12", "-6", "0", "6"], ans=1,
   why="v(t) = 3t^2 - 12t + 9 and a(t) = 6t - 12, so a(1) = -6; the value 0 is the velocity at t = 1."),
 dict(q="If f(x) = 1/x, then f''(x) =", choices=[
   "2/x^3", "-2/x^3", "1/x^2", "-1/x^2"], ans=0,
   why="f'(x) = -x^(-2) and f''(x) = 2x^(-3) = 2/x^3; the two minus signs cancel."),
 dict(q="If f(x) = x e^x, then f''(x) =", choices=[
   "(x + 2)e^x", "(x + 1)e^x", "(x + 3)e^x", "x e^x"], ans=0,
   why="f'(x) = (x + 1)e^x, and differentiating again gives (x + 1)e^x + e^x = (x + 2)e^x."),
 dict(q="What does the second derivative f'' measure?", choices=[
   "The rate at which f' is changing, which is what determines concavity",
   "The slope of the graph of f",
   "The area under the graph of f",
   "The average rate of change of f"], ans=0,
   why="f'' is the derivative of f', so it records how fast the slope itself is changing."),
 dict(q="If f(x) = sqrt(x) for x > 0, then f''(x) =", choices=[
   "-1/(4x^(3/2))", "1/(4x^(3/2))", "-1/(2x^(3/2))", "1/(2 sqrt(x))"], ans=0,
   why="f'(x) = (1/2)x^(-1/2), so f''(x) = -(1/4)x^(-3/2)."),
 dict(q="For a constant n, if f(x) = x^n then f''(x) =", choices=[
   "n(n - 1)x^(n-2)", "n x^(n-1)", "n^2 x^(n-2)", "(n - 1)x^(n-2)"], ans=0,
   why="Applying the power rule twice multiplies by n and then by n - 1."),
 dict(q="If f(x) = e^(-3x), then f'''(x) =", choices=[
   "-27e^(-3x)", "27e^(-3x)", "-9e^(-3x)", "-3e^(-3x)"], ans=0,
   why="Each differentiation multiplies by -3, and (-3)^3 = -27."),
 dict(q="If f(x) = tan(x), then f''(x) =", choices=[
   "2 sec^2(x) tan(x)", "sec^2(x)", "2 sec(x) tan(x)", "-2 sec^2(x) tan(x)"], ans=0,
   why="f'(x) = sec^2(x), and the chain rule on (sec x)^2 gives 2 sec(x) times sec(x) tan(x)."),
 dict(q="If f(x) = x^4 - 6x^2, then f''(x) = 0 at", choices=[
   "x = -1 and x = 1", "x = 0 only", "x = 0 and x = 2", "no value of x"], ans=0,
   why="f''(x) = 12x^2 - 12, which is 0 when x^2 = 1."),
 dict(q="If f(x) = (2x + 1)^4, then f''(x) =", choices=[
   "48(2x + 1)^2", "12(2x + 1)^2", "24(2x + 1)^2", "48(2x + 1)^3"], ans=0,
   why="f'(x) = 8(2x + 1)^3, and differentiating again gives 24(2x + 1)^2 times the inner derivative 2."),
 dict(q="For constants k and a positive integer n, the nth derivative of f(x) = e^(kx) is", choices=[
   "k^n e^(kx)", "n k e^(kx)", "k e^(kx)", "e^(kx)"], ans=0,
   why="Each differentiation contributes one factor of k, so n of them contribute k^n."),
 dict(q="If f(x) = x^2 sin(x), then f''(x) =", choices=[
   "(2 - x^2) sin(x) + 4x cos(x)",
   "(2 - x^2) sin(x) - 4x cos(x)",
   "2 sin(x) + 4x cos(x)",
   "-x^2 sin(x)"], ans=0,
   why="f'(x) = 2x sin(x) + x^2 cos(x), and differentiating that product-by-product gives 2 sin(x) + 4x cos(x) - x^2 sin(x)."),
 dict(q="A particle has position s(t) = t^4 - 4t^3. Its acceleration is 0 at", choices=[
   "t = 0 and t = 2", "t = 0 and t = 3", "t = 2 only", "t = 3 only"], ans=0,
   why="a(t) = s''(t) = 12t^2 - 24t = 12t(t - 2), so a(t) = 0 at t = 0 and t = 2; t = 3 is where the velocity vanishes."),
 dict(q="If f(x) = ln(x), then f'''(x) =", choices=[
   "2/x^3", "-2/x^3", "-6/x^4", "1/x^2"], ans=0,
   why="f'(x) = 1/x, f''(x) = -1/x^2, and f'''(x) = 2/x^3; -6/x^4 is the fourth derivative."),
]
