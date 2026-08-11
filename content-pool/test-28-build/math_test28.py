#!/usr/bin/env python3
"""
Original Math content for Test 28 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item makes a constant, a rate, a
                per-unit price or an unknown be recovered first and only then
                used — two or three steps throughout.
  MODULE_2_EASY genuinely one-step: one operation, no recovery step. This is
                the lower branch of the adaptive split.
  MODULE_2_HARD parameters instead of numbers, symbolic and structural answer
                choices, a composed function, a symbolic system, a symbolic
                inequality, a two-way table, and geometry that chains two
                relationships.

Thematic territory assigned to Test 28: coaching routes and stage timetables,
farriery and horseshoeing, coach building (bodies, springs, axles, lamps,
doors — deliberately NOT wheels, felloes, spokes or harness, which Test 21
holds), drovers' roads, toll gates and turnpikes.

The territory is split so that no setting appears in both Module 1 and a
Module 2 branch — a student sees Module 1 plus exactly one Module 2 module,
and a setting reused across that boundary shows the same scene twice in one
sitting:

  Module 1        coaching routes, stage timetables, booking offices, posting
                  houses, coachyards, and coach building (bodies, springs,
                  axles, lamps, doors, panels, glazing)
  Module 2 Easy   farriery and horseshoeing, drovers' roads and stances
  Module 2 Hard   toll gates, turnpike trusts and toll houses

Distance-rate-time is the most heavily banked SAT template there is and a
coaching route invites it at every turn; it is deliberately absent from this
file. The journey items turn on fares, weights, timetable stages and loading
instead.

Every stem was screened against the 1,386 live production Math stems BEFORE it
was drafted, and again afterwards by verify_math_test28.py. Templates rejected
at the screening stage because the bank already holds them, rather than written
and later discovered: a rectangle "n metres longer than it is wide" with a
given area (Test 15 M2H Q11 is the same rectangle with the same 330); a
capacity item of the form "spend a fixed sum, charge per unit, least number of
units to clear it" (Test 9 M1S Q4); "rate per unit, sold only in packs of k,
least number of packs" (Test 19 M1S Q15); a sample scaled up to a population
(Tests 9, 15 and 16); the mean of a set after one value is added or removed
(Tests 11, 12, 14 and 16); the mean of two groups pooled (Tests 10, 13 and 15);
a parallel-beam transversal with (3x+10) and (5x-30) degrees (Test 18 M2H Q19);
1/(1/u + 1/v) (Test 20 M2H Q8); "how many integer values satisfy both
inequalities" (Test 21 M2H Q3); and a cylinder compared with one of twice the
radius and half the height (Test 9 M1S Q18).

House style follows Test 1/2 (see CLAUDE.md): stems are bare HTML, simple
inline math stays plain text, every data table is real <table> markup, and all
LaTeX is typed by hand. No bulk conversion step was used anywhere in this file.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ---------------------------------------------------------------- Module 1
# Settings: coaching routes, stage timetables, booking offices, posting houses,
# coachyards, coach building.
MODULE_1 = [

 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A coachbuilder's ironmonger invoices elliptic springs and axle-boxes at fixed "
            "prices. Six springs together with five axle-boxes come to &pound;71, and four "
            "springs together with nine axle-boxes come to &pound;87. What is the cost of one "
            "spring together with one axle-box?"),
      choices=["&pound;13", "&pound;15", "&pound;17", "&pound;19"], correct="A",
      check="6s+5a=71 and 4s+9a=87 give s = 6 and a = 7, so one of each costs 13 pounds."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A stagecoach is run over a weighbridge before it sets out. With 4 passengers and "
            "their luggage aboard it weighs 1,486 kilograms, and with 9 passengers and their "
            "luggage aboard it weighs 1,861 kilograms. Every passenger with luggage adds the "
            "same weight. What does the coach weigh with no passengers aboard?"),
      choices=["811 kilograms", "1,036 kilograms", "1,111 kilograms", "1,186 kilograms"],
      correct="D",
      check="Each passenger adds (1,861-1,486)/5 = 75 kg, so the empty coach weighs "
            "1,486 - 4(75) = 1,186 kg."),

 dict(n="H1-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A coach guard is required to average at least 15 parcels a journey over the six "
            "journeys he works in a week. On the first five journeys of one week he carried 12, "
            "18, 9, 16 and 14 parcels. What is the least number of parcels he must carry on the "
            "sixth journey to meet the requirement?"),
      choices=["19", "20", "21", "22"], correct="C",
      check="Six journeys averaging 15 need 90 parcels in all, and the first five come to 69, "
            "so the sixth must carry at least 21."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A coachbuilder estimates the cost C, in pounds, of a new body as C = 14L + 9w + 60, "
            "where L is the length of the body in feet and w is the number of window lights "
            "glazed into it. Which equation gives w in terms of C and L?"),
      choices=["\\(w=\\frac{C-14L-60}{9}\\)", "\\(w=\\frac{C-14L+60}{9}\\)",
               "\\(w=\\frac{C+14L-60}{9}\\)", "\\(w=\\frac{C-60}{9}-14L\\)"], correct="A",
      check="Subtracting 14L and 60 from both sides gives 9w = C - 14L - 60."),

 dict(n="H1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a posting house the number of horses kept is three times the number of grooms "
            "employed, and the number of grooms is 4 more than the number of postboys. Counted "
            "together, the horses, the grooms and the postboys come to 71. How many postboys are "
            "employed there?"),
      choices=["9", "11", "13", "15"], correct="B",
      check="With p postboys there are p+4 grooms and 3p+12 horses, and 5p+16 = 71 gives p = 11."),

 dict(n="H1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A booking office charges a fare that is a linear function of the number of stages "
            "travelled. A journey of 3 stages is charged 11 shillings and a journey of 8 stages "
            "is charged 26 shillings. A traveller is charged 38 shillings. How many stages does "
            "that journey cover?"),
      choices=["9", "10", "11", "12"], correct="D",
      check="The fare rises 3 shillings a stage and the fixed part is 2 shillings, so "
            "3n + 2 = 38 gives n = 12."),

 dict(n="H1-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A booking office sells all 51 places on a coach. An inside place is sold for 8 "
            "shillings and an outside place for 5 shillings, and the receipts come to 333 "
            "shillings. How many inside places were sold?"),
      answers=["26"],
      check="8i + 5(51-i) = 333 gives 3i = 78 and i = 26."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A coach proprietor models the day's takings T, in pounds, from a route as "
            "\\(T=-2f^{2}+36f+40\\), where f is the fare in shillings. Which of the following "
            "equivalent forms displays the fare that gives the greatest takings as a constant in "
            "the expression?"),
      choices=["\\(T=-2(f-9)^{2}+202\\)", "\\(T=-2(f-9)^{2}+121\\)",
               "\\(T=-2(f+9)^{2}+202\\)", "\\(T=-2(f-18)^{2}+364\\)"], correct="A",
      check="Completing the square, -2(f^2-18f)+40 = -2(f-9)^2 + 162 + 40 = -2(f-9)^2 + 202."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A coachyard's average cost A, in pounds, of building each of n coaches in one season "
            "is modelled by \\(A=\\frac{18n+540}{n}\\). For how many coaches does this model "
            "give an average cost of &pound;33 each?"),
      choices=["30", "36", "45", "60"], correct="B",
      check="18n + 540 = 33n gives 15n = 540 and n = 36."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A booking office sold 20 places on a coach, some of them inside places and the rest "
            "outside places. The number of inside places multiplied by the number of outside "
            "places is 96, and more places were sold inside than outside. How many inside places "
            "were sold?"),
      choices=["8", "10", "12", "16"], correct="C",
      check="The two counts are roots of t^2 - 20t + 96 = 0, namely 12 and 8, and the larger is "
            "12."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A coachbuilder's timber allowance for a body is given by the expression "
            "\\(4x^{3}+6x^{2}-10x\\). Which of the following expresses that allowance as a "
            "product of three factors?"),
      choices=["\\(2x(2x+5)(x-1)\\)", "\\(2x(2x-5)(x+1)\\)",
               "\\(2x(x+5)(2x-1)\\)", "\\(2x(2x+1)(x-5)\\)"], correct="A",
      check="Taking out 2x leaves 2x(2x^2+3x-5), and 2x^2+3x-5 factors as (2x+5)(x-1)."),

 dict(n="H1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A coachyard's stock of seasoned ash for door pillars is modelled by "
            "\\(S=320\\left(\\frac{3}{4}\\right)^{q}\\), where S is the number of lengths in "
            "stock and q is the number of quarters since the stock was last made up. After how "
            "many quarters does the model give a stock of 135 lengths?"),
      choices=["2", "3", "4", "5"], correct="B",
      check="135/320 = 27/64, which is (3/4)^3, so q = 3."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("A coachyard has 60 lamps to japan. If it japanned 5 more lamps each day than it "
            "actually does, it would finish the whole 60 one day sooner than it will. How many "
            "lamps a day does the yard japan?"),
      answers=["15"],
      check="60/x - 60/(x+5) = 1 gives x^2 + 5x - 300 = 0, whose positive root is 15."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table records, for one week, the number of places booked at each of four "
            "booking offices on a coaching route and the number of those booked places that were "
            "actually taken up."
            + table(["Booking office", "Places booked", "Places taken up"],
                    [["Ashby", "240", "186"], ["Bramber", "180", "144"],
                     ["Corve", "300", "231"], ["Denby", "150", "117"]])
            + "At which office was the greatest percentage of booked places taken up?"),
      choices=["Ashby", "Bramber", "Corve", "Denby"], correct="B",
      check="The proportions are 0.775, 0.800, 0.770 and 0.780, so Bramber is highest."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A coachyard keeps 45 lamps, of which 18 are brass and the rest are japanned. Two "
            "thirds of the brass lamps and one third of the japanned lamps were repaired this "
            "season. One of the 45 lamps is selected at random. What is the probability that it "
            "was repaired this season?"),
      choices=["\\(\\frac{1}{3}\\)", "\\(\\frac{2}{5}\\)",
               "\\(\\frac{4}{9}\\)", "\\(\\frac{7}{15}\\)"], correct="D",
      check="12 of the 18 brass lamps and 9 of the 27 japanned lamps were repaired, so 21 of 45, "
            "or 7/15."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A coachbuilder's body varnish covers 4 square yards of panelling for every pint "
            "used. One coach body presents 288 square feet of panelling, and there are 9 square "
            "feet in a square yard. How many pints of varnish are needed for one body?"),
      choices=["2", "4", "6", "8"], correct="D",
      check="288 square feet is 32 square yards, and 32/4 = 8 pints."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table records the number of carriages of each build that one coachyard delivered "
            "in a year."
            + table(["Build", "Number delivered"],
                    [["Post chaise", "24"], ["Barouche", "15"],
                     ["Landau", "36"], ["Brougham", "45"]])
            + "One of the carriages delivered that year is selected at random. What is the "
              "probability that it is a landau or a barouche?"),
      choices=["\\(\\frac{17}{40}\\)", "\\(\\frac{3}{8}\\)",
               "\\(\\frac{7}{24}\\)", "\\(\\frac{17}{23}\\)"], correct="A",
      check="There are 120 carriages in all and 36 + 15 = 51 of them qualify, and 51/120 = 17/40."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A coachbuilder's drawing is made to a scale in which 3 inches on the drawing stand "
            "for 7 feet on the finished carriage. The body measures 6.75 inches from front to "
            "back on the drawing. How long, in feet, is the finished body?"),
      choices=["14", "15.75", "16.5", "18"], correct="B",
      check="6.75/3 = 2.25 and 2.25(7) = 15.75 feet."),

 dict(n="H1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("The front boot of a coach is braced by an isosceles triangle in which the two equal "
            "sides meet at an angle measuring \\((4x)^{\\circ}\\) and each of the two base angles "
            "measures \\((x+30)^{\\circ}\\). What is the measure of the angle at which the two "
            "equal sides meet?"),
      choices=["50&deg;", "60&deg;", "80&deg;", "100&deg;"], correct="C",
      check="4x + 2(x+30) = 180 gives x = 20, so the apex angle is 4(20) = 80 degrees."),

 dict(n="H1-20", domain="GT", skill="GT-AV", type="MC",
      stem=("The side panel of a coach body is a trapezium whose two parallel edges, the roof "
            "line and the floor line, measure 58 inches and 74 inches, and the perpendicular "
            "distance between those edges is 40 inches. A coach has two such panels, and both "
            "faces of each panel are painted. What is the total painted area, in square inches?"),
      choices=["2,640", "5,280", "10,560", "21,120"], correct="C",
      check="Each panel has area (58+74)/2 x 40 = 2,640 square inches, and there are 4 faces in "
            "all, so 10,560."),

 dict(n="H1-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A straight brace inside a coach body runs from the floor rail up to the roof rail. "
            "The brace is 82 inches long and makes an angle of measure \\(\\theta\\) with the "
            "horizontal floor rail, where \\(\\sin\\theta=\\frac{9}{41}\\). What is the "
            "horizontal distance, in inches, between the two ends of the brace?"),
      choices=["72", "76", "80", "84"], correct="C",
      check="The rise is 82(9/41) = 18, so the horizontal run is sqrt(82^2 - 18^2) = 80."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("The floor of a coach body is a rectangle 96 inches long and 54 inches wide. A "
            "rectangular trap 24 inches by 18 inches is cut through it to reach the boot. The "
            "rest of the floor is covered with matting sold by the square foot, where one square "
            "foot is 144 square inches. How many square feet of matting are needed?"),
      answers=["33"],
      check="96(54) - 24(18) = 5,184 - 432 = 4,752 square inches, and 4,752/144 = 33 square feet."),
]


# ---------------------------------------------------------- Module 2 (Easy)
# Settings: farriery and horseshoeing, drovers' roads and stances.
MODULE_2_EASY = [

 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A farrier's charge, in shillings, for shoeing n horses is 7n + 12. For how many "
            "horses is the charge 96 shillings?"),
      choices=["12", "13", "14", "15"], correct="A",
      check="7n + 12 = 96 gives 7n = 84 and n = 12."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A farrier reckons the number of nails N needed for s horseshoes as N = 8s. Which "
            "equation gives s in terms of N?"),
      choices=["\\(s=8N\\)", "\\(s=N-8\\)", "\\(s=\\frac{N}{8}\\)", "\\(s=N+8\\)"], correct="C",
      check="Dividing both sides of N = 8s by 8 gives s = N/8."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A farrier's forge burned 240 pounds of coal in one day at a steady 15 pounds an "
            "hour, so that the number of hours h the forge burned satisfies 240 = 15h. What is "
            "the value of h?"),
      answers=["16"],
      check="Dividing 240 by 15 gives h = 16."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The number N of horseshoe nails left in a farrier's keg after d days of work is "
            "given by N = 900 - 45d. How many nails are left after 12 days?"),
      choices=["300", "360", "420", "540"], correct="B",
      check="900 - 45(12) = 900 - 540 = 360."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A farrier charges 5 shillings for the iron plus a further 2 shillings for each shoe "
            "he fits. Which equation gives the charge A, in shillings, for fitting s shoes?"),
      choices=["A = 2s - 5", "A = 5s + 2", "A = 7s", "A = 2s + 5"], correct="D",
      check="The fixed 5 shillings is added to 2 shillings for each of s shoes, so A = 2s + 5."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A farrier's rule for the number h of horses he will undertake to shoe in one day is "
            "that h must satisfy 4h - 7 &gt; 21. Which of the following values of h satisfies "
            "that inequality?"),
      choices=["5", "6", "7", "8"], correct="D",
      check="4h > 28 gives h > 7, and 8 is the only listed value greater than 7."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A stance beside a drovers' road holds no more than 240 sheep, and 156 sheep have "
            "already been turned onto it. Which inequality gives all possible numbers s of "
            "further sheep that may be turned onto the stance?"),
      choices=["\\(s\\le 84\\)", "\\(s\\ge 84\\)", "\\(s\\le 396\\)", "\\(s\\ge 396\\)"],
      correct="A",
      check="156 + s <= 240 gives s <= 84."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A farrier writes the weight of a set of shoes, in pounds, as \\(6x+15\\). Which "
            "expression is equivalent to that weight?"),
      choices=["\\(2(3x+5)\\)", "\\(3(2x+5)\\)", "\\(3(2x+15)\\)", "\\(6(x+15)\\)"], correct="B",
      check="3 divides both 6x and 15, leaving 3(2x+5)."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A drover reckons the area of a rectangular fold, in square yards, as (x + 6)(x - 2). "
            "Which expression is equivalent to that area?"),
      choices=["\\(x^{2}-12\\)", "\\(x^{2}+8x-12\\)", "\\(x^{2}-4x-12\\)",
               "\\(x^{2}+4x-12\\)"], correct="D",
      check="The product is x^2 - 2x + 6x - 12 = x^2 + 4x - 12."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A farrier's charge for each horse falls when several are brought together, and is "
            "modelled by \\(c(n)=\\frac{120}{n}\\) shillings a horse when n horses are brought. "
            "What is the value of c(8)?"),
      choices=["8", "12", "15", "20"], correct="C",
      check="120 divided by 8 is 15."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of x and the corresponding values of the function f."
            + table(["x", "f(x)"], [["2", "7"], ["3", "0"], ["4", "-5"], ["5", "-8"]])
            + "What is the value of f(5) - f(2)?"),
      choices=["-15", "-1", "1", "15"], correct="A",
      check="f(5) is -8 and f(2) is 7, so the difference is -15."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A farrier's gauge setting n satisfies (n - 9)(n + 4) = 0, and n is positive. What is "
            "the value of n?"),
      choices=["4", "5", "9", "36"], correct="C",
      check="The solutions are 9 and -4, and only 9 is positive."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("The length n, in yards, of one side of a drove pen satisfies \\(n^{2}+3n=54\\), and "
            "n is positive. What is the value of n?"),
      answers=["6"],
      check="n^2 + 3n - 54 = (n+9)(n-6), whose positive root is 6."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table records the number of horseshoes made at four forges in one month."
            + table(["Forge", "Horseshoes made"],
                    [["Ashfield", "148"], ["Barlow", "96"],
                     ["Colne", "132"], ["Dell", "87"]])
            + "How many more horseshoes did the Colne forge make than the Barlow forge?"),
      choices=["24", "36", "52", "61"], correct="B",
      check="132 - 96 = 36."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table records the number of cattle counted at four stances along a drovers' road "
            "on one night."
            + table(["Stance", "Cattle counted"],
                    [["Errick", "176"], ["Fallow", "208"],
                     ["Glenmore", "149"], ["Hartrigg", "231"]])
            + "At which stance were the most cattle counted?"),
      choices=["Errick", "Fallow", "Glenmore", "Hartrigg"], correct="D",
      check="231 is the largest of the four counts, and it belongs to Hartrigg."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A farrier's keg holds 40 fore shoes and 60 hind shoes and nothing else. One shoe is "
            "taken out of the keg at random. What is the probability that it is a fore shoe?"),
      choices=["\\(\\frac{1}{40}\\)", "\\(\\frac{2}{5}\\)",
               "\\(\\frac{3}{5}\\)", "\\(\\frac{2}{3}\\)"], correct="B",
      check="40 of the 100 shoes are fore shoes, and 40/100 = 2/5."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A drover recorded the number of sheep lost on four separate droves as 8, 11, 5 and "
            "12. What is the mean of these four numbers?"),
      choices=["9", "10", "11", "12"], correct="A",
      check="The total is 36 and 36/4 = 9."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A farrier uses 32 nails for every 4 horseshoes fitted. At that rate, how many nails "
            "are used for 28 horseshoes?"),
      choices=["196", "210", "224", "252"], correct="C",
      check="32/4 = 8 nails a shoe, and 8(28) = 224."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular drove pen is 45 yards long, and the fence right round it measures 146 "
            "yards. How wide is the pen, in yards?"),
      answers=["28"],
      check="146 - 2(45) = 56 for the two widths, so each width is 28 yards."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A watering trough at a forge is a rectangular box 6 feet long and 2 feet wide, and "
            "it holds 18 cubic feet of water when it is full to the brim. How deep is the trough, "
            "in feet?"),
      choices=["1", "1.25", "1.5", "2"], correct="C",
      check="18 divided by 6(2) = 12 gives a depth of 1.5 feet."),

 dict(n="H2E-21", domain="GT", skill="GT-LA", type="MC",
      stem=("A farrier lays three bars flat on one side of a straight edge so that they all meet "
            "it at the same point. The three angles they make with the straight edge and with "
            "one another measure 38&deg;, 65&deg; and x&deg;, and together they make up the "
            "straight angle. What is the value of x?"),
      choices=["67", "77", "87", "103"], correct="B",
      check="180 - 38 - 65 = 77."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A right triangle is set out on a forge floor. Its two legs measure 9 units and 40 "
            "units. What is the tangent of the angle opposite the shorter leg?"),
      choices=["\\(\\frac{9}{40}\\)", "\\(\\frac{40}{9}\\)",
               "\\(\\frac{9}{41}\\)", "\\(\\frac{40}{41}\\)"], correct="A",
      check="The tangent is the opposite leg over the adjacent leg, or 9/40."),
]


# ---------------------------------------------------------- Module 2 (Hard)
# Settings: toll gates, turnpike trusts and toll houses.
MODULE_2_HARD = [

 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the system of equations below, a and b are constants."
            "<br/>\\(x+2y=a\\)<br/>\\(3x-y=b\\)<br/>"
            "What is x in terms of a and b?"),
      choices=["\\(\\frac{a+2b}{7}\\)", "\\(\\frac{a-2b}{7}\\)",
               "\\(\\frac{3a+b}{7}\\)", "\\(\\frac{a+2b}{5}\\)"], correct="A",
      check="Doubling the second equation and adding gives 7x = a + 2b."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the equation \\(\\frac{x}{a}-\\frac{x}{3a}=8\\), a is a positive constant. What "
            "is x in terms of a?"),
      choices=["\\(6a\\)", "\\(12a\\)", "\\(24a\\)", "\\(\\frac{a}{12}\\)"], correct="B",
      check="The left side is 2x/(3a), so 2x = 24a and x = 12a."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("For a linear function f, the difference f(n + 1) - f(n) equals -7 for every value of "
            "n, and f(3) = 20. What is the value of f(11)?"),
      choices=["-36", "-34", "76", "90"], correct="A",
      check="f falls 7 per unit and 11 is 8 units beyond 3, so f(11) = 20 - 56 = -36."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A turnpike trust's surveyor may spend on repairs no more than a ceiling of "
            "\\((40m+180)\\) pounds for m miles of road, and the sum he actually needs is "
            "\\((52m-96)\\) pounds. What is the greatest whole number of miles for which the sum "
            "he needs is below the ceiling?"),
      choices=["21", "22", "23", "24"], correct="B",
      check="52m - 96 < 40m + 180 gives 12m < 276 and m < 23, so 22 miles."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A turnpike trust lets two of its gates for a year. The rent of the first gate "
            "exceeds twice the rent of the second by &pound;35, and the two rents come to "
            "&pound;470 together. What is the rent, in pounds, of the first gate?"),
      answers=["325"],
      check="With s the second rent, (2s + 35) + s = 470 gives s = 145 and the first rent is 325."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The function f is linear, f(2) is three times f(0), and f(4) = 25. What is the value "
            "of f(0)?"),
      choices=["3", "4", "5", "6"], correct="C",
      check="With f = mx + b, 2m + b = 3b makes m = b, so f(4) = 5b = 25 and b = 5."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("In the inequality ax - b &gt; c, the constant a is negative. Which of the following "
            "describes all values of x that satisfy the inequality?"),
      choices=["\\(x>\\frac{b+c}{a}\\)", "\\(x<\\frac{c-b}{a}\\)",
               "\\(x<\\frac{b+c}{a}\\)", "\\(x>\\frac{b-c}{a}\\)"], correct="C",
      check="ax > b + c, and dividing by a negative a reverses the sign to x < (b+c)/a."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g are defined by \\(f(x)=2x-5\\) and \\(g(x)=x^{2}+3\\). Which "
            "expression is equivalent to g(f(x))?"),
      choices=["\\(2x^{2}+1\\)", "\\(4x^{2}+28\\)", "\\(4x^{2}-20x+22\\)",
               "\\(4x^{2}-20x+28\\)"], correct="D",
      check="g(f(x)) = (2x-5)^2 + 3 = 4x^2 - 20x + 25 + 3."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\sqrt{18x^{5}}\\), where x is positive?"),
      choices=["\\(2x^{2}\\sqrt{3x}\\)", "\\(3x^{2}\\sqrt{2x}\\)",
               "\\(9x^{2}\\sqrt{2x}\\)", "\\(3x^{2}\\sqrt{2}\\)"], correct="B",
      check="18x^5 = 9x^4 times 2x, and the square root of 9x^4 is 3x^2."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the equation \\(x^{2}+kx+36=0\\), k is a positive integer and the equation has "
            "two distinct real solutions. What is the least possible value of k?"),
      choices=["12", "13", "18", "37"], correct="B",
      check="Two distinct real solutions need k^2 - 144 > 0, so k > 12 and the least integer is "
            "13."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A quantity is modelled by \\(N=N_{0}(2)^{\\frac{t}{6}}\\), where \\(N_{0}\\) is a "
            "positive constant and t is measured in years. What is the least positive value of t "
            "for which the model gives N equal to eight times \\(N_{0}\\)?"),
      choices=["18", "24", "36", "48"], correct="A",
      check="2^(t/6) = 8 = 2^3 gives t/6 = 3 and t = 18."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{2}{x-3}-\\frac{5}{x+2}\\), where "
            "\\(x\\ne 3\\) and \\(x\\ne -2\\)?"),
      choices=["\\(\\frac{-3}{x^{2}-x-6}\\)", "\\(\\frac{19-3x}{x^{2}+x-6}\\)",
               "\\(\\frac{3x-19}{x^{2}-x-6}\\)", "\\(\\frac{19-3x}{x^{2}-x-6}\\)"], correct="D",
      check="Over the common denominator (x-3)(x+2) the numerator is 2(x+2) - 5(x-3) = 19 - 3x."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NF", type="FR",
      stem=("A turnpike trust's clerk works out a gate's rent with the function h defined by "
            "\\(h(x)=\\frac{5x-3}{2}\\). If h(a) = 16, what is the value of h(a + 4)?"),
      answers=["26"],
      check="5a - 3 = 32 gives a = 7, and h(11) = (55-3)/2 = 26."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A turnpike trust's gatekeeper recorded every vehicle that passed one gate in a week, "
            "noting the kind of vehicle and whether the driver paid the single toll or produced a "
            "composition ticket."
            + table(["Vehicle", "Single toll", "Composition ticket", "Total"],
                    [["Waggon", "42", "78", "120"], ["Gig", "55", "25", "80"],
                     ["Cart", "90", "60", "150"], ["Total", "187", "163", "350"]])
            + "One of the waggons recorded that week is selected at random. What is the "
              "probability that its driver produced a composition ticket?"),
      choices=["\\(\\frac{39}{175}\\)", "\\(\\frac{12}{35}\\)",
               "\\(\\frac{13}{20}\\)", "\\(\\frac{78}{163}\\)"], correct="C",
      check="Of the 120 waggons, 78 produced a ticket, and 78/120 = 13/20."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives a turnpike trust's receipts from one gate in each of four years."
            + table(["Year", "Receipts (&pound;)"],
                    [["1826", "640"], ["1827", "704"], ["1828", "792"], ["1829", "848"]])
            + "By what percentage did the receipts from this gate increase from 1826 to 1829?"),
      choices=["24.5%", "26%", "30%", "32.5%"], correct="D",
      check="The increase is 848 - 640 = 208, and 208/640 = 0.325."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A turnpike surveyor metals a road with a mixture of broken stone and gravel in the "
            "ratio 5 to 3 by weight. He has 6 tons of broken stone and gravel enough for any "
            "quantity, and metalling one mile of road takes 2.4 tons of the mixture. How many "
            "miles can he metal before the broken stone runs out?"),
      choices=["3", "3.75", "4", "5"], correct="C",
      check="6 tons of stone makes 6(8/5) = 9.6 tons of mixture, and 9.6/2.4 = 4 miles."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A turnpike trust's surveyor reports that a new toll house will cost &pound;860, with "
            "a margin of error of &pound;45. Which inequality gives all costs c, in pounds, that "
            "are consistent with the surveyor's report?"),
      choices=["\\(|c-860|\\le 45\\)", "\\(|c-45|\\le 860\\)",
               "\\(|c+860|\\le 45\\)", "\\(|c-860|\\ge 45\\)"], correct="A",
      check="The cost lies within 45 pounds of 860, which is |c - 860| <= 45."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the toll, in pence, charged at one turnpike gate for a waggon drawn "
            "by h horses, and the toll is exactly a linear function of h."
            + table(["Horses, h", "Toll (pence)"],
                    [["1", "6"], ["2", "10"], ["3", "14"], ["4", "18"]])
            + "According to this linear function, what toll would be charged for a waggon drawn "
              "by 7 horses?"),
      choices=["26", "28", "30", "32"], correct="C",
      check="The toll rises 4 pence a horse from a base of 2 pence, so 4(7) + 2 = 30."),

 dict(n="H2H-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A turnpike trust's plot of ground is right triangle ABC, with the right angle at B, "
            "the side AB measuring 9 rods and the side BC measuring 12 rods. Point D lies on side "
            "AC so that the segment BD meets AC at a right angle. What is the length, in rods, of "
            "BD?"),
      choices=["6", "7.2", "7.5", "8"], correct="B",
      check="The area is 54 square rods and AC is 15 rods, so BD = 2(54)/15 = 7.2 rods."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A toll house's rainwater cistern is a right circular cylinder of radius r and height "
            "h, open at the top. Which expression gives the combined area of the base of the "
            "cistern and its curved side?"),
      choices=["\\(\\pi r^{2}h\\)", "\\(\\pi r^{2}+\\pi rh\\)",
               "\\(2\\pi r^{2}+2\\pi rh\\)", "\\(\\pi r^{2}+2\\pi rh\\)"], correct="D",
      check="The base is a circle of area pi r^2 and the curved side unrolls to a rectangle of "
            "area 2 pi r h."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A turnpike surveyor sets out a right-angled triangular plot ABC in which the right "
            "angle is at C, the hypotenuse AB measures 27 rods, and \\(\\sin A=\\frac{2}{3}\\). "
            "What is the area of the plot, in square rods?"),
      choices=["\\(81\\sqrt{5}\\)", "\\(162\\sqrt{5}\\)",
               "\\(81\\sqrt{3}\\)", "\\(243\\)"], correct="A",
      check="BC = 27(2/3) = 18 and AC = sqrt(729-324) = 9 sqrt(5), so the area is 81 sqrt(5)."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("The metalling of a turnpike road has a cross-section in the shape of a trapezium: it "
            "is 24 feet wide across the top, 30 feet wide across the bottom, and 10 inches deep. "
            "What is the area of this cross-section, in square feet?"),
      answers=["22.5", "45/2"],
      check="10 inches is 5/6 of a foot, and (24+30)/2 x 5/6 = 27(5/6) = 22.5 square feet."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
