# CALC 4.7 Using L'Hospital's Rule for Determining Limits of Indeterminate Forms — 25 questions
# Every limit below is computed independently by sympy in verify_c4_7.py, including the
# limits in the questions where L'Hospital's Rule does NOT apply: for those the true
# limit is confirmed and the value the rule would wrongly produce is confirmed to differ.
TOPIC = ("4.7", "Using L'Hospital's Rule for Determining Limits of Indeterminate Forms", 4)
QUESTIONS = [
 dict(q="L'Hospital's Rule may be applied to lim f(x)/g(x) only when the limit has the indeterminate form",
   choices=[
     "0/0 or infinity/infinity",
     "0/0 or 1/0",
     "any form in which the denominator approaches 0",
     "any form in which f and g are both differentiable"], ans=0,
   why="Those two quotient forms are the only ones the rule covers directly; other indeterminate forms must first be rewritten as one of them."),

 dict(q="Suppose lim as x -> a of f(x)/g(x) has the form 0/0. L'Hospital's Rule concludes that this limit equals lim as x -> a of f'(x)/g'(x)",
   choices=[
     "provided that second limit exists or is infinite",
     "in every case, without further conditions",
     "provided f and g are continuous at a",
     "provided f'(a) and g'(a) are both nonzero"], ans=0,
   why="If the limit of f'/g' fails to exist, the rule draws no conclusion at all, and the original limit may still exist."),

 dict(q="To apply L'Hospital's Rule to lim as x -> 0 of (e^x - 1)/x, one should compute",
   choices=[
     "lim as x -> 0 of e^x/1, which is 1",
     "the derivative of the whole quotient using the quotient rule",
     "lim as x -> 0 of (e^x - 1)'/x, which is 0",
     "lim as x -> 0 of e^x*x, which is 0"], ans=0,
   why="The rule differentiates the numerator and denominator separately, never as a quotient; both derivatives give e^x over 1."),

 dict(q="Consider lim as x -> 0 of (x + 2)/x. Which statement is correct?",
   choices=[
     "L'Hospital's Rule does not apply, and the limit does not exist because the quotient is unbounded",
     "By L'Hospital's Rule the limit is 1",
     "By L'Hospital's Rule the limit is 2",
     "The limit is 0 because the numerator is finite"], ans=0,
   why="The form is 2/0, not 0/0 or infinity/infinity, so the rule is not available; the one-sided limits are +infinity and -infinity."),

 dict(q="A student writes lim as x -> 0 of (cos(x))/(x + 1) = lim as x -> 0 of (-sin(x))/1 = 0. What is wrong?",
   choices=[
     "The original form is 1/1, not indeterminate, so the rule does not apply and the limit is 1",
     "Nothing; the answer 0 is correct",
     "The derivative of cos(x) is sin(x), so the answer should be 0 with the opposite sign",
     "The rule applies but requires a second application"], ans=0,
   why="Substituting x = 0 gives 1/1 directly, and applying L'Hospital to a determinate form produces a wrong answer, here 0 instead of 1."),

 dict(q="Consider lim as x -> infinity of (x + sin(x))/x. Which statement is correct?",
   choices=[
     "The limit is 1, even though L'Hospital's Rule is inconclusive because lim (1 + cos(x))/1 does not exist",
     "The limit does not exist, because lim (1 + cos(x))/1 does not exist",
     "The limit is 0 by L'Hospital's Rule",
     "The limit is 2 by L'Hospital's Rule"], ans=0,
   why="Writing the quotient as 1 + sin(x)/x shows the limit is 1; the failure of lim f'/g' to exist means the rule says nothing, not that the limit fails to exist."),

 dict(q="lim as x -> 1 of (x^2 - 1)/(x - 1) is",
   choices=[
     "2",
     "0",
     "1",
     "the limit does not exist"], ans=0,
   why="The form is 0/0, and L'Hospital gives lim 2x/1 = 2, which agrees with factoring the numerator as (x - 1)(x + 1)."),

 dict(q="lim as x -> 0 of sin(3x)/x is",
   choices=[
     "3",
     "1",
     "1/3",
     "0"], ans=0,
   why="The form is 0/0 and L'Hospital gives lim 3cos(3x)/1 = 3; forgetting the chain rule's factor of 3 gives 1."),

 dict(q="lim as x -> 0 of (1 - cos(x))/x^2 is",
   choices=[
     "1/2",
     "0",
     "1",
     "the limit does not exist"], ans=0,
   why="Two applications give lim sin(x)/(2x) and then lim cos(x)/2 = 1/2."),

 dict(q="lim as x -> 0 of (1 - cos(x))/x is",
   choices=[
     "0",
     "1/2",
     "1",
     "the limit does not exist"], ans=0,
   why="One application gives lim sin(x)/1 = 0; the answer 1/2 belongs to the same numerator over x^2, a distinction students often blur."),

 dict(q="lim as x -> 0 of (e^(2x) - 1)/sin(3x) is",
   choices=[
     "2/3",
     "3/2",
     "1",
     "0"], ans=0,
   why="The form is 0/0, and L'Hospital gives lim 2e^(2x)/(3cos(3x)) = 2/3."),

 dict(q="lim as x -> infinity of (3x^2 + 5x)/(2x^2 - x) is",
   choices=[
     "3/2",
     "0",
     "infinity",
     "-5"], ans=0,
   why="The form is infinity/infinity, and two applications give lim 6/4 = 3/2, the ratio of the leading coefficients; -5 is the ratio of the linear coefficients, which does not govern the limit."),

 dict(q="lim as x -> infinity of ln(x)/x is",
   choices=[
     "0",
     "1",
     "infinity",
     "the limit does not exist"], ans=0,
   why="The form is infinity/infinity, and L'Hospital gives lim (1/x)/1 = 0, so x grows faster than ln(x)."),

 dict(q="lim as x -> infinity of x/e^x is",
   choices=[
     "0",
     "1",
     "infinity",
     "the limit does not exist"], ans=0,
   why="One application gives lim 1/e^x = 0, since the exponential outgrows any linear function."),

 dict(q="lim as x -> infinity of e^x/x^3 is",
   choices=[
     "infinity",
     "0",
     "1",
     "1/6"], ans=0,
   why="Three applications give lim e^x/6, which grows without bound, so the exponential dominates the cubic."),

 dict(q="lim as x -> 2 of (x^2 - 4)/(x^2 + x - 6) is",
   choices=[
     "4/5",
     "5/4",
     "1",
     "0"], ans=0,
   why="The form is 0/0 and L'Hospital gives lim 2x/(2x + 1) = 4/5."),

 dict(q="lim as x -> infinity of (2x + 1)/sqrt(x^2 + 3) is",
   choices=[
     "2",
     "1",
     "infinity",
     "0"], ans=0,
   why="The form is infinity/infinity, and applying the rule gives lim 2*sqrt(x^2 + 3)/x = 2, the same answer as dividing through by x."),

 dict(q="lim as x -> 0 from the right of x*ln(x) is",
   choices=[
     "0",
     "-infinity",
     "1",
     "the limit does not exist"], ans=0,
   why="The form 0 times -infinity must be rewritten as ln(x)/(1/x), which is -infinity/infinity, and then L'Hospital gives lim (1/x)/(-1/x^2) = lim (-x) = 0."),

 dict(q="lim as x -> infinity of x*sin(1/x) is",
   choices=[
     "1",
     "0",
     "infinity",
     "the limit does not exist"], ans=0,
   why="Rewriting as sin(1/x)/(1/x) gives the form 0/0, and L'Hospital gives lim cos(1/x) = 1."),

 dict(q="lim as x -> 0 of (tan(x) - x)/x^3 is",
   choices=[
     "1/3",
     "0",
     "1",
     "infinity"], ans=0,
   why="Three applications of the rule, starting from lim (sec^2(x) - 1)/(3x^2), give 1/3."),

 dict(q="lim as x -> 0 of (e^x - 1 - x)/x^2 is",
   choices=[
     "1/2",
     "0",
     "1",
     "2"], ans=0,
   why="Two applications give lim (e^x - 1)/(2x) and then lim e^x/2 = 1/2."),

 dict(q="lim as x -> 0 from the right of sin(x)/x^2 is",
   choices=[
     "infinity",
     "1",
     "0",
     "1/2"], ans=0,
   why="The form is 0/0 and the rule does apply, but it yields lim cos(x)/(2x), which grows without bound; a legitimate application can still produce an infinite limit."),

 dict(q="A student tries L'Hospital's Rule on lim as x -> infinity of x/sqrt(x^2 + 1) and finds that each application returns to a quotient of the same type. The correct conclusion is",
   choices=[
     "the limit is 1, found by dividing numerator and denominator by x, since the rule cycles without resolving",
     "the limit does not exist, since the rule never terminates",
     "the limit is 0",
     "the limit is infinity"], ans=0,
   why="Repeated application swaps the two expressions endlessly, so the rule never settles the question, while dividing by x gives 1/sqrt(1 + 1/x^2), which tends to 1."),

 dict(q="lim as x -> infinity of (ln(x))^2/x is",
   choices=[
     "0",
     "1",
     "2",
     "infinity"], ans=0,
   why="One application gives lim 2ln(x)/x, and a second gives lim 2/x = 0."),

 dict(q="lim as x -> 0 of x^2/sin(x) is",
   choices=[
     "0",
     "1",
     "infinity",
     "the limit does not exist"], ans=0,
   why="The form is 0/0, and L'Hospital gives lim 2x/cos(x) = 0/1 = 0."),
]
