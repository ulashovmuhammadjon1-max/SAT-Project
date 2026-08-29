# CALC 3.3 Differentiating Inverse Functions — 25 questions
# Every value is recomputed in verify_c3_3.py by first SOLVING f(a) = b for
# a = f^-1(b) and only then evaluating 1/f'(a) -- the same two steps a student
# has to take. Most computational questions here deliberately have
# f^-1(b) not equal to b, so the common shortcut 1/f'(b) gives a wrong answer
# that is offered as a distractor.
# Questions 1, 12, 16, 22 and 25 are conceptual.
TOPIC = ("3.3", "Differentiating Inverse Functions", 3)

TAB = dict(
    headers=["x", "f(x)", "f'(x)"],
    rows=[["1", "3", "2"], ["2", "5", "4"], ["3", "8", "1/2"], ["4", "10", "5"]],
)

QUESTIONS = [
 dict(q="If f is differentiable and invertible, then (f^-1)'(b) =", choices=[
   "1/f'(f^-1(b))", "1/f'(b)", "f'(f^-1(b))", "-1/f'(b)"], ans=0,
   why="The derivative of the inverse is the reciprocal of f' evaluated at the input that f sends to b."),
 dict(q="A differentiable invertible function f satisfies f(2) = 5 and f'(2) = 3. Then (f^-1)'(5) =", choices=[
   "1/5", "1/3", "3", "5"], ans=1,
   why="f^-1(5) = 2, so (f^-1)'(5) = 1/f'(2) = 1/3."),
 dict(q="A differentiable invertible function f satisfies f(1) = 4 and f'(1) = 1/2. Then (f^-1)'(4) =", choices=[
   "1/4", "1/2", "2", "4"], ans=2,
   why="f^-1(4) = 1, so (f^-1)'(4) = 1/f'(1) = 1/(1/2) = 2."),
 dict(q="The table gives values of an invertible differentiable function f and its derivative. Then (f^-1)'(5) =", table=TAB, choices=[
   "1/5", "1/4", "2", "4"], ans=1,
   why="The table shows f(2) = 5, so f^-1(5) = 2 and (f^-1)'(5) = 1/f'(2) = 1/4."),
 dict(q="Let f(x) = x^3 + x. Then (f^-1)'(2) =", choices=[
   "1/13", "1/4", "4", "13"], ans=1,
   why="Solve x^3 + x = 2 to get f^-1(2) = 1; f'(x) = 3x^2 + 1 gives f'(1) = 4, so the answer is 1/4. Using f'(2) = 13 by mistake gives 1/13."),
 dict(q="Let f(x) = x^3 + 2x + 1. Then (f^-1)'(1) =", choices=[
   "1/5", "1/2", "2", "5"], ans=1,
   why="Solve x^3 + 2x + 1 = 1 to get f^-1(1) = 0; f'(0) = 2, so the answer is 1/2."),
 dict(q="Let f(x) = x^5 + 3x - 1. Then (f^-1)'(3) =", choices=[
   "1/408", "1/8", "3", "8"], ans=1,
   why="Solve x^5 + 3x - 1 = 3 to get f^-1(3) = 1; f'(x) = 5x^4 + 3 gives f'(1) = 8, so the answer is 1/8."),
 dict(q="Let f(x) = e^x. Then (f^-1)'(1) =", choices=[
   "0", "1/e", "1", "e"], ans=2,
   why="f^-1(1) = 0 because e^0 = 1, and f'(0) = 1, so the answer is 1; this agrees with d/dx[ln x] = 1/x at x = 1."),
 dict(q="Let f(x) = ln(x). Then (f^-1)'(0) =", choices=[
   "-1", "0", "1", "e"], ans=2,
   why="f^-1(0) = 1 because ln(1) = 0, and f'(1) = 1, so the answer is 1; the inverse is e^x, whose derivative at 0 is 1."),
 dict(q="Let f(x) = x^2 for x >= 0, so that f is invertible. Then (f^-1)'(9) =", choices=[
   "1/18", "1/6", "6", "18"], ans=1,
   why="f^-1(9) = 3 and f'(3) = 6, so the answer is 1/6; evaluating f' at 9 instead gives the wrong 1/18."),
 dict(q="Let f(x) = sqrt(x) for x > 0. Then (f^-1)'(2) =", choices=[
   "1/4", "2 sqrt(2)", "4", "8"], ans=2,
   why="f^-1(2) = 4 since sqrt(4) = 2, and f'(4) = 1/4, so the answer is 4; the inverse is x^2, whose derivative at 2 is indeed 4."),
 dict(q="A student computes (f^-1)'(6) as 1/f'(6). When does this give the wrong answer?", choices=[
   "Whenever f^-1(6) is not equal to 6, since f' must be evaluated at f^-1(6)",
   "Never; the two expressions are always equal",
   "Only when f is decreasing",
   "Only when f'(6) = 0"], ans=0,
   why="The formula evaluates f' at the input that f maps to 6, which is usually a different number from 6."),
 dict(q="Using the table of values of f and f', the value of (f^-1)'(8) is", table=TAB, choices=[
   "1/8", "1/2", "2", "8"], ans=2,
   why="f(3) = 8, so f^-1(8) = 3 and (f^-1)'(8) = 1/f'(3) = 1/(1/2) = 2."),
 dict(q="Let f(x) = 2x + 3. Then (f^-1)'(x) =", choices=[
   "1/2", "2", "-1/2", "1/(2x + 3)"], ans=0,
   why="f^-1(x) = (x - 3)/2, a line of slope 1/2; equivalently 1/f'(anything) = 1/2."),
 dict(q="Let f(x) = x^3. Then (f^-1)'(8) =", choices=[
   "1/192", "1/12", "1/3", "12"], ans=1,
   why="f^-1(8) = 2 and f'(2) = 12, so the answer is 1/12; using f'(8) = 192 gives the wrong 1/192."),
 dict(q="How are the graphs of f and f^-1 related, and what does that say about their slopes?", choices=[
   "They are reflections across the line y = x, and the slopes at (a, b) and (b, a) are reciprocals",
   "They are reflections across the x-axis, and the slopes are negatives",
   "They are identical, and the slopes are equal",
   "They are reflections across the y-axis, and the slopes are equal"], ans=0,
   why="Reflecting across y = x exchanges rise and run, which inverts the slope."),
 dict(q="Let f(x) = tan(x) for -pi/2 < x < pi/2. Then (f^-1)'(1) =", choices=[
   "1/2", "1", "2", "sqrt(2)"], ans=0,
   why="f^-1(1) = pi/4 since tan(pi/4) = 1, and f'(pi/4) = sec^2(pi/4) = 2, so the answer is 1/2."),
 dict(q="Let f(x) = x + sin(x). Then (f^-1)'(0) =", choices=[
   "0", "1/2", "1", "2"], ans=1,
   why="f(0) = 0 so f^-1(0) = 0, and f'(x) = 1 + cos(x) gives f'(0) = 2, so the answer is 1/2."),
 dict(q="Let f(x) = x^3 + 3x - 4. Then (f^-1)'(0) =", choices=[
   "1/6", "1/3", "3", "6"], ans=0,
   why="Solve x^3 + 3x - 4 = 0 to get f^-1(0) = 1; f'(x) = 3x^2 + 3 gives f'(1) = 6, so the answer is 1/6."),
 dict(q="Let g be the inverse of the differentiable function f, and suppose f(3) = 7 and f'(3) = 1/4. Then g'(7) =", choices=[
   "1/7", "1/4", "4", "7"], ans=2,
   why="g'(7) = 1/f'(g(7)) = 1/f'(3) = 1/(1/4) = 4."),
 dict(q="An invertible differentiable function f satisfies f(0) = 1, f(1) = 3, f'(0) = 2 and f'(1) = 5. Then (f^-1)'(3) =", choices=[
   "1/5", "1/2", "2", "5"], ans=0,
   why="f(1) = 3 means f^-1(3) = 1, so the answer is 1/f'(1) = 1/5; using f'(0) because 3 appears in no other row gives the wrong 1/2."),
 dict(q="Why must f be one-to-one on an interval before (f^-1)'(b) can be discussed there?", choices=[
   "Without one-to-one behavior there is no inverse function to differentiate",
   "Because f' would otherwise be negative",
   "Because the reciprocal of f' would be undefined",
   "Because f would not be continuous"], ans=0,
   why="An inverse function exists exactly when f assigns distinct outputs to distinct inputs on that interval."),
 dict(q="Let f(x) = 2x^3 + x - 2. Then (f^-1)'(16) =", choices=[
   "1/1537", "1/25", "2", "25"], ans=1,
   why="Solve 2x^3 + x - 2 = 16 to get f^-1(16) = 2; f'(x) = 6x^2 + 1 gives f'(2) = 25, so the answer is 1/25. Evaluating f' at 16 instead gives 1/1537."),
 dict(q="An invertible differentiable function f satisfies f(2) = 5 and f'(2) = 1/3. An equation of the line tangent to y = f^-1(x) at x = 5 is", choices=[
   "y = 3x - 13",
   "y = (1/3)x + 1/3",
   "y = 3x - 5",
   "y = (1/3)(x - 2) + 5"], ans=0,
   why="(f^-1)'(5) = 1/f'(2) = 3 and f^-1(5) = 2, so the line through (5, 2) with slope 3 is y = 3x - 13."),
 dict(q="If f is differentiable with f'(x) > 0 for every x, which of the following must be true?", choices=[
   "f is invertible, and (f^-1)'(b) is positive wherever it is defined",
   "f is invertible, but (f^-1)' is negative",
   "f need not be invertible",
   "(f^-1)'(b) = f'(b) for every b"], ans=0,
   why="A positive derivative makes f strictly increasing, hence one-to-one, and the reciprocal of a positive number is positive."),
]
