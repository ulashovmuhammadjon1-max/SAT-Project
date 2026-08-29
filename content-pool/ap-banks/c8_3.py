# CALC 8.3 Using Accumulation Functions and Definite Integrals in Applied
# Contexts — 25 questions
# Net change, rate-in minus rate-out, accumulation functions, and units.
# All integrals are computed by sympy; see verify_c8_3.py.
TOPIC = ("8.3", "Using Accumulation Functions and Definite Integrals in Applied Contexts", 8)
QUESTIONS = [
 dict(q="Water flows into a tank at a rate of R(t) gallons per minute. What does int from 0 to 60 of R(t) dt represent?", choices=[
   "the number of gallons that flowed in during the first 60 minutes",
   "the rate of flow at t = 60 minutes",
   "the average flow rate over the first 60 minutes",
   "the number of gallons in the tank at t = 60 minutes"], ans=0,
   why="Integrating a rate in gallons per minute over minutes accumulates gallons, which is the amount added, not the amount present."),
 dict(q="A tank holds 50 gallons at time t = 0, and water enters at r(t) gallons per minute. How many gallons are in the tank at t = 10 minutes?", choices=[
   "50 + int from 0 to 10 of r(t) dt",
   "int from 0 to 10 of r(t) dt",
   "50 * int from 0 to 10 of r(t) dt",
   "50 + r(10)"], ans=0,
   why="The integral gives the amount added, which must be added to the initial amount."),
 dict(q="If R(t) is a differentiable quantity, what does int from a to b of R'(t) dt equal?", choices=[
   "R(b) - R(a)",
   "R(b)",
   "R(b) + R(a)",
   "the average value of R on [a, b]"], ans=0,
   why="This is the Net Change Theorem: integrating a rate of change gives the net change."),
 dict(q="Let F(x) = int from 0 to x of f(t) dt, where f is continuous. What is F'(x)?", choices=[
   "f(x)",
   "f'(x)",
   "f(x) - f(0)",
   "x*f(x)"], ans=0,
   why="This is the Fundamental Theorem of Calculus, Part 1."),
 dict(q="Let F(x) = int from 0 to x of (t^2 - 1) dt. What is F(3)?", choices=[
   "6",
   "8",
   "9",
   "12"], ans=0,
   why="An antiderivative is t^3/3 - t, whose value at 3 is 9 - 3 = 6 and at 0 is 0."),
 dict(q="Let F(x) = int from 0 to x of f(t) dt. On what set is F increasing?", choices=[
   "wherever f(x) > 0",
   "wherever f(x) is increasing",
   "wherever F(x) > 0",
   "wherever f(x) < 0"], ans=0,
   why="F' = f, so F rises exactly where f is positive."),
 dict(q="Let F(x) = int from 0 to x of f(t) dt with f continuous. F has a local maximum at x = c when", choices=[
   "f changes from positive to negative at c",
   "f changes from negative to positive at c",
   "f has a maximum at c",
   "F(c) = 0"], ans=0,
   why="F' = f, so the usual first derivative test applies to the sign change of f."),
 dict(q="Let F(x) = int from 0 to x of f(t) dt. On what set is the graph of F concave up?", choices=[
   "wherever f is increasing",
   "wherever f is positive",
   "wherever F is positive",
   "wherever f is decreasing"], ans=0,
   why="F'' = f', so F is concave up exactly where f is rising."),
 dict(q="Water enters a tank at 5 + t gallons per minute and leaves at 3 gallons per minute. What is the net change in the amount of water during the first 6 minutes?", choices=[
   "30 gallons",
   "48 gallons",
   "18 gallons",
   "12 gallons"], ans=0,
   why="The net rate is 2 + t, and its integral from 0 to 6 is 12 + 18 = 30."),
 dict(q="Water enters a tank at rate I(t) and leaves at rate O(t). The amount in the tank is decreasing exactly when", choices=[
   "O(t) > I(t)",
   "I(t) > O(t)",
   "I(t) = O(t)",
   "the integral of I is less than the integral of O"], ans=0,
   why="The amount changes at the net rate I - O, which is negative when the outflow is larger."),
 dict(q="Water enters a tank at 10 - t gallons per minute and leaves at 2 gallons per minute, for 0 <= t <= 12. At what time is the amount of water in the tank greatest?", choices=[
   "t = 8",
   "t = 10",
   "t = 12",
   "t = 2"], ans=0,
   why="The net rate 8 - t changes from positive to negative at t = 8, so the amount peaks there."),
 dict(q="A bacteria population grows at 100e^(0.1t) bacteria per hour. How many bacteria are added during the first 10 hours, to the nearest whole number?", choices=[
   "272",
   "1000",
   "1718",
   "2718"], ans=2,
   why="The integral is 1000(e - 1), which is about 1718."),
 dict(q="Let F(x) = int from 1 to x of (1/t) dt for x > 0. What is F(e)?", choices=[
   "1",
   "e",
   "e - 1",
   "0"], ans=0,
   why="The accumulation function is ln(x), and ln(e) = 1."),
 dict(q="A tank contains 10 gallons at t = 0 and water enters at 6t gallons per minute. How much water is in the tank at t = 4 minutes?", choices=[
   "58 gallons",
   "48 gallons",
   "34 gallons",
   "24 gallons"], ans=0,
   why="The integral of 6t from 0 to 4 is 48, and adding the initial 10 gives 58."),
 dict(q="What is int from 0 to 4 of (3t^2 - 12) dt?", choices=[
   "-48",
   "16",
   "64",
   "112"], ans=1,
   why="An antiderivative is t^3 - 12t, whose value at 4 is 64 - 48 = 16."),
 dict(q="A reservoir holds R(t) acre-feet of water at time t. What does int from 2 to 5 of R'(t) dt represent?", choices=[
   "the change in the amount of water from time 2 to time 5",
   "the amount of water at time 5",
   "the average amount of water between times 2 and 5",
   "the rate of change of the water at time 5"], ans=0,
   why="Integrating the derivative recovers the net change over the interval, not the amount itself."),
 dict(q="A particle's velocity v(t) is measured in meters per second and t in seconds. The units of int from 0 to 5 of v(t) dt are", choices=[
   "meters",
   "meters per second",
   "seconds",
   "meters per second squared"], ans=0,
   why="Multiplying meters per second by seconds cancels the seconds and leaves meters."),
 dict(q="Let f(t) = t for 0 <= t <= 2 and f(t) = 2 for t > 2, and let F(x) = int from 0 to x of f(t) dt. What is F(4)?", choices=[
   "4",
   "6",
   "8",
   "10"], ans=1,
   why="The first piece contributes 2 and the second contributes 2*2 = 4."),
 dict(q="A city's population changes at a rate of P'(t) people per year. What does int from 0 to 10 of P'(t) dt represent?", choices=[
   "the change in population over the ten years",
   "the population after ten years",
   "the average population over the ten years",
   "the growth rate after ten years"], ans=0,
   why="A definite integral of a rate gives the accumulated change, and the starting population would have to be added to get a total."),
 dict(q="If C'(x) is the marginal cost in dollars per unit at production level x, then int from 100 to 150 of C'(x) dx represents", choices=[
   "the additional cost of increasing production from 100 to 150 units",
   "the total cost of producing 150 units",
   "the average cost per unit between 100 and 150 units",
   "the marginal cost at 150 units"], ans=0,
   why="Integrating the marginal cost gives the change in total cost over that production range."),
 dict(q="Oil flows at R(t) liters per hour and int from 0 to 5 of R(t) dt = 120. What does 120 measure?", choices=[
   "120 liters of oil over the five hours",
   "120 liters per hour",
   "120 hours",
   "an average rate of 120 liters per hour"], ans=0,
   why="The units of the integral are liters per hour times hours, which is liters."),
 dict(q="A pump delivers water at R(t) gallons per minute for 0 <= t <= 20. Which expression gives the average rate of delivery over those 20 minutes?", choices=[
   "(1/20) * int from 0 to 20 of R(t) dt",
   "int from 0 to 20 of R(t) dt",
   "(R(0) + R(20))/2",
   "R(20) - R(0)"], ans=0,
   why="The average value of the rate is its integral divided by the length of the time interval."),
 dict(q="A tank holds 100 gallons at t = 0 and water drains at 4 gallons per minute for 10 minutes. A student computes int from 0 to 10 of 4 dt = 40 and reports that the tank holds 40 gallons at t = 10. What is the correct amount, and what went wrong?", choices=[
   "60 gallons; the integral is the amount drained, which must be subtracted from the initial 100",
   "40 gallons; the student is correct",
   "140 gallons; the integral must be added to the initial 100",
   "4 gallons; the integral was computed incorrectly"], ans=0,
   why="An integral of a rate is a change in amount, so it must be combined with the initial amount rather than reported as the amount present."),
 dict(q="Let F(x) = int from 0 to x of f(t) dt, and suppose f(t) < 0 for all t in [0, 5]. What is true of F on [0, 5]?", choices=[
   "F is decreasing and F(5) < 0",
   "F is increasing and F(5) > 0",
   "F is constant",
   "F is decreasing but F(5) > 0"], ans=0,
   why="F' = f is negative throughout, so F falls from F(0) = 0 to a negative value."),
 dict(q="A snowplow clears snow at S(t) cubic meters per hour while snow falls at F(t) cubic meters per hour. Which integral gives the net change in the snow on the road from t = 1 to t = 4?", choices=[
   "int from 1 to 4 of (F(t) - S(t)) dt",
   "int from 1 to 4 of (S(t) - F(t)) dt",
   "int from 1 to 4 of F(t) dt",
   "int from 1 to 4 of |F(t) - S(t)| dt"], ans=0,
   why="The amount on the road changes at the rate at which snow arrives minus the rate at which it is removed."),
]
