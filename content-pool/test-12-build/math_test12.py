#!/usr/bin/env python3
"""
Original Math content for Test 12 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. A constant has to be pinned down before the
                arithmetic can start, or two facts have to be combined. Harder
                than a Module 2 (Easy) item, deliberately below Module 2 (Hard).
  MODULE_2_EASY genuinely easy — one step, the lower branch of the split.
  MODULE_2_HARD hard. Parameters instead of numbers, structural answers,
                composed functions, a system conditioned on a constant, and
                geometry that needs two relationships at once.

Every setting is deliberately concrete and unusual (saffron blending, canal
locks, peat cutting, puffin colonies, wetsuit inspections, sluice gates) so
that no stem collides with the 660 Math stems already live in production.
House style follows Test 1/2 (see CLAUDE.md). LaTeX typed by hand — no bulk
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
 dict(n="E1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A saffron grower blends two grades of dried threads. The finer grade costs $9 per "
            "gram and the coarser grade costs $14 per gram. A 40-gram blend of the two grades "
            "costs $470. How many grams of the coarser grade are in that blend?"),
      choices=["16", "18", "20", "22"], correct="D",
      check="9(40-b) + 14b = 470 gives 5b = 110, so b = 22."),

 dict(n="E1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The snout of a glacier stood 1,096 metres from a marker cairn in 2005 and 1,240 "
            "metres from the same cairn in 2017, and it keeps retreating at that constant rate. "
            "In which year will the snout stand 1,396 metres from the cairn?"),
      choices=["2026", "2028", "2030", "2032"], correct="C",
      check="It retreats 144 m in 12 years, so 12 m per year; 156 more metres takes 13 years."),

 dict(n="E1-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A seed library has $540 to spend. It must first buy 3 display racks costing $46 "
            "each, and it will spend whatever is left on seed packets costing $2.75 each. What "
            "is the greatest number of seed packets the library can buy?"),
      choices=["144", "146", "148", "150"], correct="B",
      check="540 - 138 = 402 and 402/2.75 = 146.18, so 146 packets."),

 dict(n="E1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two pumps fill a canal lock working together. The larger pump moves 5 times as much "
            "water each minute as the smaller pump does. Together the two pumps deliver the "
            "lock's 4,320 cubic metres of water in 24 minutes. How many cubic metres of water "
            "does the smaller pump move each minute?"),
      choices=["25", "30", "36", "45"], correct="B",
      check="6s(24) = 4,320 gives s = 30."),

 dict(n="E1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The temperature inside a wine cellar, in degrees Celsius, t hours after the chiller "
            "is switched on is modelled by \\(T(t)=18-rt\\) , where r is a constant. The cellar "
            "is at 12.4&deg;C exactly 7 hours after the chiller is switched on. What temperature, "
            "in degrees Celsius, does the model predict 15 hours after the chiller is switched "
            "on?"),
      choices=["4.4", "5.2", "6", "7.2"], correct="C",
      check="r = 5.6/7 = 0.8, so T(15) = 18 - 12 = 6."),

 dict(n="E1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A hot-air balloon descends at a constant rate. An observer on the ground records the "
            "balloon's altitude as 1,860 metres 4 minutes after the descent begins and as 1,410 "
            "metres 10 minutes after the descent begins. What was the balloon's altitude, in "
            "metres, at the moment the descent began?"),
      choices=["1,935", "2,010", "2,085", "2,160"], correct="D",
      check="It falls 450 m in 6 minutes, so 75 m per minute; 1,860 + 4(75) = 2,160."),

 dict(n="E1-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A cheesemaker calculates the yield of one vat as \\(Y=\\frac{3m-2w}{5}\\) kilograms, "
            "where m is the mass of milk poured into the vat and w is the mass of whey drawn off, "
            "both in kilograms. Which expression gives m in terms of Y and w?"),
      choices=["\\(\\frac{5Y+2w}{3}\\)", "\\(\\frac{5Y-2w}{3}\\)",
               "\\(\\frac{Y+2w}{15}\\)", "\\(\\frac{5Y+2w}{15}\\)"], correct="A",
      check="Multiply by 5, add 2w, divide by 3."),

 dict(n="E1-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A workshop that finishes wind-turbine blades models its profit for a day, in "
            "dollars, as \\(P(b)=-25b^{2}+900b-3{,}200\\) , where b is the number of blades "
            "finished that day. For how many blades finished does this model give the greatest "
            "profit for a day?"),
      choices=["16", "18", "20", "36"], correct="B",
      check="The vertex is at b = 900/50 = 18."),

 dict(n="E1-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A book conservator measures a rectangular sheet of vellum that is 7 centimetres "
            "taller than it is wide and has an area of 330 square centimetres. What is the "
            "perimeter of the sheet, in centimetres?"),
      choices=["66", "74", "78", "82"], correct="B",
      check="w(w+7) = 330 gives w = 15 and height 22, so the perimeter is 74."),

 dict(n="E1-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A crystallographer needs the lattice factor \\(\\frac{(4a^{3}b)^{2}}{8ab^{4}}\\) "
            "rewritten so that no exponent is negative, where \\(a>0\\) and \\(b>0\\) . Which "
            "expression is equivalent to that lattice factor?"),
      choices=["\\(\\frac{2a^{5}}{b^{2}}\\)", "\\(\\frac{2a^{6}}{b^{2}}\\)",
               "\\(\\frac{a^{5}}{2b^{2}}\\)", "\\(2a^{5}b^{2}\\)"], correct="A",
      check="The numerator is 16a^6 b^2, and dividing by 8ab^4 leaves 2a^5 over b^2."),

 dict(n="E1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A museum technician applies a fresh 250-gram coat of protective wax to a bronze "
            "statue. Each month the statue loses 3% of the wax that was present at the start of "
            "that month. To the nearest gram, how much wax is present 8 months after the coat is "
            "applied?"),
      choices=["184", "190", "194", "196"], correct="D",
      check="250(0.97)^8 = 195.93, which rounds to 196."),

 dict(n="E1-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A marmalade maker fixes the mass of peel, p kilograms, and the mass of sugar, s "
            "kilograms, in one batch by the two conditions \\(p+s=30\\) and \\(ps=200\\) . The "
            "batch contains more sugar than peel. How many kilograms of sugar does the batch "
            "contain?"),
      choices=["10", "15", "20", "25"], correct="C",
      check="The two masses are the roots of t^2 - 30t + 200 = 0, namely 10 and 20."),

 dict(n="E1-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A weaver's loom takes 3 metres of warp thread for every 8 centimetres of finished "
            "cloth it produces. At that rate, how many metres of warp thread does the loom take "
            "to produce 1.4 metres of finished cloth?"),
      choices=["37.5", "42", "48", "52.5"], correct="D",
      check="140/8 = 17.5 lengths of 3 metres, which is 52.5 metres."),

 dict(n="E1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A peat cutter lifts 0.9 cubic metres of peat each hour, and the peat has a density "
            "of 400 kilograms per cubic metre. How many kilograms of peat does the cutter lift "
            "in a 7-hour working day?"),
      choices=["2,160", "2,520", "2,800", "3,150"], correct="B",
      check="0.9(400)(7) = 2,520."),

 dict(n="E1-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table records the mass of tea leaves, in kilograms, picked by each of four "
            "workers on one morning."
            + table(["Worker", "Mass picked (kg)"],
                    [["Anwar", "18.5"], ["Bilqis", "24.0"],
                     ["Chandra", "15.5"], ["Devi", "21.0"]])
            + "Each worker is paid $1.80 for every kilogram picked. How many more dollars was "
              "the highest-paid worker paid that morning than the lowest-paid worker?"),
      choices=["$12.60", "$14.40", "$15.30", "$16.20"], correct="C",
      check="24.0 - 15.5 = 8.5 kg, and 8.5(1.80) = 15.30."),

 dict(n="E1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("An apprentice cuts dovetail joints, and the mean length of the first 9 joints she "
            "cuts is 62 millimetres. After she cuts a tenth joint, the mean length of all 10 "
            "joints is 63 millimetres. What is the length, in millimetres, of the tenth joint?"),
      choices=["64", "66", "70", "72"], correct="D",
      check="10(63) - 9(62) = 630 - 558 = 72."),

 dict(n="E1-17", domain="GT", skill="GT-LA", type="MC",
      stem=("Two parallel guide rails on a drawing board are crossed by a single straight brace. "
            "The brace meets the first rail at an angle of \\((4x+16)\\)&deg; , and the angle in "
            "the corresponding position where the brace meets the second rail measures "
            "\\((6x-14)\\)&deg; . What is the measure, in degrees, of each of these two angles?"),
      choices=["15", "46", "62", "76"], correct="D",
      check="Corresponding angles are equal, so 4x + 16 = 6x - 14 gives x = 15 and the angle 76."),

 dict(n="E1-18", domain="GT", skill="GT-TR", type="MC",
      stem=("A surveyor stands on level ground 45 metres from the base of a grain elevator and "
            "measures the angle of elevation to the top of the elevator as 52&deg; . Which "
            "expression gives the height of the grain elevator, in metres?"),
      choices=["\\(45\\tan 52^{\\circ}\\)", "\\(45\\sin 52^{\\circ}\\)",
               "\\(\\frac{45}{\\tan 52^{\\circ}}\\)", "\\(45\\cos 52^{\\circ}\\)"], correct="A",
      check="The height is the side opposite the angle over the adjacent 45 metres, so 45 tan 52."),

 dict(n="E1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A rainwater cistern is a cylinder of radius 1.5 metres and depth 2.4 metres, and it "
            "is filled to 80% of its capacity. The volume of water in the cistern can be written "
            "as \\(V\\pi\\) cubic metres. What is the value of V?"),
      choices=["3.24", "4.32", "5.4", "10.8"], correct="B",
      check="1.5^2 (2.4) = 5.4 and 0.8(5.4) = 4.32."),

 dict(n="E1-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A spice cooperative buys 3 kilograms of cardamom and 5 kilograms of cloves for $196. "
            "At the same prices, 5 kilograms of cardamom and 2 kilograms of cloves cost $181. "
            "What is the price, in dollars, of one kilogram of cardamom?"),
      answers=["27"],
      check="3c + 5v = 196 and 5c + 2v = 181 give c = 27 and v = 23."),

 dict(n="E1-21", domain="ADV", skill="ADV-NF", type="FR",
      stem=("A tram's stopping distance, in metres, is modelled by "
            "\\(d(v)=\\frac{v^{2}}{20}+\\frac{v}{2}\\) , where v is the tram's speed in "
            "kilometres per hour. What stopping distance, in metres, does this model give for a "
            "tram travelling at 30 kilometres per hour?"),
      answers=["60"],
      check="900/20 + 30/2 = 45 + 15 = 60."),

 dict(n="E1-22", domain="GT", skill="GT-LA", type="FR",
      stem=("A rambler holds a 30-centimetre ruler upright at arm's length, 60 centimetres from "
            "her eye, and from that position the ruler exactly covers a cliff face that is 400 "
            "metres away. How many metres tall is the cliff face?"),
      answers=["200"],
      check="Similar triangles give 30/60 = H/400, so H = 200."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="E2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A campsite warden charges $14 for each tent pitched for one night, and one night she "
            "took $322 in pitch charges. How many tents were pitched that night?"),
      choices=["23", "25", "28", "32"], correct="A",
      check="322/14 = 23."),

 dict(n="E2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cellist practises for the same number of minutes on each of 7 days and practises "
            "546 minutes over those 7 days. For how many minutes does she practise each day?"),
      choices=["76", "78", "82", "91"], correct="B",
      check="546/7 = 78."),

 dict(n="E2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A kayak outfitter's total charge, in dollars, for a rental lasting h hours is given "
            "by \\(C=18+7h\\) . What is the total charge, in dollars, for a rental lasting 4 "
            "hours?"),
      choices=["25", "46", "72", "100"], correct="B",
      check="18 + 7(4) = 46."),

 dict(n="E2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A snow plough clears a mountain road, and \\(L(t)=45-9t\\) gives the number of "
            "kilometres of that road still uncleared t hours after the plough sets out. How many "
            "kilometres are still uncleared 3 hours after the plough sets out?"),
      choices=["18", "27", "36", "45"], correct="A",
      check="45 - 9(3) = 18."),

 dict(n="E2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A safety notice at a via ferrata bridge states that the number of climbers n on the "
            "bridge must be fewer than 9 at any moment. Which inequality gives all the possible "
            "values of n?"),
      choices=["\\(n>9\\)", "\\(n\\ge 9\\)", "\\(n<9\\)", "\\(n\\le 9\\)"], correct="C",
      check="Fewer than 9 means strictly less than 9."),

 dict(n="E2E-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A ropemaker's twisting frame produces \\(P(h)=24h\\) metres of rope after running "
            "for h hours. For how many hours must the frame run to produce 180 metres of rope?"),
      choices=["6", "7.5", "9", "156"], correct="B",
      check="180/24 = 7.5."),

 dict(n="E2E-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A stagehand counts the lamps on a lighting bar as \\(4(3n-7)+5n\\) , where n is the "
            "number of sections in the bar. Which expression is equivalent to the number of "
            "lamps?"),
      choices=["\\(8n-28\\)", "\\(12n-28\\)", "\\(17n-28\\)", "\\(17n-7\\)"], correct="C",
      check="12n - 28 + 5n = 17n - 28."),

 dict(n="E2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A greengrocer packs \\(x^{4}\\) plums into each layer of a crate and puts "
            "\\(x^{2}\\) layers in the crate, where \\(x>1\\) . Which expression gives the number "
            "of plums in the crate?"),
      choices=["\\(x^{2}\\)", "\\(x^{6}\\)", "\\(x^{8}\\)", "\\(2x^{6}\\)"], correct="B",
      check="x^4 times x^2 is x^6."),

 dict(n="E2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A lens grinder finds that polishing a mirror of diameter d centimetres takes "
            "\\(T(d)=d^{2}+5\\) minutes. How many minutes does polishing a mirror of diameter 7 "
            "centimetres take?"),
      choices=["12", "19", "54", "61"], correct="C",
      check="7^2 + 5 = 54."),

 dict(n="E2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A mat of duckweed doubles in area every week, and \\(A(w)=3(2)^{w}\\) gives its "
            "area in square metres w weeks after it is first measured. What is the area of the "
            "mat, in square metres, 4 weeks after it is first measured?"),
      choices=["24", "32", "48", "81"], correct="C",
      check="3(2^4) = 48."),

 dict(n="E2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A puzzle-box maker sets p pegs into each face of a box, and her design rule requires "
            "\\(p^{2}-9=40\\) , where p is positive. How many pegs are set into each face?"),
      choices=["5", "7", "24.5", "49"], correct="B",
      check="p^2 = 49 and p is positive, so p = 7."),

 dict(n="E2E-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A mosaicist lays a rectangular panel that is \\((x+4)\\) tiles long and "
            "\\((x-9)\\) tiles wide. Which expression gives the number of tiles in the panel?"),
      choices=["\\(x^{2}-13x-36\\)", "\\(x^{2}-5x-36\\)", "\\(x^{2}+5x-36\\)", "\\(x^{2}-36\\)"],
      correct="B",
      check="(x+4)(x-9) = x^2 - 5x - 36."),

 dict(n="E2E-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dyer's recipe uses 5 grams of madder root for every 2 litres of water. At that "
            "rate, how many grams of madder root are needed for 14 litres of water?"),
      choices=["17.5", "28", "35", "70"], correct="C",
      check="14/2 = 7 portions of 5 grams, which is 35 grams."),

 dict(n="E2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Of the 420 paper lanterns hung along a canal for a festival, 35% are red. How many "
            "of those lanterns are red?"),
      choices=["120", "126", "140", "147"], correct="D",
      check="0.35(420) = 147."),

 dict(n="E2E-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table lists the number of puffin nesting pairs recorded on three offshore sea "
            "stacks in one season."
            + table(["Sea stack", "Nesting pairs"],
                    [["Craigan", "128"], ["Sgeir Mor", "155"], ["Bo Rua", "96"]])
            + "Altogether, how many nesting pairs were recorded on the three sea stacks that "
              "season?"),
      choices=["251", "283", "341", "379"], correct="D",
      check="128 + 155 + 96 = 379."),

 dict(n="E2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The numbers of eggs counted in six wrens' nests are 4, 5, 5, 6, 7 and 9. What is the "
            "mean number of eggs per nest?"),
      choices=["4.5", "5", "5.5", "6"], correct="D",
      check="The six counts total 36, and 36/6 = 6."),

 dict(n="E2E-17", domain="GT", skill="GT-LA", type="MC",
      stem=("The gable end of a garden shed is a right triangle, and one of its acute angles "
            "measures 37&deg; . What is the measure, in degrees, of the other acute angle?"),
      choices=["43", "53", "63", "143"], correct="B",
      check="The two acute angles of a right triangle sum to 90, so 90 - 37 = 53."),

 dict(n="E2E-18", domain="GT", skill="GT-AV", type="MC",
      stem=("The floor of a hexagonal gazebo is laid as 6 identical triangular sections, and each "
            "section covers 2.5 square metres. What is the total area of the gazebo floor, in "
            "square metres?"),
      choices=["7.5", "12.5", "15", "18"], correct="C",
      check="6(2.5) = 15."),

 dict(n="E2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A circular lily pond has a radius of 6 metres. The area of the pond, in square "
            "metres, can be written as \\(k\\pi\\) . What is the value of k?"),
      choices=["6", "12", "24", "36"], correct="D",
      check="The area is pi times 6^2, so k = 36."),

 dict(n="E2E-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A chandler pours 4.5 litres of melted wax equally into 6 moulds. How many litres of "
            "wax go into each mould?"),
      answers=["0.75", ".75", "3/4"],
      check="4.5/6 = 0.75."),

 dict(n="E2E-21", domain="ADV", skill="ADV-NF", type="FR",
      stem=("A model rocket's altitude, in metres, is given by \\(a(t)=5t^{2}\\) , where t is the "
            "number of seconds since it was launched. What is the rocket's altitude, in metres, "
            "6 seconds after it is launched?"),
      answers=["180"],
      check="5(6^2) = 180."),

 dict(n="E2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("In right triangle \\(JKL\\) , angle \\(K\\) is the right angle, \\(JK=8\\) and "
            "\\(KL=15\\) . What is the value of \\(\\tan J\\) ?"),
      answers=["15/8", "1.875"],
      check="The tangent of J is the side opposite over the side adjacent, 15/8."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="E2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cartographer draws two straight contour lines in the xy-plane. One is the graph of "
            "\\(y=\\frac{3}{5}x-4\\) and the other is the graph of \\(3x-my=25\\) , where m is a "
            "constant. The two contour lines never meet. What is the value of m?"),
      choices=["-5", "3", "5", "9"], correct="C",
      check="The lines are parallel when 3/m = 3/5, so m = 5, and then they are distinct."),

 dict(n="E2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A cable railway charges \\(F(d)=a+bd\\) francs for a journey of d kilometres, where "
            "a and b are constants. A 6-kilometre journey costs 27 francs and a 14-kilometre "
            "journey costs 51 francs. What is the value of \\(a+b\\) ?"),
      choices=["9", "12", "15", "21"], correct="B",
      check="b = 24/8 = 3 and a = 27 - 18 = 9, so a + b = 12."),

 dict(n="E2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A tour operator's minibus has 17 seats and runs only when every seat is filled. An "
            "adult seat costs $32 and a child seat costs $19, and the operator must take at least "
            "$460 from the journey. What is the greatest number of children who can travel on "
            "that journey?"),
      choices=["5", "6", "7", "8"], correct="B",
      check="32(17-c) + 19c >= 460 gives 13c <= 84, so c <= 6.46 and c = 6."),

 dict(n="E2H-04", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Two sluice gates opened together drain a mill pond in 6 hours. The larger gate on "
            "its own would drain the pond in 5 hours less than the smaller gate on its own would. "
            "How many hours would the smaller gate on its own take to drain the pond?"),
      choices=["10", "12", "15", "18"], correct="C",
      check="1/s + 1/(s-5) = 1/6 gives s^2 - 17s + 30 = 0, whose root greater than 5 is 15."),

 dict(n="E2H-05", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A dye works puts every skein through two treatments modelled by \\(p(x)=2x-5\\) and "
            "\\(q(x)=x^{2}+1\\) , applied in that order so that the value p produces is fed into "
            "q. Which expression is equivalent to \\(q(p(x))\\) ?"),
      choices=["\\(4x^{2}+26\\)", "\\(2x^{2}-3\\)", "\\(4x^{2}-20x+24\\)",
               "\\(4x^{2}-20x+26\\)"], correct="D",
      check="(2x-5)^2 + 1 = 4x^2 - 20x + 26."),

 dict(n="E2H-06", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A wind-tunnel scaling law is quoted as \\(\\left(\\frac{16x^{8}}{y^{-4}}\\right)"
            "^{\\frac{3}{4}}\\) , where \\(x>0\\) and \\(y>0\\) , and an engineer must rewrite it "
            "so that no exponent is a fraction. Which expression is equivalent to that scaling "
            "law?"),
      choices=["\\(8x^{6}y^{3}\\)", "\\(12x^{6}y^{3}\\)", "\\(8x^{11}y^{3}\\)",
               "\\(64x^{6}y^{3}\\)"], correct="A",
      check="The bracket is 16x^8 y^4, and raising it to the 3/4 power gives 8x^6 y^3."),

 dict(n="E2H-07", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A bridge designer models the underside of an arch by \\(f(x)=2x^{2}+bx+18\\) , where "
            "b is a positive constant. The graph of \\(y=f(x)\\) meets the x-axis at exactly one "
            "point. What is the value of b?"),
      choices=["6", "9", "12", "18"], correct="C",
      check="The discriminant b^2 - 144 must be 0 and b is positive, so b = 12."),

 dict(n="E2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A brewer's blending ratio for a cask is \\(\\frac{x^{2}-9}{x^{2}+x-12}\\) , where "
            "\\(x>4\\) . Which expression is equivalent to that blending ratio?"),
      choices=["\\(\\frac{x-3}{x-4}\\)", "\\(\\frac{3}{x+4}\\)", "\\(\\frac{x+3}{x+4}\\)",
               "\\(\\frac{x+3}{x-4}\\)"], correct="C",
      check="Both parts share the factor x - 3, leaving (x+3)/(x+4)."),

 dict(n="E2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The cross-section of a skate ramp is modelled by \\(y=a(x-4)^{2}-12\\) , where a is "
            "a positive constant, and the modelled curve passes through the point \\((10,15)\\) . "
            "What is the value of a?"),
      choices=["\\(\\frac{1}{2}\\)", "\\(\\frac{3}{4}\\)", "\\(\\frac{4}{3}\\)", "3"],
      correct="B",
      check="36a - 12 = 15 gives 36a = 27, so a = 3/4."),

 dict(n="E2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the xy-plane, the parabola \\(y=x^{2}-4x+7\\) and the line \\(y=2x+c\\) , where c "
            "is a constant, cross at exactly two points. Which of the following could be the "
            "value of c?"),
      choices=["-5", "-3", "-2", "1"], correct="D",
      check="x^2-6x+(7-c)=0 needs 36-4(7-c) > 0, so c > -2, and only 1 qualifies."),

 dict(n="E2H-11", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A chemist records the contents of a reaction vessel twice, as \\(4x-3y=7\\) and as "
            "\\(8x+ay=1\\) , where a is a constant. For exactly one value of a there is no pair "
            "\\((x,y)\\) satisfying both records. What is that value of a?"),
      choices=["-6", "-3", "3", "6"], correct="A",
      check="The two left sides are proportional when a/(-3) = 8/4, so a = -6."),

 dict(n="E2H-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A researcher recruited 300 volunteers and randomly assigned each of them either to a "
            "new stretching routine or to their usual routine. After twelve weeks the volunteers "
            "on the new routine had significantly greater gains in flexibility than the others. "
            "Which conclusion is best supported by this study?"),
      choices=["Flexibility gains and stretching routines are unrelated among the volunteers in "
               "the study.",
               "Volunteers who take up stretching routines on their own are more flexible than "
               "volunteers who do not.",
               "The new stretching routine will produce greater gains in flexibility for every "
               "adult in the country.",
               "The new stretching routine caused greater gains in flexibility for the volunteers "
               "in the study."], correct="D",
      check="Random assignment supports a causal claim, but only for the volunteers studied."),

 dict(n="E2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A vineyard measures the sugar content of eleven grape samples and records, in "
            "degrees Brix, the values 19, 20, 20, 21, 21, 22, 22, 22, 23, 24 and 41. Which "
            "statement about these eleven values is true?"),
      choices=["The mean is less than the median.",
               "The mean is equal to the median.",
               "The mean is greater than the median.",
               "The mean is greater than every one of the recorded values."], correct="C",
      check="The mean is 255/11 = 23.18 and the median is 22, so the mean is larger."),

 dict(n="E2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A tannery mixes a brine that is 12% salt by mass with a brine that is 30% salt by "
            "mass to obtain 45 litres of brine that is 18% salt by mass. How many litres of the "
            "30% brine does the tannery use?"),
      choices=["12", "15", "18", "30"], correct="B",
      check="0.12(45-y) + 0.30y = 0.18(45) gives 0.18y = 2.7, so y = 15."),

 dict(n="E2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table summarises an inspection of 180 wetsuits carried out at two workshops."
            + table(["Workshop", "Passed", "Failed"],
                    [["Alder", "62", "13"], ["Birch", "84", "21"]])
            + "One of the wetsuits that failed the inspection is selected at random. What is the "
              "probability that the selected wetsuit was inspected at the Birch workshop?"),
      choices=["\\(\\frac{21}{180}\\)", "\\(\\frac{34}{180}\\)", "\\(\\frac{21}{105}\\)",
               "\\(\\frac{21}{34}\\)"], correct="D",
      check="34 wetsuits failed and 21 of those were at Birch."),

 dict(n="E2H-16", domain="GT", skill="GT-LA", type="MC",
      stem=("A surveyor sights across a river and obtains two similar triangles \\(PQR\\) and "
            "\\(PST\\) , where S lies on \\(\\overline{PQ}\\) , T lies on \\(\\overline{PR}\\) "
            "and \\(\\overline{ST}\\) is parallel to \\(\\overline{QR}\\) . The measurements are "
            "\\(PS=12\\) metres, \\(SQ=18\\) metres and \\(QR=45\\) metres. What is the length of "
            "\\(\\overline{ST}\\) , in metres?"),
      choices=["15", "18", "20", "27"], correct="B",
      check="PS/PQ = 12/30 = 2/5, so ST = (2/5)(45) = 18."),

 dict(n="E2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A solid brass sphere of radius 6 centimetres is melted down and cast, with no loss "
            "of brass, into solid cylindrical rods of radius 2 centimetres and length 9 "
            "centimetres. How many complete rods can be cast from the sphere?"),
      choices=["6", "8", "9", "12"], correct="B",
      check="The sphere is 288 pi and each rod is 36 pi, so 8 rods."),

 dict(n="E2H-18", domain="GT", skill="GT-TR", type="MC",
      stem=("A ship's radar plot forms a right triangle \\(XYZ\\) with the right angle at "
            "\\(Y\\) . The leg \\(XY\\) measures 9 nautical miles and the leg \\(YZ\\) measures "
            "40 nautical miles. What is the value of \\(\\cos X\\) ?"),
      choices=["\\(\\frac{41}{9}\\)", "\\(\\frac{9}{40}\\)", "\\(\\frac{40}{41}\\)",
               "\\(\\frac{9}{41}\\)"], correct="D",
      check="The hypotenuse XZ is 41, and cos X = XY/XZ = 9/41."),

 dict(n="E2H-19", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A community kitchen will cook exactly 20 kilograms of pulses, made up of lentils and "
            "beans. Each kilogram of lentils yields 6 portions and each kilogram of beans yields "
            "4 portions, and the kitchen must serve at least 90 portions. What is the least "
            "number of kilograms of lentils the kitchen can use?"),
      choices=["5", "6", "8", "10"], correct="A",
      check="6L + 4(20-L) >= 90 gives 2L >= 10, so L >= 5."),

 dict(n="E2H-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("In a three-stage relay the first runner's leg is 3 times as long as the second "
            "runner's leg, and the third runner's leg is 400 metres shorter than the first "
            "runner's leg. The three legs together measure 3,800 metres. How many metres long is "
            "the second runner's leg?"),
      answers=["600"],
      check="3b + b + (3b - 400) = 3,800 gives 7b = 4,200, so b = 600."),

 dict(n="E2H-21", domain="ALG", skill="ALG-LF", type="FR",
      stem=("A sailmaker's cutting line on a plan passes through the points \\((-2,9)\\) and "
            "\\((6,-7)\\) in the xy-plane. What is the x-coordinate of the point where this "
            "cutting line crosses the x-axis?"),
      answers=["2.5", "5/2"],
      check="The slope is -2, so y = 5 - 2x and y = 0 at x = 2.5."),

 dict(n="E2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A water trough is a prism 2 metres long whose cross-section is a trapezium with "
            "parallel sides of 40 centimetres and 60 centimetres and a perpendicular height of "
            "30 centimetres. Given that 1 litre is 1,000 cubic centimetres, how many litres of "
            "water does the full trough hold?"),
      answers=["300"],
      check="The cross-section is 1,500 sq cm, and 1,500(200) = 300,000 cubic cm = 300 litres."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
