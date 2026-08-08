#!/usr/bin/env python3
"""
Original Math content for Test 15 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item makes a constant, a rate or an
                unknown price be recovered first and only then used; two or
                three steps throughout. Deliberately harder than Module 2
                (Easy) and clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard. Parameters instead of numbers, structural answers, a
                composed function, a system conditioned on a constant, an
                inequality chain, and geometry needing two relationships.

Every setting is concrete and deliberately unlike anything already banked in
production (cooperative mills, stalagmites, canal towpaths, rope-walks, kiln
firings, allotment surveys, trestle frames, draughtsmen's set squares). House
style follows Test 1/2 — see CLAUDE.md. All LaTeX is typed by hand; no bulk
conversion step was used anywhere in this file.
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
      stem=("At a cooperative mill, milling 5 sacks of rye and 2 sacks of barley costs $76, while "
            "milling 3 sacks of rye and 4 sacks of barley costs $68. Every sack of a given grain "
            "is milled at the same price. What is the price, in dollars, of milling one sack of "
            "barley?"),
      choices=["8", "10", "12", "14"], correct="A",
      check="5r+2b=76 and 3r+4b=68 give r = 12 and b = 8."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A stalagmite in a limestone cavern grows taller at a constant rate. Its recorded "
            "height was 412 millimetres in 1985 and 445 millimetres in 2015. According to this "
            "model, in what year is the stalagmite 500 millimetres tall?"),
      choices=["2045", "2065", "2075", "2095"], correct="B",
      check="Rate = 33/30 = 1.1 mm per year, and 88/1.1 = 80 years after 1985."),

 dict(n="H1-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A film society has a grant of $1,150. It must first pay a $265 licensing fee for the "
            "season, and it will spend the rest of the grant renting films at $74 each. What is "
            "the greatest number of films the society can rent?"),
      choices=["9", "10", "11", "12"], correct="C",
      check="265 + 74n <= 1,150 gives n <= 11.9, so 11 films."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A ferry crossing carried foot passengers and bicycles and nothing else. The number of "
            "foot passengers was 3 more than twice the number of bicycles, and 78 foot passengers "
            "and bicycles were carried altogether. How many foot passengers were carried?"),
      choices=["25", "26", "39", "53"], correct="D",
      check="b + (2b+3) = 78 gives b = 25, so the foot passengers numbered 2(25)+3 = 53."),

 dict(n="H1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A weather data service charges a one-time setup fee plus a fixed fee for each month of "
            "service. A customer billed for 7 months of service has paid $332 in total, and a "
            "customer billed for 12 months has paid $532 in total. What is the setup fee, in "
            "dollars?"),
      choices=["40", "47", "52", "60"], correct="C",
      check="The monthly fee is 200/5 = 40, so the setup fee is 332 - 7(40) = 52."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two crews clear a canal towpath, starting at opposite ends and working towards each "
            "other. One crew clears 38 metres of path a day and the other clears 46 metres a day. "
            "The towpath is 1,764 metres long. After how many days do the two crews meet?"),
      choices=["14", "21", "24", "42"], correct="B",
      check="Together they clear 84 metres a day, and 1,764/84 = 21."),

 dict(n="H1-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A weaver's loom is threaded so that the number of warp threads is a linear function of "
            "the width of the cloth. A cloth 45 centimetres wide uses 1,140 warp threads, and a "
            "cloth 70 centimetres wide uses 1,740 warp threads. How many warp threads does a cloth "
            "100 centimetres wide use?"),
      choices=["2,340", "2,400", "2,460", "2,520"], correct="C",
      check="Slope 600/25 = 24 threads per cm and intercept 60, so 60 + 24(100) = 2,460."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A gearbox designer writes the total backlash of a drive train, in microns, as "
            "\\(\\frac{6x^{2}-7x-20}{3x+4}\\), where x is the number of meshing stages and "
            "\\(x>2\\). Which expression is equivalent to that backlash?"),
      choices=["\\(2x+5\\)", "\\(2x-5\\)", "\\(3x-5\\)", "\\(2x-4\\)"], correct="B",
      check="6x^2-7x-20 factors as (3x+4)(2x-5), so the quotient is 2x-5."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A cider press operator models the extra juice, in litres, obtained from n additional "
            "pressings of the same pomace as \\(J(n)=-8n^{2}+192n-300\\). How many additional "
            "pressings give the greatest extra yield under this model?"),
      choices=["6", "8", "10", "12"], correct="D",
      check="The vertex is at n = 192/16 = 12."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A fisheries survey uses a tracer whose activity, in becquerels, d days after it is "
            "released is \\(A(d)=6{,}250\\left(\\frac{1}{5}\\right)^{d}\\). After how many days "
            "does this model give an activity of 2 becquerels?"),
      choices=["3", "4", "5", "6"], correct="C",
      check="6,250/2 = 3,125 = 5^5, so d = 5."),

 dict(n="H1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The path of a survey drone is modelled by \\(y=x^{2}+4x-7\\) and a taut guide cable "
            "by \\(y=6x+8\\), where x and y are measured in metres. The two paths meet at two "
            "points. What is the sum of the x-coordinates of those two points?"),
      choices=["-15", "2", "5", "8"], correct="B",
      check="x^2+4x-7 = 6x+8 gives x^2-2x-15 = 0, whose roots 5 and -3 sum to 2."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A pipe-flow chart converts a gauge pressure g, in bars, into a flow index F using "
            "\\(F=\\frac{5g-8}{3}\\). Which expression gives g in terms of F?"),
      choices=["\\(\\frac{3F-8}{5}\\)", "\\(\\frac{5F+8}{3}\\)", "\\(\\frac{5F-8}{3}\\)",
               "\\(\\frac{3F+8}{5}\\)"], correct="D",
      check="3F = 5g - 8, so g = (3F+8)/5."),

 dict(n="H1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A wind-tunnel report gives the drag index of a fairing as \\(h(x)=3x^{2}-12x+5\\), "
            "where x is the taper setting used on the model. What is the least value the drag "
            "index takes?"),
      choices=["-7", "-5", "2", "5"], correct="A",
      check="The vertex is at x = 2, where h = 12 - 24 + 5 = -7."),

 dict(n="H1-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A charity's endowment is drawn down at a rate of 18% of its balance each year, so that "
            "82% of the balance is carried forward. The endowment is worth $12,500 now. To the "
            "nearest dollar, what will it be worth in 3 years?"),
      choices=["$6,892", "$7,175", "$8,610", "$9,225"], correct="A",
      check="12,500(0.82)^3 = 6,892.1, which rounds to 6,892."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A rope-walk twists 3 metres of finished cord from every 8 hanks of hemp, and hemp "
            "costs $6.50 a hank. What is the cost of the hemp needed to twist 21 metres of cord?"),
      choices=["$273", "$312", "$338", "$364"], correct="D",
      check="21/3 = 7 lots of 8 hanks is 56 hanks, and 56($6.50) = $364."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A commuter railway cut every fare by 15%, after which the number of journeys sold each "
            "day rose by 40%. The railway's daily fare revenue after both changes was what percent "
            "of its daily fare revenue before them?"),
      choices=["102%", "119%", "125%", "140%"], correct="B",
      check="(0.85)(1.40) = 1.19, which is 119%."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of hand-thrown pots fired in each of four kilns at a "
            "pottery, together with the percent of the pots in each kiln that cracked."
            + table(["Kiln", "Pots fired", "Percent that cracked"],
                    [["Aldon", "250", "8%"], ["Beck", "180", "5%"],
                     ["Cray", "320", "10%"], ["Dell", "150", "4%"]])
            + "How many of the pots fired in these four kilns cracked?"),
      choices=["67", "71", "76", "82"], correct="A",
      check="20 + 9 + 32 + 6 = 67."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("Over the first 8 days of a month, the mean daily rainfall recorded at a hill station "
            "was 4.5 millimetres. Over the first 12 days of that same month, the mean daily "
            "rainfall was 5.25 millimetres. What was the mean daily rainfall, in millimetres, over "
            "days 9 through 12?"),
      answers=["6.75", "27/4"],
      check="12(5.25) - 8(4.5) = 63 - 36 = 27 mm over 4 days, so the mean is 6.75."),

 dict(n="H1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A stained-glass panel is cut in the shape of triangle \\(JKL\\). Angle J measures "
            "40&deg;, and angle K measures 3 times as much as angle L. What is the measure, in "
            "degrees, of angle K?"),
      choices=["35", "70", "105", "140"], correct="C",
      check="40 + 3L + L = 180 gives L = 35, so angle K measures 105 degrees."),

 dict(n="H1-20", domain="GT", skill="GT-TR", type="MC",
      stem=("A conservator props a straight brace against a vertical wall so that the brace makes "
            "an angle of 60&deg; with the level floor and touches the wall 12 metres above the "
            "floor. What is the length of the brace, in metres?"),
      choices=["\\(4\\sqrt{3}\\)", "\\(6\\sqrt{3}\\)", "\\(8\\sqrt{3}\\)", "\\(24\\)"],
      correct="C",
      check="sin 60 = 12/L gives L = 24/sqrt(3) = 8 sqrt(3)."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A sculptor casts a small bronze maquette that uses 350 cubic centimetres of bronze, "
            "then casts a finished statue similar to the maquette with every dimension 3 times as "
            "large. How many cubic centimetres of bronze does the finished statue use?"),
      answers=["9450"],
      check="The volume ratio is 3^3 = 27, and 350(27) = 9,450."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A rainwater butt is a right circular cylinder whose base has an area of 1,800 square "
            "centimetres. The butt holds 27 litres of water, and 1 litre is 1,000 cubic "
            "centimetres. What is the depth of the water in the butt, in centimetres?"),
      answers=["15"],
      check="27,000 cubic centimetres divided by 1,800 square centimetres is 15."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A courier works out the fee for a parcel, in dollars, as \\(5x-13\\), where x is the "
            "mass of the parcel in kilograms. The fee for one parcel came to $42. What was that "
            "parcel's mass, in kilograms?"),
      choices=["6", "9", "10", "11"], correct="D",
      check="5x - 13 = 42 gives 5x = 55 and x = 11."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a harbour market, mackerel costs $4 a kilogram and squid costs $9 a kilogram. A "
            "chef bought 5 kilograms of mackerel together with some squid and spent $65 in all. "
            "How many kilograms of squid did the chef buy?"),
      choices=["4", "5", "6", "9"], correct="B",
      check="65 - 5(4) = 45, and 45/9 = 5 kilograms."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A lighthouse keeper's logbook has 260 blank pages at the start of a season, and 3 of "
            "those pages are filled in each day. Which expression gives the number of blank pages "
            "left after d days?"),
      choices=["\\(260-3d\\)", "\\(260d-3\\)", "\\(3d-260\\)", "\\(263d\\)"], correct="A",
      check="Start at 260 and take away 3 for each day."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A tram network sets the fare for a journey by the rule \\(C(k)=1.80+0.45k\\), where k "
            "is the length of the journey in kilometres and \\(C(k)\\) is the fare in dollars. "
            "What is the best interpretation of 1.80 in this model?"),
      choices=["The number of kilometres that a fare of $1.80 covers.",
               "The fare, in dollars, charged for each kilometre travelled.",
               "The total fare, in dollars, for a journey of 45 kilometres.",
               "The fixed charge, in dollars, that applies to every journey however long it is."],
      correct="D",
      check="At k = 0 the fare is $1.80, the part of the fare that does not depend on distance."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A gallery will hang an open show only if no more than 40 works are submitted. Which "
            "inequality gives all the possible numbers w of submitted works for which the show is "
            "hung?"),
      choices=["\\(w<40\\)", "\\(w\\le 40\\)", "\\(w\\ge 40\\)", "\\(w>40\\)"], correct="B",
      check="No more than 40 means 40 or fewer."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("One third of the seats in a village cinema are in the balcony. The cinema has 42 "
            "balcony seats. How many seats does the cinema have altogether?"),
      choices=["14", "84", "126", "168"], correct="C",
      check="3(42) = 126."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A church candle stands 30 centimetres tall when it is lit and burns down 2.5 "
            "centimetres in each hour that it is alight. How tall is the candle, in centimetres, "
            "after it has been alight for 6 hours?"),
      choices=["12", "15", "18", "25"], correct="B",
      check="30 - 2.5(6) = 30 - 15 = 15."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A joiner cuts \\(5m+8\\) dowels for the frame of a cabinet and \\(3m-2\\) dowels for "
            "its shelves, where m is the number of shelves. Which expression gives the total "
            "number of dowels the joiner cuts?"),
      choices=["\\(8m+6\\)", "\\(8m+10\\)", "\\(2m+10\\)", "\\(15m-16\\)"], correct="A",
      check="(5m+8) + (3m-2) = 8m + 6."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A mosaic border has an area of \\(6y^{2}-15y\\) square centimetres, where y is its "
            "width in centimetres. Which expression is equivalent to that area?"),
      choices=["\\(3y(2y+5)\\)", "\\(6y(y-15)\\)", "\\(3y(2y-15)\\)", "\\(3y(2y-5)\\)"],
      correct="D",
      check="3y is a common factor, leaving 3y(2y-5)."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A toboggan run's drag index is modelled by \\(D(v)=v^{2}-3\\), where v is the "
            "toboggan's speed in metres per second. What is the drag index at a speed of 7 metres "
            "per second?"),
      choices=["11", "32", "46", "52"], correct="C",
      check="7^2 - 3 = 46."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A colony of mites doubles in size every hour, so after x hours the colony is "
            "\\(2^{x}\\) times as large as it was at the start. After how many hours is the colony "
            "64 times as large as it was at the start?"),
      choices=["5", "6", "8", "32"], correct="B",
      check="2^6 = 64, so x = 6."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The illuminance from a lamp d metres away, in lux, is modelled by "
            "\\(L(d)=\\frac{144}{d^{2}}\\). What is the illuminance 4 metres from the lamp?"),
      choices=["9", "12", "36", "144"], correct="A",
      check="144/16 = 9."),

 dict(n="H2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A stage crew's setup time, in minutes, is \\(4(2p-3)+5p\\), where p is the number of "
            "platforms being built. Which expression is equivalent to that setup time?"),
      choices=["\\(13p-12\\)", "\\(13p-3\\)", "\\(8p-12\\)", "\\(7p-12\\)"], correct="A",
      check="4(2p-3) = 8p - 12, and 8p - 12 + 5p = 13p - 12."),

 dict(n="H2E-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A struck tuning fork has an amplitude, in micrometres, of "
            "\\(A(h)=80\\left(\\frac{1}{2}\\right)^{h}\\) after h seconds. What is the amplitude "
            "3 seconds after the fork is struck?"),
      choices=["10", "20", "40", "77"], correct="A",
      check="80(1/8) = 10."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dyer's recipe calls for 3 parts woad to 5 parts water by volume. One batch made to "
            "this recipe uses 45 litres of water. How many litres of woad does that batch use?"),
      choices=["15", "21", "27", "75"], correct="C",
      check="(3/5)(45) = 27."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A cycle shop's stock of helmets fell from 250 helmets to 210 helmets during one month. "
            "By what percent did the stock fall?"),
      choices=["16%", "20%", "25%", "40%"], correct="A",
      check="40/250 = 0.16, which is 16%."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the rainfall, in millimetres, recorded at a moorland gauge in each of "
            "four months."
            + table(["Month", "Rainfall (mm)"],
                    [["April", "62"], ["May", "48"], ["June", "35"], ["July", "41"]])
            + "What was the total rainfall, in millimetres, over these four months?"),
      choices=["176", "186", "196", "206"], correct="B",
      check="62 + 48 + 35 + 41 = 186."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("The lengths, in centimetres, of the seven pike caught during a river survey were 42, "
            "55, 61, 38, 74, 50 and 66. What is the median of these seven lengths, in "
            "centimetres?"),
      answers=["55"],
      check="In order the lengths are 38, 42, 50, 55, 61, 66, 74, and the fourth is 55."),

 dict(n="H2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A straight garden path runs into a long straight wall, meeting it at a single point "
            "and making two angles with the wall. One of those two angles measures 63&deg;. What "
            "is the measure, in degrees, of the other angle?"),
      choices=["27", "63", "117", "243"], correct="C",
      check="180 - 63 = 117."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="MC",
      stem=("An ornamental pond is a circle of radius 9 metres. What is the area of the pond, in "
            "square metres?"),
      choices=["\\(9\\pi\\)", "\\(18\\pi\\)", "\\(81\\pi\\)", "\\(162\\pi\\)"], correct="C",
      check="pi(9^2) = 81 pi."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A shipping crate is a rectangular prism measuring 4 feet long, 3 feet wide and 5 feet "
            "tall. What is the volume of the crate, in cubic feet?"),
      answers=["60"],
      check="4(3)(5) = 60."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A carpenter stiffens a right-angled corner with a straight diagonal batten. The two "
            "arms of the corner measure 9 centimetres and 12 centimetres. How many centimetres "
            "long is the batten?"),
      answers=["15"],
      check="The batten is the hypotenuse: 9-12-15 is a right triangle."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two balance conditions in a chemical process are written as \\(6x-4y=14\\) and "
            "\\(9x+ky=21\\), where k is a constant. Every pair \\((x,y)\\) that satisfies the "
            "first condition also satisfies the second. What is the value of k?"),
      choices=["-6", "-4", "4", "6"], correct="A",
      check="The second equation must be 1.5 times the first, so k = 1.5(-4) = -6."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A pressure transducer's calibration is a linear function f that turns a raw count into "
            "a corrected reading. The calibration record shows \\(f(-1)=11\\) and \\(f(5)=-7\\). "
            "What is the value of \\(f(9)\\)?"),
      choices=["-19", "-13", "-7", "5"], correct="A",
      check="Slope -18/6 = -3 and f(x) = -3x + 8, so f(9) = -19."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A joinery makes stools and benches from the same stock of oak. Each stool uses 3 "
            "board-feet of oak and each bench uses 8 board-feet, and at most 240 board-feet are "
            "available. The joinery must also make at least 3 times as many stools as benches. "
            "What is the greatest number of benches the joinery can make?"),
      choices=["10", "12", "13", "14"], correct="D",
      check="With stools at 3 times the benches, 9b + 8b = 17b <= 240 gives b <= 14.1, so 14."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tug leaves a jetty and travels along a straight channel at a constant 14 kilometres "
            "per hour. Two hours later a launch leaves the same jetty along the same channel at a "
            "constant 21 kilometres per hour. How many kilometres from the jetty does the launch "
            "draw level with the tug?"),
      choices=["56", "84", "98", "126"], correct="B",
      check="14(t+2) = 21t gives t = 4 hours for the launch, and 21(4) = 84 km."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="FR",
      stem=("A haulier charges $95 for the first 40 kilometres of any delivery and a fixed amount "
            "for each kilometre beyond the first 40. A delivery of 130 kilometres costs $455. How "
            "many dollars does a delivery of 200 kilometres cost?"),
      answers=["735"],
      check="360/90 = $4 per extra km, so 95 + 160(4) = 735."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A market stall's takings satisfy \\(3a+5c=41\\) and \\(5a+3c=47\\), where a is the "
            "price in dollars of an apron and c is the price in dollars of a cushion. What is the "
            "combined price, in dollars, of one apron and one cushion?"),
      choices=["8", "11", "16", "22"], correct="B",
      check="Adding gives 8a + 8c = 88, so a + c = 11."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A kiln must be held at a temperature of at least 940 degrees Celsius and at most 1,060 "
            "degrees Celsius. The controller reading r and the temperature T, in degrees Celsius, "
            "are related by \\(T=25r+540\\). Which inequality gives every controller reading r "
            "that holds the kiln in the required range?"),
      choices=["\\(15.2\\le r\\le 19.2\\)", "\\(16\\le r\\le 21.2\\)",
               "\\(37.6\\le r\\le 42.4\\)", "\\(16\\le r\\le 20.8\\)"], correct="D",
      check="940 <= 25r + 540 <= 1,060 gives 400 <= 25r <= 520 and 16 <= r <= 20.8."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A calibration routine for a densitometer uses the two functions \\(q(z)=z^{2}-2\\) and "
            "\\(p(z)=az+7\\), where a is a constant. Feeding the reading 3 into q and then feeding "
            "the result of that into p produces 35. What is the value of a?"),
      choices=["4", "5", "7", "28"], correct="A",
      check="q(3) = 7 and p(7) = 7a + 7 = 35, so a = 4."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("An optics model gives the effective gain of a lens stack as "
            "\\(\\frac{2x^{2}-18}{x^{2}+6x+9}\\), where \\(x>0\\). Which expression is equivalent "
            "to that gain?"),
      choices=["\\(\\frac{2(x+3)}{x-3}\\)", "\\(2x-6\\)", "\\(\\frac{2(x-3)}{x+3}\\)",
               "\\(\\frac{2x-18}{x+3}\\)"], correct="C",
      check="2(x-3)(x+3) over (x+3)^2 cancels to 2(x-3)/(x+3)."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The floor of a tunnel has the profile \\(y=x^{2}-6x+13\\), and a survey laser is set "
            "at the constant height \\(y=k\\), with x and y in metres. The laser meets the floor "
            "profile at exactly one point. What is the value of k?"),
      choices=["3", "4", "9", "13"], correct="B",
      check="x^2-6x+13-k = 0 has one solution when 36 = 4(13-k), so k = 4."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rectangular allotment plot is 7 metres longer than it is wide and covers 330 square "
            "metres. What is the perimeter of the plot, in metres?"),
      choices=["44", "64", "74", "82"], correct="C",
      check="w(w+7) = 330 gives w = 15, so the plot is 15 by 22 and the perimeter is 74."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A materials index is recorded as "
            "\\(\\frac{\\left(27b^{6}\\right)^{\\frac{4}{3}}}{9b^{5}}\\), where \\(b>0\\). Which "
            "expression is equivalent to that index?"),
      choices=["\\(3b^{2}\\)", "\\(3b^{3}\\)", "\\(9b^{2}\\)", "\\(9b^{3}\\)"], correct="D",
      check="The numerator is 81b^8, and dividing by 9b^5 leaves 9b^3."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The height of a suspended footbridge cable above the deck is modelled by "
            "\\(s(x)=\\frac{1}{50}(x-30)^{2}+c\\) metres, where x is the distance in metres from "
            "one tower and c is a constant. The cable is 20 metres above the deck at \\(x=0\\). "
            "How many metres above the deck is the cable at \\(x=50\\)?"),
      choices=["8", "10", "12", "18"], correct="B",
      check="900/50 + c = 20 gives c = 2, and 400/50 + 2 = 10."),

 dict(n="H2H-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A culture of yeast triples in mass every 5 hours, and its mass is 12 grams at the "
            "moment the culture is started. Which function gives the mass of the culture, in "
            "grams, t hours after it is started?"),
      choices=["\\(12\\cdot 3^{\\frac{t}{5}}\\)", "\\(12\\cdot 5^{\\frac{t}{3}}\\)",
               "\\(12\\cdot 3^{5t}\\)", "\\(3\\cdot 12^{\\frac{t}{5}}\\)"], correct="A",
      check="The mass is multiplied by 3 once every 5 hours, so the exponent is t/5."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean mass of the 14 salmon held in one tank of a hatchery is 4.2 kilograms, and "
            "the mean mass of the 6 salmon held in a second tank is 5.7 kilograms. What is the "
            "mean mass, in kilograms, of all 20 salmon?"),
      choices=["4.35", "4.5", "4.65", "4.95"], correct="C",
      check="(14(4.2) + 6(5.7))/20 = 93/20 = 4.65."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table summarises a survey of 240 allotment holders, each classified by whether "
            "they keep bees and by whether they grow soft fruit."
            + table(["", "Grows soft fruit", "Does not grow soft fruit"],
                    [["Keeps bees", "54", "26"], ["Does not keep bees", "96", "64"]])
            + "Of the surveyed allotment holders who grow soft fruit, what fraction keep bees?"),
      choices=["\\(\\frac{9}{40}\\)", "\\(\\frac{9}{25}\\)", "\\(\\frac{27}{40}\\)",
               "\\(\\frac{5}{8}\\)"], correct="B",
      check="150 grow soft fruit and 54 of them keep bees, so the fraction is 54/150 = 9/25."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A conveyor delivers crushed stone into a wagon at a constant 45 kilograms per minute. "
            "The wagon holds 13.5 tonnes of stone, and 1 tonne is 1,000 kilograms. How many hours "
            "does the conveyor take to fill the wagon?"),
      choices=["3", "4", "5", "6"], correct="C",
      check="13,500/45 = 300 minutes, which is 5 hours."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A researcher measured the wingspan of each of 60 randomly selected gulls from a colony "
            "of 900 gulls and found that 21 of the selected gulls had a wingspan of more than 140 "
            "centimetres. Based on this sample, how many of the 900 gulls would be estimated to "
            "have a wingspan of more than 140 centimetres?"),
      answers=["315"],
      check="(21/60)(900) = 315."),

 dict(n="H2H-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A trestle frame is built in the shape of triangle \\(ABC\\), with a cross-brace "
            "\\(DE\\) joining a point D on \\(AB\\) to a point E on \\(AC\\) so that \\(DE\\) is "
            "parallel to \\(BC\\). The brace divides \\(AB\\) so that \\(AD=6\\) feet and "
            "\\(DB=9\\) feet, and the brace itself is 8 feet long. What is the length, in feet, of "
            "\\(BC\\)?"),
      choices=["12", "14", "20", "24"], correct="C",
      check="AD/AB = 6/15 = 2/5, so BC = 8(5/2) = 20."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A grain hopper is a right circular cylinder of radius 3 metres and height 5 metres "
            "with a cone of the same radius and of height 4 metres fixed on top of it. What is the "
            "total volume of the hopper, in cubic metres?"),
      choices=["\\(45\\pi\\)", "\\(57\\pi\\)", "\\(69\\pi\\)", "\\(81\\pi\\)"], correct="B",
      check="Cylinder 45 pi plus cone 12 pi gives 57 pi."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A draughtsman's set square is a right triangle \\(LMN\\) whose right angle is at N. "
            "The leg \\(LN\\) measures 24 centimetres and the leg \\(MN\\) measures 7 centimetres. "
            "What is the value of \\(\\cos L\\)?"),
      choices=["\\(\\frac{7}{24}\\)", "\\(\\frac{7}{25}\\)", "\\(\\frac{24}{7}\\)",
               "\\(\\frac{24}{25}\\)"], correct="D",
      check="The hypotenuse is 25, so cos L = 24/25."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A solid metal cube whose edges are 10 centimetres long is melted down and recast, with "
            "no metal lost, into a single solid rectangular block measuring 25 centimetres by 8 "
            "centimetres by h centimetres. What is the value of h?"),
      answers=["5"],
      check="1,000 cubic centimetres divided by 200 square centimetres is 5."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
