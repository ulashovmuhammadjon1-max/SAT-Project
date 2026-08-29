# CALC 7.8 Exponential Models with Differential Equations — 25 questions
# Growth and decay, half-life, and doubling time. Numeric answers are recomputed
# with sympy in verify_c7_8.py.
TOPIC = ("7.8", "Exponential Models with Differential Equations", 7)
QUESTIONS = [
 dict(q="If dy/dt = ky and y(0) = y0, what is y as a function of t?", choices=[
   "y = y0*e^(kt)",
   "y = y0 + kt",
   "y = y0*e^(t/k)",
   "y = k*e^(y0*t)"], ans=0,
   why="Separating gives ln|y| = kt + C, and evaluating at t = 0 identifies the constant as y0."),
 dict(q="A population of 200 doubles every 5 years. Which function models the population P after t years?", choices=[
   "P = 200*2^(t/5)",
   "P = 200*2^(5t)",
   "P = 200*5^(t/2)",
   "P = 200 + 40t"], ans=0,
   why="Each 5 years of elapsed time must contribute one factor of 2, which the exponent t/5 provides."),
 dict(q="A radioactive substance has a half-life of 10 days. If 80 grams are present now, how much remains after 30 days?", choices=[
   "10 grams",
   "20 grams",
   "8 grams",
   "26.7 grams"], ans=0,
   why="Thirty days is three half-lives, so the amount is 80*(1/2)^3 = 10 grams."),
 dict(q="A substance decays according to dA/dt = kA and has a half-life of 10 years. What is k?", choices=[
   "k = -ln(2)/10",
   "k = ln(2)/10",
   "k = -10*ln(2)",
   "k = -1/10"], ans=0,
   why="Setting (1/2) = e^(10k) gives 10k = -ln(2), so k = -ln(2)/10."),
 dict(q="A quantity grows according to dy/dt = 0.07y. What is its doubling time, to the nearest tenth?", choices=[
   "9.9",
   "14.3",
   "7.0",
   "0.1"], ans=0,
   why="Doubling requires e^(0.07t) = 2, so t = ln(2)/0.07, which is about 9.9."),
 dict(q="An investment is modeled by V = 500e^(0.04t) dollars after t years. What is its doubling time, to the nearest hundredth of a year?", choices=[
   "17.33",
   "25.00",
   "12.50",
   "20.00"], ans=0,
   why="Setting e^(0.04t) = 2 gives t = ln(2)/0.04, which is about 17.33."),
 dict(q="Carbon-14 has a half-life of about 5730 years. What fraction of an original sample remains after 11,460 years?", choices=[
   "1/4",
   "1/2",
   "1/8",
   "0"], ans=0,
   why="11,460 years is exactly two half-lives, and (1/2)^2 = 1/4."),
 dict(q="A bacteria culture triples every 4 hours. How long does it take for the culture to become 9 times its original size?", choices=[
   "8 hours",
   "12 hours",
   "6 hours",
   "36 hours"], ans=0,
   why="Nine is 3 squared, so two tripling periods are needed."),
 dict(q="A quantity satisfies dy/dt = 0.2y with y(0) = 50. What is y(10)?", choices=[
   "50e^2",
   "50e^(0.2)",
   "50e^(20)",
   "100"], ans=0,
   why="The solution is y = 50e^(0.2t), and 0.2*10 = 2."),
 dict(q="A drug in the bloodstream satisfies dA/dt = -0.05A with A(0) = 200 milligrams. What is A(t)?", choices=[
   "A = 200e^(-0.05t)",
   "A = 200e^(0.05t)",
   "A = 200 - 0.05t",
   "A = 200*(0.05)^t"], ans=0,
   why="The exponential decay solution is the initial amount times e^(kt) with k = -0.05."),
 dict(q="Which statement characterizes a quantity satisfying dy/dt = ky with k > 0?", choices=[
   "its relative rate of change, (dy/dt)/y, is the constant k",
   "its rate of change dy/dt is the constant k",
   "it increases by k units per unit time",
   "it increases by k percent of its initial value per unit time"], ans=0,
   why="Dividing the equation by y shows the percentage rate of change, not the absolute rate, is what stays constant."),
 dict(q="A quantity is modeled by y = 100*(0.9)^t. Written as y = 100e^(kt), what is k?", choices=[
   "k = ln(0.9)",
   "k = 0.9",
   "k = -0.1",
   "k = ln(0.1)"], ans=0,
   why="Since 0.9^t = e^(t*ln(0.9)), the continuous rate constant is ln(0.9), a negative number near -0.105."),
 dict(q="A 100-gram sample decays to 25 grams in 8 hours. What is its half-life?", choices=[
   "4 hours",
   "2 hours",
   "8 hours",
   "16 hours"], ans=0,
   why="Going from 100 to 25 is two halvings, and two half-lives fit into 8 hours."),
 dict(q="A quantity satisfies dy/dt = ky with y(0) = 3 and y(2) = 12. What is y(t)?", choices=[
   "y = 3*2^t",
   "y = 3*4^t",
   "y = 3*2^(t/2)",
   "y = 3 + 4.5t"], ans=0,
   why="Quadrupling in 2 units of time means doubling in 1, so y = 3*2^t."),
 dict(q="A quantity is modeled by y = 1000e^(0.05t). To the nearest hundredth, when does y reach 3000?", choices=[
   "21.97",
   "20.00",
   "60.00",
   "13.86"], ans=0,
   why="Setting e^(0.05t) = 3 gives t = ln(3)/0.05, which is about 21.97."),
 dict(q="In the model dy/dt = 0.03y with t in years, the constant 0.03 means that", choices=[
   "the quantity grows at a continuous rate of 3 percent of its current size per year",
   "the quantity grows by 3 units per year",
   "the quantity grows by 3 percent of its initial size per year",
   "the quantity triples every year"], ans=0,
   why="The equation says the rate of change is 3 percent of the current amount, which is a continuous relative rate."),
 dict(q="In the model dy/dt = ky with k < 0 and y(0) > 0, what happens to y as t increases without bound?", choices=[
   "y decreases toward 0 but never reaches it",
   "y decreases and becomes negative",
   "y approaches a negative constant",
   "y decreases to 0 in finite time"], ans=0,
   why="The solution y0*e^(kt) with negative k is always positive and has limit 0."),
 dict(q="A tank loses liquid continuously at a rate equal to 15 percent of the amount present per hour. Which differential equation models the amount A?", choices=[
   "dA/dt = -0.15A",
   "dA/dt = -15A",
   "dA/dt = -0.15",
   "dA/dt = 0.85A"], ans=0,
   why="A continuous loss equal to a fixed percentage of the current amount is exactly a negative constant times A."),
 dict(q="After three half-lives, what fraction of a radioactive sample remains?", choices=[
   "1/8",
   "1/6",
   "1/3",
   "3/8"], ans=0,
   why="Each half-life multiplies the amount by 1/2, and (1/2)^3 = 1/8."),
 dict(q="How does the solution of dT/dt = k(T - 70) differ from a pure exponential model dy/dt = ky?", choices=[
   "it approaches 70 rather than 0, since the exponential term is added to the constant 70",
   "it is not exponential at all",
   "it approaches 0 in both cases",
   "it has no equilibrium value"], ans=0,
   why="Writing T = 70 + C*e^(kt) with k < 0 shows the exponential piece dies out and leaves the ambient value."),
 dict(q="Two samples of the same radioactive material have masses 10 grams and 400 grams. How do their half-lives compare?", choices=[
   "they are the same, because half-life does not depend on the starting amount",
   "the larger sample has the longer half-life",
   "the larger sample has the shorter half-life",
   "the half-life is 40 times as long for the larger sample"], ans=0,
   why="Half-life is determined by k alone, since the initial amount cancels when the ratio is set to 1/2."),
 dict(q="A quantity satisfies dy/dt = -0.2y. What is its half-life, to the nearest hundredth?", choices=[
   "3.47",
   "5.00",
   "0.14",
   "1.39"], ans=0,
   why="Setting e^(-0.2t) = 1/2 gives t = ln(2)/0.2, which is about 3.47."),
 dict(q="A 40-gram sample of a material with a half-life of 6 years is stored. Which function gives the amount A remaining after t years?", choices=[
   "A = 40*(1/2)^(t/6)",
   "A = 40*(1/2)^(6t)",
   "A = 40*(1/6)^(t/2)",
   "A = 40 - (40/6)t"], ans=0,
   why="Each 6 years must contribute one factor of 1/2, so the exponent is t/6."),
 dict(q="A population satisfies dP/dt = kP with P(0) = 1000 and P(3) = 8000. What is P(t)?", choices=[
   "P = 1000*2^t",
   "P = 1000*8^t",
   "P = 1000*2^(t/3)",
   "P = 1000*3^t"], ans=0,
   why="Multiplying by 8 in 3 units of time is one doubling per unit of time."),
 dict(q="A student says that exponential growth means the quantity changes at a constant rate. What is the correct statement?", choices=[
   "the quantity changes at a rate proportional to its current size, so the rate itself grows as the quantity grows",
   "the quantity changes at a constant rate, and the student is correct",
   "the quantity changes at a rate proportional to time",
   "the quantity changes at a rate proportional to the square of its size"], ans=0,
   why="dy/dt = ky says the rate is proportional to y, so the absolute rate increases as y increases."),
]
