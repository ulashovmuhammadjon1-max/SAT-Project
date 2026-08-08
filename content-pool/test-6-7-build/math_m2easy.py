"""
Math Module 2 (Easy) for Tests 6 and 7 — 44 originally authored questions.

Standing rule 4 in CLAUDE.md: every test's Math Module 2 (Easy) is authored
here, not transcribed. Requirements it imposes, all enforced by
`verify_math_m2easy.py` in this directory:

- every answer re-derived with sympy;
- checked against **every** question already in the database (330 live Math
  questions across Tests 1-5) and against each other, rejecting a repeated
  problem *template* with new numbers, not merely an exact duplicate;
- genuinely easy — this is the lower branch of the adaptive split;
- 19 MULTIPLE_CHOICE + 3 FREE_RESPONSE per module.

House style follows Test 1/2 (rule 1): stems are bare HTML with no `<p>`
wrapper, simple inline math stays plain text, and `\\( \\)` is reserved for
fractions, exponents, radicals and subscripts. No auto-conversion was used —
every LaTeX span here was typed by hand (rule 2).

Templates deliberately avoided because Test 5's M2E already uses them: a bare
two-step linear solve, a flat-fee-plus-rate cost equation, f(x)=ax+b evaluated
at a point, a two-equation substitution system, a linear function from two
points, a one-variable inequality with a "greatest integer" ask, a monomial
quotient, a binomial product, x^2+c evaluated at a negative, a factorable
quadratic, 2^x evaluated, a single square-root equation, a two-ingredient
recipe ratio, a distance-rate-time scaling, the mean of five listed values, a
two-row table difference, an isosceles angle sum, a cylinder volume, a square
area-to-perimeter conversion, and sin from a 5-12-13 triangle.

## Nine questions were replaced after the dedupe pass flagged them

The first draft collided with live production questions on nine templates. Each
was rewritten rather than renumbered:

| was | collided with | is now |
|---|---|---|
| T6 Q1 solve-then-evaluate `x-9=23`, find `x+9` | `6(x+1)=36`, find `x+1` | muffins at $3, $27 spent |
| T6 Q5 substitution system | `3x+y=14 / y=2x-1` | direct substitution `6a-b=20, b=4` |
| T6 Q9 combining like terms | `(9x^2+9)-(2x^2)` | power of a product `(3m)^3` |
| T6 Q13 exponential evaluation | `f(x)=2^x`, find `f(5)` | vertex of `y=(x-3)^2+5` |
| T6 Q18 marble-jar probability | a jar with the same 6/4/10 counts | spinner, numbers greater than 6 |
| T7 Q6 substitution system | `3x+y=14 / y=2x-1` | elimination by addition |
| T7 Q10 difference of squares | `9x^2-25` | dividing a binomial by a constant |
| T7 Q12 solutions of a factorable quadratic | Test 5 M2E `x^2-9x+20=0` | smaller root of a factored equation |
| T7 Q21 triangle base times height | base 14, height 9 | parallelogram area |

## The dedupe metric, and why the remaining flags are not repeats

A first attempt scored templates by stripping all numbers and markup and taking
Jaccard similarity on the remaining prose. That is useless in both directions:
it rated exponential evaluation against cubic evaluation at 1.00, and
difference-of-squares against radical simplification at 0.86, purely because
both share the boilerplate "which expression is equivalent to". The signature
now keeps tagged mathematical tokens (fraction, radical, pi, squared, cubed,
variable exponent, product of factors, relation) alongside the prose skeleton.

Anything at 0.90 or above fails the build. Every pair between 0.75 and 0.90 was
then read by hand; the five that remain are frame reuse, not template reuse:

- **T6 Q11 (0.87)** evaluates a quadratic at a point; the production match asks
  for a *zero* of a quadratic. Different task.
- **T7 Q11 (0.86)** evaluates a rational function `24/x`; the production match
  evaluates a cubic. "The function f is defined by ... what is f(k)?" is the
  single most common frame on a real SAT and recurs within one form.
- **T6 Q10 (0.78)** distributes then combines; the production match only
  combines like terms.
- **T7 Q14 (0.75)** adds two perfect-square radicals; the production match
  evaluates a fractional exponent.
- **T7 Q1 (0.75)** is a one-step solve; the production match solves and then
  scales the result.
"""

TEST6 = [
 # --- Algebra (8) ---
 dict(n=1, domain="ALG", skill="ALG-LE", type="MULTIPLE_CHOICE",
   stem="At a bake sale, muffins cost $3 each. If Dara spent $27 on muffins, how many muffins did she buy?",
   choices=["3", "9", "24", "81"], correct="B",
   check="27 / 3 = 9"),
 dict(n=2, domain="ALG", skill="ALG-LE", type="MULTIPLE_CHOICE",
   stem="A machine fills 45 bottles each minute. Which equation gives the number of bottles B the machine fills in m minutes?",
   choices=["B=45+m", "B=45m", "B=m/45", "B=45-m"], correct="B",
   check="constant rate 45 per minute over m minutes gives 45m"),
 dict(n=3, domain="ALG", skill="ALG-LF", type="MULTIPLE_CHOICE",
   stem="The graph of a line in the xy-plane passes through (0,-4) and has a slope of 3. What is the y-coordinate of the point on the line where x=2?",
   choices=["-1", "2", "6", "10"], correct="B",
   check="y = 3x - 4; at x=2, y = 2"),
 dict(n=4, domain="ALG", skill="ALG-LI", type="MULTIPLE_CHOICE",
   stem="A delivery van can carry a load of at most 1,200 kilograms. The van is already carrying 750 kilograms. Which inequality gives the possible additional weight w, in kilograms, the van can carry?",
   choices=["\\(w\\le 450\\)", "\\(w\\ge 450\\)", "\\(w\\le 1{,}950\\)", "\\(w\\ge 1{,}200\\)"],
   correct="A", check="750 + w <= 1200 -> w <= 450"),
 dict(n=5, domain="ALG", skill="ALG-LE", type="MULTIPLE_CHOICE",
   stem="If 6a-b=20 and b=4, what is the value of a?",
   choices=["3", "4", "16", "24"], correct="B",
   check="6a - 4 = 20 -> 6a = 24 -> a = 4"),
 dict(n=6, domain="ALG", skill="ALG-LF", type="MULTIPLE_CHOICE",
   stem="The function p is defined by p(t)=120-8t. What is the value of t when p(t)=0?",
   choices=["8", "12", "15", "112"], correct="C",
   check="120-8t=0 -> t=15"),
 dict(n=7, domain="ALG", skill="ALG-LE", type="FREE_RESPONSE",
   stem="If 7(k-2)=63, what is the value of k?",
   answers=["11"], check="k-2=9 -> k=11"),
 dict(n=8, domain="ALG", skill="ALG-LI", type="MULTIPLE_CHOICE",
   stem="Which of the following is a solution to the inequality 5x-4&gt;16?",
   choices=["2", "3", "4", "5"], correct="D",
   check="5x>20 -> x>4; only 5 qualifies"),

 # --- Advanced Math (6) ---
 dict(n=9, domain="ADV", skill="ADV-EQ", type="MULTIPLE_CHOICE",
   stem="Which expression is equivalent to \\((3m)^{3}\\)?",
   choices=["\\(3m^{3}\\)", "\\(9m^{3}\\)", "\\(27m^{3}\\)", "\\(27m\\)"], correct="C",
   check="(3m)^3 = 3^3 * m^3 = 27m^3"),
 dict(n=10, domain="ADV", skill="ADV-EQ", type="MULTIPLE_CHOICE",
   stem="Which expression is equivalent to \\(4(2x-7)+6x\\)?",
   choices=["\\(14x-28\\)", "\\(14x-7\\)", "\\(8x-28\\)", "\\(14x+28\\)"], correct="A",
   check="8x-28+6x = 14x-28"),
 dict(n=11, domain="ADV", skill="ADV-NF", type="MULTIPLE_CHOICE",
   stem="The function g is defined by \\(g(x)=3x^{2}-5\\). What is the value of g(2)?",
   choices=["1", "7", "13", "31"], correct="B",
   check="3*4-5 = 7"),
 dict(n=12, domain="ADV", skill="ADV-NE", type="MULTIPLE_CHOICE",
   stem="What is a solution to the equation \\(x^{2}=49\\)?",
   choices=["\\(\\frac{49}{2}\\)", "24.5", "7", "2401"], correct="C",
   check="x = 7 or -7; 7 is listed"),
 dict(n=13, domain="ADV", skill="ADV-NF", type="MULTIPLE_CHOICE",
   stem="In the xy-plane, the graph of \\(y=(x-3)^{2}+5\\) has its lowest point at (3,k). What is the value of k?",
   choices=["-5", "3", "5", "9"], correct="C",
   check="the squared term is zero at x=3, leaving y = 5"),
 dict(n=14, domain="ADV", skill="ADV-EQ", type="FREE_RESPONSE",
   stem="What is the value of \\(\\frac{a^{8}}{a^{5}}\\) when a=3?",
   answers=["27"], check="a^3 = 27"),

 # --- Problem-Solving and Data Analysis (4) ---
 dict(n=15, domain="PSDA", skill="PSDA-RP", type="MULTIPLE_CHOICE",
   stem="A jacket originally priced at $80 is on sale for 25% off. What is the sale price, in dollars, of the jacket?",
   choices=["20", "55", "60", "75"], correct="C",
   check="80 * 0.75 = 60"),
 dict(n=16, domain="PSDA", skill="PSDA-ST", type="MULTIPLE_CHOICE",
   stem="What is the median of the seven values in the list 3, 5, 5, 8, 11, 14, and 20?",
   choices=["5", "8", "9.4", "11"], correct="B",
   check="sorted, the 4th of 7 values is 8"),
 dict(n=17, domain="PSDA", skill="PSDA-DI", type="MULTIPLE_CHOICE",
   stem="TABLE_A The table shows the number of hours four employees worked last week. What is the total number of hours the four employees worked?",
   table=dict(headers=["Employee", "Hours worked"],
              rows=[["Nadia", "32"], ["Owen", "28"], ["Priya", "41"], ["Quinn", "19"]]),
   choices=["109", "110", "120", "128"], correct="C",
   check="32+28+41+19 = 120"),
 dict(n=18, domain="PSDA", skill="PSDA-ST", type="MULTIPLE_CHOICE",
   stem="A spinner has 8 equal sections numbered 1 through 8. What is the probability that one spin lands on a number greater than 6?",
   choices=["\\(\\frac{1}{8}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{3}{8}\\)", "\\(\\frac{3}{4}\\)"],
   correct="B", check="numbers 7 and 8 qualify: 2/8 = 1/4"),

 # --- Geometry and Trigonometry (4) ---
 dict(n=19, domain="GT", skill="GT-LA", type="MULTIPLE_CHOICE",
   stem="Two angles are supplementary. One angle measures 47&deg;. What is the measure, in degrees, of the other angle?",
   choices=["43", "133", "143", "313"], correct="B",
   check="180-47 = 133"),
 dict(n=20, domain="GT", skill="GT-AV", type="MULTIPLE_CHOICE",
   stem="A rectangle has a length of 14 centimeters and a width of 5 centimeters. What is the perimeter, in centimeters, of the rectangle?",
   choices=["19", "38", "60", "70"], correct="B",
   check="2(14+5) = 38"),
 dict(n=21, domain="GT", skill="GT-AV", type="MULTIPLE_CHOICE",
   stem="A circle has a radius of 6 inches. What is the circumference, in inches, of the circle?",
   choices=["\\(6\\pi\\)", "\\(12\\pi\\)", "\\(36\\pi\\)", "\\(72\\pi\\)"], correct="B",
   check="2*pi*6 = 12pi"),
 dict(n=22, domain="GT", skill="GT-LA", type="FREE_RESPONSE",
   stem="In a right triangle, one leg has length 9 and the other leg has length 12. What is the length of the hypotenuse?",
   answers=["15"], check="sqrt(81+144) = 15"),
]

TEST7 = [
 # --- Algebra (8) ---
 dict(n=1, domain="ALG", skill="ALG-LE", type="MULTIPLE_CHOICE",
   stem="If \\(\\frac{n}{4}=12\\), what is the value of n?",
   choices=["3", "16", "36", "48"], correct="D",
   check="n = 48"),
 dict(n=2, domain="ALG", skill="ALG-LF", type="MULTIPLE_CHOICE",
   stem="A pool contains 900 liters of water and is being drained at a constant rate of 30 liters per minute. Which equation gives the number of liters L remaining in the pool after m minutes of draining?",
   choices=["L=900+30m", "L=900-30m", "L=30m-900", "L=900m-30"], correct="B",
   check="start 900, subtract 30 per minute"),
 dict(n=3, domain="ALG", skill="ALG-LF", type="MULTIPLE_CHOICE",
   stem="What is the slope of the line that passes through the points (2,1) and (6,13) in the xy-plane?",
   choices=["\\(\\frac{1}{3}\\)", "2", "3", "7"], correct="C",
   check="(13-1)/(6-2) = 3"),
 dict(n=4, domain="ALG", skill="ALG-LE", type="MULTIPLE_CHOICE",
   stem="If 5(t+3)=2(t+3)+18, what is the value of t?",
   choices=["3", "5", "6", "9"], correct="A",
   check="3(t+3)=18 -> t+3=6 -> t=3"),
 dict(n=5, domain="ALG", skill="ALG-LI", type="MULTIPLE_CHOICE",
   stem="A student needs at least 240 points to pass a course and already has 165 points. Which inequality gives the possible numbers of additional points p the student needs?",
   choices=["\\(p\\le 75\\)", "\\(p\\ge 75\\)", "\\(p\\ge 405\\)", "\\(p\\le 240\\)"], correct="B",
   check="165 + p >= 240 -> p >= 75"),
 dict(n=6, domain="ALG", skill="ALG-LE", type="MULTIPLE_CHOICE",
   stem="5x+2y=31<br/>5x-2y=9<br/>What is the value of x in the solution to the given system of equations?",
   choices=["4", "5.5", "8", "11"], correct="A",
   check="adding the equations gives 10x = 40 -> x = 4"),
 dict(n=7, domain="ALG", skill="ALG-LF", type="FREE_RESPONSE",
   stem="A taxi ride costs $3.50 plus $2.00 for each mile traveled. How many miles were traveled on a ride that cost $19.50?",
   answers=["8"], check="(19.50 - 3.50) / 2 = 8"),
 dict(n=8, domain="ALG", skill="ALG-LE", type="MULTIPLE_CHOICE",
   stem="A number decreased by 14 is equal to 3 times the number. What is the number?",
   choices=["-7", "-3.5", "3.5", "7"], correct="A",
   check="x - 14 = 3x -> -14 = 2x -> x = -7"),

 # --- Advanced Math (6) ---
 dict(n=9, domain="ADV", skill="ADV-EQ", type="MULTIPLE_CHOICE",
   stem="Which expression is equivalent to \\((2c^{3})(7c^{4})\\)?",
   choices=["\\(9c^{7}\\)", "\\(14c^{7}\\)", "\\(14c^{12}\\)", "\\(9c^{12}\\)"], correct="B",
   check="2*7 = 14, 3+4 = 7"),
 dict(n=10, domain="ADV", skill="ADV-EQ", type="MULTIPLE_CHOICE",
   stem="Which expression is equivalent to \\(\\frac{9x+18}{3}\\)?",
   choices=["3x+6", "3x+18", "9x+6", "\\(3x+\\frac{18}{3}x\\)"], correct="A",
   check="dividing each term by 3 gives 3x + 6"),
 dict(n=11, domain="ADV", skill="ADV-NF", type="MULTIPLE_CHOICE",
   stem="The function f is defined by \\(f(x)=\\frac{24}{x}\\). What is the value of f(6)?",
   choices=["4", "18", "30", "144"], correct="A",
   check="24 / 6 = 4"),
 dict(n=12, domain="ADV", skill="ADV-NE", type="MULTIPLE_CHOICE",
   stem="What is the smaller of the two solutions to the equation (x-8)(x+2)=0?",
   choices=["-8", "-2", "2", "8"], correct="B",
   check="solutions are 8 and -2; the smaller is -2"),
 dict(n=13, domain="ADV", skill="ADV-NE", type="MULTIPLE_CHOICE",
   stem="If \\(\\sqrt{2y}=8\\), what is the value of y?",
   choices=["4", "16", "32", "64"], correct="C",
   check="2y = 64 -> y = 32"),
 dict(n=14, domain="ADV", skill="ADV-NF", type="FREE_RESPONSE",
   stem="What is the value of \\(\\sqrt{169}+\\sqrt{36}\\)?",
   answers=["19"], check="13 + 6 = 19"),

 # --- Problem-Solving and Data Analysis (4) ---
 dict(n=15, domain="PSDA", skill="PSDA-RP", type="MULTIPLE_CHOICE",
   stem="In a survey, 18 of the 300 people surveyed said they had never used a public library. What percentage of the people surveyed said they had never used a public library?",
   choices=["6%", "12%", "18%", "60%"], correct="A",
   check="18/300 = 0.06"),
 dict(n=16, domain="PSDA", skill="PSDA-RP", type="MULTIPLE_CHOICE",
   stem="A map uses a scale in which 1 centimeter represents 25 kilometers. Two cities are 7 centimeters apart on the map. What is the actual distance, in kilometers, between the two cities?",
   choices=["32", "125", "175", "250"], correct="C",
   check="7*25 = 175"),
 dict(n=17, domain="PSDA", skill="PSDA-DI", type="MULTIPLE_CHOICE",
   stem="TABLE_B The table shows the number of tickets sold for each of four film screenings. How many more tickets were sold for the screening with the greatest number of tickets sold than for the screening with the least?",
   table=dict(headers=["Screening", "Tickets sold"],
              rows=[["Morning", "58"], ["Afternoon", "94"], ["Evening", "137"], ["Late night", "45"]]),
   choices=["43", "79", "92", "137"], correct="C",
   check="137-45 = 92"),
 dict(n=18, domain="PSDA", skill="PSDA-ST", type="MULTIPLE_CHOICE",
   stem="The mean of four numbers is 15. Three of the numbers are 9, 14, and 18. What is the fourth number?",
   choices=["15", "19", "22", "60"], correct="B",
   check="total 60; 60 - (9+14+18) = 19"),

 # --- Geometry and Trigonometry (4) ---
 dict(n=19, domain="GT", skill="GT-LA", type="MULTIPLE_CHOICE",
   stem="In a triangle, the measures of two angles are 38&deg; and 61&deg;. What is the measure, in degrees, of the third angle?",
   choices=["71", "81", "99", "109"], correct="B",
   check="180 - 38 - 61 = 81"),
 dict(n=20, domain="GT", skill="GT-AV", type="MULTIPLE_CHOICE",
   stem="A rectangular prism has a length of 5 meters, a width of 4 meters, and a height of 3 meters. What is the volume, in cubic meters, of the prism?",
   choices=["12", "24", "60", "94"], correct="C",
   check="5*4*3 = 60"),
 dict(n=21, domain="GT", skill="GT-AV", type="MULTIPLE_CHOICE",
   stem="A parallelogram has a base of 12 inches and a height of 9 inches. What is the area, in square inches, of the parallelogram?",
   choices=["21", "42", "54", "108"], correct="D",
   check="base * height = 12*9 = 108"),
 dict(n=22, domain="GT", skill="GT-TR", type="FREE_RESPONSE",
   stem="In right triangle DEF, angle F is a right angle, DE=17, and EF=8. What is the length of DF?",
   answers=["15"], check="sqrt(289-64) = 15"),
]
