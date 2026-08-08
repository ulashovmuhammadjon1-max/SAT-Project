#!/usr/bin/env python3
"""
Original Math content for Test 9 — all three modules, 66 questions.

Difficulty, matching the Test 8 build:

  MODULE_1      upper-medium. Two-to-three step setups, a rearrangement before
                the arithmetic, or a constant to solve for. Still the routing
                module, so it stays below Module 2 (Hard).
  MODULE_2_EASY genuinely easy — one step, the lower branch of the split.
  MODULE_2_HARD hard. Parameters rather than numbers, structural answers,
                composed functions, systems conditioned on a constant, and
                geometry needing two relationships at once.

House style follows Test 1/2 (see CLAUDE.md). LaTeX typed by hand.
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
 dict(n="B1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A student council compares two banner printers. The first charges a $60 setup fee "
            "plus $4.00 for each banner. The second charges no setup fee but $6.50 for each "
            "banner. For how many banners would the two printers charge the same total amount?"),
      choices=["15", "18", "21", "24"], correct="D",
      check="60 + 4b = 6.5b gives 2.5b = 60 and b = 24."),

 dict(n="B1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a canteen, four sandwiches and three cartons of juice cost $26, while two "
            "sandwiches and five cartons of juice cost $20. What is the total cost, in dollars, "
            "of three sandwiches and two cartons of juice?"),
      choices=["15", "17", "19", "23"], correct="C",
      check="Sandwich $5 and juice $2, so 3(5) + 2(2) = 19."),

 dict(n="B1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A hot-air balloon descends at a constant rate. Its altitude is 1,410 metres 6 "
            "minutes after the descent begins and 1,050 metres 12 minutes after it begins. How "
            "many minutes after the descent begins is the balloon at an altitude of 450 metres?"),
      choices=["18", "22", "26", "30"], correct="B",
      check="Rate -60 m per minute, so altitude = 1770 - 60t and 450 gives t = 22."),

 dict(n="B1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A tutor spends $140 on workbooks at the start of a term and then charges $22 for "
            "each tutoring session. What is the least number of sessions the tutor must hold so "
            "that the money collected exceeds the cost of the workbooks by at least $500?"),
      choices=["27", "29", "30", "32"], correct="C",
      check="22n - 140 >= 500 needs n >= 29.09, so 30 sessions."),

 dict(n="B1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A mobile plan charges a monthly bill of \\(B=18+0.06(m-250)\\) dollars for a month "
            "in which m minutes are used, where \\(m>250\\). One month the bill was $39.60. How "
            "many minutes were used that month?"),
      choices=["360", "410", "560", "610"], correct="D",
      check="21.60/0.06 = 360 extra minutes above 250, so m = 610."),

 dict(n="B1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, a pipeline is laid along a line with slope \\(-\\frac{3}{5}\\) that "
            "passes through the point \\((10, 4)\\). A second pipeline runs parallel to the first "
            "and passes through the origin. Which point lies on the second pipeline?"),
      choices=["(5, -3)", "(3, -5)", "(-3, 5)", "(-5, -3)"], correct="A",
      check="Second line is y = -3x/5, and -3(5)/5 = -3."),

 dict(n="B1-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The members of a hiking club share the cost of a minibus equally. If three more "
            "members join the trip, the share paid by each member falls from $28 to $21. How "
            "many members were going on the trip before the three joined?"),
      choices=["6", "9", "12", "15"], correct="B",
      check="28m = 21(m+3) gives 7m = 63 and m = 9."),

 dict(n="B1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A rectangular courtyard measures \\(2x+5\\) metres by \\(x-3\\) metres. A square "
            "fountain of side \\(x\\) metres is built inside it. Which expression gives the area, "
            "in square metres, of the part of the courtyard not covered by the fountain?"),
      choices=["\\(x^{2}-x-15\\)", "\\(x^{2}+x-15\\)", "\\(x^{2}-x+15\\)", "\\(3x^{2}-x-15\\)"],
      correct="A",
      check="(2x+5)(x-3) - x^2 = 2x^2 - x - 15 - x^2 = x^2 - x - 15."),

 dict(n="B1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A workshop's cost per unit, in dollars, of producing x thousand ceramic tiles is "
            "modelled by \\(C(x)=0.5x^{2}-6x+38\\). What is the least cost per unit the model "
            "predicts?"),
      choices=["6", "14", "18", "20"], correct="D",
      check="Vertex at x = 6, and C(6) = 18 - 36 + 38 = 20."),

 dict(n="B1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The number of daily downloads of a new app is modelled by \\(D(d)=50\\cdot3^{d}\\), "
            "where d is the number of days since the app was released. After how many days does "
            "the model predict 4,050 downloads in a day?"),
      choices=["3", "4", "5", "6"], correct="B",
      check="4050/50 = 81 = 3^4, so d = 4."),

 dict(n="B1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The length and the width, in metres, of a rectangular slab are the two solutions of "
            "\\(x^{2}-14x+c=0\\), where c is a constant. The length is 6 metres greater than the "
            "width. What is the value of c?"),
      choices=["24", "32", "40", "45"], correct="C",
      check="Solutions sum to 14 and differ by 6, so they are 10 and 4 and c = 40."),

 dict(n="B1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A hardware supplier holds \\(x^{2}-9\\) bolts and \\(x^{2}+7x+12\\) nuts, where "
            "\\(x>3\\). Which expression gives the ratio of bolts to nuts in lowest terms?"),
      choices=["\\(\\frac{x+3}{x+4}\\)", "\\(\\frac{x-3}{x-4}\\)", "\\(\\frac{x-9}{x+12}\\)",
               "\\(\\frac{x-3}{x+4}\\)"], correct="D",
      check="(x-3)(x+3) over (x+3)(x+4) reduces to (x-3)/(x+4)."),

 dict(n="B1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A packaging machine bought for $18,000 loses 15% of its value at the end of each "
            "year of use. What will the machine be worth at the end of the second year?"),
      choices=["$12,750", "$13,005", "$13,230", "$15,300"], correct="B",
      check="18000(0.85)^2 = 18000(0.7225) = 13005."),

 dict(n="B1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A press prints 1,250 pages in 25 minutes. Working at that same rate without "
            "stopping, how many hours would the press take to print 21,000 pages?"),
      choices=["4.2", "5.25", "6", "7"], correct="D",
      check="50 pages per minute, so 21000/50 = 420 minutes = 7 hours."),

 dict(n="B1-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table records the rainfall measured at a weather station over four months."
            + table(["Month", "Rainfall (millimetres)"],
                    [["January", "84"], ["February", "96"], ["March", "120"], ["April", "150"]])
            + "What is the percent increase in rainfall from February to April?"),
      choices=["36%", "54%", "56.25%", "64%"], correct="C",
      check="(150-96)/96 = 0.5625, an increase of 56.25%."),

 dict(n="B1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A town has 12,000 registered voters. In a random sample of 200 of them, 45 said "
            "they had voted in the last local election. Based on this sample, what is the best "
            "estimate of the number of registered voters in the town who voted in that election?"),
      choices=["2,250", "2,700", "3,000", "4,500"], correct="B",
      check="45/200 = 0.225, and 0.225(12000) = 2700."),

 dict(n="B1-17", domain="GT", skill="GT-LA", type="MC",
      stem=("In a triangular window frame, the second angle measures 32&deg; more than the first "
            "angle and the third angle measures twice the first angle. What is the measure, in "
            "degrees, of the third angle?"),
      choices=["37", "69", "74", "106"], correct="C",
      check="a + (a+32) + 2a = 180 gives a = 37, so the third angle is 74."),

 dict(n="B1-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A grain silo is a cylinder of radius 6 metres and height 20 metres. A second silo is "
            "also a cylinder, with twice the radius and half the height of the first. The volume "
            "of the second silo is how many times the volume of the first?"),
      choices=["2", "4", "8", "16"], correct="A",
      check="(2r)^2(h/2) divided by r^2 h is 4(1/2) = 2."),

 dict(n="B1-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A loading ramp runs in a straight line from level ground up to a dock. The sloping "
            "surface of the ramp is 13 metres long and the dock is 5 metres above the ground. "
            "What is the tangent of the angle the ramp makes with the ground?"),
      choices=["\\(\\frac{5}{12}\\)", "\\(\\frac{12}{5}\\)", "\\(\\frac{5}{13}\\)",
               "\\(\\frac{12}{13}\\)"], correct="A",
      check="DF = sqrt(169-25) = 12, so tan D = 5/12."),

 dict(n="B1-20", domain="ADV", skill="ADV-NE", type="FR",
      stem=("A model rocket is launched from the ground so that its height, in metres, t seconds "
            "after launch is \\(h(t)=-5t^{2}+40t\\). For how many seconds is the rocket at a "
            "height of 60 metres or more?"),
      answers=["4"],
      check="-5t^2+40t = 60 gives t = 2 and t = 6, an interval of 4 seconds."),

 dict(n="B1-21", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A 2.5-litre bottle of squash concentrate makes 40 litres of drink once diluted. How "
            "many millilitres of concentrate are needed to make 6 litres of the drink?"),
      answers=["375"],
      check="2500 mL / 40 L = 62.5 mL per litre, and 62.5(6) = 375."),

 dict(n="B1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("An aquarium is a rectangular prism with a base measuring 80 centimetres by 40 "
            "centimetres and a depth of 50 centimetres. It is filled with water to three-quarters "
            "of its depth. How many litres of water does it hold? (1 litre = 1,000 cubic "
            "centimetres.)"),
      answers=["120"],
      check="80(40)(37.5) = 120000 cubic centimetres = 120 litres."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="B2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A parking meter accepts only quarters, each worth $0.25. A driver pays $3.50 using "
            "only quarters. How many quarters does the driver use?"),
      choices=["7", "10", "12", "14"], correct="D", check="3.50/0.25 = 14."),

 dict(n="B2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The temperature inside a freezer rose by 7 degrees Fahrenheit to reach -8&deg;F. "
            "What was the temperature, in degrees Fahrenheit, before it rose?"),
      choices=["-15", "-1", "1", "15"], correct="A", check="-8 - 7 = -15."),

 dict(n="B2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A paddling pool is 150 centimetres deep and loses 3 centimetres of depth each day to "
            "evaporation. Which equation gives the depth d, in centimetres, after t days?"),
      choices=["\\(d=150+3t\\)", "\\(d=150-3t\\)", "\\(d=3t-150\\)", "\\(d=3-150t\\)"],
      correct="B", check="Start at 150 and subtract 3 per day."),

 dict(n="B2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A taxi ride costs a flat $4 plus $1.50 for each kilometre travelled. What is the "
            "cost, in dollars, of a ride of 10 kilometres?"),
      choices=["14", "15.50", "19", "54"], correct="C", check="4 + 1.5(10) = 19."),

 dict(n="B2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A hiker's backpack must have a total mass of no more than 9 kilograms. It already "
            "holds 5.4 kilograms of gear. Which inequality describes the mass w, in kilograms, "
            "that may still be added?"),
      choices=["\\(w\\le 3.6\\)", "\\(w\\ge 3.6\\)", "\\(w\\le 14.4\\)", "\\(w\\le 9\\)"],
      correct="A", check="9 - 5.4 = 3.6, so w is at most 3.6."),

 dict(n="B2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A ticket seller sold three identical passes, took $5 off the total as a discount, "
            "and collected $22. What was the price, in dollars, of one pass before the discount?"),
      choices=["6", "7", "8", "9"], correct="D", check="3p - 5 = 22 gives p = 9."),

 dict(n="B2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A candle burns at a constant rate. Its height, in centimetres, after h hours of "
            "burning is given by \\(H=24-2h\\). By how many centimetres does the candle's height "
            "decrease each hour?"),
      choices=["1", "2", "12", "24"], correct="B", check="The rate is the coefficient of h, 2."),

 dict(n="B2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A tailor uses \\(3x+2\\) metres of ribbon on one banner and \\(5x-9\\) metres on "
            "another. Which expression gives the total length of ribbon used, in metres?"),
      choices=["\\(8x+11\\)", "\\(8x-11\\)", "\\(8x-7\\)", "\\(15x-18\\)"], correct="C",
      check="(3x+2)+(5x-9) = 8x - 7."),

 dict(n="B2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A photographer files \\(x^{8}\\) images into \\(x^{5}\\) folders, putting the same "
            "number of images into every folder, where \\(x>1\\). How many images go into each "
            "folder?"),
      choices=["\\(x^{13}\\)", "\\(x^{40}\\)", "\\(x^{4}\\)", "\\(x^{3}\\)"], correct="D",
      check="x^8 divided by x^5 is x^3."),

 dict(n="B2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A drone's altitude, in metres, t seconds after it takes off is given by "
            "\\(A(t)=2t^{2}+1\\). What is the drone's altitude 3 seconds after takeoff?"),
      choices=["13", "19", "37", "55"], correct="B", check="2(9) + 1 = 19."),

 dict(n="B2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A packing crate is a cube with a volume of 27 cubic feet. What is the length, in "
            "feet, of one edge of the crate?"),
      choices=["3", "9", "13.5", "27"], correct="A", check="The cube root of 27 is 3."),

 dict(n="B2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A colony of 30 beetles doubles in number every year. Which expression gives the "
            "number of beetles after y years?"),
      choices=["\\(30\\cdot y^{2}\\)", "\\(30+2y\\)", "\\(30\\cdot2^{y}\\)", "\\(2\\cdot30^{y}\\)"],
      correct="C", check="Doubling y times multiplies 30 by 2^y."),

 dict(n="B2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A caterer orders 6 identical boxes, and each box holds \\(2x-5\\) pastries. Which "
            "expression gives the total number of pastries ordered?"),
      choices=["\\(12x-30\\)", "\\(12x-5\\)", "\\(8x-30\\)", "\\(12x+30\\)"], correct="A",
      check="6(2x-5) = 12x - 30."),

 dict(n="B2E-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The path of a skateboard ramp is modelled in the xy-plane by \\(y=(x-2)(x+6)\\). "
            "Which value of x is an x-intercept of this graph?"),
      choices=["-2", "2", "6", "12"], correct="B", check="y = 0 at x = 2 and at x = -6."),

 dict(n="B2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A bakery sells 5 loaves of bread for $12. At that same rate, what is the cost, in "
            "dollars, of 15 loaves?"),
      choices=["18", "24", "30", "36"], correct="D", check="15 is 3 times 5, and 3(12) = 36."),

 dict(n="B2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A librarian recorded the number of books borrowed on five days: 3, 8, 11, 14 and 21. "
            "What is the median of these five values?"),
      choices=["8", "11", "11.4", "14"], correct="B", check="The middle value in order is 11."),

 dict(n="B2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of tickets a cinema sold for each of four films on one "
            "evening."
            + table(["Film", "Tickets sold"],
                    [["Aurora", "132"], ["Blue Ridge", "87"], ["Cypress", "145"],
                     ["Delta Nine", "96"]])
            + "How many more tickets were sold for Cypress than for Blue Ridge?"),
      choices=["58", "61", "87", "145"], correct="A", check="145 - 87 = 58."),

 dict(n="B2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A spinner is divided into 8 sections of equal size, and 3 of the sections are green. "
            "The spinner is spun once. What is the probability that it lands on a green section?"),
      choices=["\\(\\frac{1}{8}\\)", "\\(\\frac{3}{8}\\)", "\\(\\frac{5}{8}\\)",
               "\\(\\frac{3}{5}\\)"], correct="B", check="3 of 8 equally likely sections."),

 dict(n="B2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A fence post leans so that it makes an angle of 118&deg; with the ground on one "
            "side. What is the measure, in degrees, of the angle it makes with the ground on the "
            "other side?"),
      choices=["28", "32", "62", "152"], correct="C",
      check="The two angles are supplementary: 180 - 118 = 62."),

 dict(n="B2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A gift box in the shape of a rectangular prism measures 12 centimetres by 5 "
            "centimetres by 4 centimetres. How many cubic centimetres does the box hold?"),
      answers=["240"], check="12 times 5 times 4 = 240."),

 dict(n="B2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular swimming pool measures 25 metres by 12 metres. What is the perimeter "
            "of the pool, in metres?"),
      answers=["74"], check="2(25 + 12) = 74."),

 dict(n="B2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A rectangular gate is 9 feet wide and 12 feet tall. A brace runs in a straight line "
            "from one corner of the gate to the opposite corner. How many feet long is the "
            "brace?"),
      answers=["15"], check="sqrt(81 + 144) = sqrt(225) = 15."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="B2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("\\[ax+6y=18\\]\\[4x+ky=12\\]In the given system of equations, a and k are constants. "
            "If the system has infinitely many solutions, what is the value of \\(a+k\\)?"),
      choices=["8", "10", "12", "14"], correct="B",
      check="Scaling the second equation by 3/2 gives 6x + 1.5ky = 18, so a = 6 and k = 4."),

 dict(n="B2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, the line \\(y=mx+7\\) meets the line \\(2x+5y=20\\) at a point on "
            "the x-axis. What is the value of m?"),
      choices=["\\(-\\frac{7}{20}\\)", "\\(\\frac{7}{10}\\)", "\\(\\frac{10}{7}\\)",
               "\\(-\\frac{7}{10}\\)"], correct="D",
      check="The second line meets the x-axis at (10, 0), and 0 = 10m + 7 gives m = -7/10."),

 dict(n="B2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A workshop builds x chairs and y benches in a week. Building the chairs and benches "
            "uses \\(3x+2y\\) hours of labour, which cannot exceed 42 hours, and the workshop "
            "never builds fewer chairs than twice the number of benches. Which pair "
            "\\((x, y)\\) meets both requirements?"),
      choices=["(4, 10)", "(6, 8)", "(10, 4)", "(14, 2)"], correct="C",
      check="3(10)+2(4) = 38 <= 42 and 10 >= 2(4); every other pair fails one condition."),

 dict(n="B2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cable of length L metres is cut into two pieces so that the longer piece is k "
            "metres longer than 3 times the shorter piece. Which expression gives the length, in "
            "metres, of the shorter piece?"),
      choices=["\\(\\frac{L-k}{4}\\)", "\\(\\frac{L+k}{4}\\)", "\\(\\frac{L-k}{3}\\)",
               "\\(\\frac{L-3k}{4}\\)"], correct="A",
      check="s + (3s + k) = L gives 4s = L - k."),

 dict(n="B2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The function g is linear, \\(g(0)=c\\) and \\(g(6)=c+21\\), where c is a constant. "
            "Which expression gives the value of \\(g(10)\\)?"),
      choices=["\\(c+28\\)", "\\(c+31.5\\)", "\\(c+35\\)", "\\(c+42\\)"], correct="C",
      check="The rate of change is 21/6 = 3.5, so g(10) = c + 35."),

 dict(n="B2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("One pump can drain a reservoir in 6 hours, and a second pump can drain the same "
            "reservoir in 9 hours. If both pumps run together at their constant rates, how many "
            "hours do they take to drain the reservoir?"),
      choices=["3.6", "3.75", "4.5", "7.5"], correct="A",
      check="Combined rate 1/6 + 1/9 = 5/18 per hour, so the time is 18/5 = 3.6."),

 dict(n="B2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A machine shop accepts a bearing only if its diameter d, in millimetres, satisfies "
            "\\(|d-12.5|\\le 0.04\\). What is the smallest diameter, in millimetres, that the "
            "shop accepts?"),
      choices=["12.42", "12.46", "12.50", "12.54"], correct="B",
      check="12.5 - 0.04 = 12.46."),

 dict(n="B2H-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The number of insects caught in a trap on day x is modelled by "
            "\\(2x^{2}-12x+c\\), where c is a constant. If the model reaches zero for two "
            "distinct values of x, which inequality describes all such values of c?"),
      choices=["\\(c>18\\)", "\\(c\\le 18\\)", "\\(c\\ge 18\\)", "\\(c<18\\)"], correct="D",
      check="Two distinct real zeros need 144 - 8c > 0, so c < 18."),

 dict(n="B2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A cutting machine trims a board to a length of \\(3x-4\\) centimetres, where x is "
            "its dial setting. A press then stamps that board into a panel whose area, in square "
            "centimetres, is \\(L^{2}+2L\\), where L is the length of the trimmed board in "
            "centimetres. What is the area of the panel produced when the dial is set to 3?"),
      choices=["15", "24", "35", "44"], correct="C",
      check="f(3) = 5 and g(5) = 25 + 10 = 35."),

 dict(n="B2H-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A technician combines two measurements and obtains the expression "
            "\\[\\frac{2}{x-3}-\\frac{5}{x+2}\\]where \\(x\\ne 3\\) and \\(x\\ne -2\\). Which "
            "expression is equivalent to it?"),
      choices=["\\(\\frac{-3}{x^{2}-x-6}\\)", "\\(\\frac{-3x+19}{x^{2}-x-6}\\)",
               "\\(\\frac{7x-11}{x^{2}-x-6}\\)", "\\(\\frac{-3x-11}{x^{2}-x-6}\\)"], correct="B",
      check="2(x+2) - 5(x-3) = -3x + 19 over (x-3)(x+2)."),

 dict(n="B2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A beekeeper models a hive's population as \\(N(w)=N_{0}(1.2)^{w}\\), where w is the "
            "number of weeks since the hive was established and \\(N_{0}\\) is a constant. The "
            "model gives 864 bees after 3 weeks. What is the value of \\(N_{0}\\)?"),
      choices=["500", "600", "720", "750"], correct="A",
      check="1.2^3 = 1.728, and 864/1.728 = 500."),

 dict(n="B2H-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The side length s, in centimetres, of a square panel satisfies "
            "\\(\\sqrt{5s+6}=s\\). What is the value of s?"),
      choices=["-1", "2", "6", "11"], correct="C",
      check="s^2 - 5s - 6 = 0 gives s = 6 or s = -1, and a length must be positive."),

 dict(n="B2H-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("In a chemical mixture the mass of solute, a, and the mass of solvent, b, satisfy "
            "\\(\\frac{a}{b}=\\frac{3}{7}\\). What is the value of \\(\\frac{a+b}{b}\\)?"),
      choices=["\\(\\frac{3}{10}\\)", "\\(\\frac{10}{7}\\)", "\\(\\frac{7}{10}\\)",
               "\\(\\frac{4}{7}\\)"], correct="B",
      check="(a+b)/b = a/b + 1 = 3/7 + 1 = 10/7."),

 dict(n="B2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("In one class, 18 students scored a mean of 76 points on an assessment. In a second "
            "class, 12 students scored a mean of 86 points on the same assessment. What is the "
            "mean score of all 30 students?"),
      choices=["80", "81", "82", "86"], correct="A",
      check="(18(76) + 12(86))/30 = 2400/30 = 80."),

 dict(n="B2H-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A gallery marks up the wholesale price of a print by 40% and then sells it in a sale "
            "at 25% off the marked price. A print sells for $63 in the sale. What was its "
            "wholesale price, in dollars?"),
      choices=["54.00", "58.80", "60.00", "67.50"], correct="C",
      check="1.40(0.75) = 1.05, and 63/1.05 = 60."),

 dict(n="B2H-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of pets owned by each of the 25 households on one street."
            + table(["Number of pets", "Number of households"],
                    [["0", "4"], ["1", "9"], ["2", "5"], ["3", "4"], ["4", "3"]])
            + "How much greater is the mean number of pets per household than the median number "
              "of pets per household?"),
      choices=["0.28", "0.72", "1.00", "1.72"], correct="B",
      check="Mean 43/25 = 1.72, median is the 13th value, 1, so the difference is 0.72."),

 dict(n="B2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A researcher surveyed 300 employees selected at random from the 4,500 employees of a "
            "firm and found that 62% of those surveyed commute by train. The associated plausible "
            "range for the whole workforce is 58% to 66%. Which statement is best supported by "
            "this result?"),
      choices=["Exactly 2,790 of the 4,500 employees commute by train.",
               "It is plausible that between 174 and 198 of the 4,500 employees commute by train.",
               "Fewer than 2,610 of the 4,500 employees commute by train.",
               "It is plausible that between 2,610 and 2,970 of the 4,500 employees commute by train."],
      correct="D",
      check="58% of 4500 is 2610 and 66% is 2970."),

 dict(n="B2H-18", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle ABC, point D lies on side AB and point E lies on side AC so that DE is "
            "parallel to BC. Given that \\(AD=6\\), \\(DB=4\\) and \\(DE=9\\), what is the length "
            "of BC?"),
      choices=["6", "12", "13.5", "15"], correct="D",
      check="AD/AB = 6/10, so BC = 9(10/6) = 15."),

 dict(n="B2H-19", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle RST, angle T is a right angle and \\(\\tan R=\\frac{3}{4}\\). The "
            "hypotenuse RS has length 20. What is the length of ST?"),
      choices=["12", "15", "16", "20"], correct="A",
      check="Legs are 3k and 4k with 5k = 20, so k = 4 and ST = 12."),

 dict(n="B2H-20", domain="ADV", skill="ADV-NF", type="FR",
      stem=("A cable hangs in the shape of the parabola \\(y=x^{2}+bx+c\\), where b and c are "
            "constants, and the lowest point of the cable is at \\((3, -4)\\). What is the value "
            "of \\(b+c\\)?"),
      answers=["-1"],
      check="(x-3)^2 - 4 = x^2 - 6x + 5, so b = -6, c = 5 and b + c = -1."),

 dict(n="B2H-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A cylindrical tin is redesigned so that its radius increases by 20% and its height "
            "decreases by 25%. The volume of the redesigned tin is what percent of the volume of "
            "the original tin?"),
      answers=["108"],
      check="(1.2)^2(0.75) = 1.08, so 108 percent."),

 dict(n="B2H-22", domain="GT", skill="GT-TR", type="FR",
      stem=("An acute angle of one right triangle measures \\(2a^{\\circ}\\) and an acute angle "
            "of another right triangle measures \\(3a^{\\circ}\\). Given that "
            "\\(\\sin\\left(2a^{\\circ}\\right)=\\cos\\left(3a^{\\circ}\\right)\\), what is the "
            "value of a?"),
      answers=["18"],
      check="Sine and cosine agree on complementary angles: 2a + 3a = 90, so a = 18."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
