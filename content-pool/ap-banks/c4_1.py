# CALC 4.1 Interpreting the Meaning of the Derivative in Context — 25 questions
# Numeric answers verified with sympy; see verify_c4_1.py.
# Many items in this topic are interpretive (units and meaning) rather than
# computational, so no sympy check is possible for them: for those the units
# rule (units of f' = units of f per unit of x) and the rate-of-change reading
# were checked by hand and are stated in each `why`.
TOPIC = ("4.1", "Interpreting the Meaning of the Derivative in Context", 4)
QUESTIONS = [
 dict(q="The cost, in dollars, of running a factory for t hours is C(t). If C'(5) = 12, the best interpretation is that",
   choices=[
     "at t = 5 hours the cost is increasing at a rate of about 12 dollars per hour",
     "the cost of running the factory for 5 hours is 12 dollars",
     "the cost increased by a total of 12 dollars during the first 5 hours",
     "the average cost per hour over the first 5 hours is 12 dollars"], ans=0,
   why="C'(5) is an instantaneous rate of change, so it reports dollars per hour at the single instant t = 5, not a total or an average."),

 dict(q="A function f gives the volume of water in a tank, in liters, as a function of the time x, in minutes. The units of f'(x) are",
   choices=[
     "liters per minute",
     "liters",
     "minutes per liter",
     "liters per minute per minute"], ans=0,
   why="The units of a derivative are the units of the output divided by the units of the input, so liters divided by minutes."),

 dict(q="The volume of a sphere, in cubic centimeters, is V(r), where r is the radius in centimeters. The units of dV/dr are",
   choices=[
     "cubic centimeters per centimeter",
     "cubic centimeters",
     "centimeters per cubic centimeter",
     "square centimeters per centimeter"], ans=0,
   why="A derivative carries the output units over the input units: cubic centimeters per centimeter."),

 dict(q="A bacteria population P(t) is measured in thousands of bacteria, with t in hours. If P'(3) = -40, then at t = 3 hours the population is",
   choices=[
     "decreasing at a rate of about 40 thousand bacteria per hour",
     "decreasing by a total of 40 thousand bacteria",
     "increasing at a rate of 40 thousand bacteria per hour",
     "equal to -40 thousand bacteria"], ans=0,
   why="A negative derivative means the quantity is decreasing, and the magnitude 40 is a rate in thousands of bacteria per hour."),

 dict(q="The position of a particle, in meters, at time t seconds is s(t). The units of s''(t) are",
   choices=[
     "meters per second per second",
     "meters per second",
     "meters",
     "seconds per meter squared"], ans=0,
   why="Differentiating twice divides by the input units twice, giving meters per second per second."),

 dict(q="Water is in a tank, and W(h) is the number of gallons in the tank after h hours. If W'(2) = 0 and W''(2) < 0, then at h = 2",
   choices=[
     "the amount of water is momentarily neither rising nor falling and is at a local maximum",
     "the tank is empty",
     "water is leaving the tank at a constant rate",
     "the amount of water is at a local minimum"], ans=0,
   why="A zero first derivative with a negative second derivative is the second-derivative test for a local maximum of W."),

 dict(q="If f is differentiable on [2, 6], the average rate of change of f on that interval is given by",
   choices=[
     "(f(6) - f(2))/4",
     "f'(6) - f'(2)",
     "(f'(6) + f'(2))/2",
     "(f(6) - f(2))/(6 + 2)"], ans=0,
   why="The average rate of change is the change in output over the change in input, which is (f(6) - f(2))/(6 - 2)."),

 dict(q="A differentiable function g satisfies g(4) = 10 and g(4.2) = 10.9. The best estimate of g'(4.1) is",
   choices=[
     "4.5",
     "0.9",
     "0.18",
     "10.45"], ans=0,
   why="The difference quotient (10.9 - 10)/(4.2 - 4) = 0.9/0.2 = 4.5 approximates the derivative at the midpoint of the interval."),

 dict(q="C(x) is the cost, in dollars, of producing x bicycles. The statement C'(200) = 45 means that",
   choices=[
     "producing one more bicycle beyond the 200th costs approximately 45 dollars",
     "producing 200 bicycles costs 45 dollars",
     "the average cost per bicycle is 45 dollars",
     "the cost of producing 200 bicycles is increasing by 45 dollars per bicycle produced per bicycle"], ans=0,
   why="The derivative of a cost function is marginal cost, the approximate cost of the next unit."),

 dict(q="The temperature of a room, in degrees Fahrenheit, at time t minutes is T(t). Which statement is the correct reading of T'(20) = -0.8?",
   choices=[
     "At t = 20 minutes the room is cooling at about 0.8 degrees Fahrenheit per minute.",
     "At t = 20 minutes the room is 0.8 degrees Fahrenheit cooler than it was at t = 0.",
     "The room cools 0.8 degrees Fahrenheit in the first 20 minutes.",
     "The temperature at t = 20 minutes is -0.8 degrees Fahrenheit."], ans=0,
   why="A negative instantaneous rate of -0.8 degrees per minute is a cooling rate at that instant, not a total change."),

 dict(q="R(p) is a company's weekly revenue, in dollars, when it charges p dollars per item. If R'(30) < 0, then near p = 30",
   choices=[
     "raising the price slightly would decrease weekly revenue",
     "the company's revenue is negative",
     "raising the price slightly would increase weekly revenue",
     "revenue is at a minimum"], ans=0,
   why="A negative derivative means revenue falls as p increases, so a small price increase lowers revenue."),

 dict(q="Profit, in dollars, from selling x units is P(x). Marginal profit at x = 500 is represented by",
   choices=[
     "P'(500)",
     "P(500)",
     "P(500)/500",
     "P(501) - P(499)"], ans=0,
   why="Marginal profit is the derivative of the profit function evaluated at that production level."),

 dict(q="For a differentiable function f, the number f'(a) is",
   choices=[
     "the slope of the line tangent to the graph of f at the point where x = a",
     "the slope of the secant line through (0, f(0)) and (a, f(a))",
     "the value of f at x = a",
     "the average value of f near x = a"], ans=0,
   why="The derivative at a point is by definition the slope of the tangent line there."),

 dict(q="A baby's weight is W(t) pounds at age t months. Which of the following quantities is measured in pounds per month?",
   choices=[
     "W'(9)",
     "W(9)",
     "W(9) - W(6)",
     "the value of t for which W(t) = 20"], ans=0,
   why="Only the derivative divides pounds by months; W(9) and the difference W(9) - W(6) are both weights in pounds, and the last quantity is a time in months."),

 dict(q="A car's fuel use is modeled by g(x), the number of gallons of gasoline consumed after driving x miles. The units of g'(x) are",
   choices=[
     "gallons per mile",
     "miles per gallon",
     "gallons",
     "miles"], ans=0,
   why="Output units over input units gives gallons per mile; miles per gallon would be the reciprocal rate."),

 dict(q="A balloon's height above the ground is h(t) feet, t minutes after launch. At t = 8 it is known that h'(8) = 0 and h''(8) < 0. At t = 8 the balloon is",
   choices=[
     "momentarily at rest vertically and at its greatest height near that time",
     "on the ground",
     "rising at its fastest rate",
     "momentarily at rest and at its lowest height near that time"], ans=0,
   why="A zero rate of change with concavity turning downward identifies a local maximum height."),

 dict(q="Water flows into a reservoir at a rate r(t), measured in gallons per minute, where t is in minutes. The units of r'(t) are",
   choices=[
     "gallons per minute per minute",
     "gallons per minute",
     "gallons",
     "minutes per gallon"], ans=0,
   why="Differentiating a rate that is already in gallons per minute with respect to minutes divides by minutes again."),

 dict(q="The area of a square, in square inches, is A(s), where s is the side length in inches. Given A(s) = s^2, the value and meaning of A'(4) are",
   choices=[
     "8, meaning the area grows about 8 square inches per inch of side length when s = 4",
     "16, meaning the area is 16 square inches when s = 4",
     "8, meaning the area is 8 square inches per inch on average from s = 0 to s = 4",
     "2, meaning the area grows about 2 square inches per inch when s = 4"], ans=0,
   why="A'(s) = 2s, so A'(4) = 8 square inches per inch, an instantaneous rate rather than an average or a total."),

 dict(q="A car's fuel efficiency E(v) is measured in miles per gallon when the car travels at v miles per hour. The units of E'(v) are",
   choices=[
     "miles per gallon per mile per hour",
     "miles per gallon",
     "miles per hour per gallon",
     "gallons per hour"], ans=0,
   why="The output units are miles per gallon and the input units are miles per hour, so the derivative is miles per gallon per mile per hour."),

 dict(q="A streaming service has N(t) subscribers t months after launch, with N'(t) > 0 and N''(t) < 0 for all t in the first year. During that year the number of subscribers is",
   choices=[
     "increasing, but by less and less each month",
     "decreasing at an increasing rate",
     "increasing at an increasing rate",
     "constant"], ans=0,
   why="A positive first derivative means growth, and a negative second derivative means that growth rate is itself shrinking."),

 dict(q="D(p) is the number of items a store sells per week when the price is p dollars. If D'(12) = -25, then near a price of 12 dollars,",
   choices=[
     "raising the price by one dollar decreases weekly sales by about 25 items",
     "the store sells 25 fewer items than it did last week",
     "raising the price by one dollar increases weekly sales by about 25 items",
     "the store sells -25 items at a price of 12 dollars"], ans=0,
   why="The derivative gives approximately the change in output for a one-unit change in input, and the negative sign makes it a decrease."),

 dict(q="Which of the following is NOT a correct interpretation of f'(7) = 3 for a function f giving mass in kilograms as a function of time in seconds?",
   choices=[
     "Over the first 7 seconds, the mass increased by 3 kilograms.",
     "At t = 7 seconds, the mass is increasing at 3 kilograms per second.",
     "The tangent line to the graph of f at t = 7 has slope 3.",
     "In the next tenth of a second after t = 7, the mass increases by roughly 0.3 kilogram."], ans=0,
   why="A derivative is an instantaneous rate, and it says nothing directly about the total change accumulated over the first 7 seconds."),

 dict(q="A snowplow clears S(t) miles of road in t hours. Which expression represents the average rate at which the plow cleared road between t = 1 and t = 4 hours?",
   choices=[
     "(S(4) - S(1))/3",
     "S'(4) - S'(1)",
     "S'(2.5)",
     "(S(4) + S(1))/2"], ans=0,
   why="Average rate of change is the net change in miles divided by the 3-hour change in time."),

 dict(q="The cost, in dollars, of producing x units is C(x) = 0.02x^2 + 5x + 400. The value of C'(100) and its meaning are",
   choices=[
     "9, the approximate cost in dollars of producing the 101st unit",
     "1100, the total cost in dollars of producing 100 units",
     "11, the average cost in dollars per unit at x = 100",
     "9, the total cost in dollars of the first 100 units"], ans=0,
   why="C'(x) = 0.04x + 5 gives C'(100) = 9 dollars per unit, which is the marginal cost of the next unit."),

 dict(q="A tank is being drained, and V(t) is the volume of liquid remaining, in gallons, after t minutes. If V'(10) = -6 and V''(10) = 2, then at t = 10 minutes the tank is",
   choices=[
     "losing liquid at 6 gallons per minute, but that draining rate is slowing down",
     "losing liquid at 6 gallons per minute, and that draining rate is speeding up",
     "gaining liquid at 6 gallons per minute",
     "empty, since the volume has stopped changing"], ans=0,
   why="V' is negative so the volume falls, and V'' positive means V' is rising toward zero, so the outflow rate is decreasing in magnitude."),
]
