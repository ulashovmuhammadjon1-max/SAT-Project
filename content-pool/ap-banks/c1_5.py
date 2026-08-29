# CALC 1.5 Determining Limits Using Algebraic Properties of Limits — 25 questions
# Answers verified with sympy; see verify_c1_5.py.  The "given limits" items are
# checked by building concrete functions with the stated limits and applying the
# law to them, so the arithmetic of each law is confirmed rather than asserted.
# Questions 6, 9, 19, 22 and 25 are conceptual (when a law applies, what it does
# not tell you, and naming the law) and carry no sympy check.
#
# Stems lead with the expression being asked about rather than with the shared
# "suppose lim f = 5 and lim g = -2" preamble, so that no two stems share their
# opening 90 characters.
TOPIC = ("1.5", "Determining Limits Using Algebraic Properties of Limits", 1)
QUESTIONS = [
 dict(q="Given that lim as x -> a of f(x) = 5 and lim as x -> a of g(x) = -2, the value of lim as x -> a of (f(x) + g(x)) is", choices=[
   "-10", "-7", "3", "7"], ans=2,
   why="The limit of a sum is the sum of the limits: 5 + (-2) = 3."),
 dict(q="The value of lim as x -> a of (f(x) * g(x)), when lim as x -> a of f(x) = 5 and lim as x -> a of g(x) = -2, is", choices=[
   "-10", "-2.5", "3", "10"], ans=0,
   why="The limit of a product is the product of the limits: 5(-2) = -10."),
 dict(q="Evaluate lim as x -> a of (f(x)/g(x)) if lim as x -> a of f(x) = 5 and lim as x -> a of g(x) = -2.", choices=[
   "-5/2", "-2/5", "2/5", "5/2"], ans=0,
   why="The limit of a quotient is the quotient of the limits when the denominator's limit is not 0: 5/(-2) = -5/2."),
 dict(q="For functions with lim as x -> a of f(x) = 5 and lim as x -> a of g(x) = -2, the value of lim as x -> a of (3f(x) - 2g(x)) is", choices=[
   "11", "15", "19", "23"], ans=2,
   why="Constant multiples pull out and the limits subtract: 3(5) - 2(-2) = 15 + 4 = 19."),
 dict(q="If lim as x -> a of f(x) = 5, then lim as x -> a of (f(x))^2 equals", choices=[
   "5", "10", "25", "125"], ans=2,
   why="The power law gives (lim f)^2 = 5^2 = 25."),
 dict(q="The quotient law for limits, lim (f/g) = (lim f)/(lim g), may be applied only when", choices=[
   "f and g are both polynomials",
   "the limit of the denominator g is not 0",
   "the limit of the numerator f is not 0",
   "f and g are both continuous everywhere"], ans=1,
   why="Dividing by a limit of 0 is undefined, so that single condition is what the law requires."),
 dict(q="Suppose lim as x -> a of f(x) = 5. Then lim as x -> a of sqrt(f(x)) equals", choices=[
   "sqrt(5)", "5/2", "5", "25"], ans=0,
   why="The root law moves the square root outside the limit, giving sqrt(5)."),
 dict(q="With lim as x -> a of f(x) = 5 and lim as x -> a of g(x) = -2, the value of lim as x -> a of (g(x)/f(x)) is", choices=[
   "-5/2", "-2/5", "2/5", "5/2"], ans=1,
   why="Here the denominator's limit is 5, which is not 0, so the quotient is -2/5."),
 dict(q="Suppose lim as x -> 2 of f(x) = 4 and lim as x -> 2 of g(x) = 0. What can be concluded about lim as x -> 2 of (f(x)/g(x))?", choices=[
   "It equals 0",
   "It equals 4",
   "The quotient law does not apply, and the limit cannot be determined from the information given",
   "It equals infinity"], ans=2,
   why="With a denominator limit of 0 and a nonzero numerator limit the law is silent, and the behavior depends on how g approaches 0."),
 dict(q="Given lim as x -> 2 of f(x) = 4 and lim as x -> 2 of g(x) = 0, the value of lim as x -> 2 of (g(x)/f(x)) is", choices=[
   "0", "1/4", "4", "undefined"], ans=0,
   why="The denominator's limit is 4, which is not 0, so the quotient law gives 0/4 = 0."),
 dict(q="The value of lim as x -> a of (-4f(x)), when lim as x -> a of f(x) = 5, is", choices=[
   "-20", "-4", "1", "20"], ans=0,
   why="A constant multiple factors out of the limit: -4(5) = -20."),
 dict(q="If lim as x -> a of f(x) = 5, the value of lim as x -> a of (f(x) + 3) is", choices=[
   "3", "5", "8", "15"], ans=2,
   why="The limit of the constant 3 is 3, and the sum law gives 5 + 3 = 8."),
 dict(q="For a function with lim as x -> a of f(x) = 5, the value of lim as x -> a of (f(x))^3 is", choices=[
   "15", "25", "75", "125"], ans=3,
   why="The power law gives 5^3 = 125."),
 dict(q="Evaluate lim as x -> 3 of (2x^2 - 5x + 1).", choices=[
   "-2", "4", "13", "18"], ans=1,
   why="A polynomial's limit is found by substitution: 18 - 15 + 1 = 4."),
 dict(q="Evaluate lim as x -> 1 of (x^2 + 3)/(x + 1).", choices=[
   "1", "2", "4", "the limit does not exist"], ans=1,
   why="The denominator's limit is 2, which is not 0, so the quotient law gives 4/2 = 2."),
 dict(q="Evaluate lim as x -> 4 of sqrt(2x + 1).", choices=[
   "3", "4.5", "9", "sqrt(2)"], ans=0,
   why="The root law and substitution give sqrt(9) = 3."),
 dict(q="Evaluate lim as x -> 0 of (3cos(x) + 2).", choices=[
   "0", "2", "3", "5"], ans=3,
   why="cos(0) = 1, so the expression approaches 3(1) + 2 = 5."),
 dict(q="Suppose lim as x -> 2 of g(x) = 3 and f is a function that is continuous at 3 with f(3) = 7. Then lim as x -> 2 of f(g(x)) equals", choices=[
   "2", "3", "7", "the limit does not exist"], ans=2,
   why="Continuity of the outer function lets the limit move inside: f(lim g) = f(3) = 7."),
 dict(q="Writing lim as x -> a of (f(x)g(x)) as (lim as x -> a of f(x))(lim as x -> a of g(x)) uses which limit law?", choices=[
   "the sum law", "the product law", "the quotient law", "the root law"], ans=1,
   why="Splitting a limit of a product into a product of limits is exactly the product law."),
 dict(q="It is known that lim as x -> 1 of (f(x)/g(x)) = 3 and lim as x -> 1 of g(x) = 4. The value of lim as x -> 1 of f(x) is", choices=[
   "3/4", "4/3", "7", "12"], ans=3,
   why="Since f = (f/g)g away from any zero of g, the product law gives 3(4) = 12."),
 dict(q="It is known that lim as x -> 2 of (f(x) + g(x)) = 7 and lim as x -> 2 of f(x) = 3. The value of lim as x -> 2 of g(x) is", choices=[
   "-4", "3", "4", "10"], ans=2,
   why="Writing g = (f + g) - f and using the difference law gives 7 - 3 = 4."),
 dict(q="Suppose neither lim as x -> 0 of f(x) nor lim as x -> 0 of g(x) exists. What can be said about lim as x -> 0 of (f(x) + g(x))?", choices=[
   "It certainly does not exist",
   "It certainly exists",
   "It may exist or may fail to exist, depending on f and g",
   "It equals 0"], ans=2,
   why="Taking f(x) = |x|/x and g(x) = -|x|/x gives a sum that is identically 0, while f(x) = g(x) = |x|/x gives a sum with no limit."),
 dict(q="It is known that lim as x -> 2 of (f(x)g(x)) = 0 and lim as x -> 2 of f(x) = 3. The value of lim as x -> 2 of g(x) is", choices=[
   "0", "1/3", "3", "it cannot be determined"], ans=0,
   why="Writing g = (fg)/f and using the quotient law, valid since the limit of f is 3 and not 0, gives 0/3 = 0."),
 dict(q="If lim as x -> a of f(x) = 8, then lim as x -> a of (f(x))^(1/3) equals", choices=[
   "2", "8/3", "4", "24"], ans=0,
   why="The root law gives the cube root of 8, which is 2."),
 dict(q="Direct application of the quotient law to lim as x -> 3 of (x^2 - 9)/(x - 3) fails because", choices=[
   "the numerator's limit is not 0",
   "the denominator's limit is 0, so the law does not apply and the expression must be simplified first",
   "the expression is not a rational function",
   "the limit is infinite"], ans=1,
   why="Both parts approach 0, giving the indeterminate form 0/0, and cancelling the factor x - 3 first shows the limit is 6."),
]
