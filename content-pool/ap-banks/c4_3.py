# CALC 4.3 Rates of Change in Applied Contexts Other Than Motion — 25 questions
# Every derivative and numeric value below is recomputed in verify_c4_3.py with sympy.
# The purely interpretive items (units, "increasing at a decreasing rate") carry no
# computation; their reasoning is the units rule and the sign of the second derivative.
TOPIC = ("4.3", "Rates of Change in Applied Contexts Other Than Motion", 4)
QUESTIONS = [
 dict(q="A town's population t years from now is modeled by P(t) = 500e^(0.04t). The rate at which the population is growing at t = 10 is",
   choices=[
     "20e^(0.4), or about 29.8 people per year",
     "500e^(0.4), or about 745.9 people per year",
     "20e^(0.04), or about 20.8 people per year",
     "0.04e^(0.4), or about 0.06 people per year"], ans=0,
   why="P'(t) = 500(0.04)e^(0.04t) = 20e^(0.04t), so P'(10) = 20e^(0.4); forgetting the chain rule's factor of 0.04 gives 500e^(0.4)."),

 dict(q="For the population model P(t) = 500e^(0.04t), where P is in people and t in years, the units of P'(t) are",
   choices=[
     "people per year",
     "people",
     "years per person",
     "people per year per year"], ans=0,
   why="A derivative carries the output units over the input units, so people per year."),

 dict(q="For P(t) = 500e^(0.04t), the average rate of change of the population over the first 10 years is",
   choices=[
     "50(e^(0.4) - 1), or about 24.6 people per year",
     "20e^(0.4), or about 29.8 people per year",
     "500(e^(0.4) - 1), or about 245.9 people per year",
     "50e^(0.4), or about 74.6 people per year"], ans=0,
   why="Average rate of change is (P(10) - P(0))/10 = (500e^(0.4) - 500)/10 = 50(e^(0.4) - 1), which is not the same as the instantaneous rate."),

 dict(q="The volume of water in a tank, in gallons, after t minutes is V(t) = 100 - 5t + 0.05t^2. At t = 10 minutes the water is",
   choices=[
     "decreasing at 4 gallons per minute",
     "decreasing at 5 gallons per minute",
     "increasing at 4 gallons per minute",
     "decreasing at 55 gallons per minute"], ans=0,
   why="V'(t) = -5 + 0.1t gives V'(10) = -4, so the volume falls at 4 gallons per minute."),

 dict(q="For the tank with V(t) = 100 - 5t + 0.05t^2 gallons, the volume is momentarily neither increasing nor decreasing at",
   choices=[
     "t = 50 minutes",
     "t = 5 minutes",
     "t = 10 minutes",
     "t = 100 minutes"], ans=0,
   why="Setting V'(t) = -5 + 0.1t equal to zero gives t = 50 minutes."),

 dict(q="An object cools so that its temperature in degrees Fahrenheit after t minutes is T(t) = 70 + 30e^(-0.1t). The rate of change of the temperature at t = 0 is",
   choices=[
     "-3 degrees Fahrenheit per minute",
     "-30 degrees Fahrenheit per minute",
     "-0.1 degrees Fahrenheit per minute",
     "100 degrees Fahrenheit per minute"], ans=0,
   why="T'(t) = -3e^(-0.1t), so T'(0) = -3 degrees per minute; 100 is the initial temperature T(0), not a rate."),

 dict(q="For the cooling object with T(t) = 70 + 30e^(-0.1t) degrees Fahrenheit, which statement about t = 10 minutes is correct?",
   choices=[
     "The object is cooling at about 1.10 degrees Fahrenheit per minute.",
     "The object is warming at about 1.10 degrees Fahrenheit per minute.",
     "The object is cooling at about 3 degrees Fahrenheit per minute.",
     "The temperature has stopped changing."], ans=0,
   why="T'(10) = -3e^(-1) is about -1.10, a negative rate, so the object is still cooling but more slowly than at t = 0."),

 dict(q="The volume of a sphere of radius r centimeters is V = (4/3)pi*r^3. The rate of change of the volume with respect to the radius when r = 2 centimeters is",
   choices=[
     "16pi cubic centimeters per centimeter",
     "32pi/3 cubic centimeters per centimeter",
     "8pi cubic centimeters per centimeter",
     "4pi cubic centimeters per centimeter"], ans=0,
   why="dV/dr = 4pi*r^2, which is 16pi at r = 2; 32pi/3 is the volume V(2) rather than its rate of change."),

 dict(q="A circular oil slick has area A = pi*r^2, with r in meters. The rate of change of area with respect to radius when r = 5 meters is",
   choices=[
     "10pi square meters per meter",
     "25pi square meters per meter",
     "5pi square meters per meter",
     "10pi meters per square meter"], ans=0,
   why="dA/dr = 2pi*r = 10pi at r = 5; 25pi is the area itself, not its rate of change."),

 dict(q="A firm's revenue in dollars from selling x units is R(x) = 60x - 0.5x^2. Its marginal revenue at x = 20 is",
   choices=[
     "40 dollars per unit",
     "60 dollars per unit",
     "1000 dollars per unit",
     "50 dollars per unit"], ans=0,
   why="R'(x) = 60 - x, so R'(20) = 40 dollars per unit; 1000 is R(20), the total revenue."),

 dict(q="The cost in dollars of producing x items is C(x) = 1000 + 8x + 0.01x^2. The marginal cost at x = 300 is",
   choices=[
     "14 dollars per item",
     "8 dollars per item",
     "4300 dollars per item",
     "11 dollars per item"], ans=0,
   why="C'(x) = 8 + 0.02x, so C'(300) = 8 + 6 = 14 dollars per item; 4300 is total cost and 11 is the average cost per item."),

 dict(q="A firm has revenue R(x) = 60x - 0.5x^2 dollars and cost C(x) = 1000 + 8x + 0.01x^2 dollars for x items. Its marginal profit at x = 20 is",
   choices=[
     "31.6 dollars per item",
     "52 dollars per item",
     "20.4 dollars per item",
     "-8.4 dollars per item"], ans=0,
   why="Profit is R - C, so the marginal profit is R'(x) - C'(x) = (60 - x) - (8 + 0.02x) = 52 - 1.02x, which is 31.6 at x = 20."),

 dict(q="A bacterial culture has N(t) = 200*2^(t/3) cells after t hours. The rate of growth at t = 0 is",
   choices=[
     "(200 ln 2)/3, or about 46.2 cells per hour",
     "200/3, or about 66.7 cells per hour",
     "200 ln 2, or about 138.6 cells per hour",
     "600 ln 2, or about 415.9 cells per hour"], ans=0,
   why="N'(t) = 200*2^(t/3)*(ln 2)/3, so N'(0) = (200 ln 2)/3; omitting the factor ln 2 or the inner derivative 1/3 gives the other choices."),

 dict(q="A radioactive sample has mass A(t) = 80e^(-0.03t) grams after t years. The rate at which the mass is changing at t = 20 years is about",
   choices=[
     "-1.32 grams per year",
     "-2.40 grams per year",
     "-43.9 grams per year",
     "1.32 grams per year"], ans=0,
   why="A'(t) = -2.4e^(-0.03t), so A'(20) = -2.4e^(-0.6), which is about -1.32 grams per year."),

 dict(q="The concentration of a drug in the bloodstream, in milligrams per liter, t hours after a dose is C(t) = 5t/(t^2 + 1). The value of C'(2) is",
   choices=[
     "-0.6",
     "0.6",
     "-1.2",
     "1.25"], ans=0,
   why="The quotient rule gives C'(t) = 5(1 - t^2)/(t^2 + 1)^2, so C'(2) = 5(-3)/25 = -0.6."),

 dict(q="For the drug concentration C(t) = 5t/(t^2 + 1) milligrams per liter, the meaning of C'(2) is that at t = 2 hours the concentration is",
   choices=[
     "decreasing at about 0.6 milligram per liter per hour",
     "decreasing by a total of 0.6 milligram per liter",
     "increasing at about 0.6 milligram per liter per hour",
     "equal to 0.6 milligram per liter"], ans=0,
   why="A negative derivative is an instantaneous rate of decrease, measured in milligrams per liter per hour."),

 dict(q="A tree's height in feet after t years is h(t) = 20 - 18e^(-0.25t). The tree is growing at t = 4 years at a rate of about",
   choices=[
     "1.66 feet per year",
     "4.50 feet per year",
     "13.38 feet per year",
     "0.41 foot per year"], ans=0,
   why="h'(t) = 4.5e^(-0.25t), so h'(4) = 4.5e^(-1), about 1.66 feet per year; 13.38 is the height h(4)."),

 dict(q="A quantity Q(t) is increasing at a decreasing rate. Which pair of conditions describes this?",
   choices=[
     "Q'(t) > 0 and Q''(t) < 0",
     "Q'(t) > 0 and Q''(t) > 0",
     "Q'(t) < 0 and Q''(t) < 0",
     "Q'(t) < 0 and Q''(t) > 0"], ans=0,
   why="The quantity itself grows, so Q' > 0, while the growth rate shrinks, so Q' is decreasing and Q'' < 0."),

 dict(q="Health officials report that the number of infected people is still rising, but that the outbreak is slowing. If I(t) is the number infected, this says",
   choices=[
     "I'(t) > 0 and I''(t) < 0",
     "I'(t) < 0 and I''(t) < 0",
     "I'(t) > 0 and I''(t) > 0",
     "I(t) < 0 and I'(t) > 0"], ans=0,
   why="Still rising means a positive first derivative, and slowing means that rate is itself falling, a negative second derivative."),

 dict(q="If C(x) is the cost in dollars of producing x kilograms of a chemical, the units of dC/dx are",
   choices=[
     "dollars per kilogram",
     "kilograms per dollar",
     "dollars",
     "dollars per kilogram per kilogram"], ans=0,
   why="Output units over input units gives dollars per kilogram, the marginal cost."),

 dict(q="The number of units a store sells per week at price p dollars is q(p) = 1200 - 3p^2. The rate of change of sales with respect to price at p = 10 dollars is",
   choices=[
     "-60 units per dollar",
     "-30 units per dollar",
     "900 units per dollar",
     "60 units per dollar"], ans=0,
   why="dq/dp = -6p, so at p = 10 it is -60 units per dollar; 900 is q(10), the sales level itself."),

 dict(q="A cube has edge length x centimeters and volume V = x^3 cubic centimeters. The rate of change of the volume with respect to the edge length when x = 4 is",
   choices=[
     "48 cubic centimeters per centimeter",
     "64 cubic centimeters per centimeter",
     "12 cubic centimeters per centimeter",
     "96 cubic centimeters per centimeter"], ans=0,
   why="dV/dx = 3x^2 = 48 at x = 4; 64 is the volume and 96 is the surface area."),

 dict(q="A start-up's monthly revenue in thousands of dollars t months after launch is R(t) = 40t/(t + 4). The rate at which revenue is growing at t = 4 months is",
   choices=[
     "2.5 thousand dollars per month",
     "5 thousand dollars per month",
     "10 thousand dollars per month",
     "20 thousand dollars per month"], ans=0,
   why="The quotient rule gives R'(t) = 160/(t + 4)^2, so R'(4) = 160/64 = 2.5 thousand dollars per month; 20 is R(4), the revenue itself."),

 dict(q="For the revenue model R(t) = 40t/(t + 4) thousand dollars, what happens to R'(t) as t grows without bound?",
   choices=[
     "R'(t) approaches 0, so revenue keeps rising but levels off near 40 thousand dollars",
     "R'(t) approaches 40, so revenue rises ever faster",
     "R'(t) becomes negative, so revenue eventually falls",
     "R'(t) approaches 1, so revenue rises at a steady 1 thousand dollars per month"], ans=0,
   why="R'(t) = 160/(t + 4)^2 tends to 0 while R(t) tends to 40, so the curve flattens toward a horizontal asymptote."),

 dict(q="A fish population is modeled by P(t) = 1000/(1 + 9e^(-0.5t)), where t is in years. At the moment when the population reaches 500 fish, it is growing at a rate of",
   choices=[
     "125 fish per year",
     "250 fish per year",
     "500 fish per year",
     "62.5 fish per year"], ans=0,
   why="P = 500 when 9e^(-0.5t) = 1, and substituting into P'(t) = 4500e^(-0.5t)/(1 + 9e^(-0.5t))^2 gives 500/4 = 125 fish per year, the fastest growth the model ever reaches."),
]
