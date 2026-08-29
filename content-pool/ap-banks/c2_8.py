# CALC 2.8 The Product Rule — 25 questions
# Every derivative is confirmed with sp.diff in verify_c2_8.py, which also
# checks that no distractor is equivalent to the key. The table of values is
# read by the verifier from this file.
# Questions 1, 10 and 20 are conceptual (the statement of the rule, the
# f'g' error, and recognizing when the rule is unavoidable).
TOPIC = ("2.8", "The Product Rule", 2)

# Values of two differentiable functions and their derivatives.
TAB = dict(
    headers=["x", "f(x)", "f'(x)", "g(x)", "g'(x)"],
    rows=[["1", "3", "-2", "5", "2"],
          ["2", "3", "-1", "4", "5"],
          ["3", "2", "5", "-1", "4"]],
)

QUESTIONS = [
 dict(q="For differentiable functions f and g, d/dx[f(x) g(x)] =", choices=[
   "f'(x) g(x) + f(x) g'(x)",
   "f'(x) g'(x)",
   "f'(x) g(x) - f(x) g'(x)",
   "(f'(x) g(x) - f(x) g'(x))/(g(x))^2"], ans=0,
   why="Differentiate one factor at a time and add; the last choice is the quotient rule."),
 dict(q="If f(x) = x^2 sin(x), then f'(x) =", choices=[
   "2x sin(x) + x^2 cos(x)",
   "2x cos(x)",
   "2x sin(x) - x^2 cos(x)",
   "x^2 cos(x) + 2x cos(x)"], ans=0,
   why="The product rule gives (2x)(sin x) + (x^2)(cos x); multiplying the two derivatives gives the wrong 2x cos(x)."),
 dict(q="If f(x) = x e^x, then f'(x) =", choices=[
   "e^x + x e^x", "x e^x", "e^x", "e^x - x e^x"], ans=0,
   why="(1)(e^x) + (x)(e^x) = e^x + x e^x; each of the other choices keeps only part of the sum."),
 dict(q="If f(x) = x ln(x), then f'(x) =", choices=[
   "ln(x) + 1", "1/x", "ln(x) + x", "ln(x)/x"], ans=0,
   why="(1)(ln x) + (x)(1/x) = ln(x) + 1."),
 dict(q="If f(x) = (x^2 + 1)(x^3 - 2), then f'(x) =", choices=[
   "5x^4 + 3x^2 - 4x",
   "6x^3",
   "5x^4 - 3x^2 - 4x",
   "5x^4 + 3x^2 + 4x"], ans=0,
   why="(2x)(x^3 - 2) + (x^2 + 1)(3x^2) = 2x^4 - 4x + 3x^4 + 3x^2; the choice 6x^3 is the product of the two derivatives."),
 dict(q="If f(x) = sin(x) cos(x), then f'(x) =", choices=[
   "cos^2(x) - sin^2(x)",
   "-sin(x) cos(x)",
   "cos^2(x) + sin^2(x)",
   "sin^2(x) - cos^2(x)"], ans=0,
   why="(cos x)(cos x) + (sin x)(-sin x) = cos^2(x) - sin^2(x); the sign comes from the derivative of cosine."),
 dict(q="If f(x) = e^x ln(x), then f'(x) =", choices=[
   "e^x ln(x) + e^x/x",
   "e^x/x",
   "e^x ln(x) - e^x/x",
   "e^x/x + ln(x)"], ans=0,
   why="(e^x)(ln x) + (e^x)(1/x); the second choice is the product of the derivatives."),
 dict(q="If f(x) = 3x^2 e^x, then f'(x) =", choices=[
   "6x e^x + 3x^2 e^x",
   "6x e^x",
   "3x^2 e^x",
   "6x e^x - 3x^2 e^x"], ans=0,
   why="(6x)(e^x) + (3x^2)(e^x); both terms are needed and both are positive."),
 dict(q="The table gives values of f, f', g and g'. If h(x) = f(x) g(x), then h'(2) =", table=TAB, choices=[
   "-5", "7", "11", "12"], ans=2,
   why="h'(2) = f'(2)g(2) + f(2)g'(2) = (-1)(4) + (3)(5) = 11; -5 is the product of the derivatives."),
 dict(q="A student claims that d/dx[f(x) g(x)] = f'(x) g'(x). Which single example shows the claim is false?", choices=[
   "f(x) = g(x) = x, where the true derivative of x^2 is 2x but f'(x)g'(x) = 1",
   "f(x) = g(x) = 1, where both sides are 0",
   "f(x) = x and g(x) = 0, where both sides are 0",
   "No example exists, because the claim is true"], ans=0,
   why="With f = g = x the product is x^2, whose derivative 2x is not the constant 1; the other choices happen to agree and prove nothing."),
 dict(q="If f(x) = x^3 cos(x), then f'(x) =", choices=[
   "3x^2 cos(x) - x^3 sin(x)",
   "3x^2 cos(x) + x^3 sin(x)",
   "-3x^2 sin(x)",
   "3x^2 sin(x) - x^3 cos(x)"], ans=0,
   why="(3x^2)(cos x) + (x^3)(-sin x); the minus sign comes from differentiating cosine, not from the product rule."),
 dict(q="If f(x) = sqrt(x) e^x, then f'(x) =", choices=[
   "e^x/(2 sqrt(x)) + sqrt(x) e^x",
   "e^x/(2 sqrt(x))",
   "sqrt(x) e^x",
   "e^x/(2 sqrt(x)) - sqrt(x) e^x"], ans=0,
   why="The derivative of x^(1/2) is 1/(2 sqrt(x)), so the rule gives e^x/(2 sqrt(x)) + sqrt(x) e^x."),
 dict(q="If f(x) = (2x + 1)(x - 3), then f'(x) =", choices=[
   "4x - 5", "2x - 6", "2", "4x - 6"], ans=0,
   why="(2)(x - 3) + (2x + 1)(1) = 4x - 5, the same answer expanding first would give; the choice 2 multiplies the derivatives."),
 dict(q="The table gives values of f and f'. If h(x) = x^2 f(x), then h'(1) =", table=TAB, choices=[
   "-4", "2", "4", "6"], ans=2,
   why="h'(1) = 2(1)f(1) + (1)^2 f'(1) = 6 + (-2) = 4."),
 dict(q="If f(x) = x^2 ln(x), then f'(x) =", choices=[
   "2x ln(x) + x", "2x ln(x)", "2/x", "2x ln(x) + 1"], ans=0,
   why="(2x)(ln x) + (x^2)(1/x) = 2x ln(x) + x."),
 dict(q="If f(x) = x sin(x), then f'(pi) =", choices=[
   "-pi", "-1", "0", "pi"], ans=0,
   why="f'(x) = sin(x) + x cos(x), so f'(pi) = 0 + pi(-1) = -pi."),
 dict(q="If f(x) = (x + 1)(x + 2)(x + 3), then f'(x) =", choices=[
   "3x^2 + 12x + 11",
   "3x^2 + 6x + 11",
   "1",
   "3x^2 + 12x + 6"], ans=0,
   why="Expanding gives x^3 + 6x^2 + 11x + 6, so f'(x) = 3x^2 + 12x + 11; multiplying the three derivatives gives the wrong constant 1."),
 dict(q="If f(x) = e^x sin(x), then f'(x) =", choices=[
   "e^x sin(x) + e^x cos(x)",
   "e^x cos(x)",
   "e^x sin(x) - e^x cos(x)",
   "e^x cos(x) - e^x sin(x)"], ans=0,
   why="(e^x)(sin x) + (e^x)(cos x); both terms carry the same factor e^x."),
 dict(q="Using the table, if h(x) = f(x) g(x), then h'(3) =", table=TAB, choices=[
   "-2", "3", "18", "20"], ans=1,
   why="h'(3) = f'(3)g(3) + f(3)g'(3) = (5)(-1) + (2)(4) = 3; pairing each function with the wrong derivative gives 18."),
 dict(q="For which of the following does finding the derivative genuinely require the product rule, with no way to simplify first?", choices=[
   "y = x^2 sin(x)",
   "y = (2x)(3x)",
   "y = (x + 1)(x + 2)",
   "y = 5x^3"], ans=0,
   why="The other three are polynomials that can be multiplied out and differentiated term by term; x^2 sin(x) cannot be simplified away."),
 dict(q="If f(x) = x^2 e^x, then f'(0) =", choices=[
   "0", "1", "2", "e"], ans=0,
   why="f'(x) = 2x e^x + x^2 e^x, and both terms carry a factor of x, so f'(0) = 0."),
 dict(q="Using the table, if f(x) = x g(x), then f'(2) =", table=TAB, choices=[
   "5", "9", "14", "20"], ans=2,
   why="f'(2) = g(2) + 2 g'(2) = 4 + 2(5) = 14; the choice 5 keeps only g'(2)."),
 dict(q="If f(x) = sin(x) ln(x), then f'(x) =", choices=[
   "cos(x) ln(x) + sin(x)/x",
   "cos(x)/x",
   "cos(x) ln(x) - sin(x)/x",
   "cos(x) ln(x) + sin(x) ln(x)"], ans=0,
   why="(cos x)(ln x) + (sin x)(1/x); the second choice multiplies the two derivatives."),
 dict(q="An equation of the line tangent to y = x e^x at the origin is", choices=[
   "y = x", "y = x + 1", "y = 0", "y = ex"], ans=0,
   why="dy/dx = e^x + x e^x is 1 at x = 0, and the curve passes through (0, 0), so the tangent is y = x."),
 dict(q="The graph of y = x^2 e^x has a horizontal tangent line at", choices=[
   "x = 0 and x = -2", "x = 0 only", "x = -2 only", "no value of x"], ans=0,
   why="dy/dx = e^x(2x + x^2) = x e^x (x + 2), and since e^x is never 0 the zeros are x = 0 and x = -2."),
]
