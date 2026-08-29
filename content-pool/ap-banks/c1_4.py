# CALC 1.4 Estimating Limit Values from Tables — 25 questions
# Tables are written inline in the stem as an x row and an f(x) row, since this
# bank has no figures.  Every printed table value was generated from the stated
# function and is re-derived in verify_c1_4.py, so a mistyped entry fails the
# check rather than reaching a student.  Questions 8, 17 and 21 are conceptual
# (what a table can and cannot establish) and carry no sympy check.
TOPIC = ("1.4", "Estimating Limit Values from Tables", 1)
QUESTIONS = [
 dict(q="Values of f(x) = (x^2 - 4)/(x - 2) are given by x = 1.9, 1.99, 1.999, 2.001, 2.01, 2.1 with f(x) = 3.9000, 3.9900, 3.9990, 4.0010, 4.0100, 4.1000. Based on the table, lim as x -> 2 of f(x) is most likely", choices=[
   "0", "2", "4", "the limit does not exist"], ans=2,
   why="The tabulated values close in on 4 from both sides."),
 dict(q="Values of g(x) = (sqrt(x) - 2)/(x - 4) are given by x = 3.9, 3.99, 3.999, 4.001, 4.01, 4.1 with g(x) = 0.251582, 0.250156, 0.250016, 0.249984, 0.249844, 0.248457. Based on the table, lim as x -> 4 of g(x) is most likely", choices=[
   "0", "0.25", "0.5", "4"], ans=1,
   why="The values approach 0.25 from above on the left and from below on the right."),
 dict(q="Values of f(x) = sin(x)/x are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = 0.998334, 0.999983, 1.000000, 1.000000, 0.999983, 0.998334. Based on the table, lim as x -> 0 of sin(x)/x is most likely", choices=[
   "0", "0.5", "1", "the limit does not exist"], ans=2,
   why="The values rise toward 1 symmetrically from both sides."),
 dict(q="Values of f(x) = (1 - cos(x))/x are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = -0.049958, -0.005000, -0.000500, 0.000500, 0.005000, 0.049958. Based on the table, lim as x -> 0 of (1 - cos(x))/x is most likely", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=1,
   why="The entries shrink toward 0 from below on the left and from above on the right."),
 dict(q="Values of f(x) = (1 + x)^(1/x) are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = 2.8680, 2.7320, 2.7196, 2.7169, 2.7048, 2.5937. Based on the table, lim as x -> 0 of (1 + x)^(1/x) is most likely", choices=[
   "1", "2", "about 2.718", "the limit does not exist"], ans=2,
   why="The values squeeze toward 2.718..., the number e."),
 dict(q="A table for a function f gives f(0.9) = 3.1, f(0.99) = 3.01, f(0.999) = 3.001, f(1.001) = 6.999, f(1.01) = 6.99, and f(1.1) = 6.9. Based on the table, lim as x -> 1 of f(x)", choices=[
   "equals 3", "equals 5", "equals 7", "does not exist"], ans=3,
   why="The left entries head toward 3 and the right entries toward 7, so the two sides disagree."),
 dict(q="A table for a function h gives h(2.1) = 10, h(2.01) = 100, h(2.001) = 1000, and h(2.0001) = 10000. Based on the table, lim as x -> 2^+ of h(x)", choices=[
   "equals 0",
   "equals 10000",
   "does not exist, because the values increase without bound",
   "equals 2"], ans=2,
   why="Each tenfold step toward 2 multiplies the output by 10, with no value being approached."),
 dict(q="A table of values can suggest the value of a limit but cannot establish it, because", choices=[
   "tables are always rounded",
   "a table samples only finitely many inputs, and the function may behave differently at inputs between them",
   "limits are only defined for continuous functions",
   "a table cannot show negative numbers"], ans=1,
   why="Nothing in a finite list of samples rules out different behavior at the uncountably many inputs not listed."),
 dict(q="Values of f(x) = (x^3 - 8)/(x - 2) are given by x = 1.9, 1.99, 1.999, 2.001, 2.01, 2.1 with f(x) = 11.4100, 11.9401, 11.9940, 12.0060, 12.0601, 12.6100. Based on the table, lim as x -> 2 of f(x) is most likely", choices=[
   "2", "8", "12", "the limit does not exist"], ans=2,
   why="The values converge on 12 from both sides."),
 dict(q="Values of f(x) = tan(x)/x are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = 1.003347, 1.000033, 1.000000, 1.000000, 1.000033, 1.003347. Based on the table, lim as x -> 0 of tan(x)/x is most likely", choices=[
   "0", "1", "infinity", "the limit does not exist"], ans=1,
   why="The values descend toward 1 from above on both sides."),
 dict(q="Values of f(x) = (e^x - 1)/x are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = 0.95163, 0.99502, 0.99950, 1.00050, 1.00502, 1.05171. Based on the table, lim as x -> 0 of (e^x - 1)/x is most likely", choices=[
   "0", "1", "e", "the limit does not exist"], ans=1,
   why="The entries approach 1 from below on the left and from above on the right."),
 dict(q="Values of f(x) = (2^x - 1)/x are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = 0.66967, 0.69075, 0.69291, 0.69339, 0.69556, 0.71773. Based on the table, lim as x -> 0 of (2^x - 1)/x is most likely", choices=[
   "0", "about 0.693", "1", "2"], ans=1,
   why="The values close in on 0.693..., which is ln(2)."),
 dict(q="A table lists only inputs larger than 3: f(3.1) = 5.41, f(3.01) = 5.0401, f(3.001) = 5.004001. Which limit does this table estimate?", choices=[
   "lim as x -> 3 of f(x) = 5",
   "lim as x -> 3^+ of f(x) = 5",
   "lim as x -> 3^- of f(x) = 5",
   "lim as x -> 5 of f(x) = 3"], ans=1,
   why="Only inputs to the right of 3 are sampled, so only the right-hand limit is supported."),
 dict(q="A table for f(x) = |x - 5|/(x - 5) gives f(4.9) = -1, f(4.99) = -1, f(4.999) = -1, f(5.001) = 1, f(5.01) = 1, and f(5.1) = 1. Based on the table, lim as x -> 5 of f(x)", choices=[
   "equals -1", "equals 0", "equals 1", "does not exist"], ans=3,
   why="The left entries are all -1 and the right entries all 1, so the one-sided limits differ."),
 dict(q="A table gives f(1.1) = 10, f(1.01) = 100, f(1.001) = 1000 for the function f(x) = 1/(x - 1). Which statement is best supported?", choices=[
   "lim as x -> 1^+ of f(x) = 0",
   "lim as x -> 1^+ of f(x) = 1000",
   "lim as x -> 1^+ of f(x) does not exist, because f increases without bound",
   "lim as x -> 1^+ of f(x) = 1"], ans=2,
   why="The reciprocal of a shrinking positive quantity grows past every bound."),
 dict(q="A table gives f(2.9) = 4.97, f(2.99) = 4.997, f(3.01) = 5.003, and f(3.1) = 5.03, and the function is separately defined so that f(3) = 9. Based on this information, lim as x -> 3 of f(x) is most likely", choices=[
   "3", "5", "7", "9"], ans=1,
   why="The nearby values approach 5, and the value assigned at x = 3 itself has no effect on the limit."),
 dict(q="For f(x) = sin(pi/x), a table gives f(1) = 0, f(0.5) = 0, f(0.1) = 0, f(0.01) = 0, and f(0.001) = 0, which appears to show that lim as x -> 0 of f(x) = 0. Which criticism of that conclusion is correct?", choices=[
   "The table is fine and the limit really is 0",
   "Every sampled input happens to make pi/x an integer multiple of pi, while between those inputs f still reaches 1 and -1, so the limit does not exist",
   "The limit is 1 because sin is bounded by 1",
   "The limit is pi"], ans=1,
   why="The inputs chosen are exactly the zeros of the function, so the table hides an oscillation that never settles."),
 dict(q="Values of f(x) = (sqrt(x + 9) - 3)/x are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = 0.167132, 0.166713, 0.166671, 0.166662, 0.166620, 0.166206. Based on the table, lim as x -> 0 of f(x) is most likely", choices=[
   "0", "1/6", "1/3", "6"], ans=1,
   why="The values close in on 0.1666..., which is 1/6."),
 dict(q="A tank's volume V, in liters, is recorded near time t = 4 seconds: V(3.99) = 20.02, V(3.999) = 20.002, V(4.001) = 19.998, and V(4.01) = 19.98. The table best supports which conclusion?", choices=[
   "lim as t -> 4 of V(t) = 20 liters",
   "V(4) = 0 liters",
   "the limit does not exist",
   "lim as t -> 4 of V(t) = 4 liters"], ans=0,
   why="The recorded volumes close in on 20 liters from both sides of t = 4."),
 dict(q="A table for f gives f(2.99) = 6.98, f(2.999) = 6.998, f(3.001) = 7.002, f(3.01) = 7.02, while a separate note states f(3) = 1. Which statement is correct?", choices=[
   "lim as x -> 3 of f(x) = 1",
   "lim as x -> 3 of f(x) = 7",
   "lim as x -> 3 of f(x) does not exist",
   "lim as x -> 3 of f(x) = 4"], ans=1,
   why="The table shows both sides approaching 7, and the limit does not consult f(3)."),
 dict(q="Which of the following tables gives the strongest evidence that a limit at x = 0 does not exist?", choices=[
   "f(-0.01) = 1.99, f(-0.001) = 1.999, f(0.001) = 2.001, f(0.01) = 2.01",
   "f(-0.01) = -3.02, f(-0.001) = -3.002, f(0.001) = -2.998, f(0.01) = -2.98",
   "f(-0.01) = 4.01, f(-0.001) = 4.001, f(0.001) = -4.001, f(0.01) = -4.01",
   "f(-0.01) = 0.01, f(-0.001) = 0.001, f(0.001) = 0.001, f(0.01) = 0.01"], ans=2,
   why="Only that table has the two sides heading toward different numbers, 4 and -4."),
 dict(q="Values of f(x) = (x - 4)/(sqrt(x) - 2) are given by x = 3.9, 3.99, 3.999, 4.001, 4.01, 4.1 with f(x) = 3.974842, 3.997498, 3.999750, 4.000250, 4.002498, 4.024846. Based on the table, lim as x -> 4 of f(x) is most likely", choices=[
   "0", "2", "4", "the limit does not exist"], ans=2,
   why="The values approach 4 from both sides, matching the simplification sqrt(x) + 2."),
 dict(q="A table gives f(1.99) = -100, f(1.999) = -1000, f(2.001) = 1000, and f(2.01) = 100. Based on the table, lim as x -> 2 of f(x)", choices=[
   "equals 0",
   "equals 1000",
   "does not exist, because f falls without bound on the left and rises without bound on the right",
   "equals -1000"], ans=2,
   why="The two sides run off in opposite directions, so no value is approached."),
 dict(q="A table gives only f(1.99) = 4.9701 and f(2.01) = 5.0301. The best estimate of lim as x -> 2 of f(x) from this table is", choices=[
   "4.9701", "5", "5.0301", "10.0002"], ans=1,
   why="The two entries straddle 5 and lie about equally far from it, so 5 is the natural estimate."),
 dict(q="Values of f(x) = (cos(x) - 1)/x^2 are given by x = -0.1, -0.01, -0.001, 0.001, 0.01, 0.1 with f(x) = -0.499583, -0.499996, -0.500000, -0.500000, -0.499996, -0.499583. Based on the table, lim as x -> 0 of (cos(x) - 1)/x^2 is most likely", choices=[
   "-1", "-1/2", "0", "1/2"], ans=1,
   why="The values close in on -0.5 from both sides."),
]
