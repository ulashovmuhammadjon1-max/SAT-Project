# CALC 3.5 Selecting Procedures for Calculating Derivatives — 25 questions
# Every derivative is confirmed with sp.diff in verify_c3_5.py, which also
# checks that no distractor is equivalent to the key. The point of this topic
# is choosing the procedure, so several questions are faster to do by
# rewriting than by grinding the quotient or product rule.
# Questions 1, 2, 3 and 25 are conceptual (identifying which rules apply).
TOPIC = ("3.5", "Selecting Procedures for Calculating Derivatives", 3)
QUESTIONS = [
 dict(q="Which rule or rules are needed to differentiate y = x^2 sin(3x)?", choices=[
   "the product rule, with the chain rule inside it",
   "the chain rule only",
   "the product rule only",
   "the quotient rule"], ans=0,
   why="It is a product of two factors, and the second factor sin(3x) is itself a composite."),
 dict(q="Which rule or rules are needed to differentiate y = sin(x^2 + 1)?", choices=[
   "the chain rule only",
   "the product rule only",
   "the product rule, with the chain rule inside it",
   "the quotient rule"], ans=0,
   why="It is a single composite function, with no product or quotient anywhere."),
 dict(q="Which rule is the natural choice for y = (x^2 + 1)/(x - 3)?", choices=[
   "the quotient rule",
   "the product rule",
   "the chain rule",
   "the power rule alone, after cancelling"], ans=0,
   why="The numerator does not factor to cancel the denominator, so the quotient rule is the direct route."),
 dict(q="If f(x) = x^2 sin(3x), then f'(x) =", choices=[
   "2x sin(3x) + 3x^2 cos(3x)",
   "2x sin(3x) + x^2 cos(3x)",
   "6x cos(3x)",
   "2x cos(3x)"], ans=0,
   why="The product rule gives 2x sin(3x) + x^2 cos(3x)(3); the second choice forgets the inner derivative 3."),
 dict(q="If f(x) = e^(2x) cos(x), then f'(x) =", choices=[
   "e^(2x)(2 cos(x) - sin(x))",
   "e^(2x)(2 cos(x) + sin(x))",
   "e^(2x)(cos(x) - sin(x))",
   "-2 e^(2x) sin(x)"], ans=0,
   why="2e^(2x) cos(x) + e^(2x)(-sin x), and factoring out e^(2x) leaves 2 cos(x) - sin(x)."),
 dict(q="If f(x) = (x^2 + 1)^3 (x - 1), then f'(x) =", choices=[
   "6x(x^2 + 1)^2 (x - 1) + (x^2 + 1)^3",
   "3(x^2 + 1)^2 (x - 1) + (x^2 + 1)^3",
   "6x(x^2 + 1)^2 (x - 1)",
   "6x(x^2 + 1)^2"], ans=0,
   why="The product rule needs the chain rule on the first factor, giving 6x(x^2 + 1)^2 for its derivative."),
 dict(q="If f(x) = sin(x)/e^x, then f'(x) =", choices=[
   "(cos(x) - sin(x))/e^x",
   "(cos(x) + sin(x))/e^x",
   "cos(x)/e^x",
   "(sin(x) - cos(x))/e^x"], ans=0,
   why="Either the quotient rule or rewriting as e^(-x) sin(x) gives e^(-x)(cos x - sin x)."),
 dict(q="If f(x) = ln(x^2 e^x) for x > 0, then f'(x) =", choices=[
   "2/x + 1", "2/x", "1/(x^2 e^x)", "2x + e^x"], ans=0,
   why="Rewrite as 2 ln(x) + x using log rules, which turns a chain-rule problem into two one-line derivatives."),
 dict(q="If f(x) = sqrt(x^2 + 1)/x, then f'(x) =", choices=[
   "-1/(x^2 sqrt(x^2 + 1))",
   "1/(x^2 sqrt(x^2 + 1))",
   "-1/(x sqrt(x^2 + 1))",
   "x/sqrt(x^2 + 1)"], ans=0,
   why="The quotient rule numerator is x^2/sqrt(x^2 + 1) - sqrt(x^2 + 1), which collapses to -1/sqrt(x^2 + 1)."),
 dict(q="If f(x) = x^2 e^(3x), then f'(x) =", choices=[
   "2x e^(3x) + 3x^2 e^(3x)",
   "2x e^(3x) + x^2 e^(3x)",
   "6x e^(3x)",
   "2x e^(3x)"], ans=0,
   why="The product rule plus the chain rule on e^(3x), whose derivative is 3e^(3x)."),
 dict(q="If f(x) = tan(x^2), then f'(x) =", choices=[
   "2x sec^2(x^2)", "sec^2(x^2)", "2x sec^2(x)", "2x tan(x^2) sec(x^2)"], ans=0,
   why="The chain rule alone: sec^2 of the inside, times the inner derivative 2x."),
 dict(q="If f(x) = (ln(x))^3, then f'(x) =", choices=[
   "3(ln(x))^2/x", "3(ln(x))^2", "(ln(x))^3/x", "3(ln(x))^2 ln(x)"], ans=0,
   why="The power rule on the outside gives 3(ln x)^2, times the inner derivative 1/x."),
 dict(q="If f(x) = ln(sin(x)) on an interval where sin(x) > 0, then f'(x) =", choices=[
   "cot(x)", "tan(x)", "1/sin(x)", "-cot(x)"], ans=0,
   why="The chain rule gives cos(x)/sin(x), which is cot(x)."),
 dict(q="If f(x) = x/sin(x), then f'(x) =", choices=[
   "(sin(x) - x cos(x))/sin^2(x)",
   "(x cos(x) - sin(x))/sin^2(x)",
   "(sin(x) - x cos(x))/sin(x)",
   "1/cos(x)"], ans=0,
   why="The quotient rule numerator is (1)(sin x) - (x)(cos x); the second choice reverses it."),
 dict(q="If f(x) = e^x/(x^2 + 1), then f'(x) =", choices=[
   "e^x (x - 1)^2/(x^2 + 1)^2",
   "e^x (x + 1)^2/(x^2 + 1)^2",
   "e^x (x^2 - 2x + 1)/(x^2 + 1)",
   "e^x/(2x)"], ans=0,
   why="The numerator e^x(x^2 + 1) - e^x(2x) factors as e^x(x - 1)^2."),
 dict(q="If f(x) = x sqrt(x^2 + 1), then f'(x) =", choices=[
   "sqrt(x^2 + 1) + x^2/sqrt(x^2 + 1)",
   "sqrt(x^2 + 1) + x/sqrt(x^2 + 1)",
   "sqrt(x^2 + 1) + 2x^2/sqrt(x^2 + 1)",
   "x^2/sqrt(x^2 + 1)"], ans=0,
   why="The product rule gives (1)sqrt(x^2 + 1) + x times x/sqrt(x^2 + 1)."),
 dict(q="If f(x) = sin(cos(x)), then f'(x) =", choices=[
   "-sin(x) cos(cos(x))",
   "cos(cos(x))",
   "sin(x) cos(cos(x))",
   "-cos(sin(x))"], ans=0,
   why="The outer derivative is cos(cos x) and the inner derivative is -sin(x)."),
 dict(q="If f(x) = (x^2 + 1)/(x^2 - 1), then f'(2) =", choices=[
   "8/9", "4/9", "-4/9", "-8/9"], ans=3,
   why="f'(x) = -4x/(x^2 - 1)^2, so f'(2) = -8/9."),
 dict(q="If f(x) = (x^3 - x)/x for x not 0, then f'(x) =", choices=[
   "2x", "3x^2 - 1", "(3x^2 - 1)/x", "2x - 1"], ans=0,
   why="Cancel the x first to get x^2 - 1; the quotient rule works too but is far more effort."),
 dict(q="If f(x) = e^(x^2) sin(x), then f'(x) =", choices=[
   "e^(x^2)(2x sin(x) + cos(x))",
   "e^(x^2)(2x sin(x) - cos(x))",
   "e^(x^2)(sin(x) + cos(x))",
   "2x e^(x^2) cos(x)"], ans=0,
   why="The product rule with the chain rule on e^(x^2), whose derivative is 2x e^(x^2)."),
 dict(q="If f(x) = ln((x + 1)/(x - 1)) for x > 1, then f'(x) =", choices=[
   "-2/(x^2 - 1)",
   "2/(x^2 - 1)",
   "1/(x + 1) + 1/(x - 1)",
   "(x - 1)/(x + 1)"], ans=0,
   why="Rewrite as ln(x + 1) - ln(x - 1), so f'(x) = 1/(x + 1) - 1/(x - 1) = -2/(x^2 - 1)."),
 dict(q="If f(x) = sqrt(tan(2x)) on an interval where tan(2x) > 0, then f'(x) =", choices=[
   "sec^2(2x)/sqrt(tan(2x))",
   "sec^2(2x)/(2 sqrt(tan(2x)))",
   "1/(2 sqrt(tan(2x)))",
   "2 sec^2(2x) sqrt(tan(2x))"], ans=0,
   why="Three layers: 1/(2 sqrt(tan 2x)), times sec^2(2x), times 2, and the 2s cancel."),
 dict(q="If f(x) = x^2 ln(3x) for x > 0, then f'(x) =", choices=[
   "2x ln(3x) + x", "2x ln(3x) + 3x", "2x ln(3x)", "2x/(3x)"], ans=0,
   why="The product rule gives 2x ln(3x) + x^2(1/x), since d/dx[ln(3x)] = 1/x."),
 dict(q="If f(x) = (2x + 1)^3 e^(-x), then f'(0) =", choices=[
   "-1", "1", "5", "6"], ans=2,
   why="f'(x) = 6(2x + 1)^2 e^(-x) - (2x + 1)^3 e^(-x), so f'(0) = 6 - 1 = 5."),
 dict(q="What is the most efficient way to differentiate y = ln(x^5) for x > 0?", choices=[
   "Rewrite it as 5 ln(x), so the derivative is 5/x",
   "Apply the chain rule and stop at 5x^4, the derivative of the inside",
   "Use the quotient rule",
   "Use the product rule on ln(x) times x^5"], ans=0,
   why="A log rule turns the composite into a constant multiple; the chain rule also works but must divide by x^5, which is where the second choice stops too early."),
]
