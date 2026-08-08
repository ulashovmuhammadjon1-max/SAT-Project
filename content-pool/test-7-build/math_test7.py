#!/usr/bin/env python3
"""
Original Math content for Test 7 — Module 1 (Standard) and Module 2 (Hard).

Every question here is written from scratch. Nothing is transcribed from a
source paper and nothing is reused from Tests 1-6; `verify_math_test7.py`
re-derives each answer with sympy and rejects any stem that repeats a template
already live in the database.

House style follows Test 1/2, per CLAUDE.md:
  - LaTeX typed by hand, never bulk-converted
  - simple inline arithmetic stays plain text; `\\( \\)` is for fractions,
    exponents, radicals and subscripts
  - function names escaped (`\\sin`, `\\cos`, `\\tan`, `\\log`)
  - a space either side of every inline span
  - `&deg;` rather than a raw glyph, and real `<table>` markup for data
  - display equations use `\\[ ... \\]` and are followed by bare prose, not a
    `<p>` wrapper

Difficulty is carried by the module, and each question's own `difficulty` field
is set to match at assembly time (MEDIUM for Module 1, HARD for Module 2 Hard) —
that is the Test 1/2 convention. Tests 3-6 left every question MEDIUM, which is
why their Question Bank difficulty badges are wrong.

Field shape per question:
    n        stable id, used by the verifier and for dedupe reporting
    domain   Domain.code          skill  Skill.code
    type     "MC" | "FR"
    stem     final HTML
    choices  4 strings for MC, omitted for FR
    correct  "A".."D" for MC
    answers  list of accepted strings for FR (assembler JSON-encodes it)
    check    one line saying how the answer is obtained
"""

TABLE = ('<table style="border-collapse:collapse;margin:0.75rem 0;">'
         "{head}{body}</table>")
TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">{}</th>')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ---------------------------------------------------------------------------
# Module 1 — Standard. Medium difficulty: one or two steps, no layered setups.
# Domain mix 7 ALG / 7 ADV / 4 PSDA / 4 GT, matching the blueprint measured
# across Tests 1-6 (ALG 33%, ADV 30%, PSDA 20%, GT 17%).
# ---------------------------------------------------------------------------
MODULE_1 = [
 dict(n="M1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A landscaping crew charges $65 to visit a site plus $28 for each hour worked. For "
            "one job the crew billed a total of $289. For how many hours did the crew work?"),
      choices=["4", "6", "8", "9"], correct="C",
      check="65 + 28h = 289 gives 28h = 224 and h = 8."),

 dict(n="M1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("\\[2x+3y=19\\]\\[x-y=2\\]For the given system of equations, what is the value of "
            "\\(x+y\\)?"),
      choices=["5", "6", "8", "11"], correct="C",
      check="x = y+2 gives 5y+4 = 19, y = 3 and x = 5, so x+y = 8."),

 dict(n="M1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem="Line k passes through the points (2, -1) and (6, 7) in the xy-plane. What is the slope of line k?",
      choices=["\\(\\frac{1}{2}\\)", "2", "3", "4"], correct="B",
      check="(7-(-1))/(6-2) = 8/4 = 2."),

 dict(n="M1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A technician models the temperature of a cooling engine with "
            "\\(T(m)=94-2.5m\\), where T is the temperature in degrees Celsius m minutes after "
            "the engine is switched off. After how many minutes does the model predict a "
            "temperature of 34 degrees Celsius?"),
      choices=["16", "20", "24", "38"], correct="C",
      check="94 - 2.5m = 34 gives 2.5m = 60 and m = 24."),

 dict(n="M1-05", domain="ALG", skill="ALG-LI", type="MC",
      stem="Which of the following describes all values of x that satisfy \\(4-2x>10\\)?",
      choices=["\\(x>3\\)", "\\(x<3\\)", "\\(x>-3\\)", "\\(x<-3\\)"], correct="D",
      check="-2x > 6, and dividing by -2 reverses the sign: x < -3."),

 dict(n="M1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A caterer charges a fixed booking fee plus a fixed amount per guest. The total "
            "charge for 20 guests is $930, and the total charge for 35 guests is $1,470. What "
            "is the caterer's booking fee, in dollars?"),
      choices=["$140", "$170", "$180", "$210"], correct="D",
      check="Per guest = (1470-930)/15 = 36; fee = 930 - 20(36) = 210."),

 dict(n="M1-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A tank contains 240 litres of water and is drained at a constant rate of 8 litres "
            "per minute. Which equation gives the volume V, in litres, of water remaining in "
            "the tank t minutes after draining begins, for \\(0\\le t\\le 30\\)?"),
      choices=["\\(V=240+8t\\)", "\\(V=8t-240\\)", "\\(V=240-\\frac{t}{8}\\)", "\\(V=240-8t\\)"],
      correct="D",
      check="Starts at 240 and falls 8 per minute."),

 dict(n="M1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A rectangular garden bed has a length of \\(2x-5\\) metres and a width of "
            "\\(x+4\\) metres. Which expression represents the area of the bed, in square "
            "metres?"),
      choices=["\\(3x-1\\)", "\\(2x^{2}+3x-20\\)", "\\(2x^{2}-3x-20\\)", "\\(2x^{2}-20\\)"],
      correct="B",
      check="(2x-5)(x+4) = 2x^2 + 3x - 20."),

 dict(n="M1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A cinema finds that its daily profit, in dollars, is modelled by "
            "\\(P(d)=d^{2}-8d+13\\), where d is the ticket discount in dollars. What is the "
            "least daily profit predicted by this model?"),
      choices=["-3", "-1", "4", "13"], correct="A",
      check="Vertex at d = 4; P(4) = 16 - 32 + 13 = -3."),

 dict(n="M1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A colony of algae covers an area that triples each week. The colony covered 3 square "
            "metres at the start of the study and covers 243 square metres now. How many weeks "
            "have passed since the start of the study?"),
      choices=["2", "3", "4", "27"], correct="C",
      check="3 * 3^w = 243 gives 3^w = 81 and w = 4."),

 dict(n="M1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The two solutions to the equation \\(x^{2}-5x-24=0\\) are the lengths, in "
            "centimetres, of two segments in a construction diagram, one of which is discarded "
            "for being negative. What is the length of the segment that is kept?"),
      choices=["3", "5", "8", "24"], correct="C",
      check="Roots are 8 and -3; the positive one is 8."),

 dict(n="M1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{12a^{5}b^{3}}{3a^{2}b^{7}}\\) for "
            "\\(a>0\\) and \\(b>0\\)?"),
      choices=["\\(\\frac{4a^{3}}{b^{4}}\\)", "\\(4a^{3}b^{4}\\)",
               "\\(\\frac{4a^{7}}{b^{10}}\\)", "\\(\\frac{9a^{3}}{b^{4}}\\)"], correct="A",
      check="12/3 = 4, a^(5-2) = a^3, b^(3-7) = b^-4."),

 dict(n="M1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A ball is thrown upward from a platform. Its height h, in metres, t seconds after "
            "release is given by \\(h(t)=-5t^{2}+20t+12\\). How many seconds after release does "
            "the ball reach its greatest height?"),
      choices=["2", "4", "12", "32"], correct="A",
      check="Vertex at t = -20/(2(-5)) = 2."),

 dict(n="M1-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The population of a colony of bacteria triples every 6 hours. If the colony starts "
            "with 400 bacteria, which function gives the number of bacteria, \\(P(t)\\), after t "
            "hours?"),
      choices=["\\(P(t)=400(3)^{6t}\\)", "\\(P(t)=400(3)^{\\frac{t}{6}}\\)",
               "\\(P(t)=400(6)^{\\frac{t}{3}}\\)", "\\(P(t)=400+3t\\)"], correct="B",
      check="Tripling every 6 hours means exponent t/6."),

 dict(n="M1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A recipe uses 3 cups of flour for every 4 cups of milk. If a baker uses 18 cups of "
            "flour, how many cups of milk are needed?"),
      choices=["13.5", "19", "24", "27"], correct="C",
      check="18 * 4/3 = 24."),

 dict(n="M1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The price of a jacket was reduced by 20%, and the reduced price was then reduced by "
            "a further 15%. The final price is what percent of the original price?"),
      choices=["65%", "68%", "70%", "72%"], correct="B",
      check="0.80 * 0.85 = 0.68."),

 dict(n="M1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table shows the number of books borrowed from a library on each of five days."
            + table(["Day", "Books borrowed"],
                    [["Monday", "42"], ["Tuesday", "38"], ["Wednesday", "51"],
                     ["Thursday", "47"], ["Friday", "62"]])
            + "What is the median number of books borrowed per day?"),
      choices=["42", "47", "48", "51"], correct="B",
      check="Sorted: 38, 42, 47, 51, 62; the middle value is 47."),

 dict(n="M1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A quality inspector examines a batch of 400 components and finds that 26 of them are "
            "defective. Based on this rate, how many defective components would be expected in a "
            "shipment of 5,000 components?"),
      choices=["260", "325", "400", "520"], correct="B",
      check="26/400 * 5000 = 325."),

 dict(n="M1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("In a triangle, an exterior angle at one vertex measures 118&deg;. One of the two "
            "non-adjacent interior angles measures 47&deg;. What is the measure, in degrees, of "
            "the other non-adjacent interior angle?"),
      choices=["47", "62", "71", "133"], correct="C",
      check="An exterior angle equals the sum of the two remote interior angles: 118 - 47 = 71."),

 # ---- free response: 3 per module, the Test 1 target -----------------------
 dict(n="M1-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A right circular cylinder has a radius of 5 centimetres and a height of 12 "
            "centimetres. What is the volume, in cubic centimetres, of the cylinder? (Round to "
            "the nearest whole number.)"),
      answers=["942"],
      check="pi * 25 * 12 = 300pi = 942.48..., which rounds to 942."),

 dict(n="M1-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The sum of three consecutive even integers is 138. What is the greatest of the "
            "three integers?"),
      answers=["48"],
      check="n + (n+2) + (n+4) = 138 gives n = 44; the greatest is 48."),

 dict(n="M1-22", domain="GT", skill="GT-TR", type="FR",
      stem=("In right triangle PQR, angle Q is a right angle, \\(PQ=9\\) and \\(QR=12\\). What "
            "is the length of PR?"),
      answers=["15"],
      check="sqrt(81+144) = sqrt(225) = 15."),
]


# ---------------------------------------------------------------------------
# Module 2 — Hard. Multi-step setups, non-obvious rearrangement, or a
# structural rather than numeric answer.
# ---------------------------------------------------------------------------
MODULE_2_HARD = [
 dict(n="H2-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A theatre sold 340 tickets for a performance. Adult tickets cost $18 and student "
            "tickets cost $11, and the total revenue was $4,790. How many student tickets were "
            "sold?"),
      choices=["130", "180", "190", "210"], correct="C",
      check="18a + 11s = 4790 with a + s = 340 gives 7a = 4790 - 3740 = 1050, a = 150, s = 190."),

 dict(n="H2-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("\\[9x-3y=15\\]\\[cx-y=8\\]In the given system of equations, c is a constant. "
            "For which value of c does the system have no solution?"),
      choices=["-3", "3", "8", "9"], correct="B",
      check="Parallel needs c/9 = 1/3, so c = 3, and the constants then disagree."),

 dict(n="H2-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A line in the xy-plane passes through \\((-4, 9)\\) and is perpendicular to the line "
            "\\(y=\\frac{2}{3}x+5\\). What is the y-coordinate of the point where the line "
            "crosses the y-axis?"),
      choices=["-3", "1", "3", "15"], correct="C",
      check="Perpendicular slope is -3/2; 9 = -3/2(-4) + b gives b = 3."),

 dict(n="H2-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A shop sells notebooks for $4 each and folders for $3 each. A customer buys a total "
            "of 20 items and spends no more than $68. What is the greatest number of notebooks "
            "the customer could have bought?"),
      choices=["6", "7", "8", "12"], correct="C",
      check="4n + 3(20-n) <= 68 gives n <= 8."),

 dict(n="H2-05", domain="ADV", skill="ADV-NE", type="MC",
      stem=("\\[x^{2}+bx+45=0\\]In the given equation, b is a constant. If the equation has "
            "exactly one real solution, and b is positive, what is the value of b?"),
      choices=["\\(3\\sqrt{5}\\)", "9", "\\(6\\sqrt{5}\\)", "45"], correct="C",
      check="Discriminant b^2-180 = 0 gives b = 6*sqrt(5) for the positive root."),

 dict(n="H2-06", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function g is defined by \\(g(x)=2x^{2}-12x+7\\). The graph of \\(y=g(x)\\) in "
            "the xy-plane has its vertex at the point \\((h, k)\\). What is the value of "
            "\\(h+k\\)?"),
      choices=["-11", "-8", "-5", "3"], correct="B",
      check="h = 3, k = g(3) = 18-36+7 = -11, so h+k = -8."),

 dict(n="H2-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The functions f and g are defined by \\(f(x)=x^{2}-1\\) and \\(g(x)=2x+3\\). "
            "What is the value of \\(f(g(2))\\)?"),
      choices=["15", "24", "48", "49"], correct="C",
      check="g(2) = 7 and f(7) = 49 - 1 = 48."),

 dict(n="H2-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A cable of length \\(x+4\\) metres is stretched so that its length equals "
            "\\(\\sqrt{2x+11}\\) metres. Given that the length is positive, what is the "
            "value of x?"),
      choices=["-5", "-1", "1", "5"], correct="B",
      check="2x+11 = (x+4)^2 gives x^2+6x+5 = 0; of the roots -1 and -5 only -1 keeps the length positive."),

 dict(n="H2-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=k(2)^{x}\\), where k is a positive constant. "
            "If \\(f(5)-f(3)=96\\), what is the value of k?"),
      choices=["4", "6", "8", "12"], correct="A",
      check="k(32-8) = 24k = 96, so k = 4."),

 dict(n="H2-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The side length of a cube, in centimetres, is \\(\\sqrt[3]{V}\\), where V is "
            "its volume in cubic centimetres. If a cube has volume \\(64y^{12}\\) cubic "
            "centimetres, where \\(y>0\\), what is its side length, in centimetres?"),
      choices=["\\(4y^{4}\\)", "\\(8y^{4}\\)", "\\(4y^{9}\\)", "\\(16y^{4}\\)"], correct="A",
      check="64^(1/3) = 4 and (y^12)^(1/3) = y^4."),

 dict(n="H2-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function h is defined by \\(h(x)=3x^{2}+6x-2\\). For what value of x does "
            "\\(h(x)\\) attain its minimum, and what is that minimum value?"),
      choices=["\\(x=-1\\), minimum \\(-5\\)", "\\(x=-1\\), minimum \\(1\\)",
               "\\(x=1\\), minimum \\(7\\)", "\\(x=-2\\), minimum \\(-2\\)"], correct="A",
      check="Vertex x = -1; h(-1) = 3-6-2 = -5."),

 dict(n="H2-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A data set of 8 values has a mean of 24. When a ninth value is added, the mean of "
            "the 9 values is 26. What is the ninth value?"),
      choices=["26", "34", "42", "50"], correct="C",
      check="9(26) - 8(24) = 234 - 192 = 42."),

 dict(n="H2-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table summarises the results of a survey of 200 students."
            + table(["", "Prefers cycling", "Prefers walking", "Total"],
                    [["Year 10", "48", "52", "100"],
                     ["Year 11", "62", "38", "100"],
                     ["Total", "110", "90", "200"]])
            + "One of the students who prefers cycling is selected at random. What is the "
              "probability that the student is in Year 11?"),
      choices=["\\(\\frac{31}{100}\\)", "\\(\\frac{31}{55}\\)", "\\(\\frac{11}{20}\\)",
               "\\(\\frac{62}{90}\\)"], correct="B",
      check="62/110 = 31/55."),

 dict(n="H2-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A car travels the first 60 kilometres of a journey at an average speed of 40 "
            "kilometres per hour and the remaining 60 kilometres at an average speed of 60 "
            "kilometres per hour. What is the car's average speed, in kilometres per hour, for "
            "the whole journey?"),
      choices=["44", "48", "50", "52"], correct="B",
      check="Total time 1.5+1 = 2.5 h for 120 km, so 48 km/h."),

 dict(n="H2-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A biologist measured the mass, in grams, of each of 40 seedlings. The mean mass was "
            "reported as 6.4 grams. The biologist later found that one measurement had been "
            "recorded as 9.2 grams when the true value was 2.2 grams. What is the correct mean "
            "mass, in grams?"),
      choices=["6.05", "6.225", "6.4", "6.575"], correct="B",
      check="Total falls by 7, so the mean falls by 7/40 = 0.175 to 6.225."),

 dict(n="H2-16", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle DEF, side DE has length 12 and side DF has length 18. Point G lies on "
            "DE and point H lies on DF so that GH is parallel to EF. If \\(DG=8\\), what is the "
            "length of DH?"),
      choices=["10", "12", "13.5", "16"], correct="B",
      check="DG/DE = DH/DF gives 8/12 = DH/18, so DH = 12."),

 dict(n="H2-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A sphere and a right circular cone have equal volumes. The sphere has radius 3 and "
            "the cone has radius 3. What is the height of the cone?"),
      choices=["4", "9", "12", "36"], correct="C",
      check="(4/3)pi(27) = (1/3)pi(9)h gives 36pi = 3pi h, h = 12."),

 dict(n="H2-18", domain="GT", skill="GT-TR", type="MC",
      stem=("A ramp rises 5 metres over a slope length of 13 metres. What is the horizontal "
            "distance, in metres, covered by the ramp?"),
      choices=["8", "12", "\\(\\sqrt{194}\\)", "18"], correct="B",
      check="sqrt(13^2 - 5^2) = sqrt(144) = 12."),

 dict(n="H2-19", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A subscription service charges the same amount each month. A customer who has paid "
            "for 2 months has been billed $47 in total, including a one-time joining fee, and a "
            "customer who has paid for 6 months has been billed $131 in total. What is the "
            "one-time joining fee, in dollars?"),
      choices=["$5", "$11", "$21", "$26"], correct="A",
      check="Monthly = (131-47)/4 = 21; fee = 47 - 2(21) = 5."),

 # ---- free response --------------------------------------------------------
 dict(n="H2-20", domain="ADV", skill="ADV-NE", type="FR",
      stem=("\\[2x^{2}-11x+12=0\\]What is the sum of the solutions to the given equation? "
            "(Express your answer as a fraction or a decimal.)"),
      answers=["11/2", "5.5"],
      check="Sum of roots = -b/a = 11/2."),

 dict(n="H2-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A chemist has one solution that is 20% acid and another that is 50% acid. How many "
            "litres of the 50% solution must be added to 12 litres of the 20% solution to "
            "produce a mixture that is 30% acid?"),
      answers=["6"],
      check="0.2(12)+0.5v = 0.3(12+v) gives 2.4+0.5v = 3.6+0.3v, v = 6."),

 dict(n="H2-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular prism has a square base. Its height is 3 times the side length of the "
            "base, and its volume is 375 cubic centimetres. What is the side length, in "
            "centimetres, of the base?"),
      answers=["5"],
      check="s^2 * 3s = 3s^3 = 375 gives s^3 = 125, s = 5."),
]

ALL = MODULE_1 + MODULE_2_HARD
