# CALC 1.15 Connecting Limits at Infinity and Horizontal Asymptotes — 25 questions
# Verified with sympy; see verify_c1_15.py.
# Two things this topic exists to catch are both represented more than once:
# sqrt(x^2) equals |x|, not x, so the limit of sqrt(x^2 + 1)/x is 1 going right
# and -1 going left; and a graph may cross a horizontal asymptote, unlike a
# vertical one.
TOPIC = ("1.15", "Connecting Limits at Infinity and Horizontal Asymptotes", 1)
QUESTIONS = [
 dict(q="The statement lim as x -> infinity of f(x) = L means that", choices=[
   "f eventually equals L",
   "the values of f(x) can be made arbitrarily close to L by taking x large enough, and the line y = L is a horizontal asymptote of the graph",
   "f(L) = infinity",
   "f is increasing without bound"], ans=1,
   why="A limit at infinity describes the height the graph settles toward far out to the right, which is exactly a horizontal asymptote."),
 dict(q="For a rational function whose numerator has smaller degree than its denominator, the limit as x approaches infinity is", choices=[
   "0", "1", "the ratio of the leading coefficients", "infinite"], ans=0,
   why="The denominator outgrows the numerator, so the quotient is driven to 0."),
 dict(q="For a rational function whose numerator and denominator have the same degree, the limit as x approaches infinity equals", choices=[
   "0",
   "the ratio of the leading coefficients",
   "the ratio of the constant terms",
   "infinity"], ans=1,
   why="Dividing top and bottom by the common highest power leaves the leading coefficients and terms that vanish."),
 dict(q="For a rational function whose numerator has larger degree than its denominator, what does the graph have as x approaches infinity?", choices=[
   "a horizontal asymptote at y = 0",
   "a horizontal asymptote at the ratio of the leading coefficients",
   "no horizontal asymptote, because the values grow without bound",
   "a vertical asymptote"], ans=2,
   why="The numerator outgrows the denominator, so no finite height is approached."),
 dict(q="Evaluate lim as x -> infinity of (3x + 2)/(5x - 1).", choices=[
   "0", "3/5", "5/3", "infinity"], ans=1,
   why="Dividing by x leaves (3 + 2/x)/(5 - 1/x), which approaches 3/5."),
 dict(q="Evaluate lim as x -> infinity of (2x^2 + 3)/(x^3 - 1).", choices=[
   "0", "2", "2/3", "infinity"], ans=0,
   why="The denominator's degree is larger, so the quotient is driven to 0."),
 dict(q="Evaluate lim as x -> infinity of (x^3 + 1)/(x^2 + 4).", choices=[
   "0", "1", "1/4", "infinity"], ans=3,
   why="The numerator's degree is larger, so the values grow without bound and there is no horizontal asymptote."),
 dict(q="Evaluate lim as x -> -infinity of (4x^2 - x)/(2x^2 + 7).", choices=[
   "-2", "0", "2", "-infinity"], ans=2,
   why="Equal degrees give the ratio of leading coefficients, 4/2 = 2, in either direction."),
 dict(q="What is the horizontal asymptote of the graph of f(x) = (6x - 1)/(3x + 5)?", choices=[
   "y = 0", "y = 1/5", "y = 2", "there is none"], ans=2,
   why="Equal degrees give the ratio of leading coefficients, 6/3 = 2."),
 dict(q="What is the horizontal asymptote of the graph of f(x) = (x^2 + 1)/(x^2 - 4)?", choices=[
   "y = 0", "y = 1", "y = -1/4", "there is none"], ans=1,
   why="Equal degrees give 1/1 = 1; the zeros of the denominator produce vertical, not horizontal, asymptotes."),
 dict(q="Evaluate lim as x -> infinity of 1/x.", choices=[
   "-1", "0", "1", "infinity"], ans=1,
   why="The reciprocal of an arbitrarily large number is arbitrarily close to 0."),
 dict(q="Evaluate lim as x -> infinity of ln(x)/x.", choices=[
   "0", "1", "e", "infinity"], ans=0,
   why="The logarithm grows much more slowly than x, so the quotient is driven to 0."),
 dict(q="Evaluate lim as x -> infinity of sin(x)/x.", choices=[
   "-1", "0", "1", "the limit does not exist"], ans=1,
   why="The numerator stays within [-1, 1] while the denominator grows, so the quotient is squeezed to 0."),
 dict(q="Evaluate lim as x -> infinity of e^(-x).", choices=[
   "-infinity", "0", "1", "infinity"], ans=1,
   why="e^(-x) = 1/e^x, and the denominator grows without bound, so the graph has the horizontal asymptote y = 0."),
 dict(q="Evaluate lim as x -> -infinity of e^x.", choices=[
   "-infinity", "0", "1", "infinity"], ans=1,
   why="Far to the left the exponential decays toward 0, giving the horizontal asymptote y = 0 on that side."),
 dict(q="Evaluate lim as x -> infinity of arctan(x).", choices=[
   "0", "1", "pi/2", "infinity"], ans=2,
   why="The arctangent levels off at pi/2, which is a horizontal asymptote of its graph."),
 dict(q="Evaluate lim as x -> infinity of sqrt(x^2 + 1)/x.", choices=[
   "-1", "0", "1", "infinity"], ans=2,
   why="For large positive x, sqrt(x^2 + 1) is very nearly x, so the quotient approaches 1."),
 dict(q="Evaluate lim as x -> -infinity of sqrt(x^2 + 1)/x.", choices=[
   "-1", "0", "1", "infinity"], ans=0,
   why="sqrt(x^2) equals |x|, which is -x when x is negative, so the quotient approaches -1 rather than 1."),
 dict(q="What is the largest number of horizontal asymptotes the graph of a function can have?", choices=[
   "0", "1", "2", "there is no limit to the number"], ans=2,
   why="There are only two directions to run off in, so at most one asymptote to the right and one to the left."),
 dict(q="Evaluate lim as x -> infinity of (3x^2 - x)/(x^2 + 2x + 1).", choices=[
   "0", "1", "3", "infinity"], ans=2,
   why="Equal degrees give the ratio of leading coefficients, 3/1 = 3."),
 dict(q="Evaluate lim as x -> infinity of (2x + 1)/sqrt(x^2 + 3).", choices=[
   "0", "1", "2", "infinity"], ans=2,
   why="Dividing by x, and using that sqrt(x^2 + 3)/x approaches 1 for large positive x, leaves 2."),
 dict(q="Evaluate lim as x -> infinity of 5x/sqrt(4x^2 + 1).", choices=[
   "0", "5/4", "5/2", "infinity"], ans=2,
   why="For large positive x, sqrt(4x^2 + 1) is very nearly 2x, so the quotient approaches 5/2."),
 dict(q="Can the graph of a function cross one of its horizontal asymptotes?", choices=[
   "No, never",
   "Yes; the asymptote describes only the far-out behavior, so the graph may cross it any number of times closer in",
   "Only if the function is a rational function",
   "Only at the origin"], ans=1,
   why="For example sin(x)/x crosses y = 0 infinitely often while still approaching it, unlike a vertical asymptote which the graph can never meet."),
 dict(q="How many horizontal asymptotes does the graph of f(x) = 2x/sqrt(x^2 + 1) have, and what are they?", choices=[
   "one, y = 2",
   "one, y = 0",
   "two, y = 2 and y = -2",
   "none"], ans=2,
   why="The limit is 2 as x runs to the right and -2 as x runs to the left, because sqrt(x^2 + 1) behaves like |x|."),
 dict(q="Evaluate lim as x -> infinity of x/e^x.", choices=[
   "0", "1", "e", "infinity"], ans=0,
   why="The exponential eventually outgrows any power of x, so the quotient is driven to 0."),
]
