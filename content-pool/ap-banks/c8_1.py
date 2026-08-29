# CALC 8.1 Finding the Average Value of a Function on an Interval — 25 questions
# The average value is (1/(b - a)) * int from a to b of f(x) dx, NOT the average
# of the endpoint values and NOT the average rate of change. Every integral is
# computed by sympy; see verify_c8_1.py.
TOPIC = ("8.1", "Finding the Average Value of a Function on an Interval", 8)
QUESTIONS = [
 dict(q="What is the average value of a continuous function f on the interval [a, b]?", choices=[
   "(1/(b - a)) * int from a to b of f(x) dx",
   "(f(a) + f(b))/2",
   "int from a to b of f(x) dx",
   "(f(b) - f(a))/(b - a)"], ans=0,
   why="The average value is the integral divided by the length of the interval."),
 dict(q="What is the average value of f(x) = x^2 on [0, 3]?", choices=[
   "1",
   "3",
   "4.5",
   "9"], ans=1,
   why="The integral is 9 and the interval has length 3, so the average value is 9/3 = 3."),
 dict(q="What is the average value of f(x) = 2x on [1, 5]?", choices=[
   "6",
   "8",
   "12",
   "24"], ans=0,
   why="The integral is 25 - 1 = 24 and the interval has length 4, so the average is 6."),
 dict(q="What is the average value of f(x) = sin(x) on [0, pi]?", choices=[
   "2/pi",
   "2",
   "1/pi",
   "0"], ans=0,
   why="The integral of sin from 0 to pi is 2, and dividing by the length pi gives 2/pi."),
 dict(q="What is the average value of f(x) = x^3 on [0, 2]?", choices=[
   "1",
   "2",
   "4",
   "8"], ans=1,
   why="The integral is 16/4 = 4, and dividing by the length 2 gives 2."),
 dict(q="A student computes the average value of f(x) = x^2 on [0, 3] as (0 + 9)/2 = 4.5. What is wrong?", choices=[
   "averaging the endpoint values ignores the whole interior of the interval; the correct value is the integral divided by 3, which is 3",
   "nothing is wrong",
   "the endpoints should be multiplied, not averaged",
   "the average value of x^2 on that interval really is 4.5"], ans=0,
   why="Average value is an integral average over every point of the interval, not a two-point average."),
 dict(q="What is the average value of f(x) = 1/x on [1, e]?", choices=[
   "1/(e - 1)",
   "e - 1",
   "1",
   "ln(e - 1)"], ans=0,
   why="The integral is ln(e) - ln(1) = 1, and the interval has length e - 1."),
 dict(q="What is the average value of f(x) = e^x on [0, 1]?", choices=[
   "e - 1",
   "e",
   "e + 1",
   "(e - 1)/2"], ans=0,
   why="The integral is e - 1 and the interval has length 1."),
 dict(q="What is the average value of the constant function f(x) = 7 on [2, 11]?", choices=[
   "3.5",
   "7",
   "9",
   "63"], ans=1,
   why="The integral is 7*9 = 63, and dividing by the length 9 returns the constant 7."),
 dict(q="The average value of f on [0, 4] is 5. What is int from 0 to 4 of f(x) dx?", choices=[
   "1.25",
   "5",
   "9",
   "20"], ans=3,
   why="Multiplying the average value by the length of the interval recovers the integral."),
 dict(q="The Mean Value Theorem for Integrals guarantees a number c in [a, b] with f(c) equal to the average value of f, provided that", choices=[
   "f is continuous on [a, b]",
   "f is increasing on [a, b]",
   "f is differentiable on (a, b) but need not be continuous",
   "f is positive on [a, b]"], ans=0,
   why="Continuity on the closed interval is the hypothesis; it lets the Intermediate Value Theorem produce the number c."),
 dict(q="For f(x) = x^2 on [1, 4], what is the average value, and how does it compare with the average rate of change on the same interval?", choices=[
   "the average value is 7 and the average rate of change is 5, so they are different quantities",
   "both are 7",
   "both are 5",
   "the average value is 5 and the average rate of change is 7"], ans=0,
   why="The average value is (1/3)(64/3 - 1/3) = 7 while the average rate of change is (16 - 1)/3 = 5."),
 dict(q="What is the average value of f(x) = sqrt(x) on [0, 4]?", choices=[
   "4/3",
   "2",
   "8/3",
   "16/3"], ans=0,
   why="The integral is (2/3)*8 = 16/3, and dividing by the length 4 gives 4/3."),
 dict(q="A particle has velocity v(t) = 3t^2 for 0 <= t <= 4. What is its average velocity on that interval?", choices=[
   "16",
   "24",
   "48",
   "64"], ans=0,
   why="The integral of v is 64, the total displacement, and dividing by the elapsed time 4 gives 16."),
 dict(q="For what value of b > 0 is the average value of f(x) = x on [0, b] equal to 5?", choices=[
   "2.5",
   "5",
   "10",
   "25"], ans=2,
   why="The average value is (1/b)(b^2/2) = b/2, so b/2 = 5 gives b = 10."),
 dict(q="What is the average value of f(x) = cos(x) on [0, pi/2]?", choices=[
   "2/pi",
   "1",
   "pi/2",
   "1/2"], ans=0,
   why="The integral is 1, and dividing by the length pi/2 gives 2/pi."),
 dict(q="What is the average value of f(x) = |x| on [-2, 2]?", choices=[
   "0",
   "1",
   "2",
   "4"], ans=1,
   why="The integral is 4 by symmetry, and dividing by the length 4 gives 1."),
 dict(q="What is the average value of f(x) = x^3 on [-2, 2]?", choices=[
   "0",
   "2",
   "4",
   "8"], ans=0,
   why="The function is odd, so the integral over a symmetric interval is 0, and so is the average value."),
 dict(q="For f(x) = x^2 on [0, 3], the Mean Value Theorem for Integrals guarantees a number c with f(c) equal to the average value. What is c?", choices=[
   "sqrt(3)",
   "3",
   "1.5",
   "9"], ans=0,
   why="The average value is 3, so c^2 = 3 and the number in the interval is c = sqrt(3)."),
 dict(q="What is the average value of f(x) = 4 - x^2 on [0, 2]?", choices=[
   "4/3",
   "2",
   "8/3",
   "16/3"], ans=2,
   why="The integral is 8 - 8/3 = 16/3, and dividing by the length 2 gives 8/3."),
 dict(q="A tank's inflow rate R(t) is measured in gallons per minute for 0 <= t <= 30 minutes. The average value of R on that interval has units of", choices=[
   "gallons per minute",
   "gallons",
   "minutes",
   "gallons per minute squared"], ans=0,
   why="The integral has units of gallons and dividing by minutes returns the original rate units."),
 dict(q="What is the average value of f(x) = 1/x^2 on [1, 2]?", choices=[
   "1/4",
   "3/8",
   "1/2",
   "1"], ans=2,
   why="The integral is 1 - 1/2 = 1/2, and the interval has length 1."),
 dict(q="What is the average value of f(x) = 6x on [0, 4]?", choices=[
   "6",
   "12",
   "24",
   "48"], ans=1,
   why="The integral is 3*16 = 48, and dividing by the length 4 gives 12."),
 dict(q="The average value of f on [2, 6] is 7, and the average value of f on [6, 10] is 3. What is the average value of f on [2, 10]?", choices=[
   "4",
   "5",
   "10",
   "40"], ans=1,
   why="The two integrals are 28 and 12, so the total is 40 over an interval of length 8."),
 dict(q="A student computes int from 1 to 5 of f(x) dx = 36 and reports 36 as the average value of f on [1, 5]. What is the average value?", choices=[
   "7.2",
   "9",
   "18",
   "36"], ans=1,
   why="The integral must still be divided by the interval length 4, giving 36/4 = 9."),
]
