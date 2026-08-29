# CALC 6.2 Approximating Areas with Riemann Sums — 25 questions
# Every sum is recomputed in verify_c6_2.py; the tables below are the ones the
# stems refer to, and the verifier reads them from this file so the numbers a
# question is graded against are the numbers a student sees.
# Questions 1, 5, 14, 18, 19, 20, 22, 23, 25 are conceptual (endpoint rules and
# over/under-estimate reasoning); their reasoning is stated in the verifier.
TOPIC = ("6.2", "Approximating Areas with Riemann Sums", 6)

# f is increasing throughout; subinterval widths are unequal.
TAB_A = dict(
    headers=["t (minutes)", "v(t) (gallons per minute)"],
    rows=[["0", "4"], ["2", "6"], ["5", "9"], ["9", "11"], ["12", "14"]],
)
# Equally spaced, width 1; increasing.
TAB_B = dict(
    headers=["x", "f(x)"],
    rows=[["0", "3"], ["1", "5"], ["2", "6"], ["3", "8"],
          ["4", "11"], ["5", "13"], ["6", "16"]],
)
# Decreasing throughout; unequal widths.
TAB_C = dict(
    headers=["t (hours)", "g(t) (liters per hour)"],
    rows=[["0", "20"], ["3", "14"], ["6", "9"], ["10", "5"]],
)
# Equally spaced, width 10.
TAB_D = dict(
    headers=["t (seconds)", "v(t) (feet per second)"],
    rows=[["0", "0"], ["10", "14"], ["20", "22"], ["30", "30"], ["40", "35"]],
)

QUESTIONS = [
 dict(q="In a left Riemann sum approximation of int from a to b of f(x) dx, the height of each rectangle is", choices=[
   "the value of f at the left endpoint of that subinterval",
   "the value of f at the right endpoint of that subinterval",
   "the average of f at the two endpoints of that subinterval",
   "the smallest value of f on that subinterval"], ans=0,
   why="A left Riemann sum evaluates f at the left endpoint of each subinterval; only for an increasing function does that also happen to be the smallest value there."),
 dict(q="The table gives values of v, the rate at which water enters a tank, in gallons per minute. Using a left Riemann sum with the four subintervals indicated by the table, approximate int from 0 to 12 of v(t) dt.", table=TAB_A, choices=[
   "95 gallons",
   "110 gallons",
   "125 gallons",
   "168 gallons"], ans=0,
   why="The widths are 2, 3, 4, and 3 and the left-endpoint heights are 4, 6, 9, and 11, giving 8 + 18 + 36 + 33 = 95 gallons."),
 dict(q="Using the values in the table and a right Riemann sum with the four subintervals indicated, approximate int from 0 to 12 of v(t) dt.", table=TAB_A, choices=[
   "95 gallons",
   "110 gallons",
   "125 gallons",
   "168 gallons"], ans=2,
   why="The right-endpoint heights are 6, 9, 11, and 14 against widths 2, 3, 4, and 3, giving 12 + 27 + 44 + 42 = 125 gallons."),
 dict(q="Using the values in the table and a trapezoidal sum with the four subintervals indicated, approximate int from 0 to 12 of v(t) dt.", table=TAB_A, choices=[
   "95 gallons",
   "110 gallons",
   "125 gallons",
   "220 gallons"], ans=1,
   why="Each trapezoid uses the average of its two endpoint values: 5(2) + 7.5(3) + 10(4) + 12.5(3) = 110, which is also the average of the left sum 95 and the right sum 125."),
 dict(q="The values of v in the table increase throughout the interval. What can be said about the left Riemann sum approximation of int from 0 to 12 of v(t) dt?", table=TAB_A, choices=[
   "It overestimates the integral.",
   "It underestimates the integral.",
   "It equals the integral exactly.",
   "Nothing can be said without knowing whether v is concave up or concave down."], ans=1,
   why="For an increasing function the left endpoint gives the smallest value on each subinterval, so every rectangle sits below the curve and the sum is too small."),
 dict(q="The table gives values of a function f. Using a left Riemann sum with the six subintervals of width 1, approximate int from 0 to 6 of f(x) dx.", table=TAB_B, choices=[
   "46",
   "52.5",
   "59",
   "62"], ans=0,
   why="The left-endpoint values are 3, 5, 6, 8, 11, and 13, and each has width 1, so the sum is 46."),
 dict(q="Using the table and a right Riemann sum with the six subintervals of width 1, approximate int from 0 to 6 of f(x) dx.", table=TAB_B, choices=[
   "46",
   "52.5",
   "59",
   "62"], ans=2,
   why="The right-endpoint values are 5, 6, 8, 11, 13, and 16, each of width 1, so the sum is 59."),
 dict(q="Using the table and a midpoint Riemann sum with three subintervals of equal width, approximate int from 0 to 6 of f(x) dx.", table=TAB_B, choices=[
   "40",
   "52",
   "53",
   "66"], ans=1,
   why="The three subintervals [0,2], [2,4], [4,6] have midpoints 1, 3, and 5, where f is 5, 8, and 13, so the sum is 2(5 + 8 + 13) = 52."),
 dict(q="Using the table and a trapezoidal sum with the six subintervals of width 1, approximate int from 0 to 6 of f(x) dx.", table=TAB_B, choices=[
   "46",
   "52.5",
   "53",
   "59"], ans=1,
   why="The trapezoidal sum is the average of the left sum 46 and the right sum 59, which is 52.5."),
 dict(q="Using the table and a trapezoidal sum with three subintervals of equal width 2, approximate int from 0 to 6 of f(x) dx.", table=TAB_B, choices=[
   "40",
   "52",
   "53",
   "66"], ans=2,
   why="The three trapezoids have averaged heights 4.5, 8.5, and 13.5 and width 2 each, so the sum is 2(4.5 + 8.5 + 13.5) = 53."),
 dict(q="The table gives g, the rate at which oil drains from a tank, in liters per hour. Using a left Riemann sum with the three subintervals indicated by the table, approximate int from 0 to 10 of g(t) dt.", table=TAB_C, choices=[
   "89 liters",
   "113.5 liters",
   "138 liters",
   "170 liters"], ans=2,
   why="The widths are 3, 3, and 4 with left-endpoint heights 20, 14, and 9, so the sum is 60 + 42 + 36 = 138 liters."),
 dict(q="Using the values of g in the table and a right Riemann sum with the three subintervals indicated, approximate int from 0 to 10 of g(t) dt.", table=TAB_C, choices=[
   "89 liters",
   "113.5 liters",
   "138 liters",
   "170 liters"], ans=0,
   why="The right-endpoint heights are 14, 9, and 5 against widths 3, 3, and 4, giving 42 + 27 + 20 = 89 liters."),
 dict(q="Using the values of g in the table and a trapezoidal sum with the three subintervals indicated, approximate int from 0 to 10 of g(t) dt.", table=TAB_C, choices=[
   "89 liters",
   "113.5 liters",
   "138 liters",
   "227 liters"], ans=1,
   why="The trapezoidal sum averages the left sum 138 and the right sum 89, giving 113.5 liters."),
 dict(q="The values of g in the table are decreasing throughout. What can be said about the right Riemann sum approximation of int from 0 to 10 of g(t) dt?", table=TAB_C, choices=[
   "It overestimates the integral.",
   "It underestimates the integral.",
   "It equals the integral exactly.",
   "It underestimates only if g is concave up."], ans=1,
   why="For a decreasing function the right endpoint is the smallest value on each subinterval, so every rectangle lies below the curve."),
 dict(q="Approximate int from 0 to 4 of x^2 dx using a right Riemann sum with four subintervals of equal width.", choices=[
   "14",
   "21",
   "22",
   "30"], ans=3,
   why="With width 1 the right endpoints are 1, 2, 3, and 4, so the sum is 1 + 4 + 9 + 16 = 30."),
 dict(q="Approximate int from 0 to 4 of x^2 dx using a left Riemann sum with four subintervals of equal width.", choices=[
   "14",
   "21",
   "22",
   "30"], ans=0,
   why="With width 1 the left endpoints are 0, 1, 2, and 3, so the sum is 0 + 1 + 4 + 9 = 14."),
 dict(q="Approximate int from 0 to 4 of x^2 dx using a midpoint Riemann sum with four subintervals of equal width.", choices=[
   "14",
   "21",
   "22",
   "30"], ans=1,
   why="The midpoints are 0.5, 1.5, 2.5, and 3.5, so the sum is 0.25 + 2.25 + 6.25 + 12.25 = 21."),
 dict(q="If f is concave up on [a, b], the trapezoidal approximation of int from a to b of f(x) dx", choices=[
   "overestimates the integral",
   "underestimates the integral",
   "equals the integral exactly",
   "overestimates only if f is also increasing"], ans=0,
   why="A chord joining two points on a concave-up curve lies above the curve, so every trapezoid contains extra area."),
 dict(q="If f is concave up on [a, b], the midpoint approximation of int from a to b of f(x) dx", choices=[
   "overestimates the integral",
   "underestimates the integral",
   "equals the integral exactly",
   "underestimates only if f is also decreasing"], ans=1,
   why="The tangent line at the midpoint lies below a concave-up curve, and the midpoint rectangle has the same area as the region under that tangent line, so the approximation falls short."),
 dict(q="If f is concave down on [a, b], the trapezoidal approximation of int from a to b of f(x) dx", choices=[
   "overestimates the integral",
   "underestimates the integral",
   "equals the integral exactly",
   "cannot be compared to the integral"], ans=1,
   why="Chords lie below a concave-down curve, so each trapezoid misses the sliver of area between the chord and the curve."),
 dict(q="Approximate int from 1 to 3 of (1/x) dx using a right Riemann sum with four subintervals of equal width.", choices=[
   "0.950",
   "1.117",
   "1.283",
   "1.900"], ans=0,
   why="The width is 0.5 and the right endpoints are 1.5, 2, 2.5, and 3, so the sum is 0.5(2/3 + 1/2 + 2/5 + 1/3) = 0.95."),
 dict(q="A function f is increasing and differentiable on [a, b]. Which approximation of int from a to b of f(x) dx is guaranteed to be an overestimate?", choices=[
   "the left Riemann sum",
   "the right Riemann sum",
   "the midpoint Riemann sum",
   "the trapezoidal sum"], ans=1,
   why="For an increasing function the right endpoint is the largest value on each subinterval; the midpoint and trapezoidal sums depend on concavity, not on whether f increases."),
 dict(q="As the number of equal subintervals n used in a Riemann sum for a continuous function f on [a, b] increases without bound, the sum", choices=[
   "approaches int from a to b of f(x) dx regardless of which sample points are used",
   "approaches f(b) - f(a)",
   "approaches the average value of f on [a, b]",
   "approaches int from a to b of f(x) dx only if left endpoints are used"], ans=0,
   why="For a continuous function every choice of sample points gives sums with the same limit, which is the definite integral."),
 dict(q="The table gives the velocity of a car in feet per second. Using a midpoint Riemann sum with two subintervals of equal width, approximate the distance the car travels from t = 0 to t = 40 seconds.", table=TAB_D, choices=[
   "660 feet",
   "835 feet",
   "880 feet",
   "1010 feet"], ans=2,
   why="The subintervals [0,20] and [20,40] have midpoints 10 and 30, where v is 14 and 30, so the sum is 20(14) + 20(30) = 880 feet."),
 dict(q="A continuous function h increases on [0, 2] and decreases on [2, 5]. What can be concluded about a left Riemann sum for int from 0 to 5 of h(x) dx using subintervals that do not have a partition point at x = 2?", choices=[
   "It must be an overestimate.",
   "It must be an underestimate.",
   "It cannot be determined whether it overestimates or underestimates.",
   "It must equal the integral."], ans=2,
   why="The left-endpoint rectangles fall short where h is increasing and run over where h is decreasing, and without more information the two errors cannot be compared."),
]
