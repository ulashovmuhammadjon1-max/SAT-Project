# CALC 10.12 Lagrange Error Bound — 25 questions
# Answers verified with sympy; see verify_c10_12.py
# |f(x) - P_n(x)| <= M*|x - a|^(n+1)/(n+1)!, where M is a bound on the
# (n+1)st derivative between a and x.  Note the (n+1) three times: the
# derivative order, the power, and the factorial.  Two items contrast this with
# the alternating series bound of 10.10, which uses the first omitted term.
TOPIC = ("10.12", "Lagrange Error Bound", 10)
QUESTIONS = [
 dict(q="If P_n is the nth-degree Taylor polynomial for f about x = a, the Lagrange error bound states that |f(x) - P_n(x)| is at most", choices=[
   "M*|x - a|^(n+1)/(n+1)!",
   "M*|x - a|^n/n!",
   "M*|x - a|^(n+1)/n!",
   "M*|x - a|^n/(n+1)!"], ans=0,
   why="The power, the factorial, and the derivative order are all n + 1."),

 dict(q="In the Lagrange error bound, the constant M must be", choices=[
   "the maximum of |f| on the interval between a and x",
   "the maximum of |f^(n)| on the interval between a and x",
   "the maximum of |f^(n+1)| on the interval between a and x",
   "the value f^(n+1)(a)"], ans=2,
   why="The bound uses an upper bound for the next derivative after the last one the polynomial used."),

 dict(q="The Lagrange form of the remainder states that for some c between a and x,", choices=[
   "R_n(x) = f^(n+1)(c)*(x - a)^(n+1)/(n+1)!",
   "R_n(x) = f^(n)(c)*(x - a)^n/n!",
   "R_n(x) = f^(n+1)(a)*(x - a)^(n+1)/(n+1)!",
   "R_n(x) = f(c)*(x - a)^(n+1)/(n+1)!"], ans=0,
   why="The remainder is one more Taylor term with the derivative evaluated at an unknown interior point c."),

 dict(q="For f(x) = e^x and its third-degree Maclaurin polynomial, the Lagrange error bound on the interval |x| <= 1 is", choices=[
   "1/24",
   "e/6",
   "e/24",
   "e/120"], ans=2,
   why="The fourth derivative is e^x, at most e on [-1, 1], so the bound is e*1^4/4! = e/24."),

 dict(q="For f(x) = sin(x) and its third-degree Maclaurin polynomial, using M = 1 as a bound on the fourth derivative, the Lagrange error bound for |x| <= 0.5 is", choices=[
   "1/3840",
   "1/384",
   "1/96",
   "1/24"], ans=1,
   why="Every derivative of sin is bounded by 1, so the bound is 1*(0.5)^4/4! = 1/384."),

 dict(q="For f(x) = cos(x) and its second-degree Maclaurin polynomial, using M = 1 as a bound on the third derivative, the Lagrange error bound at x = 0.1 is", choices=[
   "1/60000",
   "1/6000",
   "1/600",
   "1/60"], ans=1,
   why="The third derivative is sin(x), bounded by 1, so the bound is 1*(0.1)^3/3! = 0.001/6 = 1/6000."),

 dict(q="Suppose |f^(4)(x)| <= 10 for all x in [1, 2]. The Lagrange error bound for the third-degree Taylor polynomial about x = 1, evaluated at x = 2, is", choices=[
   "5/12",
   "10/6",
   "5/6",
   "10"], ans=0,
   why="The bound is 10*|2 - 1|^4/4! = 10/24 = 5/12."),

 dict(q="Suppose |f^(5)(x)| <= 24 on the relevant interval. The Lagrange error bound for the fourth-degree Taylor polynomial at a point with |x - a| = 1/2 is", choices=[
   "1/160",
   "1/80",
   "1/40",
   "1/5"], ans=0,
   why="The bound is 24*(1/2)^5/5! = 24/(32*120) = 1/160."),

 dict(q="To bound the error of the fifth-degree Taylor polynomial, the Lagrange bound requires an upper bound on", choices=[
   "|f^(5)|",
   "|f^(6)|",
   "|f^(4)|",
   "|f|"], ans=1,
   why="The bound always uses the derivative of order one more than the degree of the polynomial."),

 dict(q="A student bounds the error of P_3 using the maximum of |f'''| instead of |f^(4)|. This is", choices=[
   "correct, since f''' is the last derivative used",
   "incorrect; the bound requires the fourth derivative",
   "correct, since the two maxima are always equal",
   "incorrect only when f is not a polynomial"], ans=1,
   why="The remainder term is the next term in the series, so it involves the fourth derivative, not the third."),

 dict(q="For f(x) = e^x and its second-degree Maclaurin polynomial, the Lagrange error bound at x = 0.5 is", choices=[
   "e^(1/2)/6",
   "e^(1/2)/48",
   "1/48",
   "e^(1/2)/16"], ans=1,
   why="M = e^(1/2) on [0, 0.5], and the bound is M*(0.5)^3/3! = e^(1/2)/48."),

 dict(q="For f(x) = ln(1 + x) and its second-degree Maclaurin polynomial, the Lagrange error bound at x = 0.1 is", choices=[
   "1/30000",
   "1/6000",
   "1/3000",
   "1/300"], ans=2,
   why="f'''(x) = 2/(1+x)^3 is at most 2 on [0, 0.1], so the bound is 2*(0.1)^3/3! = 1/3000."),

 dict(q="The smallest degree n for which the Lagrange bound guarantees that P_n approximates e^x to within 0.001 on the interval |x| <= 1 is", choices=[
   "4",
   "5",
   "6",
   "7"], ans=2,
   why="The bound is e/(n+1)!, and (n+1)! > 1000e = 2718 first holds at (n+1)! = 5040, so n + 1 = 7 and n = 6."),

 dict(q="To bound the error in approximating a function by a Taylor polynomial when nothing is known about the signs of the terms, the appropriate tool is", choices=[
   "the alternating series error bound",
   "the Lagrange error bound",
   "the integral test remainder bound",
   "the ratio test"], ans=1,
   why="The alternating series bound needs an alternating series satisfying that test; the Lagrange bound needs only a bound on the next derivative."),

 dict(q="For f(x) = sin(x) and its fifth-degree Maclaurin polynomial, using M = 1 as a bound on the sixth derivative, the Lagrange error bound for |x| <= pi/2 is", choices=[
   "(pi/2)^6/720",
   "(pi/2)^5/120",
   "(pi/2)^6/120",
   "(pi/2)^7/5040"], ans=0,
   why="M = 1 and n = 5, so the bound is 1*(pi/2)^6/6! = (pi/2)^6/720."),

 dict(q="Suppose every derivative of f satisfies |f^(k)(x)| <= 3 on [0, 2]. The Lagrange error bound for the fourth-degree Maclaurin polynomial at x = 2 is", choices=[
   "2/5",
   "4/5",
   "8/5",
   "3"], ans=1,
   why="The bound is 3*2^5/5! = 96/120 = 4/5."),

 dict(q="As n increases with x and a fixed and M unchanged, the Lagrange error bound tends to 0 because", choices=[
   "|x - a|^(n+1) tends to 0",
   "(n+1)! grows faster than |x - a|^(n+1)",
   "M tends to 0",
   "the Taylor polynomial tends to 0"], ans=1,
   why="Factorial growth outpaces any fixed base raised to the nth power, which is why Taylor series converge for such functions."),

 dict(q="The Lagrange error bound gives", choices=[
   "the exact error |f(x) - P_n(x)|",
   "an upper bound for |f(x) - P_n(x)|, usually larger than the true error",
   "a lower bound for |f(x) - P_n(x)|",
   "the error only when f is a polynomial"], ans=1,
   why="It replaces the unknown f^(n+1)(c) by its maximum, so the result is an overestimate of the error."),

 dict(q="For f(x) = 1/x and its second-degree Taylor polynomial about x = 1, the Lagrange error bound on the interval [1, 1.5] is", choices=[
   "1/16",
   "1/8",
   "1/4",
   "3/4"], ans=1,
   why="f'''(x) = -6/x^4 has |f'''| at most 6 on [1, 1.5], so the bound is 6*(0.5)^3/3! = 1/8."),

 dict(q="For f(x) = e^x and its first-degree Maclaurin polynomial at x = 0.2, using M = 2 as a bound for the second derivative, the Lagrange error bound is", choices=[
   "0.02",
   "0.04",
   "0.2",
   "0.4"], ans=1,
   why="The bound is 2*(0.2)^2/2! = 2(0.04)/2 = 0.04."),

 dict(q="For f(x) = cos(x) and its fourth-degree Maclaurin polynomial, using M = 1 as a bound on the fifth derivative, the Lagrange error bound for |x| <= 1 is", choices=[
   "1/720",
   "1/120",
   "1/24",
   "1/5"], ans=1,
   why="The fifth derivative of cos is -sin, bounded by 1, so the bound is 1*1^5/5! = 1/120."),

 dict(q="Which error bound uses the maximum of the (n+1)st derivative?", choices=[
   "The alternating series error bound",
   "The Lagrange error bound",
   "Both bounds use it",
   "Neither bound uses derivatives"], ans=1,
   why="The alternating series bound uses only the first omitted term of the series, with no derivatives at all."),

 dict(q="For f(x) = e^x and its second-degree Maclaurin polynomial at x = 1, the Lagrange bound is e/6, about 0.453, while the true error e - 2.5 is about 0.218. This illustrates that", choices=[
   "the bound was computed incorrectly",
   "the true error is at most the bound, and often well below it",
   "the true error should equal the bound",
   "the bound applies only for |x| < 1"], ans=1,
   why="Replacing f'''(c) by its maximum on the interval makes the bound larger than the actual error."),

 dict(q="For f(x) = sin(x) or f(x) = cos(x), the value M = 1 always works in the Lagrange bound because", choices=[
   "these functions are periodic",
   "every derivative of sin or cos is +/- sin or +/- cos, and all of those are bounded by 1 in absolute value",
   "their Maclaurin series have alternating signs",
   "their Taylor polynomials have degree at most 5"], ans=1,
   why="Differentiating cycles among sin, cos and their negatives, none of which exceeds 1 in absolute value."),

 dict(q="If |f^(n+1)(x)| <= M for every n on an interval containing a and x, then as n increases the Lagrange bound shows that", choices=[
   "P_n(x) approaches f(x)",
   "P_n(x) approaches 0",
   "the error approaches M",
   "nothing can be concluded"], ans=0,
   why="The bound M*|x-a|^(n+1)/(n+1)! approaches 0, so the Taylor polynomials converge to f(x)."),
]
