# CALC 6.6 Applying Properties of Definite Integrals — 25 questions
# Answers verified with sympy; see verify_c6_6.py, which realizes each set of
# given integral values with an explicit function whose integrals really are
# those numbers, then computes the requested integral with sp.integrate rather
# than reusing the arithmetic in the rationale.
# Questions 1, 2, 12, 13, 15, 18 are conceptual (statements of the properties).
TOPIC = ("6.6", "Applying Properties of Definite Integrals", 6)
QUESTIONS = [
 dict(q="For any function f that is continuous at a, what is the value of int from a to a of f(x) dx?", choices=[
   "0",
   "f(a)",
   "a",
   "It depends on f."], ans=0,
   why="An interval of zero width accumulates nothing, so the integral is 0 for every integrand."),
 dict(q="For a continuous f, int from b to a of f(x) dx is equal to", choices=[
   "-int from a to b of f(x) dx",
   "int from a to b of f(x) dx",
   "int from a to b of -f(-x) dx",
   "1/(int from a to b of f(x) dx)"], ans=0,
   why="Reversing the limits of integration reverses the sign of the definite integral."),
 dict(q="If int from 0 to 5 of f(x) dx = 8 and int from 5 to 9 of f(x) dx = 3, what is int from 0 to 9 of f(x) dx?", choices=[
   "5",
   "11",
   "24",
   "It cannot be determined."], ans=1,
   why="Integrals add over adjacent intervals: 8 + 3 = 11."),
 dict(q="If int from 0 to 9 of f(x) dx = 11 and int from 0 to 5 of f(x) dx = 8, what is int from 5 to 9 of f(x) dx?", choices=[
   "-3",
   "3",
   "19",
   "88"], ans=1,
   why="Additivity gives int from 5 to 9 = 11 - 8 = 3."),
 dict(q="If int from 1 to 4 of f(x) dx = 6, what is int from 4 to 1 of f(x) dx?", choices=[
   "-6",
   "0",
   "6",
   "1/6"], ans=0,
   why="Swapping the limits changes the sign."),
 dict(q="If int from 2 to 6 of f(x) dx = 5, what is int from 2 to 6 of 3 f(x) dx?", choices=[
   "5/3",
   "8",
   "15",
   "20"], ans=2,
   why="A constant factor may be pulled out of an integral: 3(5) = 15."),
 dict(q="If int from 0 to 4 of f(x) dx = 7 and int from 0 to 4 of g(x) dx = -2, what is int from 0 to 4 of (f(x) + g(x)) dx?", choices=[
   "-14",
   "5",
   "9",
   "It cannot be determined."], ans=1,
   why="The integral of a sum is the sum of the integrals: 7 + (-2) = 5."),
 dict(q="Given int from 0 to 4 of f(x) dx = 7 and int from 0 to 4 of g(x) dx = -2, what is int from 0 to 4 of (2 f(x) - 3 g(x)) dx?", choices=[
   "8",
   "11",
   "20",
   "-42"], ans=2,
   why="Linearity gives 2(7) - 3(-2) = 14 + 6 = 20."),
 dict(q="What is the value of int from 1 to 5 of 4 dx?", choices=[
   "4",
   "9",
   "16",
   "20"], ans=2,
   why="The integral of a constant c over [a, b] is c(b - a) = 4(4) = 16."),
 dict(q="If int from 2 to 5 of f(x) dx = 9, what is int from 2 to 5 of (f(x) + 2) dx?", choices=[
   "11",
   "13",
   "15",
   "18"], ans=2,
   why="The constant contributes 2(5 - 2) = 6, giving 9 + 6 = 15."),
 dict(q="If int from 0 to 3 of f(x) dx = 5 and int from 0 to 7 of f(x) dx = 2, what is int from 3 to 7 of f(x) dx?", choices=[
   "-3",
   "3",
   "7",
   "10"], ans=0,
   why="int from 3 to 7 = int from 0 to 7 - int from 0 to 3 = 2 - 5 = -3."),
 dict(q="Suppose f(x) <= g(x) for every x in [a, b], with a < b. Which statement must be true?", choices=[
   "int from a to b of f(x) dx <= int from a to b of g(x) dx",
   "int from a to b of f(x) dx >= int from a to b of g(x) dx",
   "int from a to b of f(x) dx = int from a to b of g(x) dx",
   "Nothing can be concluded without knowing the signs of f and g."], ans=0,
   why="The comparison property preserves the inequality when both integrals run over the same interval in the same direction."),
 dict(q="If f(x) >= 0 for every x in [a, b] with a < b, then int from a to b of f(x) dx", choices=[
   "is greater than or equal to 0",
   "is strictly positive",
   "is less than or equal to 0",
   "may have either sign"], ans=0,
   why="Non-negative area gives a non-negative integral; it is 0 exactly when f is 0 throughout, so strict positivity is not guaranteed."),
 dict(q="What is the value of int from -2 to 2 of x^3 dx?", choices=[
   "-8",
   "0",
   "4",
   "8"], ans=1,
   why="The integrand is odd, so the area below the axis on [-2, 0] cancels the equal area above it on [0, 2]."),
 dict(q="If f is an even function and int from 0 to a of f(x) dx = k, then int from -a to a of f(x) dx equals", choices=[
   "2k",
   "0",
   "k",
   "-k"], ans=0,
   why="An even integrand contributes equal amounts on the two halves of a symmetric interval."),
 dict(q="If 2 <= f(x) <= 5 for every x in [1, 7], which inequality must hold for I = int from 1 to 7 of f(x) dx?", choices=[
   "2 <= I <= 5",
   "12 <= I <= 30",
   "14 <= I <= 35",
   "0 <= I <= 30"], ans=1,
   why="Bounding the integrand bounds the integral by those constants times the width 6, giving 12 and 30."),
 dict(q="If int from 0 to 6 of f(x) dx = 10, what is int from 0 to 6 of (f(x)/2) dx?", choices=[
   "2",
   "5",
   "10",
   "20"], ans=1,
   why="Dividing the integrand by 2 divides the integral by 2."),
 dict(q="Which statement about definite integrals is FALSE?", choices=[
   "The integral of a sum is the sum of the integrals.",
   "A constant multiple may be moved outside the integral.",
   "The integral of a product is the product of the integrals.",
   "Integrals over adjacent intervals add."], ans=2,
   why="There is no product rule for integrals; int of f times g is generally not the product of the two integrals."),
 dict(q="If int from 1 to 3 of f(x) dx = 4 and int from 3 to 8 of f(x) dx = 6, what is int from 8 to 1 of f(x) dx?", choices=[
   "-10",
   "-2",
   "2",
   "10"], ans=0,
   why="int from 1 to 8 = 4 + 6 = 10, and reversing the limits negates it."),
 dict(q="What is the value of int from 5 to 5 of (x^3 + 2x) dx?", choices=[
   "0",
   "135",
   "150",
   "175"], ans=0,
   why="The limits are equal, so the integral is 0 no matter how complicated the integrand looks."),
 dict(q="Suppose int from 0 to 2 of f(x) dx = 3 and int from 0 to 6 of f(x) dx = 7. What is int from 6 to 2 of f(x) dx?", choices=[
   "-10",
   "-4",
   "4",
   "10"], ans=1,
   why="int from 2 to 6 = 7 - 3 = 4, and reversing the limits gives -4."),
 dict(q="What is the value of int from -3 to 3 of (x^3 + 4) dx?", choices=[
   "0",
   "12",
   "24",
   "51"], ans=2,
   why="The odd term integrates to 0 over the symmetric interval and the constant contributes 4(6) = 24."),
 dict(q="If int from 1 to 4 of f(x) dx = 5, what is int from 1 to 4 of (2 f(x) - 1) dx?", choices=[
   "4",
   "7",
   "9",
   "10"], ans=1,
   why="Linearity gives 2(5) minus 1(4 - 1) = 10 - 3 = 7."),
 dict(q="Given only that int from 0 to 4 of f(x) dx = 9 and int from 0 to 4 of g(x) dx = 4, which quantity CANNOT be determined?", choices=[
   "int from 0 to 4 of (f(x) - g(x)) dx",
   "int from 0 to 4 of 5 f(x) dx",
   "int from 0 to 4 of f(x) g(x) dx",
   "int from 4 to 0 of g(x) dx"], ans=2,
   why="Linearity handles sums, differences, constant multiples, and reversed limits, but the integral of a product is not determined by the two separate integrals."),
 dict(q="Suppose 0 <= f(x) <= 3 for every x in [0, 4]. Which value is impossible for int from 0 to 4 of f(x) dx?", choices=[
   "0",
   "5",
   "12",
   "15"], ans=3,
   why="The integral is at most 3(4) = 12, so 15 cannot occur, while 0, 5, and 12 are all attainable."),
]
