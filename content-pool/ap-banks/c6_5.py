# CALC 6.5 Interpreting the Behavior of Accumulation Functions Involving Area — 25 questions
# Answers verified with sympy; see verify_c6_5.py, which builds a concrete
# function matching each described sign pattern or list of signed areas and
# confirms the claimed increase, extremum, concavity, or value.
# Questions 14, 15, 16, 17, 25 are conceptual (F' = f and F'' = f').
TOPIC = ("6.5", "Interpreting the Behavior of Accumulation Functions Involving Area", 6)

# f is continuous, with f(3) = f(7) = 0 and the signs below.
SIGNS = dict(
    headers=["Interval", "Sign of f(t)"],
    rows=[["0 < t < 3", "positive"], ["3 < t < 7", "negative"], ["7 < t < 10", "positive"]],
)
# Signed areas of the regions between the graph of the continuous f and the t-axis.
AREAS = dict(
    headers=["Interval", "Region between the graph of f and the t-axis"],
    rows=[["[0, 3]", "area 6, lying above the axis"],
          ["[3, 5]", "area 4, lying below the axis"],
          ["[5, 9]", "area 5, lying above the axis"]],
)

QUESTIONS = [
 dict(q="On which set is F increasing, where F(x) = int from 0 to x of f(t) dt and f is the continuous function whose signs are given in the table?", table=SIGNS, choices=[
   "0 < x < 3 and 7 < x < 10",
   "3 < x < 7",
   "0 < x < 10",
   "only 7 < x < 10"], ans=0,
   why="F'(x) = f(x), so F increases exactly where f is positive."),
 dict(q="At which value of x does F have a local maximum, where F(x) = int from 0 to x of f(t) dt and f has the signs given in the table?", table=SIGNS, choices=[
   "x = 3",
   "x = 7",
   "x = 0",
   "x = 10"], ans=0,
   why="F' = f changes from positive to negative at x = 3, which is the first-derivative test for a local maximum."),
 dict(q="At which value of x does F have a local minimum, given that F(x) = int from 0 to x of f(t) dt and f has the signs shown in the table?", table=SIGNS, choices=[
   "x = 3",
   "x = 7",
   "x = 5",
   "F has no local minimum."], ans=1,
   why="F' = f changes from negative to positive at x = 7."),
 dict(q="The graph of F has a horizontal tangent line at which values of x, if F(x) = int from 0 to x of f(t) dt and f is as described in the table?", table=SIGNS, choices=[
   "x = 3 and x = 7 only",
   "x = 0 only",
   "x = 0, 3, 7, and 10",
   "nowhere on 0 < x < 10"], ans=0,
   why="A horizontal tangent means F'(x) = f(x) = 0, which happens only at x = 3 and x = 7."),
 dict(q="What is F(3), where F(x) = int from 0 to x of f(t) dt and the regions between the graph of f and the axis are described in the table?", table=AREAS, choices=[
   "-6",
   "2",
   "6",
   "7"], ans=2,
   why="On [0, 3] the region lies above the axis, so the accumulation is +6."),
 dict(q="What is F(5), for the accumulation function F(x) = int from 0 to x of f(t) dt with f as described in the table?", table=AREAS, choices=[
   "-4",
   "2",
   "6",
   "10"], ans=1,
   why="Area below the axis counts as negative, so F(5) = 6 - 4 = 2."),
 dict(q="What is F(9), for F(x) = int from 0 to x of f(t) dt with the areas given in the table?", table=AREAS, choices=[
   "3",
   "7",
   "11",
   "15"], ans=1,
   why="Adding the signed areas gives 6 - 4 + 5 = 7."),
 dict(q="At what value of x does F attain its absolute maximum on [0, 9], where F(x) = int from 0 to x of f(t) dt and f is described in the table?", table=AREAS, choices=[
   "x = 0",
   "x = 3",
   "x = 5",
   "x = 9"], ans=3,
   why="The candidates are the endpoints and the critical points, where F takes the values 0, 6, 2, and 7, and the largest is F(9) = 7."),
 dict(q="At what value of x does F attain its absolute minimum on [0, 9], for F(x) = int from 0 to x of f(t) dt with f as in the table?", table=AREAS, choices=[
   "x = 0",
   "x = 3",
   "x = 5",
   "x = 9"], ans=0,
   why="The values at the candidates are F(0) = 0, F(3) = 6, F(5) = 2, and F(9) = 7, so the minimum is at the left endpoint, a place students often forget to test."),
 dict(q="Which interval is an interval on which F is decreasing, where F(x) = int from 0 to x of f(t) dt and the table describes f?", table=AREAS, choices=[
   "[0, 3]",
   "[3, 5]",
   "[5, 9]",
   "F is never decreasing."], ans=1,
   why="F decreases where f is negative, and the table places the below-axis region on [3, 5]."),
 dict(q="Let F(x) = int from 0 to x of (t - 4) dt. Which expression equals F(x)?", choices=[
   "x^2/2 - 4x",
   "x^2/2 - 4x + 8",
   "x - 4",
   "x^2 - 4x"], ans=0,
   why="Antidifferentiating gives t^2/2 - 4t evaluated from 0 to x, and the lower limit contributes nothing."),
 dict(q="For F(x) = int from 0 to x of (t - 4) dt, at what value of x does F have its minimum value?", choices=[
   "x = 0",
   "x = 2",
   "x = 4",
   "x = 8"], ans=2,
   why="F'(x) = x - 4 changes from negative to positive at x = 4."),
 dict(q="For the accumulation function F(x) = int from 0 to x of (t - 4) dt, what is F(6)?", choices=[
   "-8",
   "-6",
   "2",
   "6"], ans=1,
   why="F(6) = 36/2 - 24 = 18 - 24 = -6."),
 dict(q="Let F(x) = int from 0 to x of f(t) dt, where f is differentiable. On an interval where f is increasing, the graph of F is", choices=[
   "concave up",
   "concave down",
   "linear",
   "decreasing"], ans=0,
   why="F'' = f', which is positive exactly where f increases; whether F itself rises depends on the sign of f, not on f increasing."),
 dict(q="Let G(x) = int from 0 to x of g(t) dt, where g is differentiable and decreasing on (a, b). On that interval the graph of G is", choices=[
   "concave up",
   "concave down",
   "increasing",
   "decreasing"], ans=1,
   why="G'' = g' < 0 where g decreases, which makes G concave down regardless of the sign of g."),
 dict(q="An accumulation function F(x) = int from 0 to x of f(t) dt has a point of inflection at x = c when", choices=[
   "f has a local maximum or local minimum at c",
   "f(c) = 0",
   "F(c) = 0",
   "f changes sign at c"], ans=0,
   why="An inflection point of F needs F'' = f' to change sign, which happens where f turns around, not merely where f is zero."),
 dict(q="Suppose f(t) > 0 for every real number t and F(x) = int from 0 to x of f(t) dt. Which statement must be true?", choices=[
   "F is increasing on the whole real line",
   "F(x) > 0 for every x",
   "F is concave up on the whole real line",
   "F has a minimum at x = 0"], ans=0,
   why="F' = f > 0 forces F to increase, but for x < 0 the accumulation runs backward and F(x) is negative, and concavity would require information about f'."),
 dict(q="Let F(x) = int from 2 to x of f(t) dt, where f(t) = (t - 1)(t - 5). At which value of x does F have a local maximum?", choices=[
   "x = 1",
   "x = 2",
   "x = 3",
   "x = 5"], ans=0,
   why="F' = f is positive for x < 1 and negative for 1 < x < 5, so F turns from rising to falling at x = 1."),
 dict(q="Let F(x) = int from 2 to x of (t - 1)(t - 5) dt. At which value of x does the graph of F have a point of inflection?", choices=[
   "x = 1",
   "x = 3",
   "x = 5",
   "x = 2"], ans=1,
   why="F'' = f' = 2t - 6 changes sign at t = 3, which is where the parabola f has its vertex."),
 dict(q="Let F(x) = int from 0 to x of sin(t) dt. What is the maximum value of F on [0, 2pi]?", choices=[
   "0",
   "1",
   "2",
   "pi"], ans=2,
   why="F(x) = 1 - cos(x), which is largest when cos(x) = -1 at x = pi, giving F(pi) = 2."),
 dict(q="Order the values F(0), F(5), and F(9) from smallest to largest, where F(x) = int from 0 to x of f(t) dt and f is the function whose regions are described in the table.", table=AREAS, choices=[
   "F(0) < F(5) < F(9)",
   "F(5) < F(0) < F(9)",
   "F(9) < F(5) < F(0)",
   "F(0) < F(9) < F(5)"], ans=0,
   why="The signed areas give F(0) = 0, F(5) = 6 - 4 = 2, and F(9) = 6 - 4 + 5 = 7."),
 dict(q="Let F(x) = int from 0 to x of (t^2 - 9) dt. At which value of x does F have a local maximum?", choices=[
   "x = -3",
   "x = 0",
   "x = 3",
   "x = 9"], ans=0,
   why="F' = t^2 - 9 is positive for t < -3 and negative on (-3, 3), so F turns from rising to falling at x = -3."),
 dict(q="Let F(x) = int from 1 to x of (t - 3) dt. What is the absolute minimum value of F on [0, 5]?", choices=[
   "-2",
   "-1.5",
   "0",
   "2"], ans=0,
   why="F' = x - 3 gives the only critical point x = 3, and F(3) = -2 is smaller than F(0) = 2.5 and F(5) = 0."),
 dict(q="If F(x) = int from 0 to x of f(t) dt and the graph of f lies below the t-axis for all t in (a, b), then on (a, b) the graph of F", choices=[
   "lies below the x-axis",
   "is decreasing",
   "is concave down",
   "has a local minimum"], ans=1,
   why="A negative integrand makes F' negative, so F falls; the value of F can still be positive if enough area was accumulated before x = a."),
 dict(q="Let F(x) = int from 0 to x of (t - 3)^2 dt. Which statement about x = 3 is correct?", choices=[
   "F has a local maximum at x = 3.",
   "F has a local minimum at x = 3.",
   "F has a horizontal tangent at x = 3 but no extremum there.",
   "F is not differentiable at x = 3."], ans=2,
   why="F'(3) = 0, but F' = (x - 3)^2 does not change sign, so F keeps increasing through x = 3."),
]
