# CALC 3.1 The Chain Rule — 25 questions
# Every derivative is confirmed with sp.diff in verify_c3_1.py, which also
# checks that no distractor is equivalent to the key. Every computational
# question carries the "dropped the inner derivative" answer as a distractor,
# since that is the error this topic exists to catch.
# Questions 1 and 14 are conceptual (the statement of the rule and a diagnosed
# student error). The table of values is read by the verifier from this file.
TOPIC = ("3.1", "The Chain Rule", 3)

TAB = dict(
    headers=["x", "f(x)", "f'(x)", "g(x)", "g'(x)"],
    rows=[["1", "2", "5", "3", "-2"],
          ["2", "3", "3", "3", "4"],
          ["3", "-1", "5", "2", "6"]],
)

QUESTIONS = [
 dict(q="If f and g are differentiable, then d/dx[f(g(x))] =", choices=[
   "f'(g(x)) g'(x)", "f'(g(x))", "f'(x) g'(x)", "f'(g'(x))"], ans=0,
   why="Differentiate the outer function at the inner one, then multiply by the derivative of the inner function."),
 dict(q="If f(x) = (3x + 1)^5, then f'(x) =", choices=[
   "15(3x + 1)^4", "5(3x + 1)^4", "3(3x + 1)^4", "15(3x + 1)^5"], ans=0,
   why="5(3x + 1)^4 times the inner derivative 3 gives 15(3x + 1)^4; the second choice drops that factor of 3."),
 dict(q="If f(x) = sin(3x), then f'(x) =", choices=[
   "3 cos(3x)", "cos(3x)", "3 cos(x)", "-3 cos(3x)"], ans=0,
   why="The outer derivative is cos(3x) and the inner derivative is 3."),
 dict(q="If f(x) = e^(2x), then f'(x) =", choices=[
   "2e^(2x)", "e^(2x)", "2e^x", "e^(2x)/2"], ans=0,
   why="e^(2x) is its own outer derivative, and the inner derivative is 2."),
 dict(q="If f(x) = ln(5x), then f'(x) =", choices=[
   "1/x", "5/x", "1/(5x)", "ln(5)/x"], ans=0,
   why="The chain rule gives (1/(5x))(5) = 1/x, so the 5 cancels; ln(5x) = ln 5 + ln x makes the same point."),
 dict(q="If f(x) = cos(x^2), then f'(x) =", choices=[
   "-2x sin(x^2)", "-sin(x^2)", "2x sin(x^2)", "-2x cos(x^2)"], ans=0,
   why="The outer derivative is -sin(x^2) and the inner derivative is 2x; the second choice drops the 2x."),
 dict(q="If f(x) = (x^2 + 1)^3, then f'(x) =", choices=[
   "6x(x^2 + 1)^2", "3(x^2 + 1)^2", "6(x^2 + 1)^2", "6x(x^2 + 1)^3"], ans=0,
   why="3(x^2 + 1)^2 times the inner derivative 2x gives 6x(x^2 + 1)^2."),
 dict(q="If f(x) = sqrt(4x + 1), then f'(x) =", choices=[
   "2/sqrt(4x + 1)", "1/(2 sqrt(4x + 1))", "4/sqrt(4x + 1)", "2 sqrt(4x + 1)"], ans=0,
   why="The outer derivative is 1/(2 sqrt(4x + 1)) and the inner derivative is 4, and 4/2 = 2."),
 dict(q="If f(x) = e^(x^2), then f'(x) =", choices=[
   "2x e^(x^2)", "e^(x^2)", "2x e^(2x)", "x^2 e^(x^2 - 1)"], ans=0,
   why="The inner derivative 2x multiplies the exponential; the last choice wrongly applies the power rule to an exponent."),
 dict(q="If f(x) = tan(2x), then f'(x) =", choices=[
   "2 sec^2(2x)", "sec^2(2x)", "2 sec^2(x)", "2 tan(2x) sec(2x)"], ans=0,
   why="The outer derivative is sec^2(2x) and the inner derivative is 2."),
 dict(q="If f(x) = ln(x^2 + 1), then f'(x) =", choices=[
   "2x/(x^2 + 1)", "1/(x^2 + 1)", "2x/(x^2 + 1)^2", "1/(2x)"], ans=0,
   why="The derivative of ln(u) is u'/u, and here u' = 2x."),
 dict(q="If f(x) = sin^2(x), then f'(x) =", choices=[
   "2 sin(x) cos(x)", "2 sin(x)", "2 cos(x)", "-2 sin(x) cos(x)"], ans=0,
   why="Treat it as (sin x)^2: the outer derivative is 2 sin(x) and the inner derivative is cos(x)."),
 dict(q="If f(x) = (2x - 5)^(-2), then f'(x) =", choices=[
   "-4(2x - 5)^(-3)", "-2(2x - 5)^(-3)", "4(2x - 5)^(-3)", "-4(2x - 5)^(-1)"], ans=0,
   why="-2(2x - 5)^(-3) times the inner derivative 2 gives -4(2x - 5)^(-3)."),
 dict(q="A student writes d/dx[sin(4x)] = cos(4x). What is missing?", choices=[
   "A factor of 4, the derivative of the inner function 4x",
   "A minus sign, since the derivative of sine is negative",
   "A factor of x, from the inner function",
   "Nothing; the answer is correct"], ans=0,
   why="The chain rule multiplies by the inner derivative, so the answer is 4 cos(4x)."),
 dict(q="The table gives values of f, f', g and g'. If h(x) = f(g(x)), then h'(2) =", table=TAB, choices=[
   "5", "12", "20", "30"], ans=2,
   why="h'(2) = f'(g(2)) g'(2) = f'(3)(4) = (5)(4) = 20; the choice 5 drops the inner derivative and 12 uses f'(2) instead of f'(g(2))."),
 dict(q="Using the same table, if k(x) = g(f(x)), then k'(2) =", table=TAB, choices=[
   "24", "18", "12", "6"], ans=1,
   why="k'(2) = g'(f(2)) f'(2) = g'(3)(3) = (6)(3) = 18; the order of composition matters, so this is not the same as h'(2)."),
 dict(q="If f(x) = e^(sin(x)), then f'(x) =", choices=[
   "cos(x) e^(sin(x))", "e^(sin(x))", "e^(cos(x))", "sin(x) e^(sin(x))"], ans=0,
   why="The exponential is its own outer derivative and the inner derivative is cos(x)."),
 dict(q="If f(x) = sqrt(x^2 + 9), then f'(x) =", choices=[
   "x/sqrt(x^2 + 9)",
   "1/(2 sqrt(x^2 + 9))",
   "2x/sqrt(x^2 + 9)",
   "x/(2 sqrt(x^2 + 9))"], ans=0,
   why="The outer derivative 1/(2 sqrt(x^2 + 9)) times the inner derivative 2x leaves x on top."),
 dict(q="If f(x) = (x^2 + 3)^4, then f'(1) =", choices=[
   "128", "256", "512", "1024"], ans=2,
   why="f'(x) = 8x(x^2 + 3)^3, so f'(1) = 8(64) = 512."),
 dict(q="If f(x) = ln(cos(x)), then f'(x) =", choices=[
   "-tan(x)", "tan(x)", "1/cos(x)", "-1/cos(x)"], ans=0,
   why="The derivative of ln(u) is u'/u, giving -sin(x)/cos(x) = -tan(x)."),
 dict(q="If f(x) = sin^2(3x), then f'(x) =", choices=[
   "6 sin(3x) cos(3x)", "2 sin(3x) cos(3x)", "6 sin(3x)", "2 sin(3x)"], ans=0,
   why="Two chain rules apply: 2 sin(3x) times cos(3x) times the inner derivative 3."),
 dict(q="If f(x) = e^(3x^2 - x), then f'(x) =", choices=[
   "(6x - 1) e^(3x^2 - x)",
   "e^(3x^2 - x)",
   "(6x - 1) e^(6x - 1)",
   "(3x^2 - x) e^(3x^2 - x - 1)"], ans=0,
   why="The inner derivative of 3x^2 - x is 6x - 1, and the exponent itself is unchanged."),
 dict(q="If f(x) = cos^3(2x), then f'(x) =", choices=[
   "-6 cos^2(2x) sin(2x)",
   "3 cos^2(2x)",
   "-3 cos^2(2x) sin(2x)",
   "6 cos^2(2x) sin(2x)"], ans=0,
   why="Three layers: 3 cos^2(2x), times -sin(2x), times the inner derivative 2."),
 dict(q="If h(x) = f(x^3) and f'(8) = 2, then h'(2) =", choices=[
   "2", "6", "12", "24"], ans=3,
   why="h'(x) = f'(x^3)(3x^2), so h'(2) = f'(8)(12) = (2)(12) = 24."),
 dict(q="The slope of the line tangent to y = sqrt(x^2 + 9) at x = 4 is", choices=[
   "3/5", "4/5", "5/4", "4"], ans=1,
   why="dy/dx = x/sqrt(x^2 + 9), which at x = 4 is 4/5."),
]
