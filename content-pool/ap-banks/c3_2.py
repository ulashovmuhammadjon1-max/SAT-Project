# CALC 3.2 Implicit Differentiation — 25 questions
# Every dy/dx is confirmed with sympy's idiff in verify_c3_2.py, which also
# checks that no distractor is equivalent to the key. Each question carries the
# "forgot the dy/dx factor on the y terms" answer as a distractor.
# Questions 12 and 13 are conceptual (when implicit differentiation is called
# for, and the diagnosed missing chain-rule factor).
TOPIC = ("3.2", "Implicit Differentiation", 3)
QUESTIONS = [
 dict(q="If y is a differentiable function of x, then d/dx[y^2] =", choices=[
   "2y dy/dx", "2y", "2 dy/dx", "y^2 dy/dx"], ans=0,
   why="y^2 is a composite function of x, so the chain rule contributes the factor dy/dx."),
 dict(q="If x^2 + y^2 = 25, then dy/dx =", choices=[
   "-x/y", "x/y", "-y/x", "-x"], ans=0,
   why="Differentiating gives 2x + 2y dy/dx = 0, so dy/dx = -x/y."),
 dict(q="The slope of the line tangent to the circle x^2 + y^2 = 25 at the point (3, 4) is", choices=[
   "-4/3", "-3/4", "3/4", "4/3"], ans=1,
   why="dy/dx = -x/y = -3/4 at that point, which is perpendicular to the radius of slope 4/3."),
 dict(q="If xy = 6, then dy/dx =", choices=[
   "-y/x", "y/x", "-x/y", "1/x"], ans=0,
   why="The product rule gives y + x dy/dx = 0, so dy/dx = -y/x."),
 dict(q="If x^2 + xy = 4, then dy/dx =", choices=[
   "-(2x + y)/x", "(2x + y)/x", "-(2x + y)/y", "-2x/x"], ans=0,
   why="Differentiating gives 2x + y + x dy/dx = 0, so dy/dx = -(2x + y)/x."),
 dict(q="If y^3 = x^2, then dy/dx =", choices=[
   "2x/(3y^2)", "2x/(3y)", "3y^2/(2x)", "2x/3"], ans=0,
   why="3y^2 dy/dx = 2x, so dy/dx = 2x/(3y^2); the last choice drops the y factor entirely."),
 dict(q="If sin(y) = x, then dy/dx =", choices=[
   "1/cos(y)", "cos(y)", "1/sin(y)", "-1/sin(y)"], ans=0,
   why="cos(y) dy/dx = 1, so dy/dx = 1/cos(y)."),
 dict(q="If e^y = x for x > 0, then dy/dx =", choices=[
   "1/x", "e^y", "x e^y", "ln(x)"], ans=0,
   why="e^y dy/dx = 1, and since e^y = x this is dy/dx = 1/x, matching y = ln(x)."),
 dict(q="If x^2 y = 1, then dy/dx =", choices=[
   "-2y/x", "2y/x", "-y/(2x)", "-2xy"], ans=0,
   why="The product rule gives 2xy + x^2 dy/dx = 0, so dy/dx = -2y/x."),
 dict(q="If x^3 + y^3 = 6xy, then dy/dx =", choices=[
   "(2y - x^2)/(y^2 - 2x)",
   "(x^2 - 2y)/(y^2 - 2x)",
   "(2y - x^2)/(y^2 + 2x)",
   "x^2/y^2"], ans=0,
   why="3x^2 + 3y^2 dy/dx = 6y + 6x dy/dx, and collecting the dy/dx terms gives (2y - x^2)/(y^2 - 2x)."),
 dict(q="The slope of the line tangent to the ellipse x^2 + 4y^2 = 25 at the point (3, 2) is", choices=[
   "-3/8", "-3/4", "3/8", "8/3"], ans=0,
   why="2x + 8y dy/dx = 0 gives dy/dx = -x/(4y) = -3/8."),
 dict(q="Implicit differentiation is the right tool when", choices=[
   "an equation relates x and y but is not conveniently solved for y",
   "the function is a polynomial",
   "the equation contains no y terms",
   "the derivative is known to be constant"], ans=0,
   why="It finds dy/dx directly from the relation, without needing an explicit formula y = f(x)."),
 dict(q="A student differentiates x^2 + y^2 = 25 and writes 2x + 2y = 0. What is missing?", choices=[
   "The factor dy/dx on the y term, from the chain rule",
   "A minus sign on the y term",
   "The constant 25 should have been differentiated to 25",
   "Nothing; the work is correct"], ans=0,
   why="y is a function of x, so d/dx[y^2] = 2y dy/dx, not 2y."),
 dict(q="An equation of the line tangent to x^2 + y^2 = 25 at the point (3, 4) is", choices=[
   "3x + 4y = 25", "4x + 3y = 25", "3x - 4y = 25", "3x + 4y = 0"], ans=0,
   why="The slope is -3/4, so y - 4 = -(3/4)(x - 3), which rearranges to 3x + 4y = 25."),
 dict(q="If x + y = xy, then dy/dx =", choices=[
   "(y - 1)/(1 - x)",
   "(1 - y)/(1 - x)",
   "(y - 1)/(1 + x)",
   "y/x"], ans=0,
   why="1 + dy/dx = y + x dy/dx, so dy/dx(1 - x) = y - 1."),
 dict(q="If cos(x) + y^2 = 5, then dy/dx =", choices=[
   "sin(x)/(2y)", "-sin(x)/(2y)", "sin(x)/(2y^2)", "-sin(x)/2"], ans=0,
   why="-sin(x) + 2y dy/dx = 0, so dy/dx = sin(x)/(2y); the two minus signs cancel."),
 dict(q="The circle x^2 + y^2 = 25 has a horizontal tangent line at", choices=[
   "(0, 5) and (0, -5)",
   "(5, 0) and (-5, 0)",
   "(3, 4) and (3, -4)",
   "no point"], ans=0,
   why="dy/dx = -x/y is 0 when x = 0, which happens at the top and bottom of the circle."),
 dict(q="The circle x^2 + y^2 = 25 has a vertical tangent line at", choices=[
   "(5, 0) and (-5, 0)",
   "(0, 5) and (0, -5)",
   "(4, 3) and (-4, 3)",
   "no point"], ans=0,
   why="dy/dx = -x/y is undefined when y = 0, which happens at the left and right ends of the circle."),
 dict(q="If ln(y) = x^2 with y > 0, then dy/dx =", choices=[
   "2xy", "2x/y", "2x", "y/(2x)"], ans=0,
   why="(1/y) dy/dx = 2x, so dy/dx = 2xy."),
 dict(q="If x^2 y^3 = 8, then dy/dx =", choices=[
   "-2y/(3x)", "2y/(3x)", "-3y/(2x)", "-2y^3/(3x^2)"], ans=0,
   why="2x y^3 + 3x^2 y^2 dy/dx = 0, and dividing by x y^2 gives dy/dx = -2y/(3x)."),
 dict(q="If x sin(y) = 1, then dy/dx =", choices=[
   "-tan(y)/x", "tan(y)/x", "-sin(y)/x", "-1/(x cos(y))"], ans=0,
   why="sin(y) + x cos(y) dy/dx = 0, so dy/dx = -sin(y)/(x cos(y)) = -tan(y)/x."),
 dict(q="The slope of the line tangent to x^3 + y^3 = 9 at the point (1, 2) is", choices=[
   "-4", "-1/4", "1/4", "4"], ans=1,
   why="3x^2 + 3y^2 dy/dx = 0 gives dy/dx = -x^2/y^2 = -1/4."),
 dict(q="The slope of the line tangent to 4x^2 + 9y^2 = 36 at the point (0, 2) is", choices=[
   "-2/3", "0", "2/3", "4/9"], ans=1,
   why="8x + 18y dy/dx = 0 gives dy/dx = -4x/(9y), which is 0 when x = 0."),
 dict(q="If x^2 - 2xy + y^2 = 4, then at every point where y is not equal to x, dy/dx =", choices=[
   "1", "-1", "0", "x/y"], ans=0,
   why="The relation is (x - y)^2 = 4, so x - y is constant and dy/dx = 1; implicitly, 2x - 2y - 2x dy/dx + 2y dy/dx = 0 gives the same."),
 dict(q="The slope of the line tangent to xy^2 = 12 at the point (3, 2) is", choices=[
   "-2/3", "-1/3", "1/3", "2/3"], ans=1,
   why="y^2 + 2xy dy/dx = 0 gives dy/dx = -y/(2x) = -2/6 = -1/3."),
]
