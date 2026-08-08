#!/usr/bin/env python3
"""
Original Math content for Test 14 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. A constant, a rate or a scale factor has to be
                recovered before the question can be answered; two or three
                steps throughout. Deliberately harder than Module 2 (Easy) and
                below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard. Parameters instead of numbers, structural answers, a
                composed function, a system conditioned on a constant, two
                simultaneous constraints, and geometry needing two
                relationships at once.

Every setting is concrete and deliberately unlike anything already banked in
production (apiary, letterpress shop, lighthouse paraffin store, bell tower
peal, peat core tracer, tunicate colony, cooper's staving hours, vellum
margins, kiln firings). House style follows Test 1/2 — see CLAUDE.md. All LaTeX
is typed by hand; no bulk conversion step was used anywhere in this file.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ---------------------------------------------------------------- Module 1
MODULE_1 = [
 dict(n="G1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An apiary sells jars of blossom honey for $9 each and jars of heather honey for $14 "
            "each. At one market it sold 5 more jars of blossom honey than of heather honey and "
            "took $436 from honey sales altogether. How many jars of heather honey did the apiary "
            "sell?"),
      choices=["13", "17", "22", "25"], correct="B",
      check="9(h+5) + 14h = 23h + 45 = 436, so h = 17."),

 dict(n="G1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A letterpress shop charges a fixed setup price for each poster design plus a fixed "
            "price for each copy printed. An order of 3 designs and 120 copies costs $402, and an "
            "order of 5 designs and 90 copies costs $450. How many dollars does the shop charge to "
            "set up one design?"),
      choices=["$26", "$42", "$48", "$54"], correct="D",
      check="3p+120c=402 and 5p+90c=450 give p = 54 and c = 2."),

 dict(n="G1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A lighthouse keeper's store of paraffin is drawn down at a constant rate through the "
            "season. On day 6 of the season the store held 528 litres, and on day 20 it held 402 "
            "litres. The store is refilled as soon as it falls to 150 litres. On which day of the "
            "season is it refilled?"),
      choices=["36", "42", "48", "54"], correct="C",
      check="Rate = 126/14 = 9 litres per day; 528 - 9(t-6) = 150 gives t = 48."),

 dict(n="G1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A film society has $1,250 for a screening season. It must pay a one-time licence fee "
            "of $290, and it must keep at least $110 of the money unspent for publicity. Each film "
            "print it hires costs $84. What is the greatest number of prints the society can hire?"),
      choices=["9", "10", "11", "13"], correct="B",
      check="290 + 84k <= 1,250 - 110 gives 84k <= 850 and k <= 10.1, so 10 prints."),

 dict(n="G1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A cider press charges a fixed delivery fee plus a constant amount for each crate of "
            "apples pressed. Pressing 14 crates costs $173, and pressing 22 crates costs $261. How "
            "many dollars does the press charge for pressing 30 crates?"),
      choices=["$319", "$330", "$349", "$360"], correct="C",
      check="Slope = 88/8 = 11 per crate and the fee is 19, so 19 + 30(11) = 349."),

 dict(n="G1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A peal rung in a bell tower is made up of two kinds of change. Each plain change takes "
            "4 seconds to ring and each dodging change takes 7 seconds. A peal of 96 changes lasted "
            "507 seconds. How many dodging changes were in that peal?"),
      choices=["33", "41", "55", "63"], correct="B",
      check="p + d = 96 and 4p + 7d = 507 give d = 41."),

 dict(n="G1-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, one edge of a mown strip of lawn lies along the line \\(4x-5y=20\\). "
            "The opposite edge is parallel to that line and passes through the point \\((10,3)\\). "
            "At what y-coordinate does the opposite edge cross the y-axis?"),
      choices=["-13", "-8", "-5", "4"], correct="C",
      check="The slope is 4/5, and 3 = (4/5)(10) + b gives b = -5."),

 dict(n="G1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A telemetry engineer writes the usable bandwidth of a link as "
            "\\(\\frac{6x^{2}-19x+10}{3x-2}\\), where x is the number of channels and \\(x>1\\). "
            "Which expression is equivalent to that bandwidth?"),
      choices=["\\(2x-5\\)", "\\(2x+5\\)", "\\(2x-10\\)", "\\(3x-5\\)"], correct="A",
      check="6x^2-19x+10 factors as (3x-2)(2x-5), so the quotient is 2x-5."),

 dict(n="G1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The height of a stone arch above its springing line, in feet, is modelled by "
            "\\(h(x)=-\\frac{1}{4}(x-6)(x-30)\\), where x is the horizontal distance in feet from a "
            "marker set beside the arch. What is the greatest height, in feet, that the arch "
            "reaches above its springing line?"),
      choices=["24", "36", "48", "54"], correct="B",
      check="The zeros are 6 and 30, so the vertex is at x = 18 and h(18) = -(1/4)(12)(-12) = 36."),

 dict(n="G1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A tracer added to a peat core decays so that the amount of it remaining, in "
            "micrograms, d decades later is \\(A(d)=6{,}250\\left(\\frac{1}{5}\\right)^{d}\\). "
            "After how many decades does this model give 10 micrograms of the tracer?"),
      choices=["2", "3", "4", "5"], correct="C",
      check="6,250/10 = 625 = 5^4, so d = 4."),

 dict(n="G1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The curved edge of a stained-glass panel follows \\(y=x^{2}+2x-15\\) and a strip of "
            "lead came follows \\(y=x+5\\), where x and y are measured in inches. The two curves "
            "meet at two points. What is the product of the x-coordinates of those two points?"),
      choices=["-20", "-5", "-1", "4"], correct="A",
      check="x^2+2x-15 = x+5 gives x^2+x-20 = 0, whose roots -5 and 4 multiply to -20."),

 dict(n="G1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A dye works converts a bath concentration c into a scaled index J using "
            "\\(J=\\frac{5c-12}{3}\\). Which expression gives c in terms of J?"),
      choices=["\\(\\frac{3J+12}{5}\\)", "\\(\\frac{3J-12}{5}\\)", "\\(\\frac{5J+12}{3}\\)",
               "\\(\\frac{J+12}{5}\\)"], correct="A",
      check="3J = 5c - 12, so c = (3J+12)/5."),

 dict(n="G1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A soil scientist models the settlement of a new road bed as \\(g(x)=ax^{2}+7\\), where "
            "a is a constant and x is the number of years since the bed was paved. The model gives "
            "\\(g(3)=-11\\). What is the value of \\(g(6)\\)?"),
      choices=["-119", "-83", "-72", "-65"], correct="D",
      check="9a + 7 = -11 gives a = -2, so g(6) = -2(36) + 7 = -65."),

 dict(n="G1-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A colony of tunicates on a pier piling covers an area that is multiplied by the same "
            "factor every month. The colony covered 12 square centimetres at the start of March and "
            "300 square centimetres at the start of May. According to this model, how many square "
            "centimetres did the colony cover at the start of April?"),
      choices=["60", "96", "150", "156"], correct="A",
      check="The two-month factor is 25, so the monthly factor is 5 and 12(5) = 60."),

 dict(n="G1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A canal barge burns 5 litres of fuel for every 4 kilometres it travels, and fuel costs "
            "$1.80 per litre. How many dollars of fuel does a 96-kilometre trip use?"),
      choices=["$150", "$180", "$196", "$216"], correct="D",
      check="96/4 = 24, so the trip burns 120 litres, and 120(1.80) = 216."),

 dict(n="G1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A ringing station recorded the wingspans, in centimetres, of five kestrels as 68, 71, "
            "74, 74 and 78. A sixth kestrel was then measured, and the mean wingspan of all six "
            "birds was 74 centimetres. What was the wingspan, in centimetres, of the sixth "
            "kestrel?"),
      choices=["70", "74", "76", "79"], correct="D",
      check="6(74) - 365 = 444 - 365 = 79."),

 dict(n="G1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of loaves of each kind that a bakery stall sold on Saturday "
            "and on Sunday of one weekend."
            + table(["Kind of loaf", "Saturday", "Sunday"],
                    [["Rye", "46", "39"], ["Spelt", "58", "63"], ["Barley", "36", "48"]])
            + "Of the loaves the stall sold on Sunday, what percent were spelt?"),
      choices=["32%", "38%", "42%", "45%"], correct="C",
      check="Sunday total is 150 loaves, and 63/150 = 42%."),

 dict(n="G1-18", domain="GT", skill="GT-LA", type="MC",
      stem=("Two straight rafters in a roof truss are parallel, and a tie beam crosses both of "
            "them. On the same side of the tie beam, the angle it makes with one rafter measures "
            "\\((5x+8)\\)&deg; and the angle it makes with the other rafter measures "
            "\\((3x+12)\\)&deg;. What is the value of x?"),
      choices=["10", "20", "22", "25"], correct="B",
      check="Same-side interior angles are supplementary: 8x + 20 = 180 gives x = 20."),

 dict(n="G1-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A rope 18 metres long runs from the top of a flagpole to a point on level ground and "
            "makes an angle of 60&deg; with the ground. How many metres tall is the flagpole?"),
      choices=["\\(9\\)", "\\(9\\sqrt{2}\\)", "\\(9\\sqrt{3}\\)", "\\(18\\sqrt{3}\\)"],
      correct="C",
      check="The height is 18 sin 60 = 9 sqrt(3)."),

 dict(n="G1-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular tank measures 1.2 metres by 0.8 metres by 0.5 metres, and it is filled "
            "to \\(\\frac{3}{4}\\) of its capacity. Given that one cubic metre of water is 1,000 "
            "litres, how many litres of water are in the tank?"),
      answers=["360"],
      check="The tank holds 0.48 cubic metres, or 480 litres, and (3/4)(480) = 360."),

 dict(n="G1-21", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A glaze is mixed from silica, feldspar and whiting in the ratio 5 to 3 to 2 by mass. A "
            "batch of the glaze contains 780 grams of feldspar. What is the total mass, in grams, "
            "of that batch?"),
      answers=["2600"],
      check="780/3 = 260 grams per part, and the batch is 10 parts, so 2,600 grams."),

 dict(n="G1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("Two copper vats are similar solids. The smaller vat stands 12 centimetres tall and "
            "holds 486 millilitres. The larger vat stands 20 centimetres tall. How many millilitres "
            "does the larger vat hold?"),
      answers=["2250"],
      check="The volume ratio is (20/12)^3 = 125/27, and 486(125/27) = 2,250."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="G2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A bookbinder sews 6 signatures into every volume and used 138 signatures in one week, "
            "with none left over. How many volumes did the bookbinder sew that week?"),
      choices=["18", "21", "23", "27"], correct="C",
      check="138/6 = 23."),

 dict(n="G2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A stall sells crab rolls. An order of 4 rolls costs $26, which includes a $2 charge "
            "for the bag. How many dollars does one crab roll cost?"),
      choices=["5", "6", "6.50", "7"], correct="B",
      check="(26-2)/4 = 6."),

 dict(n="G2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A bicycle hire charges a $6 unlocking fee plus $3.50 for each hour the bicycle is "
            "kept. How many dollars does a 5-hour hire cost?"),
      choices=["17.50", "21.00", "23.50", "29.00"], correct="C",
      check="6 + 5(3.50) = 23.50."),

 dict(n="G2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A piano tuner charges a $25 call-out fee plus $12 for each hour of work. Which "
            "expression gives the total charge, in dollars, for h hours of work?"),
      choices=["\\(12h+25\\)", "\\(12h-25\\)", "\\(25h+12\\)", "\\(37h\\)"], correct="A",
      check="The fee is fixed and the hourly amount is multiplied by h."),

 dict(n="G2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The air in a fermenting room must stay below 24&deg;C. The air is at 17&deg;C now and "
            "warms by 2&deg;C every hour. What is the greatest whole number of hours the room can "
            "be left before it must be cooled?"),
      choices=["3", "4", "7", "12"], correct="A",
      check="17 + 2h < 24 gives h < 3.5, so 3 whole hours."),

 dict(n="G2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A ferry charges $9 for each adult ticket and $4 for each child ticket. How many "
            "dollars do 3 adult tickets and 5 child tickets cost altogether?"),
      choices=["39", "45", "47", "52"], correct="C",
      check="3(9) + 5(4) = 27 + 20 = 47."),

 dict(n="G2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A hot-air balloon descends so that \\(H(t)=1{,}200-40t\\) gives its height above the "
            "ground, in metres, t minutes after the descent begins. What is the meaning of 40 in "
            "this model?"),
      choices=["The number of metres the balloon descends each minute.",
               "The number of metres above the ground at which the descent begins.",
               "The number of minutes the balloon takes to reach the ground.",
               "The number of metres above the ground after 1,200 minutes."],
      correct="A",
      check="40 multiplies t, so it is the rate of descent in metres per minute."),

 dict(n="G2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A stagehand needs \\(3n+5\\) minutes to set the props for a scene and \\(2n-8\\) "
            "minutes to strike them, where n is the number of scenes. Which expression gives the "
            "total number of minutes for both tasks?"),
      choices=["\\(5n-3\\)", "\\(5n+13\\)", "\\(6n-3\\)", "\\(6n-40\\)"], correct="A",
      check="(3n+5) + (2n-8) = 5n - 3."),

 dict(n="G2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A signwriter uses \\(3(2m-7)\\) grams of gold leaf for a job, where m is the number of "
            "letters in the sign. Which expression is equivalent to \\(3(2m-7)\\)?"),
      choices=["\\(2m-21\\)", "\\(5m-7\\)", "\\(6m-7\\)", "\\(6m-21\\)"], correct="D",
      check="Distributing gives 6m - 21."),

 dict(n="G2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of tiles in the kth ring of a mosaic is \\(k^{2}+3\\). How many tiles are "
            "in the 6th ring?"),
      choices=["15", "21", "33", "39"], correct="D",
      check="6^2 + 3 = 39."),

 dict(n="G2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A marble rolls \\(3t^{2}\\) centimetres in the first t seconds after it is released. "
            "How many seconds does the marble take to roll 108 centimetres?"),
      choices=["6", "12", "18", "36"], correct="A",
      check="3t^2 = 108 gives t^2 = 36 and t = 6."),

 dict(n="G2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A workshop chart gives the magnification of an eyepiece as \\(M(d)=\\frac{72}{d}-1\\), "
            "where d is the diameter of the eyepiece in millimetres. What is the value of "
            "\\(M(8)\\)?"),
      choices=["8", "9", "71", "72"], correct="A",
      check="72/8 - 1 = 9 - 1 = 8."),

 dict(n="G2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A pupil simplifying a physics formula reaches the product \\(t^{6}\\cdot t^{3}\\), "
            "where \\(t>1\\). Which of the following is equal to that product?"),
      choices=["\\(t^{2}\\)", "\\(t^{9}\\)", "\\(t^{18}\\)", "\\(t^{63}\\)"], correct="B",
      check="Add the exponents: 6 + 3 = 9."),

 dict(n="G2E-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of bacteria on a cheese rind h hours after the rind is washed is "
            "\\(B(h)=3\\cdot 4^{h}\\). How many bacteria are on the rind 3 hours after it is "
            "washed?"),
      choices=["36", "48", "144", "192"], correct="D",
      check="3(4^3) = 3(64) = 192."),

 dict(n="G2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A paint is mixed with 3 parts pigment to 5 parts base by mass. One batch contains 45 "
            "grams of pigment. How many grams of base are in that batch?"),
      choices=["27", "60", "75", "120"], correct="C",
      check="(5/3)(45) = 75."),

 dict(n="G2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The price of a season ticket fell from $250 to $210. By what percent did the price "
            "fall?"),
      choices=["14%", "16%", "19%", "40%"], correct="B",
      check="40/250 = 0.16, which is 16%."),

 dict(n="G2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A mobile library van keeps a count of the books borrowed at each stop it makes. Its "
            "count for one Tuesday is given in the table."
            + table(["Stop", "Books borrowed"],
                    [["Hollin", "24"], ["Ings", "31"], ["Kettle", "19"], ["Lawn", "27"]])
            + "How many more books were borrowed at Ings than at Kettle?"),
      choices=["7", "12", "19", "50"], correct="B",
      check="31 - 19 = 12."),

 dict(n="G2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A warden counted the eggs in each of seven nests and recorded 2, 3, 3, 4, 6, 6 and 11 "
            "eggs. What is the median number of eggs per nest?"),
      choices=["3", "4", "5", "6"], correct="B",
      check="The middle value of the seven ordered counts is 4."),

 dict(n="G2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("One angle of a sign shaped like a parallelogram measures 62&deg;. What is the measure, "
            "in degrees, of an angle of the sign next to it?"),
      choices=["28", "62", "118", "128"], correct="C",
      check="Adjacent angles of a parallelogram are supplementary: 180 - 62 = 118."),

 dict(n="G2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular allotment measures 24 metres by 15 metres. What is the area of the "
            "allotment, in square metres?"),
      answers=["360"],
      check="24(15) = 360."),

 dict(n="G2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A crate in the shape of a cube has a volume of 512 cubic feet. How many feet long is "
            "each edge of the crate?"),
      answers=["8"],
      check="The cube root of 512 is 8."),

 dict(n="G2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A guy wire runs from the top of a mast 12 metres tall to a point on level ground 9 "
            "metres from the foot of the mast. How many metres long is the guy wire?"),
      answers=["15"],
      check="sqrt(12^2 + 9^2) = sqrt(225) = 15."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="G2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a foundry two blending constraints are written as \\(6x-4y=10\\) and "
            "\\(9x+cy=15\\), where x and y are the numbers of tonnes of two ores and c is a "
            "constant. The system has infinitely many solutions. What is the value of c?"),
      choices=["-6", "-4", "4", "6"], correct="A",
      check="Scaling the first equation by 3/2 gives 9x - 6y = 15, so c = -6."),

 dict(n="G2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A flow meter's calibration is a linear function f that satisfies "
            "\\(f(x+3)=f(x)+12\\) for every value of x. Given that \\(f(2)=5\\), what is the value "
            "of \\(f(11)\\)?"),
      choices=["29", "36", "41", "53"], correct="C",
      check="The slope is 12/3 = 4, so f(11) = 5 + 4(9) = 41."),

 dict(n="G2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A cooper makes barrels and firkins. Each barrel takes 3 hours of staving and each "
            "firkin takes 2 hours, and at most 96 hours of staving are available. The cooper must "
            "also make at least 3 firkins for every barrel. What is the greatest number of barrels "
            "the cooper can make?"),
      choices=["10", "12", "16", "32"], correct="A",
      check="With firkins at their minimum, 3b + 2(3b) = 9b <= 96 gives b <= 10.6, so 10 barrels."),

 dict(n="G2H-04", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rectangular sheet of vellum measures 30 centimetres by 20 centimetres. A margin of "
            "uniform width w centimetres is left on all four sides, and the written area inside the "
            "margin is 264 square centimetres. What is the value of w?"),
      choices=["3", "4", "5", "6"], correct="B",
      check="(30-2w)(20-2w) = 264 gives w^2 - 25w + 84 = 0, whose root below 10 is 4."),

 dict(n="G2H-05", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A lens designer's profile curve \\(y=f(x)\\) is a parabola whose vertex is at "
            "\\((2,5)\\). The designer then plots the curve \\(y=f(x-3)+4\\). What are the "
            "coordinates of the vertex of the plotted curve?"),
      choices=["\\((-1,1)\\)", "\\((-1,9)\\)", "\\((5,1)\\)", "\\((5,9)\\)"],
      correct="D",
      check="Replacing x by x-3 shifts right 3 and adding 4 shifts up 4, so (2,5) moves to (5,9)."),

 dict(n="G2H-06", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A wind-load report gives the deflection of a mast, in millimetres, as "
            "\\(h(x)=3x^{2}+18x+5\\). Which form of the expression displays the least deflection "
            "the mast reaches as a constant or coefficient?"),
      choices=["\\(3(x+3)^{2}-22\\)", "\\(3(x+3)^{2}+5\\)", "\\(3(x+6)^{2}-22\\)",
               "\\((3x+9)^{2}-22\\)"], correct="A",
      check="3(x+3)^2 - 22 expands to 3x^2 + 18x + 5, and the least deflection is -22."),

 dict(n="G2H-07", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A launch travels 24 kilometres up a river and then 24 kilometres back down, taking 5 "
            "hours in total. The current flows at a constant 2 kilometres per hour. What is the "
            "launch's speed in still water, in kilometres per hour?"),
      choices=["8", "10", "12", "14"], correct="B",
      check="24/(v-2) + 24/(v+2) = 5 gives 5v^2 - 48v - 20 = 0, whose root above 2 is 10."),

 dict(n="G2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The combined value of a resistance network is written as "
            "\\(\\frac{1}{x-3}-\\frac{2}{x+1}\\), where \\(x>3\\). Which single fraction is equal "
            "to that value?"),
      choices=["\\(\\frac{-1}{x^{2}-2x-3}\\)", "\\(\\frac{x+7}{x^{2}-2x-3}\\)",
               "\\(\\frac{7-x}{x^{2}-3}\\)", "\\(\\frac{7-x}{x^{2}-2x-3}\\)"], correct="D",
      check="A common denominator gives ((x+1) - 2(x-3))/((x-3)(x+1)) = (7-x)/(x^2-2x-3)."),

 dict(n="G2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A parabolic arch is modelled by \\(y=-\\frac{1}{50}(x-h)^{2}+18\\), where h is a "
            "positive constant and x and y are measured in metres. The arch meets the ground, where "
            "\\(y=0\\), at \\(x=0\\) and at one other value of x. How many metres apart are the two "
            "places where the arch meets the ground?"),
      choices=["30", "45", "60", "75"], correct="C",
      check="0 = -(1/50)h^2 + 18 gives h = 30, so the feet are at x = 0 and x = 60."),

 dict(n="G2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A gauge's calibration relation is \\(\\frac{2x-1}{x+4}=\\frac{3}{x}\\), where "
            "\\(x\\ne 0\\) and \\(x\\ne -4\\). The relation has two solutions. What is the sum of "
            "those two solutions?"),
      choices=["-6", "-2", "2", "4"], correct="C",
      check="Cross-multiplying gives 2x^2-4x-12 = 0, or x^2-2x-6 = 0, whose roots sum to 2."),

 dict(n="G2H-11", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An alloy that is 30% tin by mass is melted together with an alloy that is 8% tin by "
            "mass to make 44 kilograms of an alloy that is 15% tin by mass. How many kilograms of "
            "the 30% alloy are used?"),
      choices=["12", "14", "18", "30"], correct="B",
      check="0.30a + 0.08(44-a) = 6.6 gives 0.22a = 3.08 and a = 14."),

 dict(n="G2H-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A horticulturist randomly assigned 240 seedlings of a single variety to two mulches "
            "and found that the seedlings grown under bark mulch grew significantly taller, on "
            "average, than those grown under straw mulch. Which of the following is the most "
            "appropriate conclusion?"),
      choices=["The difference in growth was caused by the kind of mulch, for seedlings like those "
               "in the study.",
               "Bark mulch makes any plant grow taller than straw mulch does.",
               "The difference in growth cannot have been caused by the kind of mulch.",
               "Every seedling of this variety grows taller under bark mulch than under straw "
               "mulch."],
      correct="A",
      check="Random assignment supports a causal conclusion, but only for subjects like those studied."),

 dict(n="G2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean mass of 12 core samples was 47 grams. Two of the samples, of masses 35 grams "
            "and 34 grams, were then removed from the set. What is the mean mass, in grams, of the "
            "10 remaining samples?"),
      choices=["47", "48.5", "49", "49.5"], correct="D",
      check="12(47) - 35 - 34 = 495, and 495/10 = 49.5."),

 dict(n="G2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A press run needs ink and extender mixed in the ratio 5 to 2 by volume. The shop has "
            "80 litres of ink and 40 litres of extender and can obtain no more of either. What is "
            "the greatest number of litres of the mixture the shop can make?"),
      choices=["112", "120", "140", "168"], correct="A",
      check="The ink allows 80(7/5) = 112 litres and the extender allows 40(7/2) = 140, so 112."),

 dict(n="G2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives, for each of four kilns at a pottery, the number of firings in a year, "
            "the number of pieces loaded into each firing, and the percent of the loaded pieces "
            "lost to cracking."
            + table(["Kiln", "Firings", "Pieces per firing", "Percent lost"],
                    [["Alder", "14", "60", "5%"], ["Birch", "9", "80", "10%"],
                     ["Cedar", "11", "50", "4%"], ["Damson", "6", "90", "8%"]])
            + "How many more pieces survived firing in the Alder kiln than in the Birch kiln?"),
      choices=["108", "120", "150", "192"], correct="C",
      check="Alder: 840 loaded, 798 survive. Birch: 720 loaded, 648 survive. 798 - 648 = 150."),

 dict(n="G2H-16", domain="GT", skill="GT-LA", type="MC",
      stem=("In a right triangle, the altitude drawn from the right angle to the hypotenuse "
            "measures 12 centimetres, and it divides the hypotenuse into two segments, the shorter "
            "of which measures 9 centimetres. What is the length, in centimetres, of the "
            "hypotenuse?"),
      choices=["16", "20", "21", "25"], correct="D",
      check="The altitude is the geometric mean of the segments: 12^2 = 9k gives k = 16, so 9 + 16 = 25."),

 dict(n="G2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A solid sphere fits exactly inside a closed cylindrical tin, touching the curved "
            "surface of the tin and both of its flat ends. What fraction of the volume of the tin "
            "does the sphere occupy?"),
      choices=["\\(\\frac{1}{2}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{2}{3}\\)",
               "\\(\\frac{3}{4}\\)"], correct="C",
      check="With radius r the sphere is (4/3) pi r^3 and the tin is 2 pi r^3, a ratio of 2/3."),

 dict(n="G2H-18", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle \\(JKL\\) the right angle is at L, and \\(\\cos J=\\frac{7}{25}\\). "
            "What is the value of \\(\\tan J\\)?"),
      choices=["\\(\\frac{7}{24}\\)", "\\(\\frac{24}{25}\\)", "\\(\\frac{24}{7}\\)",
               "\\(\\frac{25}{7}\\)"], correct="C",
      check="Legs 7 and 24 with hypotenuse 25 give tan J = 24/7."),

 dict(n="G2H-19", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A courier's van can carry a total mass of at most 1,400 kilograms and at most 60 "
            "parcels. Heavy parcels have a mass of 40 kilograms each and light parcels a mass of 15 "
            "kilograms each, and the van must carry at least 20 light parcels. What is the greatest "
            "number of heavy parcels the van can carry?"),
      choices=["25", "27", "29", "35"], correct="B",
      check="20 light parcels weigh 300 kg, leaving 1,100 kg, and 1,100/40 = 27.5, so 27 parcels."),

 dict(n="G2H-20", domain="ALG", skill="ALG-LF", type="FR",
      stem=("The stretch of a spring is a linear function of the load it carries. A load of 4 "
            "kilograms stretches the spring 9 centimetres, and a load of 10 kilograms stretches it "
            "21 centimetres. What load, in kilograms, stretches the spring 33 centimetres?"),
      answers=["16"],
      check="Slope 12/6 = 2 cm per kg and intercept 1, so 2m + 1 = 33 gives m = 16."),

 dict(n="G2H-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A cyclist rides from a village to a mill at a constant 24 kilometres per hour and "
            "returns along the same road at a constant 16 kilometres per hour. The whole journey "
            "takes 5 hours. How many kilometres is it from the village to the mill?"),
      answers=["48"],
      check="d/24 + d/16 = 5 gives 5d/48 = 5 and d = 48."),

 dict(n="G2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A packing case has a square base, stands 9 centimetres tall, and holds 576 cubic "
            "centimetres. What is the total surface area of the six faces of the case, in square "
            "centimetres?"),
      answers=["416"],
      check="The base area is 64, so the base edge is 8; 2(64) + 4(8)(9) = 128 + 288 = 416."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
