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
      stem=("A booking clerk pays over two fifths of a day's takings to the coach proprietor, "
            "then pays &pound;7 out of what is left for stabling, and &pound;53 remains in the "
            "box. What were the day's takings, in pounds?"),
      choices=["&pound;100", "&pound;110", "&pound;120", "&pound;150"], correct="A",
      check="Three fifths of the takings less 7 leaves 53, so three fifths of the takings is 60 "
            "and the takings are 100 pounds."),

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
      stem=("Of the places on a coach, three eighths were taken at the head office. Of the places "
            "still unsold after that, 20 were taken at wayside offices and 5 were never sold at "
            "all. How many places does the coach carry?"),
      choices=["40", "45", "56", "64"], correct="A",
      check="Five eighths of the places were still unsold after the head office, and those came "
            "to 20 + 5 = 25, so the coach carries 25(8/5) = 40 places."),


 dict(n="H1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a posting house the horses are kept in three stables, and the numbers in the "
            "three stables are in the ratio 2 to 3 to 5. The largest stable holds 18 more horses "
            "than the smallest. How many horses are kept at the posting house altogether?"),
      choices=["45", "60", "72", "90"], correct="B",
      check="The largest exceeds the smallest by 3 parts, so one part is 6 horses and the ten "
            "parts come to 60."),


 dict(n="H1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Two coachbuilders each price a new body as a fixed sum together with a charge for "
            "every window light glazed into it. Alder charges &pound;54 plus &pound;3 for each "
            "light, and Birch charges &pound;30 plus &pound;5 for each light. For how many "
            "lights do the two builders charge the same?"),
      choices=["6", "8", "10", "12"], correct="D",
      check="54 + 3n = 30 + 5n gives 2n = 24 and n = 12."),

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
      stem=("A coachbuilder's costing rule leads to the equation \\(2x^{2}-11x+k=0\\), where k "
            "is a constant, and one of its solutions is \\(x=4\\). What is the other "
            "solution?"),
      choices=["\\(\\frac{2}{3}\\)", "\\(\\frac{4}{3}\\)",
               "\\(\\frac{3}{2}\\)", "\\(3\\)"], correct="C",
      check="Putting x = 4 gives 32 - 44 + k = 0, so k = 12, and 2x^2 - 11x + 12 factors as "
            "(2x-3)(x-4), whose other root is 3/2."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A coachbuilder's timber allowance for a body is given by the expression "
            "\\(4x^{3}+6x^{2}-10x\\). Which of the following expresses that allowance as a "
            "product of three factors?"),
      choices=["\\(2x(2x+5)(x-1)\\)", "\\(2x(2x-5)(x+1)\\)",
               "\\(2x(x+5)(2x-1)\\)", "\\(2x(2x+1)(x-5)\\)"], correct="A",
      check="Taking out 2x leaves 2x(2x^2+3x-5), and 2x^2+3x-5 factors as (2x+5)(x-1)."),


 dict(n="H1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of days a posting house's stock of oats lasts varies inversely with the "
            "number of horses stabled there. The stock lasts 24 horses 15 days. For how many "
            "days would the same stock last 40 horses?"),
      choices=["8", "9", "12", "25"], correct="B",
      check="Inverse variation makes the product constant, and 24(15) = 360, so 360/40 = 9 "
            "days."),

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
      stem=("A coachyard keeps 63 lamps, of which 28 are brass and the rest are japanned. Three "
            "quarters of the brass lamps and two fifths of the japanned lamps were repaired this "
            "season. One of the 63 lamps is selected at random. What is the probability that it "
            "was repaired this season?"),
      choices=["\\(\\frac{1}{3}\\)", "\\(\\frac{4}{9}\\)",
               "\\(\\frac{1}{2}\\)", "\\(\\frac{5}{9}\\)"], correct="D",
      check="21 of the 28 brass lamps and 14 of the 35 japanned lamps were repaired, so 35 of 63, "
            "or 5/9."),

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
      stem=("The imperial on a coach roof is a rectangular box 48 inches long, 24 inches wide and "
            "18 inches deep, and a second rectangular box 24 inches long, 24 inches wide and 12 "
            "inches deep stands on top of it. One cubic foot is 1,728 cubic inches. What is the "
            "combined volume of the two boxes, in cubic feet?"),
      answers=["16"],
      check="48(24)(18) = 20,736 and 24(24)(12) = 6,912, and 27,648/1,728 = 16 cubic feet."),

]


# ---------------------------------------------------------- Module 2 (Easy)
# Settings: farriery and horseshoeing, drovers' roads and stances.
MODULE_2_EASY = [


 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A farrier charges 9 pence for each horse he shoes all round and 4 pence for each "
            "horse he shoes before only. In one day he shoes b horses all round and f horses "
            "before only. Which expression gives his takings for that day, in pence?"),
      choices=["9b + 4f", "4b + 9f", "13bf", "13(b + f)"], correct="A",
      check="Nine pence for each of b horses and four pence for each of f horses come to "
            "9b + 4f pence."),

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
      stem=("The table gives a farrier's charge, in shillings, for shoeing n horses at one "
            "visit, and the charge rises by the same amount for every additional horse."
            + table(["Horses, n", "Charge (shillings)"],
                    [["2", "26"], ["5", "50"], ["8", "74"]])
            + "By how many shillings does the charge rise for each additional horse?"),
      choices=["4", "6", "7", "8"], correct="D",
      check="The charge rises 24 shillings over 3 horses, so it rises 8 shillings a horse."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A farrier's rule for the number h of horses he will undertake to shoe in one day is "
            "that h must satisfy 4h - 7 &gt; 21. Which of the following values of h satisfies "
            "that inequality?"),
      choices=["5", "6", "7", "8"], correct="D",
      check="4h > 28 gives h > 7, and 8 is the only listed value greater than 7."),


 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A stance charges 3 pence for each head of cattle turned onto it, together with 20 "
            "pence for the use of the pen. A drover has 140 pence to spend. Which inequality "
            "gives all possible numbers h of head that he can turn onto the stance?"),
      choices=["\\(3h+20\\le 140\\)", "\\(3h+20\\ge 140\\)",
               "\\(20h+3\\le 140\\)", "\\(3h-20\\le 140\\)"], correct="A",
      check="The pen costs 20 pence and each head 3 pence, so 3h + 20 must be at most 140."),


 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A farrier writes the iron allowance for a set of shoes as \\(8a^{2}b-12ab^{2}\\). "
            "Which expression is equivalent to that allowance?"),
      choices=["\\(4ab(2a+3b)\\)", "\\(4ab(2a-3b)\\)",
               "\\(4a^{2}b^{2}(2a-3b)\\)", "\\(2ab(4a-6)\\)"], correct="B",
      check="4ab divides both terms, leaving 4ab(2a - 3b)."),


 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A square drove pen has sides of length \\(x-5\\) yards. Which expression is "
            "equivalent to the area of the pen, in square yards?"),
      choices=["\\(x^{2}-25\\)", "\\(x^{2}+25\\)", "\\(x^{2}-5x+25\\)",
               "\\(x^{2}-10x+25\\)"], correct="D",
      check="(x-5)(x-5) = x^2 - 5x - 5x + 25 = x^2 - 10x + 25."),


 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of lambs in a drover's fold is modelled by the function f defined by "
            "\\(f(x)=5(3)^{x}\\), where x is the number of seasons since the fold was made up. "
            "What is the value of f(0)?"),
      choices=["0", "3", "5", "15"], correct="C",
      check="3 raised to the power 0 is 1, so f(0) = 5(1) = 5."),


 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A farrier's rasp gauge is worked out with \\(g(x)=\\frac{9}{x-4}\\), and one line of "
            "the printed gauge has had to be left blank. For what value of x is \\(g(x)\\) "
            "undefined?"),
      choices=["4", "0", "9", "-4"], correct="A",
      check="The quotient is undefined only where the denominator is 0, that is where x = 4."),

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
                    [["Ashfield", "90"], ["Barlow", "60"],
                     ["Colne", "120"], ["Dell", "30"]])
            + "What fraction of all the horseshoes made that month were made at the Colne "
              "forge?"),
      choices=["\\(\\frac{1}{4}\\)", "\\(\\frac{2}{5}\\)",
               "\\(\\frac{1}{2}\\)", "\\(\\frac{3}{5}\\)"], correct="B",
      check="The four forges made 300 in all and Colne made 120, and 120/300 = 2/5."),

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
      stem=("Of the 80 horses brought to a fair, 24 had been newly shod. One of the 80 horses is "
            "picked at random. What is the probability that it had not been newly shod?"),
      choices=["\\(\\frac{3}{10}\\)", "\\(\\frac{7}{10}\\)",
               "\\(\\frac{2}{5}\\)", "\\(\\frac{3}{4}\\)"], correct="B",
      check="56 of the 80 horses had not been newly shod, and 56/80 = 7/10."),


 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A drover recorded the number of sheep lost on each of seven droves as 5, 8, 5, 12, "
            "9, 5 and 11. Which of these numbers occurs most often in the list?"),
      choices=["5", "8", "9", "11"], correct="A",
      check="5 appears three times and no other number appears more than once."),


 dict(n="H2E-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A drover pays 4 pence for each head of cattle he takes over a private drove road, "
            "and there are 12 pence in one shilling. What does he pay, in shillings, for a drove "
            "of 63 head?"),
      choices=["16", "18", "21", "24"], correct="C",
      check="4(63) = 252 pence, and 252/12 = 21 shillings."),

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
      stem=("Two bars lean against a straight edge from the same point and on the same side of "
            "it, and the two angles they make with the straight edge measure \\((2x)^{\\circ}\\) "
            "and \\((3x+30)^{\\circ}\\). Together the two angles make up the straight angle. What "
            "is the value of x?"),
      choices=["25", "30", "36", "50"], correct="B",
      check="2x + 3x + 30 = 180 gives 5x = 150 and x = 30."),


 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A right triangle is set out on a forge floor. Its two legs measure 20 units and 21 "
            "units. What is the sine of the angle opposite the leg that measures 20 units?"),
      choices=["\\(\\frac{20}{29}\\)", "\\(\\frac{21}{29}\\)",
               "\\(\\frac{20}{21}\\)", "\\(\\frac{29}{20}\\)"], correct="A",
      check="The hypotenuse is sqrt(400+441) = 29, and the sine is the opposite leg over the "
            "hypotenuse, or 20/29."),

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
      stem=("In the xy-plane the line \\(cx-4y=56\\) crosses the x-axis at the point \\((8,0)\\), "
            "where c is a constant. What is the value of c?"),
      choices=["7", "8", "14", "28"], correct="A",
      check="Putting y = 0 and x = 8 gives 8c = 56, so c = 7."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A turnpike trust's surveyor may spend on repairs no more than a ceiling of "
            "\\((40m+180)\\) pounds for m miles of road, and the sum he actually needs is "
            "\\((52m-96)\\) pounds. What is the greatest whole number of miles for which the sum "
            "he needs is below the ceiling?"),
      choices=["21", "22", "23", "24"], correct="B",
      check="52m - 96 < 40m + 180 gives 12m < 276 and m < 23, so 22 miles."),


 dict(n="H2H-05", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The equation \\(4(x-c)=4x-20\\) is true for every value of x, where c is a constant. "
            "What is the value of c?"),
      answers=["5"],
      check="Expanding the left side gives 4x - 4c, so -4c = -20 and c = 5."),


 dict(n="H2H-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The functions f and g are defined by \\(f(x)=3x+7\\) and \\(g(x)=f(x-4)\\). Which "
            "expression defines g(x)?"),
      choices=["\\(3x+3\\)", "\\(3x-12\\)", "\\(3x+11\\)", "\\(3x-5\\)"], correct="D",
      check="g(x) = 3(x-4) + 7 = 3x - 12 + 7 = 3x - 5."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("In the inequality ax - b &gt; c, the constant a is negative. Which of the following "
            "describes all values of x that satisfy the inequality?"),
      choices=["\\(x>\\frac{b+c}{a}\\)", "\\(x<\\frac{b+c}{a}\\)",
               "\\(x<\\frac{c-b}{a}\\)", "\\(x>\\frac{b-c}{a}\\)"], correct="B",
      check="ax > b + c, and dividing by a negative a reverses the sign to x < (b+c)/a."),


 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("For the quadratic function f, \\(f(2)=f(10)\\), and the graph of \\(y=f(x)\\) in the "
            "xy-plane has its vertex at the point \\((h,k)\\). What is the value of h?"),
      choices=["4", "5", "6", "8"], correct="C",
      check="A parabola takes equal values at points equidistant from its axis, so h is the "
            "midpoint of 2 and 10, namely 6."),


 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A turnpike trust's clerk reduces the quantity "
            "\\(\\frac{\\frac{1}{x}+\\frac{1}{3}}{x+3}\\) while casting up a composition, where x "
            "is positive. Which expression is equivalent to that quantity?"),
      choices=["\\(\\frac{1}{3}\\)", "\\(\\frac{x+3}{3x}\\)",
               "\\(\\frac{3x}{x+3}\\)", "\\(\\frac{1}{3x}\\)"], correct="D",
      check="The numerator is (3+x)/(3x), and dividing that by (x+3) leaves 1/(3x)."),


 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The system of equations below has two solutions."
            "<br/>\\(y=x^{2}+2x-3\\)<br/>\\(y=2x+6\\)<br/>"
            "What is the sum of the two y-coordinates of those solutions?"),
      choices=["0", "6", "12", "18"], correct="C",
      check="x^2 + 2x - 3 = 2x + 6 gives x^2 = 9 and x = 3 or x = -3, whose y values are 12 and "
            "0, summing to 12."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A quantity is modelled by \\(N=N_{0}(2)^{\\frac{t}{6}}\\), where \\(N_{0}\\) is a "
            "positive constant and t is measured in years. What is the least positive value of t "
            "for which the model gives N equal to eight times \\(N_{0}\\)?"),
      choices=["18", "24", "36", "48"], correct="A",
      check="2^(t/6) = 8 = 2^3 gives t/6 = 3 and t = 18."),


 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A turnpike gate's letting price is reckoned from \\(\\frac{6x+13}{x+2}\\), where "
            "\\(x\\ne -2\\). Which of the following is equivalent to that reckoning?"),
      choices=["\\(6-\\frac{1}{x+2}\\)", "\\(3+\\frac{7}{x+2}\\)",
               "\\(6+\\frac{13}{x+2}\\)", "\\(6+\\frac{1}{x+2}\\)"], correct="D",
      check="6x + 13 = 6(x+2) + 1, so the quotient is 6 + 1/(x+2)."),


 dict(n="H2H-13", domain="ADV", skill="ADV-NF", type="FR",
      stem=("A turnpike clerk's schedule of gate rents is set out by \\(h(x)=\\frac{24}{x-2}\\). "
            "For what value of x does \\(h(x)=h(10)+1\\)?"),
      answers=["8"],
      check="h(10) = 24/8 = 3, so h(x) = 4, and 24/(x-2) = 4 gives x - 2 = 6 and x = 8."),


 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A turnpike trust's gatekeeper recorded every vehicle that passed one gate in a week, "
            "noting the kind of vehicle and whether the driver paid the single toll or produced a "
            "composition ticket."
            + table(["Vehicle", "Single toll", "Composition ticket", "Total"],
                    [["Waggon", "42", "78", "120"], ["Gig", "55", "25", "80"],
                     ["Cart", "90", "60", "150"], ["Total", "187", "163", "350"]])
            + "What fraction of all the vehicles recorded that week were gigs whose drivers paid "
              "the single toll?"),
      choices=["\\(\\frac{11}{70}\\)", "\\(\\frac{11}{16}\\)",
               "\\(\\frac{8}{35}\\)", "\\(\\frac{55}{187}\\)"], correct="A",
      check="55 of the 350 vehicles were gigs paying the single toll, and 55/350 = 11/70."),


 dict(n="H2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the toll, in pounds, taken at one gate on each of five days of a "
            "week. The entry for Thursday has been rubbed out of the book."
            + table(["Day", "Toll taken (&pound;)"],
                    [["Monday", "34"], ["Tuesday", "29"], ["Wednesday", "41"],
                     ["Thursday", "?"], ["Friday", "46"]])
            + "The five days together yielded &pound;187. What toll was taken on Thursday?"),
      choices=["&pound;32", "&pound;35", "&pound;37", "&pound;39"], correct="C",
      check="The four legible days come to 150 pounds, and 187 - 150 = 37."),

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
      stem=("The table gives the length of road, in miles, under the care of each of four "
            "turnpike trusts in one county."
            + table(["Trust", "Miles of road"],
                    [["Ancaster", "96"], ["Bewdley", "60"],
                     ["Cranfield", "144"], ["Dunmow", "100"]])
            + "What percent of the county's turnpike mileage is under the care of the Cranfield "
              "trust?"),
      choices=["24%", "30%", "36%", "40%"], correct="C",
      check="The four trusts hold 400 miles in all and Cranfield holds 144, and 144/400 = "
            "0.36."),


 dict(n="H2H-19", domain="GT", skill="GT-LA", type="MC",
      stem=("The three sides of a triangular piece of ground beside a toll house measure 9 rods, "
            "14 rods and x rods, where x is a whole number of rods. What is the greatest possible "
            "value of x?"),
      choices=["5", "22", "23", "26"], correct="B",
      check="Any side is shorter than the other two together, so x < 23 and the greatest whole "
            "number is 22."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A toll house's rainwater cistern is a right circular cylinder of radius r and height "
            "h, open at the top. Which expression gives the combined area of the base of the "
            "cistern and its curved side?"),
      choices=["\\(\\pi r^{2}h\\)", "\\(\\pi r^{2}+\\pi rh\\)",
               "\\(2\\pi r^{2}+2\\pi rh\\)", "\\(\\pi r^{2}+2\\pi rh\\)"], correct="D",
      check="The base is a circle of area pi r^2 and the curved side unrolls to a rectangle of "
            "area 2 pi r h."),


 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC the right angle is at C, \\(\\tan A=\\frac{5}{12}\\), and the "
            "side AC measures 12m, where m is a positive constant. What is the length of the "
            "hypotenuse AB in terms of m?"),
      choices=["\\(5m\\)", "\\(13m\\)", "\\(17m\\)", "\\(\\frac{60m}{13}\\)"], correct="B",
      check="The tangent is BC/AC, so BC = 5m, and AB = sqrt((12m)^2 + (5m)^2) = 13m."),


 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A toll gate turns on a circular iron plate of radius 13 inches from which a circular "
            "hole of radius 5 inches has been cut at the centre. The area of the iron that "
            "remains is \\(k\\pi\\) square inches. What is the value of k?"),
      answers=["144"],
      check="The area is pi(13^2) - pi(5^2) = pi(169 - 25) = 144 pi."),

]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
