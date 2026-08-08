#!/usr/bin/env python3
"""
Original Math content for Test 20 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium, deliberately harder than a stock Module 1. Almost
                every item makes a constant, a rate, a unit price or an unknown
                be recovered first and only then used; two or three steps
                throughout. Clearly above Module 2 (Easy), clearly below
                Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
                One operation, no recovery step.
  MODULE_2_HARD hard: parameters instead of numbers, structural and symbolic
                answer choices, a composed function, an inequality chain, a
                two-way table, a work-rate pair, and geometry that needs two
                relationships chained.

Every setting is drawn from Test 20's assigned thematic territory — coal mining
and pit props, gas works and coke ovens, telegraphy and submarine cable laying,
tramways and trolleybuses, iron foundries and pattern making, boiler making and
riveting, tunnelling and shield driving, dockside cranes, pumping engines,
winding gear, ventilation fans, tram signal cabins, scrap sorting and wire
drawing — and is deliberately unlike anything already banked in production.

Settings are partitioned across the modules, because a student sees Module 1
plus exactly one Module 2 branch and must never meet the same scene twice:

  MODULE_1      coal face and colliery districts, iron foundry and pattern
                making, tunnelling and shield driving, dockside cranes,
                scrap sorting
  MODULE_2_EASY gas works and retorts, tramways and trolleybuses, tram signal
                cabins, wire drawing, pumping engines
  MODULE_2_HARD submarine cable laying, telegraphy, boiler making and riveting,
                mine ventilation fans

House style follows Test 1/2 (see CLAUDE.md): bare HTML stems, simple inline
maths left as plain text, real <table> markup for every data table, &deg; as an
entity. All LaTeX is typed by hand; no bulk conversion step was used anywhere
in this file.
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
 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a coal face two teams fill tubs during one shift. The hewing team fills 3 more "
            "tubs than twice the number the packing team fills, and the two teams fill 84 tubs "
            "between them. Each tub holds 0.45 tonnes. How many tonnes does the hewing team fill "
            "during the shift?"),
      choices=["12.15", "24.30", "25.65", "37.80"], correct="C",
      check="p + (2p+3) = 84 gives p = 27, so the hewing team fills 57 tubs and 57 lots of 0.45 is 25.65 tonnes."),

 dict(n="H1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A scrap yard takes in a 15-tonne load made up only of cast iron and copper. Cast "
            "iron fetches $60 a tonne and copper fetches $130 a tonne, and the whole load fetched "
            "$1,180. The yard is charged $18 for every tonne of copper it has to sort out. How "
            "many dollars did the yard keep after that sorting charge?"),
      choices=["$1,036", "$1,108", "$1,162", "$1,180"], correct="B",
      check="60(15-u) + 130u = 1,180 gives u = 4 tonnes of copper, and 1,180 - 4(18) = 1,108."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The charge for hiring a dockside crane is a linear function of the number of hours "
            "the crane is used. A 5-hour hire cost $310 and a 12-hour hire cost $618. For how many "
            "hours can the crane be hired for $750?"),
      choices=["15", "17", "19", "22"], correct="A",
      check="The hourly part is 308/7 = 44 and the standing part is 310 - 5(44) = 90, so (750-90)/44 = 15 hours."),

 dict(n="H1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The distance a tunnelling shield has driven is a linear function of the number of "
            "lining rings erected behind it. After 40 rings the shield had driven 96 metres, and "
            "after 105 rings it had driven 252 metres. How many rings must be erected for the "
            "shield to have driven 420 metres?"),
      choices=["150", "175", "187", "210"], correct="B",
      check="156 metres over 65 rings is 2.4 metres a ring, and 40(2.4) = 96 leaves no constant, so 420/2.4 = 175."),

 dict(n="H1-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A dockside crane may lift no more than 9.5 tonnes at one time. The lifting beam and "
            "chains together have a mass of 1,180 kilograms, and each bale of sorted scrap has a "
            "mass of 640 kilograms. What is the greatest number of bales the crane can lift at "
            "one time?"),
      choices=["13", "14", "16", "18"], correct="A",
      check="9,500 - 1,180 = 8,320 kilograms are left for bales, and 8,320/640 = 13 exactly."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A foundry pours wheel castings and pipe castings from a single melt. Each wheel "
            "casting takes 4 kilograms more iron than each pipe casting. A melt that filled 9 "
            "wheel moulds and 14 pipe moulds used 634 kilograms of iron. How many kilograms of "
            "iron does one wheel casting take?"),
      choices=["26", "28", "30", "34"], correct="C",
      check="9(q+4) + 14q = 634 gives 23q = 598 and q = 26, so a wheel casting takes 30 kilograms."),

 dict(n="H1-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A pattern maker starts from a square board of side \\(2x-5\\) centimetres and cuts "
            "from it a square hole of side \\(x-8\\) centimetres. Which expression gives the area "
            "of the board that remains, in square centimetres?"),
      choices=["\\(3x^{2}-4x+89\\)", "\\(3x^{2}-36x+89\\)", "\\(5x^{2}-36x+89\\)",
               "\\(3x^{2}-4x-39\\)"], correct="D",
      check="(2x-5)^2 is 4x^2-20x+25 and (x-8)^2 is x^2-16x+64, and the difference is 3x^2-4x-39."),

 dict(n="H1-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A scrap baler's daily output, in tonnes, when the machine is run at s strokes each "
            "minute is modelled by \\(T(s)=-2s^{2}+72s-160\\). What is the greatest daily output, "
            "in tonnes, that this model gives?"),
      choices=["392", "440", "464", "488"], correct="D",
      check="The greatest value is at s = 72/4 = 18 strokes, and -2(324) + 72(18) - 160 = 488."),

 dict(n="H1-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The floor of a spoil skip at a tunnel heading is a rectangle whose length is 3 metres "
            "greater than its width, and its area is 54 square metres. What is the width of the "
            "floor, in metres?"),
      choices=["6", "7", "9", "12"], correct="A",
      check="w(w+3) = 54 gives w^2 + 3w - 54 = 0, whose positive root is 6."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A foundry sizes the runner that feeds a mould by the rule \\(d=14\\sqrt[3]{m}\\), "
            "where d is the diameter of the runner in millimetres and m is the mass of the casting "
            "in kilograms. A casting needs a runner 56 millimetres in diameter. What is the mass "
            "of that casting, in kilograms?"),
      choices=["16", "64", "125", "216"], correct="B",
      check="14 times the cube root of m is 56, so the cube root of m is 4 and m is 64."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A colliery's total output up to and including week n is modelled by "
            "\\(f(n)=n^{2}+6n\\) hundred tonnes. For which value of n does week n+1 by itself "
            "account for 39 hundred tonnes?"),
      choices=["14", "16", "18", "32"], correct="B",
      check="f(n+1) - f(n) works out to 2n + 7, and 2n + 7 = 39 gives n = 16."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A pattern maker's core allowance, in square centimetres, is written as "
            "\\((x+6)(x-2)-(x-3)(x+4)\\), where x is a length in centimetres. Which expression is "
            "equivalent to that allowance?"),
      choices=["\\(3x\\)", "\\(3x-24\\)", "\\(5x-24\\)", "\\(2x^{2}+5x-24\\)"], correct="A",
      check="The first product is x^2+4x-12 and the second is x^2+x-12, so the squares and the constants both cancel."),

 dict(n="H1-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A scrap yard buys 240 tonnes of mixed steel at $46 a tonne. Baling drives off 12% of "
            "that mass as dirt and rust, and the baled steel sells at $62 a tonne. What is the "
            "yard's gain, in dollars, on the whole lot?"),
      choices=["$2,054.40", "$2,844.00", "$3,840.00", "$13,094.40"], correct="A",
      check="240(0.88) = 211.2 tonnes sell for 13,094.40, and the lot cost 240(46) = 11,040."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Cast iron has a mass of 7.2 grams for each cubic centimetre, and a foundry buys iron "
            "at $0.44 a kilogram. What does the iron in a casting of volume 12,500 cubic "
            "centimetres cost?"),
      choices=["$3.96", "$5.50", "$27.50", "$39.60"], correct="D",
      check="12,500(7.2) = 90,000 grams, which is 90 kilograms, and 90(0.44) = 39.60."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A dock recorded the number of lifts each of its four cranes made in one day, together "
            "with the mean mass of a lift for that crane."
            + table(["Crane", "Lifts made", "Mean mass of a lift (tonnes)"],
                    [["No. 1", "46", "3.5"], ["No. 2", "38", "4.2"],
                     ["No. 3", "52", "3.0"], ["No. 4", "30", "5.4"]])
            + "Which crane moved the greatest total mass that day?"),
      choices=["No. 1", "No. 2", "No. 3", "No. 4"], correct="D",
      check="The four totals are 161, 159.6, 156 and 162 tonnes, and the greatest belongs to No. 4."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A scrap store holds 180 bales: 45 of copper, 63 of brass and the rest of lead. One "
            "bale is picked at random from the store. What is the probability that the bale picked "
            "is a lead bale?"),
      choices=["\\(\\frac{1}{4}\\)", "\\(\\frac{7}{20}\\)", "\\(\\frac{2}{5}\\)",
               "\\(\\frac{3}{5}\\)"], correct="C",
      check="180 - 45 - 63 = 72 lead bales, and 72/180 reduces to 2/5."),

 dict(n="H1-17", domain="GT", skill="GT-TR", type="MC",
      stem=("A dockside crane's jib is 32 metres long and is pivoted 4 metres above the quay. When "
            "the jib is raised to 62&deg; above the horizontal, how high above the quay is the "
            "head of the jib, to the nearest metre?"),
      choices=["28", "32", "36", "40"], correct="B",
      check="32 times the sine of 62 degrees is about 28.3 metres above the pivot, and 28.3 + 4 rounds to 32."),

 dict(n="H1-18", domain="GT", skill="GT-LA", type="MC",
      stem=("A tunnel is lined with rings, and each ring is built from 8 identical segments that "
            "close up into a regular octagon. What is the measure, in degrees, of each interior "
            "angle of that octagon?"),
      choices=["108", "120", "135", "150"], correct="C",
      check="The interior angles of an 8-sided polygon sum to (8-2)(180) = 1,080 degrees, and 1,080/8 = 135."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A dockside crane's ballast box is an open-topped rectangular tank 3 metres long, 2 "
            "metres wide and 1.5 metres deep. How many square metres of steel sheet do its base "
            "and its four sides take together?"),
      choices=["12", "15", "21", "27"], correct="C",
      check="The base is 6 square metres, the two long sides are 9 and the two short sides are 6, giving 21."),

 dict(n="H1-20", domain="PSDA", skill="PSDA-DI", type="FR",
      stem=("The table gives the number of tubs drawn from each of four districts of a colliery in "
            "one week, together with the mean mass of a tub in that district."
            + table(["District", "Tubs drawn", "Mean mass of a tub (tonnes)"],
                    [["Bute", "300", "0.55"], ["Garth", "240", "0.60"],
                     ["Rhas", "180", "0.45"], ["Tir", "260", "0.50"]])
            + "How many tonnes of coal were drawn from the four districts altogether that week?"),
      answers=["520"],
      check="165 + 144 + 81 + 130 = 520 tonnes."),

 dict(n="H1-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A foundry's cupola burns 0.6 tonnes of coke to bring itself up to heat and then a "
            "further 1 tonne of coke for every 8 tonnes of iron it melts. One melt used 5.1 tonnes "
            "of coke altogether. How many tonnes of iron were melted?"),
      answers=["36"],
      check="0.6 tonnes goes on heating up, leaving 4.5 tonnes at 1 tonne per 8 tonnes of iron, so 8(4.5) = 36."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A casting is a closed hollow box whose outside measurements are 40 centimetres by 30 "
            "centimetres by 20 centimetres. Its walls are 2.5 centimetres thick everywhere, "
            "including the top and the bottom. How many cubic centimetres of iron does the casting "
            "contain?"),
      answers=["10875"],
      check="Outside 40(30)(20) = 24,000 and the cavity is 35(25)(15) = 13,125, leaving 10,875."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A gas works charges its 7 retorts with equal shares of 154 hundredweight of fuel. How "
            "many hundredweight of fuel go into each retort?"),
      choices=["22", "24", "26", "28"], correct="A",
      check="154/7 = 22."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tramway sold 468 tickets one morning. Of these, 129 were child tickets and the rest "
            "were adult tickets. How many adult tickets were sold?"),
      choices=["329", "339", "349", "597"], correct="B",
      check="468 - 129 = 339."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A pumping engine's total discharge, in gallons, t minutes after it is started is given "
            "by p=250t+400. How many gallons has it discharged 6 minutes after it is started?"),
      choices=["1,000", "1,650", "1,900", "3,900"], correct="C",
      check="250(6) + 400 = 1,900."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The cost of stringing overhead wire for a trolleybus route is modelled by "
            "c=1,450+380m, where c is the cost in dollars and m is the number of miles of route "
            "strung. What does 380 represent in this model?"),
      choices=["The total cost, in dollars, of stringing the whole route",
               "The number of miles of route that can be strung for $1,450",
               "The cost, in dollars, incurred before any wire is strung",
               "The cost, in dollars, of stringing each mile of route"], correct="D",
      check="380 multiplies the number of miles, so it is the cost added by each further mile."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A tramway rule requires that the number n of cars running on the Canal Road route be "
            "at least 6 and no more than 11. Which inequality represents this rule?"),
      choices=["\\(6\\le n\\le 11\\)", "\\(6<n\\le 11\\)", "\\(6\\le n<11\\)", "\\(6<n<11\\)"],
      correct="A",
      check="At least 6 allows 6 itself and no more than 11 allows 11 itself, so both ends are inclusive."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tram conductor's takings x, in dollars, satisfy \\(\\frac{x}{4}+7=19\\). What is the "
            "value of x?"),
      choices=["12", "21", "48", "104"], correct="C",
      check="x/4 = 12, so x = 48."),

 dict(n="H2E-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The time, in minutes, needed to clean x tram cars is given by \\(4(3x-7)+5x\\). Which "
            "expression is equivalent to it?"),
      choices=["\\(17x-28\\)", "\\(17x-7\\)", "\\(12x-28\\)", "\\(7x-28\\)"], correct="A",
      check="4(3x-7) is 12x - 28, and adding 5x gives 17x - 28."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A gas works records a leakage allowance as \\((x+9)(x-9)\\). Which expression is "
            "equivalent to that allowance?"),
      choices=["\\(x^{2}+81\\)", "\\(x^{2}-18x-81\\)", "\\(x^{2}+18x-81\\)", "\\(x^{2}-81\\)"],
      correct="D",
      check="The two middle terms are +9x and -9x, so they cancel and only x squared minus 81 is left."),

 dict(n="H2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A wire-drawing bench's wear index is given by \\(h(x)=x^{2}-9\\), where x is the "
            "number of dies fitted. What is the value of \\(h(5)\\)?"),
      choices=["1", "16", "25", "34"], correct="B",
      check="25 - 9 = 16."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of cars in service on a tramway is modelled by \\(T(y)=40(1.25)^{y}\\), "
            "where y is the number of years since the tramway opened. By what percent does the "
            "model say the number of cars increases each year?"),
      choices=["1.25%", "12.5%", "25%", "125%"], correct="C",
      check="A yearly factor of 1.25 is an increase of 0.25, which is 25%."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A gas works doubles its stock of fuel each hour, so that after y hours it holds "
            "\\(3\\cdot 2^{y}\\) tonnes. After how many hours does it hold 96 tonnes?"),
      choices=["4", "5", "6", "32"], correct="B",
      check="96/3 = 32, and 32 is 2 to the fifth power, so y = 5."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A tram signal cabin times its interlocking with the function f. The table gives four "
            "values of f."
            + table(["x", "\\(f(x)\\)"],
                    [["-2", "11"], ["-1", "4"], ["0", "-1"], ["1", "-4"]])
            + "What is the value of \\(f(1)\\)?"),
      choices=["-4", "-1", "4", "11"], correct="A",
      check="The row for x = 1 gives -4."),

 dict(n="H2E-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Three tram cars take 21 litres of oil between them for a full greasing. At the same "
            "rate, how many litres are needed to grease 8 tram cars?"),
      choices=["24", "42", "49", "56"], correct="D",
      check="21/3 = 7 litres a car, and 7(8) = 56."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A tram fare of $1.20 is raised by 25%. What is the new fare?"),
      choices=["$0.30", "$1.25", "$1.45", "$1.50"], correct="D",
      check="1.20(1.25) = 1.50."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of cars kept at each of four tram depots."
            + table(["Depot", "Cars kept"],
                    [["Canal Road", "48"], ["Marsh Lane", "61"],
                     ["Old Wharf", "37"], ["Bell Green", "55"]])
            + "How many more cars are kept at Marsh Lane than at Old Wharf?"),
      choices=["24", "37", "61", "98"], correct="A",
      check="61 - 37 = 24."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A tram signal cabin recorded the number of levers pulled in each of five hours: 22, "
            "19, 25, 19 and 30. What is the range of these five numbers?"),
      choices=["6", "11", "19", "22"], correct="B",
      check="30 - 19 = 11."),

 dict(n="H2E-17", domain="GT", skill="GT-LA", type="MC",
      stem=("A trolleybus route runs in a straight line through three stops A, B and C, in that "
            "order. It is 14 kilometres from A to B and 37 kilometres from A to C. How many "
            "kilometres is it from B to C?"),
      choices=["14", "23", "37", "51"], correct="B",
      check="37 - 14 = 23."),

 dict(n="H2E-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A gas holder's tank is a cylinder whose base has an area of 1,250 square metres. Gas "
            "fills the tank to a depth of 18 metres. How many cubic metres of gas does the tank "
            "hold?"),
      choices=["4,500", "11,250", "22,500", "45,000"], correct="C",
      check="1,250(18) = 22,500."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A trolleybus reversing loop sweeps a quarter of a circle of radius 12 metres. What is "
            "the area of the ground it sweeps, in square metres?"),
      choices=["\\(6\\pi\\)", "\\(9\\pi\\)", "\\(36\\pi\\)", "\\(144\\pi\\)"], correct="C",
      check="A whole circle of radius 12 covers 144 pi, and a quarter of that is 36 pi."),

 dict(n="H2E-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("The number of coils of wire drawn on each of six days was 34, 41, 38, 45, 39 and 43. "
            "What is the median number of coils drawn per day?"),
      answers=["40"],
      check="In order the six values are 34, 38, 39, 41, 43, 45, and the middle pair average to 40."),

 dict(n="H2E-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A wire-drawing bench drew 72 coils in one shift, and \\(\\frac{5}{8}\\) of them were "
            "of the finest gauge. How many coils of the finest gauge were drawn that shift?"),
      answers=["45"],
      check="72 times 5/8 is 45."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A tramway crossover is set out as right triangle PQR with the right angle at R. The "
            "hypotenuse PQ measures 25 metres and side QR measures 7 metres. What is the value of "
            "\\(\\sin P\\)?"),
      answers=["7/25", "0.28"],
      check="The sine of P is the side opposite P over the hypotenuse, which is 7 over 25."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cable ship's manifest sets two conditions on the numbers x and y of the two sizes "
            "of cable drum carried:<br/>3x+5y=41<br/>5x+3y=39<br/>What is the value of x+y?"),
      choices=["8", "10", "16", "80"], correct="B",
      check="Adding the two conditions gives 8x + 8y = 80, so x + y = 10."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("On a cable ship's plotting sheet a straight course is the set of points \\((x,y)\\) "
            "satisfying \\(y=mx+b\\), where m and b are constants. The course passes through "
            "\\((-2,9)\\) and \\((6,-7)\\). What is the value of \\(m+b\\)?"),
      choices=["-2", "3", "5", "7"], correct="B",
      check="The slope is -16/8 = -2, and 9 = -2(-2) + b gives b = 5, so m + b = 3."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A mine ventilation fan must be run so that the air quantity q, in thousands of cubic "
            "feet each minute, satisfies both \\(3q-8\\ge 40\\) and \\(2q+5\\le 65\\). What is the "
            "greatest possible value of q?"),
      choices=["12", "16", "24", "30"], correct="D",
      check="The first condition gives q at least 16 and the second gives q at most 30."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A boiler shop rivets seams in two patterns. Four metres of the double-riveted pattern "
            "together with seven metres of the single-riveted pattern take 63 rivets, while seven "
            "metres of the double-riveted pattern together with four metres of the single-riveted "
            "pattern take 69 rivets. How many rivets does one metre of the double-riveted pattern "
            "take?"),
      choices=["5", "6", "7", "9"], correct="C",
      check="Adding the two conditions gives 11 metres of each pattern taking 132 rivets, and subtracting them gives 3 more rivets for 3 metres of double, so double is 7 and single is 5."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A telegraph company's charge for a new line is \\(C(n)=an+b\\) dollars for a line n "
            "miles long, where a and b are constants. A 30-mile line costs $1,290 and a 50-mile "
            "line costs $2,050. Which expression gives the charge, in dollars, for a line m miles "
            "long?"),
      choices=["\\(38m+150\\)", "\\(38m+43\\)", "\\(41m+60\\)", "\\(43m\\)"], correct="A",
      check="760 dollars over 20 miles gives a = 38, and 1,290 - 30(38) = 150 gives b."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cable ship pays out cable at a steady rate. Three hours after paying out began, 8.4 "
            "nautical miles of cable remained on the drum; seven hours after it began, 5.2 "
            "nautical miles remained. The ship must leave at least 1.2 nautical miles on the drum. "
            "For how many further hours after the seventh hour can the ship go on paying out?"),
      choices=["4", "5", "6.5", "8"], correct="B",
      check="3.2 nautical miles over 4 hours is 0.8 an hour, and 4 nautical miles are still free, so 5 hours."),

 dict(n="H2H-07", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A telegraph office converts a reading with \\(g(x)=2x-5\\) and then converts the "
            "result back with \\(f(x)=\\frac{x+5}{2}\\). Which expression is equivalent to "
            "\\(f(g(x))\\)?"),
      choices=["\\(x\\)", "\\(x-5\\)", "\\(x+5\\)", "\\(4x-5\\)"], correct="A",
      check="Substituting 2x-5 into f gives (2x-5+5)/2, which is x."),

 dict(n="H2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A boiler shop writes the combined allowance of two riveted seams as "
            "\\(\\frac{1}{\\frac{1}{u}+\\frac{1}{v}}\\), where u and v are positive. Which "
            "expression is equivalent to that allowance?"),
      choices=["\\(\\frac{u+v}{uv}\\)", "\\(u+v\\)", "\\(\\frac{1}{u+v}\\)",
               "\\(\\frac{uv}{u+v}\\)"], correct="D",
      check="The denominator adds to (v+u)/(uv), and dividing 1 by that turns it upside down."),

 dict(n="H2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A telegraph repeater station's traffic is modelled by \\(M(t)=k\\cdot 4^{\\frac{t}{5}}\\) "
            "messages, where t is the number of hours since midnight and k is a constant. The "
            "model gives 1,728 messages at \\(t=15\\). How many messages does the model give at "
            "\\(t=0\\)?"),
      choices=["27", "108", "432", "864"], correct="A",
      check="4 raised to 15/5 is 64, so k = 1,728/64 = 27, which is also the value at t = 0."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A boiler designer's two working stresses are the two solutions of "
            "\\(3x^{2}-12x-7=0\\). What is the sum of those two solutions?"),
      choices=["\\(-\\frac{7}{3}\\)", "\\(\\frac{7}{3}\\)", "4", "12"], correct="C",
      check="For a quadratic the two roots sum to minus the x coefficient over the leading coefficient, here 12/3 = 4."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A ventilation gauge is out of true whenever \\(|2x-9|=15\\), where x is the reading in "
            "inches of water. What is the sum of the two values of x that satisfy this equation?"),
      choices=["9", "12", "15", "24"], correct="A",
      check="Either 2x-9 is 15, giving x = 12, or it is -15, giving x = -3, and 12 + (-3) = 9."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A boiler designer writes a plate-strength ratio as "
            "\\(\\frac{a^{\\frac{3}{4}}}{a^{\\frac{1}{6}}}\\), where \\(a>1\\). Which expression "
            "is equivalent to that ratio?"),
      choices=["\\(a^{\\frac{7}{12}}\\)", "\\(a^{\\frac{1}{2}}\\)", "\\(a^{\\frac{11}{12}}\\)",
               "\\(a^{\\frac{9}{2}}\\)"], correct="A",
      check="Dividing subtracts the exponents, and 3/4 - 1/6 = 9/12 - 2/12 = 7/12."),

 dict(n="H2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A ventilation engineer measured the air quantity at 30 randomly chosen of the 400 "
            "working places in one mine and found a mean of 3,100 cubic feet each minute. To which "
            "group is it most appropriate to generalize this result?"),
      choices=["Only the 30 working places at which the air quantity was measured",
               "All working places in every mine in the district",
               "All ventilation fans in use in the district",
               "All 400 working places in that mine"], correct="D",
      check="A random sample supports an inference about the population it was drawn from, which is the 400 working places in that one mine."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table shows the results of a hydraulic test on 300 boiler plates, sorted by the "
            "thickness of the plate."
            + table(["Result", "12 mm", "16 mm", "20 mm", "Total"],
                    [["Passed", "84", "96", "60", "240"],
                     ["Failed", "16", "24", "20", "60"],
                     ["Total", "100", "120", "80", "300"]])
            + "Of the plates that failed the test, what fraction were 16 millimetres thick?"),
      choices=["\\(\\frac{2}{25}\\)", "\\(\\frac{1}{5}\\)", "\\(\\frac{1}{4}\\)",
               "\\(\\frac{2}{5}\\)"], correct="D",
      check="24 of the 60 plates that failed were 16 millimetres thick, and 24/60 reduces to 2/5."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A mine's ventilation fan was speeded up so that the air quantity rose by 15%. The fan "
            "drift was then widened so that the quantity rose by a further 20%. By what percent is "
            "the final air quantity greater than the quantity before either change?"),
      choices=["35%", "36%", "38%", "41%"], correct="C",
      check="1.15 times 1.20 is 1.38, an increase of 38%."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean thickness of 12 boiler plates was measured as 15.4 millimetres. When one "
            "plate was set aside, the mean thickness of the remaining 11 was 15.6 millimetres. "
            "What was the thickness, in millimetres, of the plate that was set aside?"),
      choices=["11.6", "13.2", "15.0", "17.6"], correct="B",
      check="12(15.4) = 184.8 and 11(15.6) = 171.6, and the difference is 13.2."),

 dict(n="H2H-17", domain="GT", skill="GT-TR", type="MC",
      stem=("A boiler shop's templet is a right triangle \\(ABC\\) with the right angle at C. The "
            "shop's record gives \\(\\sin A=\\frac{7}{25}\\) and \\(BC=21\\) centimetres. What is "
            "the length of \\(AC\\), in centimetres?"),
      choices=["24", "54", "72", "75"], correct="C",
      check="The sine of A is BC over AB, so AB is 75, and AC is the square root of 75 squared minus 21 squared, which is 72."),

 dict(n="H2H-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A boiler shell is a cylinder 10 feet long closed at each end by a hemisphere. The "
            "cylinder and both hemispheres have a radius of 3 feet. What is the total volume of "
            "the shell, in cubic feet?"),
      choices=["\\(108\\pi\\)", "\\(126\\pi\\)", "\\(144\\pi\\)", "\\(162\\pi\\)"], correct="B",
      check="The cylinder holds 90 pi and the two hemispheres together hold 36 pi."),

 dict(n="H2H-19", domain="GT", skill="GT-LA", type="MC",
      stem=("Two telegraph wires are strung parallel to each other, and a straight stay wire "
            "crosses both. The angle the stay makes with the upper wire and the angle it makes "
            "with the lower wire are corresponding angles, and they measure \\((7x-4)\\)&deg; and "
            "\\((3x+24)\\)&deg;. What is the measure, in degrees, of each of those two angles?"),
      choices=["7", "28", "45", "135"], correct="C",
      check="Corresponding angles are equal, so 7x - 4 = 3x + 24 gives x = 7 and each angle is 45."),

 dict(n="H2H-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A submarine cable is made up of three sections. The second section is twice as long "
            "as the first, and the third is 40 nautical miles longer than the second. The whole "
            "cable is 620 nautical miles long. How many nautical miles long is the third section?"),
      answers=["272"],
      check="f + 2f + (2f+40) = 620 gives 5f = 580 and f = 116, so the third section is 272."),

 dict(n="H2H-21", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("In a riveted boiler seam the ratio of rivets accepted to rivets cut out is 23 to 2. A "
            "seam took 1,150 rivets altogether, and every rivet cut out cost the shop $3.40 in "
            "lost time. What was the total lost-time cost, in dollars, for that seam?"),
      answers=["312.80", "312.8"],
      check="1,150 splits into 25 parts of 46, so 2 parts is 92 rivets cut out, and 92(3.40) = 312.80."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A ventilation drift is a rectangular airway 3.5 metres wide and 2.4 metres high, and "
            "air moves along it at 6 metres each second. How many cubic metres of air pass a point "
            "in the drift each minute?"),
      answers=["3024"],
      check="The cross-section is 8.4 square metres, 8.4(6) = 50.4 cubic metres a second, and 50.4(60) = 3,024."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
