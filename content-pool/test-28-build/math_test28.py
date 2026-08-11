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
                choices, a composed function, conditioned systems, a two-way
                table, and geometry that chains two relationships.

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
      stem=("A coach proprietor pays &pound;264 a week for the keep of his horses and a further "
            "&pound;3 every time a fresh team is put to. The coach runs 5 journeys a week and "
            "takes a fresh team 4 times on each journey. Every passenger pays &pound;9. How many "
            "passengers must be carried in a week for the week's takings to exceed the week's "
            "outgoings by more than &pound;150?"),
      choices=["52", "53", "54", "55"], correct="B",
      check="Outgoings are 264 + 3(20) = 324, and 9p - 324 > 150 gives p > 52.6..., so 53."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A coachbuilder estimates the cost C, in pounds, of a new body as C = 14L + 9w + 60, "
            "where L is the length of the body in feet and w is the number of window lights "
            "glazed into it. Which equation gives w in terms of C and L?"),
      choices=["\\(w=\\frac{C-14L-60}{9}\\)", "\\(w=\\frac{C-14L+60}{9}\\)",
               "\\(w=\\frac{C+14L-60}{9}\\)", "\\(w=\\frac{C-60}{9}-14L\\)"], correct="A",
      check="Subtracting 14L and 60 from both sides gives 9w = C - 14L - 60."),

 dict(n="H1-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A gauge in a coachbuilder's shop passes an axle-arm only when its diameter d, in "
            "millimetres, satisfies \\(|2d-104|\\le 1.6\\). What is the greatest diameter, in "
            "millimetres, that the gauge passes?"),
      choices=["51.2", "52.4", "52.8", "53.6"], correct="C",
      check="The condition is equivalent to 51.2 <= d <= 52.8, so the greatest is 52.8."),

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
      stem=("In the equation \\(x^{2}-14x+k=0\\), k is a constant. The equation has exactly one "
            "real solution. What is the value of k?"),
      choices=["7", "14", "49", "196"], correct="C",
      check="One real solution needs 14^2 - 4k = 0, so k = 49."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{(4a^{3}b)^{2}}{8a^{2}b^{5}}\\), where a "
            "and b are positive?"),
      choices=["\\(\\frac{2a^{4}}{b^{3}}\\)", "\\(\\frac{2a^{4}}{b^{4}}\\)",
               "\\(\\frac{a^{4}}{2b^{3}}\\)", "\\(\\frac{2a^{6}}{b^{3}}\\)"], correct="A",
      check="The numerator is 16a^6 b^2, and dividing by 8a^2 b^5 leaves 2a^4 over b^3."),

 dict(n="H1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A coachyard's stock of seasoned ash for door pillars is modelled by "
            "\\(S=320\\left(\\frac{3}{4}\\right)^{q}\\), where S is the number of lengths in "
            "stock and q is the number of quarters since the stock was last made up. After how "
            "many quarters does the model give a stock of 135 lengths?"),
      choices=["2", "3", "4", "5"], correct="B",
      check="135/320 = 27/64, which is (3/4)^3, so q = 3."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("What is the solution to the equation \\(\\sqrt{2x+11}=x-2\\)?"),
      answers=["7"],
      check="Squaring gives x^2 - 6x - 7 = 0, whose roots are 7 and -1; only 7 makes x-2 "
            "non-negative."),

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
      stem=("Over 9 journeys a coach carried a mean of 14 parcels a journey. Over the first 5 of "
            "those journeys it carried a mean of 11 parcels a journey. What was the mean number "
            "of parcels a journey over the remaining 4 journeys?"),
      choices=["17", "17.5", "17.75", "18"], correct="C",
      check="The total is 126 and the first five account for 55, so the remaining four average "
            "71/4 = 17.75."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A coachbuilder's shop uses 7 pints of body varnish for every 4 door panels it "
            "finishes. Varnish is bought only in casks holding 12 pints. What is the smallest "
            "number of casks that must be bought to finish 96 door panels?"),
      choices=["11", "12", "13", "14"], correct="D",
      check="96 panels need 24 lots of 7 pints, or 168 pints, and 168/12 = 14 casks exactly."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-ST", type="MC",
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
      stem=("Two straight iron stays cross one another inside a coach body. One of the four "
            "angles they make measures \\((3x+14)^{\\circ}\\) and the angle vertically opposite "
            "to it measures \\((5x-26)^{\\circ}\\). What is the measure of an angle adjacent to "
            "these two?"),
      choices=["64&deg;", "74&deg;", "96&deg;", "106&deg;"], correct="D",
      check="3x + 14 = 5x - 26 gives x = 20 and an angle of 74 degrees, so an adjacent angle is "
            "180 - 74 = 106 degrees."),

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
      stem=("What value of x satisfies the equation \\(\\frac{x}{5}+4=13\\)?"),
      choices=["30", "35", "40", "45"], correct="D",
      check="x/5 = 9, so x = 45."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("What value of p satisfies the equation 8p = 5p + 51?"),
      answers=["17"],
      check="3p = 51, so p = 17."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The number N of horseshoe nails left in a farrier's keg after d days of work is "
            "given by N = 900 - 45d. How many nails are left after 12 days?"),
      choices=["300", "360", "420", "540"], correct="B",
      check="900 - 45(12) = 900 - 540 = 360."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("For a linear function f, f(0) = 13 and f(4) = 41. What is the value of f(2)?"),
      choices=["24", "27", "30", "34"], correct="B",
      check="f rises 28 over 4 units, so f(2) = 13 + 2(7) = 27."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Which of the following values of x satisfies the inequality 4x - 7 &gt; 21?"),
      choices=["5", "6", "7", "8"], correct="D",
      check="4x > 28 gives x > 7, and 8 is the only listed value greater than 7."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A stance beside a drovers' road holds no more than 240 sheep, and 156 sheep have "
            "already been turned onto it. Which inequality gives all possible numbers s of "
            "further sheep that may be turned onto the stance?"),
      choices=["\\(s\\le 84\\)", "\\(s\\ge 84\\)", "\\(s\\le 396\\)", "\\(s\\ge 396\\)"],
      correct="A",
      check="156 + s <= 240 gives s <= 84."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to 5(2x + 7) - 3x?"),
      choices=["7x + 35", "7x + 7", "13x + 35", "10x + 4"], correct="A",
      check="5(2x+7) = 10x + 35, and 10x + 35 - 3x = 7x + 35."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to (x + 6)(x - 2)?"),
      choices=["\\(x^{2}-12\\)", "\\(x^{2}+8x-12\\)", "\\(x^{2}-4x-12\\)",
               "\\(x^{2}+4x-12\\)"], correct="D",
      check="The product is x^2 - 2x + 6x - 12 = x^2 + 4x - 12."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=x^{2}-5\\). What is the value of f(4)?"),
      choices=["3", "11", "16", "27"], correct="B",
      check="4^2 - 5 = 11."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of x and the corresponding values of the function f."
            + table(["x", "f(x)"], [["2", "7"], ["3", "0"], ["4", "-5"], ["5", "-8"]])
            + "For which value of x in the table is f(x) equal to 0?"),
      choices=["2", "3", "4", "5"], correct="B",
      check="The row with f(x) = 0 is the row for x = 3."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("If (n - 9)(n + 4) = 0 and n is positive, what is the value of n?"),
      choices=["4", "5", "9", "36"], correct="C",
      check="The solutions are 9 and -4, and only 9 is positive."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("If \\(\\sqrt{x}=12\\), what is the value of x?"),
      answers=["144"],
      check="Squaring both sides gives x = 144."),

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
      stem=("On five days a farrier shod 9, 12, 7, 12 and 15 horses. What is the median of these "
            "five numbers?"),
      choices=["7", "11", "12", "15"], correct="C",
      check="In order the values are 7, 9, 12, 12, 15, and the middle value is 12."),

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
      stem=("A stance beside a drovers' road is a rectangle 45 yards long and 28 yards wide. What "
            "is its area, in square yards?"),
      answers=["1260"],
      check="45(28) = 1,260 square yards."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A watering trough at a forge is a rectangular box 6 feet long, 2 feet wide and 1.5 "
            "feet deep. What is its volume, in cubic feet?"),
      choices=["9", "12", "18", "24"], correct="C",
      check="6(2)(1.5) = 18 cubic feet."),

 dict(n="H2E-21", domain="GT", skill="GT-LA", type="MC",
      stem=("In a triangle, two of the angles measure 43&deg; and 68&deg;. What is the measure of "
            "the third angle?"),
      choices=["59&deg;", "69&deg;", "79&deg;", "111&deg;"], correct="B",
      check="180 - 43 - 68 = 69 degrees."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("In a right triangle, the leg opposite one of the acute angles is 7 units long and "
            "the hypotenuse is 25 units long. What is the sine of that acute angle?"),
      choices=["\\(\\frac{7}{25}\\)", "\\(\\frac{24}{25}\\)",
               "\\(\\frac{7}{24}\\)", "\\(\\frac{25}{7}\\)"], correct="A",
      check="The sine is the opposite leg over the hypotenuse, or 7/25."),
]


# ---------------------------------------------------------- Module 2 (Hard)
# Settings: toll gates, turnpike trusts and toll houses.
MODULE_2_HARD = [

 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the system of equations below, k is a constant and the system has infinitely many "
            "solutions.<br/>\\(3x+ky=18\\)<br/>\\(9x+12y=54\\)<br/>What is the value of k?"),
      choices=["3", "4", "6", "12"], correct="B",
      check="The second equation is 3 times 3x + 4y = 18, so k must be 4."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the equation \\(\\frac{x}{a}-\\frac{x}{3a}=8\\), a is a positive constant. What "
            "is x in terms of a?"),
      choices=["\\(12a\\)", "\\(6a\\)", "\\(24a\\)", "\\(\\frac{a}{12}\\)"], correct="A",
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
      stem=("In the xy-plane, the line \\(y=ax+b\\) passes through the points \\((-2,11)\\) and "
            "\\((4,-7)\\), where a and b are constants. What is the value of a + b?"),
      choices=["-2", "1", "2", "8"], correct="C",
      check="The slope is -18/6 = -3 and the intercept is 11 - (-3)(-2) = 5, so a + b = 2."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Which of the following describes all values of x that satisfy "
            "\\(-3\\le 2-5x\\le 17\\)?"),
      choices=["\\(-3\\le x\\le 1\\)", "\\(-1\\le x\\le 3\\)",
               "\\(1\\le x\\le 5\\)", "\\(-3\\le x\\le 5\\)"], correct="A",
      check="Subtracting 2 gives -5 <= -5x <= 15, and dividing by -5 reverses both signs to "
            "-3 <= x <= 1."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g are defined by \\(f(x)=2x-5\\) and \\(g(x)=x^{2}+3\\). Which "
            "expression is equivalent to g(f(x))?"),
      choices=["\\(2x^{2}+1\\)", "\\(4x^{2}+28\\)", "\\(4x^{2}-20x+28\\)",
               "\\(4x^{2}-20x+22\\)"], correct="C",
      check="g(f(x)) = (2x-5)^2 + 3 = 4x^2 - 20x + 25 + 3."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{1}{a}+\\frac{1}{a+3}\\), where a is "
            "positive?"),
      choices=["\\(\\frac{2a+3}{a^{2}+3a}\\)", "\\(\\frac{2}{a^{2}+3a}\\)",
               "\\(\\frac{1}{2a+3}\\)", "\\(\\frac{2a+3}{a+3}\\)"], correct="A",
      check="Over the common denominator a(a+3) the numerator is (a+3) + a = 2a + 3."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("What is the sum of the solutions to the equation \\(\\frac{12}{x-2}=x+3\\)?"),
      choices=["-3", "-1", "1", "3"], correct="B",
      check="Clearing the denominator gives x^2 + x - 18 = 0, whose two solutions sum to -1."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A quantity is modelled by \\(N=N_{0}(2)^{\\frac{t}{6}}\\), where \\(N_{0}\\) is a "
            "positive constant and t is measured in years. What is the least positive value of t "
            "for which the model gives N equal to eight times \\(N_{0}\\)?"),
      choices=["12", "18", "24", "48"], correct="B",
      check="2^(t/6) = 8 = 2^3 gives t/6 = 3 and t = 18."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{x^{2}-9}{x^{2}+x-12}\\), where "
            "\\(x\\ne 3\\) and \\(x\\ne -4\\)?"),
      choices=["\\(\\frac{x-3}{x+4}\\)", "\\(\\frac{x+3}{x-4}\\)",
               "\\(\\frac{x-3}{x-4}\\)", "\\(\\frac{x+3}{x+4}\\)"], correct="D",
      check="The numerator is (x-3)(x+3) and the denominator is (x-3)(x+4), leaving (x+3)/(x+4)."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NF", type="FR",
      stem=("The function h is defined by \\(h(x)=\\frac{5x-3}{2}\\). If h(a) = 16, what is the "
            "value of h(a + 4)?"),
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
      stem=("In triangle ABC, point D lies on side AB and point E lies on side AC so that segment "
            "DE is parallel to side BC. The length of AD is 6, the length of DB is 9, and the "
            "length of DE is 8. What is the length of BC?"),
      choices=["12", "14", "18", "20"], correct="D",
      check="AD/AB = 6/15 = 2/5, so BC = 8(5/2) = 20."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A toll house has a rainwater cistern in the shape of a right circular cylinder of "
            "radius r and height h. A second cistern is a right circular cylinder whose radius is "
            "twice r and whose height is half of h. The volume of the second cistern is how many "
            "times the volume of the first?"),
      choices=["1", "2", "4", "8"], correct="B",
      check="The ratio is (2r)^2(h/2) divided by r^2 h, which is 4 times one half, or 2."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC, the right angle is at C, the length of hypotenuse AB is 27, "
            "and \\(\\sin A=\\frac{2}{3}\\). What is the area of triangle ABC?"),
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
