# CALC 2.10 Finding the Derivatives of Tangent, Cotangent, Secant, and Cosecant — 25 questions
# Every derivative is confirmed with sp.diff in verify_c2_10.py, which also
# checks that no distractor is equivalent to the key -- a real risk here,
# since sec^2(x) - 1 and tan^2(x) are the same function.
# Questions 5, 15 and 21 are conceptual (deriving tan and sec from the
# quotient rule, and which derivatives carry a minus sign).
TOPIC = ("2.10", "Finding the Derivatives of Tangent, Cotangent, Secant, and Cosecant", 2)
QUESTIONS = [
 dict(q="d/dx[tan(x)] =", choices=[
   "sec^2(x)", "-csc^2(x)", "sec(x) tan(x)", "cot(x)"], ans=0,
   why="Tangent differentiates to secant squared, with no minus sign."),
 dict(q="d/dx[cot(x)] =", choices=[
   "-csc^2(x)", "csc^2(x)", "-sec^2(x)", "-csc(x) cot(x)"], ans=0,
   why="Cotangent is a co-function, so its derivative carries a minus sign: -csc^2(x)."),
 dict(q="d/dx[sec(x)] =", choices=[
   "sec(x) tan(x)", "-sec(x) tan(x)", "sec^2(x)", "csc(x) cot(x)"], ans=0,
   why="The derivative of secant is the product sec(x) tan(x), with no minus sign."),
 dict(q="d/dx[csc(x)] =", choices=[
   "-csc(x) cot(x)", "csc(x) cot(x)", "-csc^2(x)", "-cot(x)"], ans=0,
   why="Cosecant is a co-function, so its derivative is -csc(x) cot(x)."),
 dict(q="Applying the quotient rule to tan(x) = sin(x)/cos(x), the numerator of the result simplifies to", choices=[
   "cos^2(x) + sin^2(x), which is 1",
   "cos^2(x) - sin^2(x)",
   "sin^2(x) - cos^2(x)",
   "2 sin(x) cos(x)"], ans=0,
   why="(cos x)(cos x) - (sin x)(-sin x) = cos^2(x) + sin^2(x) = 1, so the derivative is 1/cos^2(x) = sec^2(x)."),
 dict(q="If f(x) = 3 tan(x), then f'(x) =", choices=[
   "3 sec^2(x)", "3 sec(x) tan(x)", "-3 csc^2(x)", "sec^2(x)"], ans=0,
   why="The constant 3 stays in front of sec^2(x)."),
 dict(q="If f(x) = x tan(x), then f'(x) =", choices=[
   "tan(x) + x sec^2(x)", "sec^2(x)", "tan(x) + sec^2(x)", "x sec^2(x)"], ans=0,
   why="The product rule gives (1)(tan x) + (x)(sec^2 x)."),
 dict(q="If f(x) = x^2 sec(x), then f'(x) =", choices=[
   "2x sec(x) + x^2 sec(x) tan(x)",
   "2x sec(x) tan(x)",
   "2x sec(x) - x^2 sec(x) tan(x)",
   "x^2 sec(x) tan(x)"], ans=0,
   why="The product rule gives (2x)(sec x) + (x^2)(sec x tan x); multiplying the derivatives gives the wrong second choice."),
 dict(q="If f(x) = tan(x), then f'(pi/4) =", choices=[
   "1", "sqrt(2)", "2", "4"], ans=2,
   why="f'(x) = sec^2(x), and sec(pi/4) = sqrt(2), so f'(pi/4) = 2; the value 1 is tan(pi/4)."),
 dict(q="If f(x) = sec(x), then f'(pi/3) =", choices=[
   "sqrt(3)", "2", "2 sqrt(3)", "4"], ans=2,
   why="f'(x) = sec(x) tan(x) = (2)(sqrt 3) = 2 sqrt(3) at x = pi/3."),
 dict(q="If f(x) = csc(x), then f'(pi/2) =", choices=[
   "-1", "0", "1", "2"], ans=1,
   why="f'(x) = -csc(x) cot(x), and cot(pi/2) = 0, so the product is 0."),
 dict(q="If f(x) = cot(x), then f'(pi/4) =", choices=[
   "-2", "-1", "1", "2"], ans=0,
   why="f'(x) = -csc^2(x), and csc(pi/4) = sqrt(2), so f'(pi/4) = -2."),
 dict(q="If f(x) = tan(x) - x, then f'(x) =", choices=[
   "sec^2(x) - 1", "sec^2(x)", "sec^2(x) + 1", "-csc^2(x) - 1"], ans=0,
   why="Differentiate term by term; the result sec^2(x) - 1 is another name for tan^2(x), which is never negative."),
 dict(q="If f(x) = sec(x)/x, then f'(x) =", choices=[
   "(x sec(x) tan(x) - sec(x))/x^2",
   "(sec(x) - x sec(x) tan(x))/x^2",
   "sec(x) tan(x)/x^2",
   "(x sec(x) tan(x) - sec(x))/x"], ans=0,
   why="The quotient rule gives (sec x tan x)(x) - (sec x)(1), all over x^2."),
 dict(q="Among the derivatives of tan(x), cot(x), sec(x) and csc(x), which carry a leading minus sign?", choices=[
   "cot(x) and csc(x)",
   "tan(x) and sec(x)",
   "sec(x) and csc(x)",
   "tan(x) and cot(x)"], ans=0,
   why="The two co-functions, cotangent and cosecant, are the ones whose derivatives are negative; this pattern matches cos(x) as well."),
 dict(q="If f(x) = 5 csc(x), then f'(x) =", choices=[
   "-5 csc(x) cot(x)", "5 csc(x) cot(x)", "-5 csc^2(x)", "-csc(x) cot(x)"], ans=0,
   why="The constant 5 stays in front and the derivative of csc(x) is -csc(x) cot(x)."),
 dict(q="If f(x) = tan(x)/x, then f'(x) =", choices=[
   "(x sec^2(x) - tan(x))/x^2",
   "(tan(x) - x sec^2(x))/x^2",
   "sec^2(x)",
   "(x sec^2(x) - tan(x))/x"], ans=0,
   why="The quotient rule gives (sec^2 x)(x) - (tan x)(1), all over x^2."),
 dict(q="The slope of the line tangent to y = tan(x) at x = 0 is", choices=[
   "-1", "0", "1", "2"], ans=2,
   why="dy/dx = sec^2(x), and sec(0) = 1, so the slope is 1."),
 dict(q="The graph of y = tan(x) has a horizontal tangent line at", choices=[
   "x = 0 only",
   "x = pi/2 only",
   "x = 0 and x = pi",
   "no value of x"], ans=3,
   why="dy/dx = sec^2(x) is at least 1 wherever it is defined, so it is never 0."),
 dict(q="If f(x) = cot(x) + csc(x), then f'(x) =", choices=[
   "-csc^2(x) - csc(x) cot(x)",
   "csc^2(x) + csc(x) cot(x)",
   "-csc^2(x) + csc(x) cot(x)",
   "-sec^2(x) - sec(x) tan(x)"], ans=0,
   why="Both terms are co-functions, so both derivatives are negative."),
 dict(q="Writing sec(x) = 1/cos(x) and applying the quotient rule gives", choices=[
   "sin(x)/cos^2(x), which equals sec(x) tan(x)",
   "-sin(x)/cos^2(x), which equals -sec(x) tan(x)",
   "1/cos^2(x), which equals sec^2(x)",
   "-1/sin(x), which equals -csc(x)"], ans=0,
   why="The numerator is (0)(cos x) - (1)(-sin x) = sin(x), and sin(x)/cos^2(x) factors as (1/cos x)(sin x/cos x)."),
 dict(q="On the interval 0 <= x < pi/2, the line tangent to y = tan(x) has slope 2 at", choices=[
   "x = pi/6", "x = pi/4", "x = pi/3", "x = pi/2"], ans=1,
   why="sec^2(x) = 2 gives cos^2(x) = 1/2, so x = pi/4 on that interval."),
 dict(q="If f(x) = sec(x), then f'(pi/4) =", choices=[
   "1", "sqrt(2)", "2", "2 sqrt(2)"], ans=1,
   why="f'(x) = sec(x) tan(x) = (sqrt 2)(1) = sqrt(2) at x = pi/4."),
 dict(q="If f(x) = x cot(x), then f'(x) =", choices=[
   "cot(x) - x csc^2(x)",
   "cot(x) + x csc^2(x)",
   "-csc^2(x)",
   "cot(x) - csc^2(x)"], ans=0,
   why="The product rule gives (1)(cot x) + (x)(-csc^2 x)."),
 dict(q="If f(x) = sec(x) tan(x), then f'(x) =", choices=[
   "sec(x) tan^2(x) + sec^3(x)",
   "sec^2(x) tan(x)",
   "sec(x) tan^2(x) - sec^3(x)",
   "sec^3(x)"], ans=0,
   why="The product rule gives (sec x tan x)(tan x) + (sec x)(sec^2 x); the second choice multiplies the two derivatives."),
]
