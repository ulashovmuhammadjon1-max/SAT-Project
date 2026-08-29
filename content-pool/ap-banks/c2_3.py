# CALC 2.3 Estimating Derivatives of a Function at a Point — 25 questions
# Every estimate is recomputed in verify_c2_3.py, which reads the tables from
# this file so the numbers a question is graded against are the numbers a
# student sees.
# Questions 6, 7, 9, 12 and 18 are conceptual (which interval to use, why a
# table cannot give an exact derivative, units, and one-sided versus symmetric
# estimates); their reasoning is stated in the verifier.
TOPIC = ("2.3", "Estimating Derivatives of a Function at a Point", 2)

# A differentiable function sampled at unequal spacing; increasing, concave down.
TAB_A = dict(
    headers=["x", "f(x)"],
    rows=[["1.0", "3.0"], ["1.5", "4.2"], ["2.0", "5.0"], ["2.5", "5.4"], ["3.0", "5.5"]],
)
# Position of a particle, sampled every 2 seconds.
TAB_B = dict(
    headers=["t (seconds)", "s(t) (meters)"],
    rows=[["0", "0"], ["2", "7"], ["4", "16"], ["6", "27"], ["8", "40"]],
)
# Temperature in a greenhouse, sampled every 5 minutes.
TAB_C = dict(
    headers=["t (minutes)", "H(t) (degrees Celsius)"],
    rows=[["0", "65"], ["5", "71"], ["10", "78"], ["15", "84"], ["20", "87"]],
)

QUESTIONS = [
 dict(q="The table gives values of a differentiable function f. Using the values at x = 1.5 and x = 2.5, the best estimate of f'(2) is", table=TAB_A, choices=[
   "0.6", "0.8", "1.2", "1.6"], ans=2,
   why="(f(2.5) - f(1.5))/(2.5 - 1.5) = (5.4 - 4.2)/1.0 = 1.2; dividing by 2 instead of by the change in x gives 0.6."),
 dict(q="Using the values in the table at x = 1.0 and x = 1.5, the best estimate of f'(1.25) is", table=TAB_A, choices=[
   "0.6", "1.2", "2.4", "4.8"], ans=2,
   why="(4.2 - 3.0)/(1.5 - 1.0) = 1.2/0.5 = 2.4; 1.2 is the change in f without dividing by the change in x."),
 dict(q="Using the values in the table at x = 2.5 and x = 3.0, the best estimate of f'(2.75) is", table=TAB_A, choices=[
   "0.05", "0.1", "0.2", "0.5"], ans=2,
   why="(5.5 - 5.4)/(3.0 - 2.5) = 0.1/0.5 = 0.2."),
 dict(q="The table gives the position s(t) of a particle. Using the values at t = 2 and t = 6, the best estimate of s'(4) is", table=TAB_B, choices=[
   "5.5", "5", "4.5", "4"], ans=1,
   why="(27 - 7)/(6 - 2) = 20/4 = 5 meters per second; 5.5 and 4.5 are the one-sided estimates from [4, 6] and [2, 4]."),
 dict(q="Using the values in the table at t = 4 and t = 8, the best estimate of s'(6) is", table=TAB_B, choices=[
   "12", "6.5", "6", "5.5"], ans=2,
   why="(40 - 16)/(8 - 4) = 24/4 = 6 meters per second; 12 forgets to divide by the 4-second change in t."),
 dict(q="A differentiable function f is known only at x = 1.0, 1.5, 2.0, 2.5 and 3.0. Which pair of values gives the most reliable estimate of f'(2)?", table=TAB_A, choices=[
   "the values at x = 1.5 and x = 2.5, the closest points on either side of 2",
   "the values at x = 1.0 and x = 3.0, because a wider interval uses more information",
   "the values at x = 1.0 and x = 1.5, because they come first",
   "the values at x = 2.5 and x = 3.0, because f changes least there"], ans=0,
   why="A difference quotient estimates the derivative best over the narrowest interval that brackets the point."),
 dict(q="As the width of the interval used in a difference quotient estimate of f'(a) shrinks toward 0, the estimate", choices=[
   "generally approaches f'(a), since f'(a) is defined as that limit",
   "generally moves away from f'(a)",
   "stays exactly the same for every width",
   "approaches f(a)"], ans=0,
   why="The derivative is by definition the limit of the difference quotient, so narrower intervals generally give better estimates."),
 dict(q="The table gives the temperature H(t) in a greenhouse. Using the values at t = 5 and t = 15, the best estimate of H'(10) is", table=TAB_C, choices=[
   "1.2", "1.3", "1.4", "2.6"], ans=1,
   why="(84 - 71)/(15 - 5) = 13/10 = 1.3 degrees Celsius per minute; 1.2 and 1.4 are the one-sided estimates and 2.6 divides by 5 instead of 10."),
 dict(q="With H(t) measured in degrees Celsius and t in minutes, the estimate of H'(10) obtained from the table is measured in", table=TAB_C, choices=[
   "degrees Celsius per minute",
   "degrees Celsius",
   "minutes per degree Celsius",
   "degrees Celsius per minute per minute"], ans=0,
   why="A difference quotient carries the units of the output divided by the units of the input."),
 dict(q="Using the values in the table at t = 0 and t = 5, the best estimate of H'(2.5) is", table=TAB_C, choices=[
   "0.6", "1.2", "1.4", "6"], ans=1,
   why="(71 - 65)/(5 - 0) = 6/5 = 1.2 degrees Celsius per minute."),
 dict(q="Using only the values in the table, the best estimate of H'(20) is", table=TAB_C, choices=[
   "0.3", "0.6", "1.2", "3"], ans=1,
   why="Only a backward difference is available at the last data point: (87 - 84)/(20 - 15) = 3/5 = 0.6."),
 dict(q="Why can a table of values give only an estimate of f'(a), never the exact value?", choices=[
   "A table gives finitely many values, while f'(a) depends on the behavior of f at every point near a",
   "Tables always contain rounding errors",
   "The derivative is not defined unless a formula for f is given",
   "A table can give the exact value whenever the spacing is small enough"], ans=0,
   why="A difference quotient over any interval of positive width is an average rate, and nothing in the table says how f behaves between the listed points."),
 dict(q="A function f satisfies f(3) = 8 and f(3.01) = 8.06. The best estimate of f'(3) is", choices=[
   "0.06", "0.6", "6", "60"], ans=2,
   why="(8.06 - 8)/(3.01 - 3) = 0.06/0.01 = 6."),
 dict(q="A function g satisfies g(5) = 12 and g(5.2) = 12.9. The best estimate of g'(5) is", choices=[
   "0.9", "4.5", "9", "45"], ans=1,
   why="(12.9 - 12)/(5.2 - 5) = 0.9/0.2 = 4.5."),
 dict(q="A function f satisfies f(1.99) = 7.02 and f(2.01) = 6.98. The best estimate of f'(2) is", choices=[
   "-2", "-0.04", "0.04", "2"], ans=0,
   why="(6.98 - 7.02)/(2.01 - 1.99) = -0.04/0.02 = -2; the negative sign says f is decreasing near x = 2."),
 dict(q="Suppose f is concave up on [1, 3]. Compared with the true value of f'(2), the estimate (f(2.5) - f(2))/0.5 is", choices=[
   "an overestimate",
   "an underestimate",
   "exactly equal to f'(2)",
   "an overestimate only if f is also increasing"], ans=0,
   why="Concave up means f' is increasing, so the secant slope over [2, 2.5] exceeds the tangent slope at the left endpoint."),
 dict(q="Let g be a function that is concave up on [1, 3]. The backward difference (g(2) - g(1.5))/0.5, used as an estimate of g'(2), is", choices=[
   "an underestimate",
   "an overestimate",
   "exactly equal to g'(2)",
   "an underestimate only if g is also decreasing"], ans=0,
   why="Concave up means g' is increasing, so the secant slope over [1.5, 2] is smaller than the tangent slope at the right endpoint."),
 dict(q="For a smooth function, why is the symmetric estimate (f(a + h) - f(a - h))/(2h) usually more accurate than the one-sided estimate (f(a + h) - f(a))/h?", choices=[
   "The symmetric estimate averages the two one-sided estimates, so their opposite errors largely cancel",
   "The symmetric estimate uses a larger value of h",
   "The one-sided estimate is not a difference quotient",
   "The symmetric estimate is exact for every function"], ans=0,
   why="The forward and backward errors have opposite signs for a function of constant concavity, so averaging them cancels the leading error."),
 dict(q="Using the values in the table, the average rate of change of f on the interval [1.0, 3.0] is", table=TAB_A, choices=[
   "0.625", "1.2", "1.25", "2.5"], ans=2,
   why="(5.5 - 3.0)/(3.0 - 1.0) = 2.5/2 = 1.25; 2.5 is the change in f alone."),
 dict(q="For f(x) = ln(x), the forward difference estimate of f'(1) with h = 0.1 is closest to", choices=[
   "0.100", "0.953", "1.000", "1.054"], ans=1,
   why="(ln(1.1) - ln(1))/0.1 = 0.0953/0.1 = 0.953; the exact value f'(1) = 1 is only the limit, and 1.054 is the backward estimate."),
 dict(q="For f(x) = e^x, the symmetric difference estimate of f'(0) with h = 0.1 is closest to", choices=[
   "0.9516", "1.0000", "1.0017", "1.0517"], ans=2,
   why="(e^0.1 - e^(-0.1))/0.2 = 0.20033/0.2 = 1.0017, very close to the exact value 1 and far better than either one-sided estimate."),
 dict(q="Using the values in the table at t = 6 and t = 8, the best estimate of the particle's velocity at t = 7 is", table=TAB_B, choices=[
   "13", "6.5", "6", "5.5"], ans=1,
   why="(40 - 27)/(8 - 6) = 13/2 = 6.5 meters per second; 13 forgets to divide by the 2-second interval."),
 dict(q="A function f satisfies f(4) = 10.0, f(4.1) = 10.3 and f(4.2) = 10.5. Which conclusion about f' on [4, 4.2] is best supported?", choices=[
   "f' appears to be decreasing, so f appears to be concave down there",
   "f' appears to be increasing, so f appears to be concave up there",
   "f' appears to be constant, so f appears to be linear there",
   "f' appears to be negative there"], ans=0,
   why="The successive difference quotients are 3.0 and 2.0, a decreasing slope, which indicates concave down."),
 dict(q="A function f satisfies f(2) = 5, f(2.1) = 5.32 and f(2.01) = 5.0302. Which is the best estimate of f'(2)?", choices=[
   "0.302", "3.02", "3.20", "5.00"], ans=1,
   why="Both difference quotients are valid estimates, but the one over the narrower interval, (5.0302 - 5)/0.01 = 3.02, is the better one."),
 dict(q="A car's odometer reads s(0) = 0, s(1) = 42 and s(2) = 90 miles, with t in hours. The best estimate of the car's speed at t = 1 is", choices=[
   "42", "45", "48", "90"], ans=1,
   why="The symmetric estimate (90 - 0)/(2 - 0) = 45 miles per hour uses the closest values on both sides; 42 and 48 are the one-sided estimates."),
]
