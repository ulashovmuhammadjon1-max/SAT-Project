"""
Authored medium/hard Math multiple-choice questions for Tests 6 and 7.

Why these exist: the transcribed Math pool yields only 18 unused multiple-choice
questions once flagged and internally duplicate items are removed, while Math
Module 1 and Module 2 (Hard) need 19 MC each per test. Free response is not the
problem — 22 unused FR items remain, well past the 3-per-module cap. The gap is
entirely in multiple choice.

These 20 close the gap for **Test 6**. They sit above the Module 2 (Easy) set in
difficulty, as Module 1 and Module 2 (Hard) require: each one takes at least two
steps, and several turn on a condition (no solution, infinitely many solutions, an
extraneous root, a zero discriminant) rather than on plugging in a value.

House style per rule 1: bare HTML stems, plain text for simple inline math,
`\\( \\)` reserved for fractions, exponents, radicals and subscripts, all typed by
hand. `verify_math_authored_mc.py` re-derives every answer with sympy and dedupes
against the 330 live production Math stems, the 44 authored Module 2 (Easy)
questions and the transcribed pool.
"""

QUESTIONS = [
 # ------------------------------------------------------------- Algebra (6)
 dict(n="H1", domain="ALG", skill="ALG-LE", stem=
   "6x+2y=10<br/>9x+cy=4<br/>In the given system of equations, c is a constant. If the system has no "
   "solution, what is the value of c?",
   choices=["\\(\\frac{4}{3}\\)", "3", "6", "12"], correct="B",
   check="no solution means the lines are parallel but distinct: 9/6 = c/2 gives c = 3, and 4/10 differs from 9/6"),

 dict(n="H2", domain="ALG", skill="ALG-LI", stem=
   "Which of the following is the solution set to the inequality \\(|x-4|&lt;6\\)?",
   choices=["\\(x&lt;10\\)", "\\(-2&lt;x&lt;10\\)", "\\(x&gt;-2\\)", "\\(-10&lt;x&lt;2\\)"],
   correct="B",
   check="|x-4| < 6 unfolds to -6 < x-4 < 6, so -2 < x < 10"),

 dict(n="H3", domain="ALG", skill="ALG-LE", stem=
   "A store sells notebooks for $4 each and pens for $2 each. A customer buys 15 of these items and "
   "spends $46 in total. How many notebooks did the customer buy?",
   choices=["4", "7", "11", "8"], correct="D",
   check="4n + 2(15-n) = 46 gives 2n = 16, so n = 8"),

 dict(n="H4", domain="ALG", skill="ALG-LF", stem=
   "The equation S=(n-2)(180) gives the sum S, in degrees, of the interior angle measures of a polygon "
   "with n sides. Which equation correctly expresses n in terms of S?",
   choices=["\\(n=\\frac{S}{180}+2\\)", "\\(n=\\frac{S+2}{180}\\)", "\\(n=\\frac{S}{180}-2\\)",
            "\\(n=180S+2\\)"],
   correct="A", check="divide both sides by 180 and add 2"),

 dict(n="H5", domain="ALG", skill="ALG-LE", stem=
   "4x-6y=14<br/>-2x+3y=k<br/>In the given system of equations, k is a constant. If the system has "
   "infinitely many solutions, what is the value of k?",
   choices=["-7", "-2", "7", "14"], correct="A",
   check="multiplying the second equation by -2 gives 4x-6y=-2k, so -2k = 14 and k = -7"),

 dict(n="H6", domain="ALG", skill="ALG-LF", stem=
   "In the xy-plane, line m is perpendicular to the line \\(y=-\\frac{1}{3}x+5\\) and passes through the "
   "point (0,-2). Which equation defines line m?",
   choices=["\\(y=-\\frac{1}{3}x-2\\)", "\\(y=\\frac{1}{3}x-2\\)", "\\(y=3x-2\\)", "\\(y=-3x-2\\)"],
   correct="C",
   check="perpendicular slope is the negative reciprocal of -1/3, which is 3; the y-intercept is -2"),

 # -------------------------------------------------------- Advanced Math (6)
 dict(n="H7", domain="ADV", skill="ADV-NF", stem=
   "The function f is defined by \\(f(x)=2x^{2}-12x+23\\). What is the minimum value of f(x)?",
   choices=["3", "5", "11", "23"], correct="B",
   check="vertex at x = 12/(2*2) = 3; f(3) = 18 - 36 + 23 = 5"),

 dict(n="H8", domain="ADV", skill="ADV-NF", stem=
   "A population of bacteria decreases by 15% each hour. At time t=0 hours the population is 8,000. "
   "Which function models the population P after t hours?",
   choices=["\\(P(t)=8{,}000(0.15)^{t}\\)", "\\(P(t)=8{,}000-0.15t\\)", "\\(P(t)=8{,}000(1.15)^{t}\\)", "\\(P(t)=8{,}000(0.85)^{t}\\)"], correct="D", check="a 15% decrease per hour multiplies by 1 - 0.15 = 0.85 each hour"),

 dict(n="H9", domain="ADV", skill="ADV-NE", stem=
   "The equation \\(2^{x+3}=32\\) is true for what value of x?",
   choices=["2", "3", "5", "29"], correct="A",
   check="32 = 2^5, so x+3 = 5 and x = 2"),

 dict(n="H10", domain="ADV", skill="ADV-NE", stem=
   "What is the solution to the equation \\(\\sqrt{3x+4}=x\\)?",
   choices=["-1", "1", "4", "-1 and 4"], correct="C",
   check="squaring gives x^2-3x-4=0 with roots 4 and -1; x = -1 is extraneous because a square root "
         "cannot equal a negative number"),

 dict(n="H11", domain="ADV", skill="ADV-EQ", stem=
   "\\[p(x)=x^{3}-4x^{2}+kx-6\\]In the given polynomial, k is a constant. If x-3 is a factor of p(x), "
   "what is the value of k?",
   choices=["-5", "3", "15", "5"], correct="D",
   check="p(3) = 27 - 36 + 3k - 6 = 0 gives 3k = 15, so k = 5"),

 dict(n="H12", domain="ADV", skill="ADV-NE", stem=
   "How many distinct real solutions does the equation \\(3x^{2}-12x+12=0\\) have?",
   choices=["Zero", "Exactly one", "Exactly two", "Infinitely many"], correct="B",
   check="the discriminant is 144 - 4(3)(12) = 0, so there is one repeated real root"),

 # ------------------------------ Problem-Solving and Data Analysis (4) ------
 dict(n="H13", domain="PSDA", skill="PSDA-RP", stem=
   "The price of a jacket is increased by 20%. The new price is then decreased by 20%. The final price "
   "is what percent of the original price?",
   choices=["96%", "98%", "100%", "104%"], correct="A",
   check="1.20 * 0.80 = 0.96"),

 dict(n="H14", domain="PSDA", skill="PSDA-ST", stem=
   "In a group of 30 students, the 18 students in the morning session scored a mean of 84 points on a "
   "test and the 12 students in the afternoon session scored a mean of 74 points. What is the mean "
   "score, in points, of all 30 students?",
   choices=["78", "79", "82", "80"], correct="D",
   check="(18*84 + 12*74)/30 = 2400/30 = 80"),

 dict(n="H15", domain="PSDA", skill="PSDA-DI",
   stem="TABLE_H15 The table shows the number of students in each grade who selected each elective. "
        "If a student who selected chemistry is chosen at random, what is the probability that the "
        "student is a junior?",
   table=dict(headers=["Grade", "Chemistry", "Studio art", "Total"],
              rows=[["Juniors", "36", "24", "60"], ["Seniors", "44", "16", "60"],
                    ["Total", "80", "40", "120"]]),
   choices=["\\(\\frac{9}{20}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{3}{10}\\)", "\\(\\frac{2}{3}\\)"],
   correct="A", check="36 juniors out of the 80 students who chose chemistry: 36/80 = 9/20"),

 dict(n="H16", domain="PSDA", skill="PSDA-RP", stem=
   "A printer produces 45 pages per minute. At this rate, how many hours will it take the printer to "
   "produce 54,000 pages?",
   choices=["12", "20", "24", "45"], correct="B",
   check="54000/45 = 1200 minutes = 20 hours"),

 # ----------------------------------------- Geometry and Trigonometry (4) ---
 dict(n="H17", domain="GT", skill="GT-AV", stem=
   "\\[x^{2}+y^{2}-6x+8y=0\\]The given equation defines a circle in the xy-plane. What is the radius of "
   "the circle?",
   choices=["3", "4", "5", "25"], correct="C",
   check="completing the square gives (x-3)^2 + (y+4)^2 = 25, so the radius is 5"),

 dict(n="H18", domain="GT", skill="GT-LA", stem=
   "Triangle ABC is similar to triangle DEF, where side AB corresponds to side DE. The length of AB is "
   "9, the length of DE is 15, and the perimeter of triangle ABC is 24. What is the perimeter of "
   "triangle DEF?",
   choices=["30", "36", "45", "40"], correct="D",
   check="perimeters scale by the similarity ratio 15/9, so 24 * 15/9 = 40"),

 dict(n="H19", domain="GT", skill="GT-AV", stem=
   "A circle has a radius of 10 inches. What is the length, in inches, of an arc intercepted by a "
   "central angle measuring 72&deg;?",
   choices=["\\(2\\pi\\)", "\\(4\\pi\\)", "\\(10\\pi\\)", "\\(20\\pi\\)"], correct="B",
   check="(72/360) * 2*pi*10 = 4pi"),

 dict(n="H20", domain="GT", skill="GT-TR", stem=
   "In right triangle XYZ, angle Z is a right angle. If \\(\\sin X=0.6\\), what is the value of "
   "\\(\\cos Y\\)?",
   choices=["0.4", "0.6", "0.8", "1.6"], correct="B",
   check="angles X and Y are complementary, and the cosine of an angle equals the sine of its complement"),

 # --- four more, replacing transcribed items whose figure exists only as a
 # prose description in the transcript (a scatterplot, a dot plot, a labelled
 # triangle and an exponential graph). Rule 3 forbids a description standing in
 # for the picture, and the transcripts kept no source image to crop.
 dict(n="H21", domain="ALG", skill="ALG-LI", stem=
   "A gym charges a one-time joining fee of $40 plus $25 for each month of membership. Sam wants to "
   "spend no more than $340 in total. What is the greatest number of whole months of membership Sam "
   "can buy?",
   choices=["11", "12", "13", "15"], correct="B",
   check="25m + 40 <= 340 gives m <= 12, so 12 whole months"),

 dict(n="H22", domain="ADV", skill="ADV-EQ", stem=
   "Which expression is equivalent to \\((x+4)^{2}-(x-4)^{2}\\)?",
   choices=["0", "\\(2x^{2}\\)", "16x", "32"], correct="C",
   check="expanding gives (x^2+8x+16) - (x^2-8x+16) = 16x"),

 dict(n="H23", domain="PSDA", skill="PSDA-ST", stem=
   "The mean of a list of 6 numbers is 21. When a seventh number is added to the list, the mean of the "
   "7 numbers is 23. What is the seventh number?",
   choices=["25", "29", "33", "35"], correct="D",
   check="7*23 - 6*21 = 161 - 126 = 35"),

 dict(n="H24", domain="GT", skill="GT-AV", stem=
   "A right circular cone has a radius of 6 centimeters and a height of 10 centimeters. What is the "
   "volume, in cubic centimeters, of the cone?",
   choices=["\\(60\\pi\\)", "\\(120\\pi\\)", "\\(240\\pi\\)", "\\(360\\pi\\)"],
   correct="B", check="(1/3)*pi*6^2*10 = 120pi"),
]
