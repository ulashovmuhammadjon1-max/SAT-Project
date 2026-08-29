# CALC 7.1 Modeling Situations with Differential Equations — 25 questions
# Translating verbal descriptions of rates into differential equations.
# Answers verified with sympy where a computation exists; see verify_c7_1.py.
# Many items here are modeling/translation items with no numeric answer to
# compute — for those the verify file checks the keyed string and, where a
# candidate equation can be tested, substitutes the stated solution.
TOPIC = ("7.1", "Modeling Situations with Differential Equations", 7)
QUESTIONS = [
 dict(q="The rate of change of a quantity y with respect to time t is proportional to y. Which differential equation models this situation?", choices=[
   "dy/dt = ky",
   "dy/dt = kt",
   "dy/dt = k/y",
   "y = kt"], ans=0,
   why="'Proportional to y' means the derivative equals a constant times y itself."),
 dict(q="The rate of change of y with respect to t is inversely proportional to y. Which differential equation models this?", choices=[
   "dy/dt = k/y",
   "dy/dt = ky",
   "dy/dt = -ky",
   "dy/dt = y/k"], ans=0,
   why="Inverse proportionality puts y in the denominator: dy/dt = k/y."),
 dict(q="A population P grows at a rate proportional to the square of the population. Which differential equation models this?", choices=[
   "dP/dt = kP^2",
   "dP/dt = (kP)^(1/2)",
   "dP/dt = 2kP",
   "dP/dt = kP"], ans=0,
   why="'Proportional to the square of P' gives dP/dt = kP^2."),
 dict(q="A cup of coffee at temperature T sits in a room held at 68 degrees. Its temperature changes at a rate proportional to the difference between its temperature and the room's temperature. Which differential equation models this?", choices=[
   "dT/dt = k(T - 68)",
   "dT/dt = kT - 68",
   "dT/dt = k(68 - t)",
   "dT/dt = 68 - kT"], ans=0,
   why="Newton's law of cooling makes the rate proportional to the temperature difference T - 68."),
 dict(q="A fish population P in a lake changes at a rate jointly proportional to P and to 4000 - P. Which differential equation models this?", choices=[
   "dP/dt = kP(4000 - P)",
   "dP/dt = kP + k(4000 - P)",
   "dP/dt = k(4000 - P)",
   "dP/dt = 4000kP"], ans=0,
   why="'Jointly proportional' to two quantities means the rate is a constant times their product."),
 dict(q="The rate of change of the amount A of a substance is proportional to the square root of A. Which differential equation models this?", choices=[
   "dA/dt = k*sqrt(A)",
   "dA/dt = sqrt(kA)",
   "dA/dt = k/sqrt(A)",
   "dA/dt = (kA)^2"], ans=0,
   why="Proportional to sqrt(A) means dA/dt = k*sqrt(A)."),
 dict(q="A quantity y satisfies 'y is proportional to t'. Which statement is correct?", choices=[
   "y = kt, so dy/dt = k is constant",
   "dy/dt = kt, so y = kt^2/2",
   "dy/dt = ky",
   "dy/dt = k/t"], ans=0,
   why="Saying the quantity itself is proportional to t is a statement about y, not about dy/dt, and it forces a constant rate."),
 dict(q="The rate of change of y with respect to t is proportional to t. Which differential equation models this?", choices=[
   "dy/dt = kt",
   "dy/dt = ky",
   "dy/dt = k",
   "dy/dt = kty"], ans=0,
   why="Here the rate depends on the independent variable t, not on y."),
 dict(q="At every point (x, y) on a curve, the slope of the tangent line equals twice the product of the coordinates. Which differential equation does the curve satisfy?", choices=[
   "dy/dx = 2xy",
   "dy/dx = 2x + 2y",
   "dy/dx = 2x/y",
   "dy/dx = (2x)(2y)"], ans=0,
   why="The slope is dy/dx, and twice the product of x and y is 2xy."),
 dict(q="At every point (x, y) on a curve the slope of the tangent line equals the sum of the coordinates. Which differential equation does the curve satisfy?", choices=[
   "dy/dx = x + y",
   "dy/dx = xy",
   "dy/dx = x - y",
   "y = x + y"], ans=0,
   why="Slope means dy/dx, and the sum of the coordinates is x + y."),
 dict(q="At every point (x, y) with x not 0 on a curve, the slope of the tangent equals the ratio of y to x. Which differential equation does the curve satisfy?", choices=[
   "dy/dx = y/x",
   "dy/dx = x/y",
   "dy/dx = xy",
   "dy/dx = y - x"], ans=0,
   why="The ratio of y to x is y/x, and the slope is dy/dx."),
 dict(q="Water flows into a tank at a constant 7 gallons per minute and drains out at a constant 3 gallons per minute. If V is the volume of water in gallons, which differential equation models V?", choices=[
   "dV/dt = 4",
   "dV/dt = 7 - 3V",
   "dV/dt = 21",
   "dV/dt = 7V - 3V"], ans=0,
   why="The net rate is the constant 7 - 3 = 4 gallons per minute."),
 dict(q="A tank holds 200 gallons of brine. Brine containing 2 pounds of salt per gallon enters at 5 gallons per minute, and the well-mixed solution leaves at 5 gallons per minute. If S is the pounds of salt in the tank, which differential equation models S?", choices=[
   "dS/dt = 10 - S/40",
   "dS/dt = 10 - 5S",
   "dS/dt = 2 - S/200",
   "dS/dt = 10 - 200S"], ans=0,
   why="Salt enters at 2*5 = 10 lb/min and leaves at (S/200)*5 = S/40 lb/min."),
 dict(q="A drug is infused into a patient at a constant rate of r milligrams per hour and is eliminated at a rate proportional to the amount A present. Which differential equation models A?", choices=[
   "dA/dt = r - kA",
   "dA/dt = rA - k",
   "dA/dt = r - k",
   "dA/dt = kA - r"], ans=0,
   why="The net rate is the constant intake r minus the proportional elimination kA."),
 dict(q="An object falls under gravity with air resistance proportional to its velocity v. Taking down as positive with gravitational acceleration g, which differential equation models v?", choices=[
   "dv/dt = g - kv",
   "dv/dt = g + kv",
   "dv/dt = gv - k",
   "dv/dt = -g - kv"], ans=0,
   why="Gravity contributes the constant g and drag opposes motion, subtracting a term proportional to v."),
 dict(q="A radioactive sample decays at a rate proportional to the amount A remaining. Which differential equation, with k > 0, models the decay?", choices=[
   "dA/dt = -kA",
   "dA/dt = kA",
   "dA/dt = -k",
   "dA/dt = -kt"], ans=0,
   why="Decay means the amount decreases, so the constant of proportionality must be negative: dA/dt = -kA with k > 0."),
 dict(q="A rumor spreads through a town of 12,000 people at a rate proportional to the product of the number y who have heard it and the number who have not. Which differential equation models y?", choices=[
   "dy/dt = ky(12000 - y)",
   "dy/dt = k(12000 - y)",
   "dy/dt = ky - 12000",
   "dy/dt = 12000ky"], ans=0,
   why="The number who have not heard it is 12000 - y, and the rate is proportional to the product."),
 dict(q="The value V of an investment changes at a rate proportional to the difference between V and 500, and V approaches 500 from below over time. Which differential equation is consistent with this description?", choices=[
   "dV/dt = k(500 - V) with k > 0",
   "dV/dt = k(V - 500) with k > 0",
   "dV/dt = kV - 500 with k > 0",
   "dV/dt = k(500 - t) with k > 0"], ans=0,
   why="If V < 500 and V is increasing, the rate must be positive there, which 500 - V provides."),
 dict(q="A spherical raindrop evaporates at a rate proportional to its surface area. Since the surface area of a sphere is proportional to V^(2/3), which differential equation models the volume V?", choices=[
   "dV/dt = -kV^(2/3)",
   "dV/dt = -kV^3",
   "dV/dt = -kV",
   "dV/dt = -kV^(3/2)"], ans=0,
   why="Surface area is proportional to V^(2/3), and evaporation makes dV/dt negative."),
 dict(q="An object moves so that its acceleration is proportional to its displacement y from the origin and is always directed toward the origin. Which differential equation models the motion?", choices=[
   "d^2y/dt^2 = -ky with k > 0",
   "d^2y/dt^2 = ky with k > 0",
   "dy/dt = -ky with k > 0",
   "d^2y/dt^2 = -kt with k > 0"], ans=0,
   why="Acceleration is the second derivative, and 'toward the origin' makes it opposite in sign to y."),
 dict(q="Which situation is modeled by dy/dt = 0.4y(1 - y/800)?", choices=[
   "A population growing logistically toward a maximum sustainable size of 800",
   "A population growing exponentially without bound",
   "A quantity decaying toward zero",
   "A quantity changing at the constant rate 0.4"], ans=0,
   why="The factor (1 - y/800) shrinks the growth rate to zero as y approaches 800, the carrying capacity."),
 dict(q="A quantity y decreases at a rate of 6 units per unit increase in x. Which differential equation models this?", choices=[
   "dy/dx = -6",
   "dy/dx = -6y",
   "dy/dx = 6",
   "dy/dx = -6x"], ans=0,
   why="A constant rate of decrease of 6 per unit of x is exactly dy/dx = -6."),
 dict(q="A cube of side s dissolves so that its volume decreases at a rate proportional to its surface area. Which conclusion about the side length follows?", choices=[
   "ds/dt is a negative constant, so the side length decreases at a constant rate",
   "ds/dt is proportional to s, so the side decreases exponentially",
   "ds/dt is proportional to s^2",
   "ds/dt is proportional to 1/s"], ans=0,
   why="V = s^3 gives dV/dt = 3s^2 ds/dt, and setting that equal to -k(6s^2) cancels s^2 and leaves ds/dt = -2k."),
 dict(q="If y is measured in grams and t in hours, what are the units of k in the model dy/dt = ky?", choices=[
   "per hour",
   "grams per hour",
   "grams",
   "hours per gram"], ans=0,
   why="dy/dt has units of grams per hour and y has units of grams, so k must have units of 1/hour."),
 dict(q="Which of the following statements about the model dy/dt = k(M - y), with k > 0 and M a positive constant, is true?", choices=[
   "The rate of change is largest when y is farthest below M and shrinks to zero as y approaches M",
   "The rate of change is largest when y is close to M",
   "The rate of change is constant for all values of y",
   "The rate of change is largest when y = M/2"], ans=0,
   why="The factor M - y is largest when y is smallest and goes to zero as y approaches M."),
]
