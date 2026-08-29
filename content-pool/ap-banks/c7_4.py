# CALC 7.4 Reasoning Using Slope Fields — 25 questions
# Equilibrium solutions, stability, concavity of solution curves, and long-run
# behavior. No figures: every field is given by its equation or described in
# words. Verified with sympy; see verify_c7_4.py.
TOPIC = ("7.4", "Reasoning Using Slope Fields", 7)
QUESTIONS = [
 dict(q="What are the equilibrium solutions of dy/dt = y(y - 3)?", choices=[
   "y = 0 and y = 3",
   "y = 3 only",
   "y = 0 only",
   "there are none"], ans=0,
   why="An equilibrium solution is a constant function making dy/dt = 0, and y(y - 3) = 0 when y = 0 or y = 3."),
 dict(q="For dy/dt = y - 4, what happens to the solution with y(0) = 6 as t increases?", choices=[
   "it increases without bound",
   "it decreases toward 4",
   "it stays constant at 6",
   "it increases toward 4"], ans=0,
   why="At y = 6 the rate y - 4 = 2 is positive, and it only grows larger as y grows, so the solution runs away from 4."),
 dict(q="For dy/dt = 4 - y, what happens to every solution as t increases?", choices=[
   "it approaches 4",
   "it approaches 0",
   "it increases without bound",
   "it approaches 4 only if y(0) < 4"], ans=0,
   why="The rate is positive below 4 and negative above 4, so solutions on either side move toward the equilibrium y = 4."),
 dict(q="For dy/dt = y(2 - y), what is the long-run behavior of the solution with y(0) = 1?", choices=[
   "it increases and approaches 2",
   "it decreases and approaches 0",
   "it increases without bound",
   "it stays constant at 1"], ans=0,
   why="At y = 1 the rate is (1)(1) = 1 > 0, and the rate stays positive for 0 < y < 2 and vanishes at y = 2."),
 dict(q="For dy/dt = y(2 - y), what is the long-run behavior of the solution with y(0) = -1?", choices=[
   "it decreases without bound",
   "it increases toward 0",
   "it increases toward 2",
   "it stays constant at -1"], ans=0,
   why="At y = -1 the rate is (-1)(3) = -3 < 0, and the rate is negative for every y < 0, so the solution falls away."),
 dict(q="Solutions of dy/dx = x - y behave in what way as x increases without bound?", choices=[
   "they approach the line y = x - 1",
   "they approach the line y = x",
   "they approach the x-axis",
   "they approach the horizontal line y = 1"], ans=0,
   why="y = x - 1 is itself a solution, since its derivative 1 equals x - (x - 1), and the general solution is y = x - 1 + C*e^(-x), whose extra term dies out."),
 dict(q="In a slope field, the segments along the horizontal line y = 2 are horizontal, solutions below y = 2 rise toward it, and solutions above y = 2 fall toward it. What does this say about y = 2?", choices=[
   "y = 2 is a stable equilibrium solution",
   "y = 2 is an unstable equilibrium solution",
   "y = 2 is a semi-stable equilibrium solution",
   "y = 2 is not a solution at all"], ans=0,
   why="Nearby solutions on both sides move toward it, which is exactly what stability means."),
 dict(q="For dy/dx = y, describe the solution curve through the point (0, 1).", choices=[
   "increasing and concave up",
   "increasing and concave down",
   "decreasing and concave up",
   "constant"], ans=0,
   why="At (0, 1) the slope is 1 > 0, and d^2y/dx^2 = dy/dx = y is also positive there."),
 dict(q="For dy/dx = x + y, what is the value of d^2y/dx^2 at the point (0, 1) on a solution curve?", choices=[
   "2",
   "0",
   "1",
   "3"], ans=0,
   why="Differentiating gives d^2y/dx^2 = 1 + dy/dx = 1 + x + y, which is 1 + 0 + 1 = 2 at that point."),
 dict(q="Which differential equation has exactly one equilibrium solution, the line y = -3?", choices=[
   "dy/dx = y + 3",
   "dy/dx = y - 3",
   "dy/dx = x + 3",
   "dy/dx = (y + 3)(y - 3)"], ans=0,
   why="y + 3 = 0 exactly when y = -3, and nowhere else."),
 dict(q="For dy/dx = y^2 - 1, describe the solution with y(0) = 0 as x increases.", choices=[
   "it decreases and approaches -1",
   "it increases and approaches 1",
   "it decreases without bound",
   "it stays constant at 0"], ans=0,
   why="At y = 0 the rate is -1 < 0, and the rate stays negative for -1 < y < 1 and vanishes at y = -1."),
 dict(q="For dy/dt = (y - 1)(y - 5), what happens to the solution with y(0) = 3?", choices=[
   "it decreases and approaches 1",
   "it increases and approaches 5",
   "it increases without bound",
   "it decreases without bound"], ans=0,
   why="At y = 3 the rate is (2)(-2) = -4 < 0, and the rate is negative throughout 1 < y < 5, with equilibrium at y = 1."),
 dict(q="For dy/dt = (y - 1)(y - 5), what happens to the solution with y(0) = 6?", choices=[
   "it increases without bound",
   "it decreases and approaches 5",
   "it decreases and approaches 1",
   "it stays constant at 6"], ans=0,
   why="At y = 6 the rate is (5)(1) = 5 > 0, and the rate stays positive for every y > 5."),
 dict(q="For dy/dx = (y - 2)^2, which description of the equilibrium solution y = 2 is correct?", choices=[
   "it is semi-stable: solutions below it rise toward 2 while solutions above it move away",
   "it is stable: solutions on both sides approach 2",
   "it is unstable: solutions on both sides move away from 2",
   "it is not an equilibrium solution"], ans=0,
   why="A square is never negative, so every solution is increasing, which carries lower solutions up toward 2 and upper solutions away."),
 dict(q="A slope field has horizontal segments exactly along the x-axis and along the line y = 4. Which differential equation produced it?", choices=[
   "dy/dx = y(4 - y)",
   "dy/dx = y - 4",
   "dy/dx = x(4 - x)",
   "dy/dx = 4 - y"], ans=0,
   why="The product y(4 - y) vanishes exactly when y = 0 or y = 4, giving two horizontal lines of equilibrium."),
 dict(q="Why can two distinct solution curves of dy/dx = f(y), with f continuous and differentiable, never cross each other?", choices=[
   "a crossing point would give two different solutions through the same point, contradicting uniqueness",
   "solution curves must all be parallel",
   "a crossing point would make dy/dx undefined",
   "solution curves are always straight lines"], ans=0,
   why="Under those hypotheses the initial value problem has exactly one solution through each point, so two curves cannot pass through the same point."),
 dict(q="In a slope field every segment has positive slope. What is true of every solution curve?", choices=[
   "each is increasing on its whole domain",
   "each is concave up",
   "each has a maximum",
   "each approaches a horizontal asymptote"], ans=0,
   why="Positive slope everywhere means dy/dx > 0 at every point of every solution."),
 dict(q="For dy/dx = x + y with y(0) = 1, the tangent line at (0, 1) is used to approximate y(0.5). Is the approximation an overestimate or an underestimate?", choices=[
   "an underestimate, because the solution is concave up near x = 0",
   "an overestimate, because the solution is concave down near x = 0",
   "an underestimate, because the solution is decreasing",
   "exact, because the solution is linear"], ans=0,
   why="d^2y/dx^2 = 1 + x + y is positive near (0, 1), so the curve bends above its tangent line."),
 dict(q="A cooling object satisfies dT/dt = -0.5(T - 70). What is the long-run behavior of T?", choices=[
   "T approaches 70 no matter what T(0) is",
   "T approaches 0",
   "T increases without bound if T(0) > 70",
   "T approaches 70 only if T(0) > 70"], ans=0,
   why="The rate is negative above 70 and positive below it, so every solution is drawn to the equilibrium T = 70."),
 dict(q="How many equilibrium solutions does dy/dx = e^y have?", choices=[
   "none, because e^y is never 0",
   "one, at y = 0",
   "one, at y = 1",
   "infinitely many"], ans=0,
   why="An exponential is strictly positive, so dy/dx is never zero and no constant function solves the equation."),
 dict(q="What are the equilibrium solutions of dP/dt = 0.2P(1 - P/50)?", choices=[
   "P = 0 and P = 50",
   "P = 50 only",
   "P = 0 and P = 0.2",
   "P = 25 only"], ans=0,
   why="Setting the rate to zero gives P = 0 or 1 - P/50 = 0, which is P = 50."),
 dict(q="For dy/dx = x^2 + 1, what is true of the solution curve through the origin?", choices=[
   "it is increasing everywhere, with slope never less than 1",
   "it has a minimum at the origin",
   "it is decreasing for x < 0",
   "it approaches a horizontal asymptote"], ans=0,
   why="x^2 + 1 is at least 1 for every x, so the slope is always positive and never small."),
 dict(q="For x > 0 and y > 0, the solution curves of dy/dx = -y/x are", choices=[
   "hyperbolas of the form xy = C",
   "circles of the form x^2 + y^2 = C",
   "lines of the form y = Cx",
   "parabolas of the form y = Cx^2"], ans=0,
   why="If y = C/x then dy/dx = -C/x^2 = -(C/x)/x = -y/x."),
 dict(q="For y > 0, the solution curves of dy/dx = x/y are", choices=[
   "hyperbolas of the form y^2 - x^2 = C",
   "circles of the form x^2 + y^2 = C",
   "lines of the form y = x + C",
   "parabolas of the form y = x^2 + C"], ans=0,
   why="Implicitly differentiating y^2 - x^2 = C gives 2y*dy/dx - 2x = 0, so dy/dx = x/y."),
 dict(q="A solution of dy/dx = (y - 1)(y + 2) has y(0) = 1. What is the solution?", choices=[
   "the constant function y = 1 for all x",
   "an increasing function approaching 1",
   "a decreasing function approaching -2",
   "a function that increases without bound"], ans=0,
   why="y = 1 makes the right side zero, so it is an equilibrium solution, and uniqueness makes it the only solution through (0, 1)."),
]
