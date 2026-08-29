# CALC 7.9 Logistic Models with Differential Equations — 25 questions
# BC only. Carrying capacity, the equilibrium solutions, and the fact that the
# fastest growth happens at HALF the carrying capacity. Verified by sympy
# maximization and limits in verify_c7_9.py.
TOPIC = ("7.9", "Logistic Models with Differential Equations", 7)
QUESTIONS = [
 dict(q="A population satisfies dP/dt = 0.5P(1 - P/200). What is the carrying capacity?", choices=[
   "200",
   "100",
   "0.5",
   "400"], ans=0,
   why="The carrying capacity is the nonzero value of P making dP/dt = 0, which is P = 200."),
 dict(q="A population satisfies dP/dt = 0.5P(1 - P/200). At what population is the population growing fastest?", choices=[
   "100",
   "200",
   "50",
   "400"], ans=0,
   why="The growth rate is a downward parabola in P with zeros at 0 and 200, so it peaks halfway between, at half the carrying capacity."),
 dict(q="A population satisfies dP/dt = 0.5P(1 - P/200). What is the maximum value of dP/dt?", choices=[
   "25",
   "50",
   "100",
   "12.5"], ans=0,
   why="The maximum occurs at P = 100 and equals 0.5*100*(1 - 100/200) = 25."),
 dict(q="A population satisfies dP/dt = 0.03P(500 - P). What is the carrying capacity?", choices=[
   "500",
   "250",
   "0.03",
   "15"], ans=0,
   why="Setting the rate to zero gives P = 0 or P = 500, and 500 is the value solutions approach."),
 dict(q="A population satisfies dP/dt = 0.03P(500 - P). At what population is the growth rate greatest?", choices=[
   "250",
   "500",
   "125",
   "0.015"], ans=0,
   why="The rate is a parabola in P with zeros at 0 and 500, so it is largest at the midpoint, half the carrying capacity."),
 dict(q="A population satisfies dP/dt = 0.03P(500 - P). What is the greatest value of dP/dt?", choices=[
   "1875",
   "3750",
   "7500",
   "937.5"], ans=0,
   why="At P = 250 the rate is 0.03*250*250 = 1875."),
 dict(q="For the logistic equation dP/dt = kP(1 - P/K) with k > 0 and P(0) > 0, what is the limit of P as t increases without bound?", choices=[
   "K",
   "0",
   "K/2",
   "infinity"], ans=0,
   why="The rate is positive below K and negative above K, so every positive solution is drawn to the carrying capacity."),
 dict(q="For the logistic equation dP/dt = kP(1 - P/K) with k > 0, what happens to a solution with P(0) > K?", choices=[
   "it decreases toward K",
   "it increases without bound",
   "it decreases toward 0",
   "it stays constant"], ans=0,
   why="Above K the factor (1 - P/K) is negative, so the population falls, and it levels off at K."),
 dict(q="A logistic solution curve has an inflection point at what population?", choices=[
   "P = K/2, half the carrying capacity",
   "P = K, the carrying capacity",
   "P = 0",
   "logistic curves have no inflection point"], ans=0,
   why="The inflection point is where dP/dt is maximized, which is at half the carrying capacity."),
 dict(q="What are the equilibrium solutions of dP/dt = kP(1 - P/K)?", choices=[
   "P = 0 and P = K",
   "P = K only",
   "P = K/2 only",
   "P = 0 and P = K/2"], ans=0,
   why="A product is zero when either factor vanishes, giving P = 0 or 1 - P/K = 0."),
 dict(q="Which formula is the general solution of the logistic equation dP/dt = kP(1 - P/K)?", choices=[
   "P = K/(1 + A*e^(-kt))",
   "P = K*e^(-kt)",
   "P = K/(1 + A*e^(kt))",
   "P = K + A*e^(-kt)"], ans=0,
   why="The logistic solution is a carrying capacity divided by 1 plus a decaying exponential term."),
 dict(q="A population is modeled by P = 800/(1 + 7e^(-0.2t)). What is the carrying capacity?", choices=[
   "800",
   "7",
   "100",
   "5600"], ans=0,
   why="As t grows the exponential term goes to 0 and P approaches 800/1."),
 dict(q="A population is modeled by P = 800/(1 + 7e^(-0.2t)). What is P(0)?", choices=[
   "100",
   "800",
   "114",
   "700"], ans=0,
   why="At t = 0 the denominator is 1 + 7 = 8, and 800/8 = 100."),
 dict(q="A population is modeled by P = 800/(1 + 7e^(-0.2t)). At what time is the population growing fastest, to the nearest hundredth?", choices=[
   "9.73",
   "4.87",
   "3.47",
   "19.46"], ans=0,
   why="Fastest growth occurs at P = 400, which requires 7e^(-0.2t) = 1, so t = ln(7)/0.2."),
 dict(q="Which of the following is a logistic differential equation with carrying capacity 200?", choices=[
   "dP/dt = 2P - 0.01P^2",
   "dP/dt = 2P - 200",
   "dP/dt = 0.01P^2 - 2P",
   "dP/dt = 2P + 0.01P^2"], ans=0,
   why="Factoring gives 2P(1 - P/200), which is logistic with k = 2 and K = 200."),
 dict(q="When a logistic population is very small compared with its carrying capacity, its growth is approximately", choices=[
   "exponential, since the factor (1 - P/K) is close to 1",
   "linear, since dP/dt is nearly constant",
   "zero, since small populations cannot grow",
   "decreasing"], ans=0,
   why="With P much smaller than K, the logistic equation is close to dP/dt = kP."),
 dict(q="For a logistic population with 0 < P(0) < K, on what interval is the graph of P concave up?", choices=[
   "while P is below K/2",
   "while P is above K/2",
   "everywhere",
   "nowhere"], ans=0,
   why="The growth rate is increasing while P climbs toward K/2 and decreasing afterward, so the curve bends upward below half the capacity."),
 dict(q="For dP/dt = kP(1 - P/K) with P(0) = K, what is the solution?", choices=[
   "the constant function P = K",
   "a function increasing toward K",
   "a function decreasing toward K/2",
   "a function increasing without bound"], ans=0,
   why="P = K makes the right side zero, so it is an equilibrium solution, and uniqueness makes it the only solution through that point."),
 dict(q="A population satisfies dy/dt = 0.1y(1 - y/50) with y(0) = 10. What is the long-run population?", choices=[
   "50",
   "25",
   "10",
   "0"], ans=0,
   why="The solution rises from 10 and levels off at the carrying capacity 50."),
 dict(q="A population satisfies dP/dt = 0.4P(1 - P/60). What is dP/dt when P = 30?", choices=[
   "6",
   "12",
   "3",
   "24"], ans=0,
   why="Substituting gives 0.4*30*(1 - 30/60) = 0.4*30*0.5 = 6."),
 dict(q="For dP/dt = kP(1 - P/K), what is the maximum possible value of dP/dt, in terms of k and K?", choices=[
   "kK/4",
   "kK/2",
   "kK",
   "k/K"], ans=0,
   why="At P = K/2 the rate is k*(K/2)*(1/2) = kK/4."),
 dict(q="A student says a logistic population grows fastest when it reaches its carrying capacity. What is wrong?", choices=[
   "at the carrying capacity the growth rate is 0; the fastest growth happens at half the carrying capacity",
   "nothing is wrong",
   "the fastest growth happens when P = 0",
   "the growth rate is constant, so there is no fastest moment"], ans=0,
   why="The rate factors as kP(1 - P/K), which vanishes at P = K and peaks at P = K/2."),
 dict(q="A population is modeled by P = 1200/(1 + 3e^(-0.5t)). At what time is the population growing fastest, to the nearest hundredth?", choices=[
   "2.20",
   "1.10",
   "4.39",
   "0.55"], ans=0,
   why="Fastest growth is at P = 600, which needs 3e^(-0.5t) = 1, so t = ln(3)/0.5, about 2.20."),
 dict(q="A population satisfies dP/dt = 0.02P(1000 - P). What is the greatest possible growth rate?", choices=[
   "5000",
   "10000",
   "2500",
   "20000"], ans=0,
   why="The rate peaks at P = 500 and equals 0.02*500*500 = 5000."),
 dict(q="A logistic population with carrying capacity 1000 currently numbers 900. Which statement is correct?", choices=[
   "it is still increasing, but more slowly than when it numbered 500",
   "it is decreasing toward 500",
   "it is growing faster than it did at 500",
   "it has stopped changing"], ans=0,
   why="Above half the carrying capacity the rate is still positive but is falling off toward zero as P approaches 1000."),
]
