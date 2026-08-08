#!/usr/bin/env python3
"""
Original Math content for Test 10 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Two-to-three step setups: a rearrangement before
                the arithmetic, or a constant to solve for first. Harder than a
                Module 2 (Easy) item, deliberately below Module 2 (Hard).
  MODULE_2_EASY genuinely easy — one step, the lower branch of the split.
  MODULE_2_HARD hard. Parameters instead of numbers, structural answers,
                composed functions, a system conditioned on a constant, and
                geometry that needs two relationships at once.

Every setting is deliberately concrete (beekeeping, ferries, kilns, foundries,
zip lines) so that no stem collides with the bare-skill algebra already banked
in production. House style follows Test 1/2 (see CLAUDE.md). LaTeX typed by
hand — no bulk conversion step was used anywhere in this file.
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
 dict(n="C1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A beekeeper bottles a harvest in two jar sizes: a small jar holds 250 grams of "
            "honey and a large jar holds 450 grams. She fills 4 more small jars than large jars "
            "and uses exactly 6,600 grams of honey. How many large jars did she fill?"),
      choices=["6", "8", "12", "15"], correct="B",
      check="250(L+4) + 450L = 6,600 gives 700L = 5,600, so L = 8."),

 dict(n="C1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A coastal ferry charges one fare for a car and a different fare for a bicycle. A "
            "crossing carrying 3 cars and 5 bicycles collected $97, and a crossing carrying 2 "
            "cars and 9 bicycles collected $93. What is the fare, in dollars, for one car?"),
      choices=["24", "26", "29", "32"], correct="A",
      check="3c+5b=97 and 2c+9b=93 give c = 24 and b = 5."),

 dict(n="C1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A pillar candle is 30 centimetres tall when it is lit and burns down at a constant "
            "rate. Forty-five minutes after it is lit the candle is 26.4 centimetres tall. How "
            "many minutes after it is lit will the candle be 12 centimetres tall?"),
      choices=["180", "200", "225", "250"], correct="C",
      check="It burns 3.6 cm in 45 min, so 0.08 cm per minute; 18 cm takes 225 minutes."),

 dict(n="C1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A hoist in a granary may lift a total mass of no more than 900 kilograms. The "
            "operator, whose mass is 78 kilograms, rides up with sacks of grain that each have a "
            "mass of 34 kilograms. What is the greatest number of sacks that can ride with the "
            "operator?"),
      choices=["24", "25", "26", "27"], correct="A",
      check="34s <= 822 gives s <= 24.17, so 24 sacks."),

 dict(n="C1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A climbing gym sets its monthly charge, in dollars, by the rule \\(C=29+k(v-3)\\), "
            "where v is the number of visits in the month and k is a constant. A member who "
            "visited 11 times was charged $69. How many dollars is a member charged for 20 "
            "visits in a month?"),
      choices=["99", "104", "109", "114"], correct="D",
      check="29 + 8k = 69 gives k = 5, so C = 29 + 5(17) = 114."),

 dict(n="C1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A harbour gauge records the water level falling at a constant rate on an outgoing "
            "tide. At 2:00 p.m. the level is 4.6 metres and at 5:00 p.m. it is 2.8 metres. If the "
            "level keeps falling at the same rate, how many hours after 5:00 p.m. will it reach "
            "1.6 metres?"),
      choices=["1", "1.5", "2", "3"], correct="C",
      check="The level falls 0.6 m per hour; 2.8 - 1.6 = 1.2 m takes 2 hours."),

 dict(n="C1-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A potter's kiln heats at a constant rate. Its temperature is 18&deg;C when firing "
            "begins and 453&deg;C after 3 hours. The glaze on the pots matures at 1,033&deg;C. "
            "How many hours after firing begins does the kiln reach that temperature?"),
      choices=["5", "7", "8", "10"], correct="B",
      check="Rate = (453-18)/3 = 145 per hour; (1033-18)/145 = 7."),

 dict(n="C1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A machinist writes the cost of finishing a batch of parts, in dollars, as "
            "\\(\\frac{6x^{2}+13x-5}{3x-1}\\), where x is the number of parts and "
            "\\(x>1\\). Which expression is equivalent to the machinist's cost?"),
      choices=["\\(2x-5\\)", "\\(3x+5\\)", "\\(2x+1\\)", "\\(2x+5\\)"], correct="D",
      check="6x^2+13x-5 factors as (3x-1)(2x+5), so the quotient is 2x+5."),

 dict(n="C1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A stunt kite is released from a cliff, and its height above the beach, in metres, "
            "t seconds after release is modelled by \\(h(t)=-0.5t^{2}+12t+3\\). What is the "
            "greatest height above the beach, in metres, that this model predicts?"),
      choices=["51", "69", "75", "147"], correct="C",
      check="Vertex at t = 12; h(12) = -72 + 144 + 3 = 75."),

 dict(n="C1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A photographer stacks identical grey filters in front of a lens. Each filter passes "
            "\\(\\frac{1}{3}\\) of the light that reaches it, so a stack of x filters passes "
            "\\(\\left(\\frac{1}{3}\\right)^{x}\\) of the light reaching the first filter. One "
            "stack passes \\(\\frac{1}{243}\\) of that light. How many filters are in the stack?"),
      choices=["5", "6", "81", "243"], correct="A",
      check="243 = 3^5, so x = 5."),

 dict(n="C1-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A drone crosses a canyon along a path modelled by \\(y=x^{2}-14x+40\\), where x is "
            "the horizontal distance in metres from the canyon's western rim and y is the height "
            "in metres relative to the rims. The drone is level with the rims at two horizontal "
            "positions. How many metres apart are those two positions?"),
      choices=["4", "6", "10", "14"], correct="B",
      check="x^2-14x+40 = 0 has roots 4 and 10, which are 6 apart."),

 dict(n="C1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A packaging engineer writes the surface area of a closed carton that has a square "
            "base of side s centimetres and a height of h centimetres as \\(A=2s^{2}+4sh\\) "
            "square centimetres. Which expression gives h in terms of A and s?"),
      choices=["\\(\\frac{A-2s^{2}}{4s}\\)", "\\(\\frac{A+2s^{2}}{4s}\\)",
               "\\(\\frac{A-2s^{2}}{4}\\)", "\\(\\frac{A-s^{2}}{2s}\\)"], correct="A",
      check="Subtract 2s^2 and divide by 4s."),

 dict(n="C1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A jeweller models the mass of a hollow silver bead of outer radius x millimetres as "
            "\\(m(x)=\\frac{x^{3}}{4}-2\\) grams. A bead made to this design has a mass of 14 "
            "grams. What is its outer radius, in millimetres?"),
      choices=["4", "6", "8", "64"], correct="A",
      check="x^3/4 = 16 gives x^3 = 64 and x = 4."),

 dict(n="C1-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A wildlife trust holds $2,500 in a fund that grows by 4% of its value each year, "
            "with no money added or withdrawn. To the nearest dollar, how much will the fund "
            "hold 3 years from now?"),
      choices=["$2,750", "$2,800", "$2,812", "$2,900"], correct="C",
      check="2500(1.04)^3 = 2812.16, which rounds to 2,812."),

 dict(n="C1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A newspaper press prints 1,250 sheets every 8 minutes. Working at that constant "
            "rate, how many minutes does the press take to print 21,875 sheets?"),
      choices=["112", "140", "150", "175"], correct="B",
      check="21,875/1,250 = 17.5 batches, and 17.5(8) = 140 minutes."),

 dict(n="C1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A rucksack is marked down 20% in a sale, and a loyalty card then takes a further "
            "15% off the sale price. A shopper using the card pays $102. What was the price of "
            "the rucksack, in dollars, before the sale?"),
      choices=["$127.50", "$135", "$142.50", "$150"], correct="D",
      check="(0.80)(0.85) = 0.68 and 102/0.68 = 150."),

 dict(n="C1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the mass of paper, in kilograms, that a school collected for "
            "recycling in each of four weeks."
            + table(["Week", "Mass collected (kg)"],
                    [["1", "42"], ["2", "58"], ["3", "61"], ["4", "39"]])
            + "The school had set a four-week goal of 250 kilograms. By what percent did the "
              "collected mass fall short of that goal?"),
      choices=["10%", "15%", "18%", "20%"], correct="D",
      check="Total 200 kg; the shortfall of 50 kg is 50/250 = 20% of the goal."),

 dict(n="C1-18", domain="GT", skill="GT-LA", type="MC",
      stem=("The three angles of a triangular window pane measure \\((2x+10)\\)&deg;, "
            "\\((3x-5)\\)&deg; and \\((x+7)\\)&deg;. What is the measure, in degrees, of the "
            "largest of the three angles?"),
      choices=["35", "66", "79", "96"], correct="C",
      check="6x + 12 = 180 gives x = 28, so the angles are 66, 79 and 35."),

 dict(n="C1-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A guy wire runs in a straight line from the top of a radio mast to a ground anchor, "
            "making an angle of 30&deg; with the level ground. The anchor is 24 metres from the "
            "foot of the mast. What is the length of the wire, in metres?"),
      choices=["\\(12\\sqrt{3}\\)", "\\(16\\sqrt{3}\\)", "\\(24\\sqrt{3}\\)", "48"], correct="B",
      check="cos 30 = 24/L gives L = 48/sqrt(3) = 16 sqrt(3)."),

 dict(n="C1-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular swimming pool is 12 metres long and 5 metres wide, with a uniform "
            "depth of 1.6 metres. A pump delivers water at a constant 4 cubic metres per minute. "
            "How many minutes does the pump take to fill the empty pool to the brim?"),
      answers=["24"],
      check="Volume 12(5)(1.6) = 96 cubic metres; 96/4 = 24 minutes."),

 dict(n="C1-21", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("In a survey of 240 randomly selected households in a lakeside town, 54 households "
            "reported owning a canoe. There are 8,000 households in the town. Based on this "
            "survey, what is the best estimate of the number of households in the town that own "
            "a canoe?"),
      answers=["1800"],
      check="(54/240)(8,000) = 1,800."),

 dict(n="C1-22", domain="GT", skill="GT-LA", type="FR",
      stem=("A rectangular playing field measures 105 metres by 88 metres. A gravel path runs in "
            "a straight line from one corner of the field to the opposite corner. How many metres "
            "long is the path?"),
      answers=["137"],
      check="sqrt(105^2 + 88^2) = sqrt(18,769) = 137."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="C2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A walking-tour guide collected $8 from every visitor on one tour and took in $192 "
            "altogether. How many visitors were on the tour?"),
      choices=["12", "16", "24", "32"], correct="C",
      check="192/8 = 24."),

 dict(n="C2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A baker divides 3.6 kilograms of dough equally among 8 loaf tins. What mass of "
            "dough, in kilograms, goes into each tin?"),
      choices=["0.35", "0.45", "0.50", "4.5"], correct="B",
      check="3.6/8 = 0.45."),

 dict(n="C2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A bike-share scheme charges $2 to unlock a bicycle plus $0.25 for each minute of "
            "the ride. Which equation gives the total charge C, in dollars, for a ride lasting "
            "m minutes?"),
      choices=["\\(C=2+0.25m\\)", "\\(C=2.25m\\)", "\\(C=0.25+2m\\)", "\\(C=2(0.25m)\\)"],
      correct="A",
      check="A fixed $2 plus $0.25 per minute."),

 dict(n="C2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A tap is opened on a full water butt, and \\(v(t)=54-6t\\) gives the volume of "
            "water remaining, in litres, t minutes after the tap is opened. How many litres "
            "remain 5 minutes after the tap is opened?"),
      choices=["24", "30", "48", "54"], correct="A",
      check="54 - 6(5) = 24."),

 dict(n="C2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A goods lift may carry a total mass of no more than 600 kilograms. Which inequality "
            "gives all the possible values of the total mass m, in kilograms, that the lift may "
            "carry?"),
      choices=["\\(m<600\\)", "\\(m>600\\)", "\\(m\\ge 600\\)", "\\(m\\le 600\\)"], correct="D",
      check="No more than 600 means at most 600."),

 dict(n="C2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A rectangular vegetable bed has a perimeter of 26 metres and a length of 8 metres. "
            "What is its width, in metres?"),
      choices=["5", "9", "13", "18"], correct="A",
      check="2(8 + w) = 26 gives w = 5."),

 dict(n="C2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, a line passes through the point \\((0, 6)\\) and has a slope of "
            "\\(-2\\). What is the value of y on this line when \\(x=3\\)?"),
      choices=["-3", "0", "3", "12"], correct="B",
      check="y = 6 - 2(3) = 0."),

 dict(n="C2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A triangular pennant has a base of x centimetres and a height of 6 centimetres. "
            "Which expression gives the area of the pennant, in square centimetres?"),
      choices=["\\(x+6\\)", "\\(\\frac{x}{6}\\)", "\\(3x\\)", "\\(6x\\)"], correct="C",
      check="(1/2)(x)(6) = 3x."),

 dict(n="C2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A tiler's cost for one row of a border is \\(5(2p+3)\\) dollars, where p is the "
            "number of patterned tiles in the row. Which expression is equivalent to the cost of "
            "one row?"),
      choices=["\\(10p+3\\)", "\\(7p+8\\)", "\\(10p+8\\)", "\\(10p+15\\)"], correct="D",
      check="5(2p+3) = 10p + 15."),

 dict(n="C2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A crochet pattern spirals outward, and \\(S(r)=4r^{2}\\) gives the number of "
            "stitches worked after r complete rounds. How many stitches have been worked after "
            "5 rounds?"),
      choices=["20", "40", "100", "400"], correct="C",
      check="4(25) = 100."),

 dict(n="C2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A cube-shaped shipping crate has a volume of 64 cubic decimetres. What is the "
            "length, in decimetres, of one edge of the crate?"),
      choices=["4", "8", "16", "32"], correct="A",
      check="The cube root of 64 is 4."),

 dict(n="C2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=3x^{2}-x\\). What is the value of \\(f(2)\\)?"),
      choices=["4", "10", "11", "34"], correct="B",
      check="3(4) - 2 = 10."),

 dict(n="C2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("An archivist splits \\(x^{8}\\) scanned pages into \\(x^{3}\\) equally sized "
            "batches, where \\(x>1\\). Which expression gives the number of pages in each batch?"),
      choices=["\\(x^{5}\\)", "\\(x^{11}\\)", "\\(x^{24}\\)", "\\(5x\\)"], correct="A",
      check="x^8 divided by x^3 is x^5."),

 dict(n="C2E-14", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A single yeast cell divides so that the number of cells present after n rounds of "
            "division is \\(h(n)=2^{n}\\). How many cells are present after 6 rounds?"),
      choices=["12", "32", "64", "128"], correct="C",
      check="2^6 = 64."),

 dict(n="C2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A joiner uses 3 litres of varnish to cover 12 square metres of decking. At that "
            "rate, how many litres of varnish are needed to cover 40 square metres of decking?"),
      choices=["4", "6", "8", "10"], correct="D",
      check="(3/12)(40) = 10."),

 dict(n="C2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A cinema screen has 250 seats, and 40% of them were occupied at one showing. How "
            "many seats were occupied at that showing?"),
      choices=["60", "100", "150", "210"], correct="B",
      check="0.40(250) = 100."),

 dict(n="C2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of books borrowed from a library branch in each of three "
            "months."
            + table(["Month", "Books borrowed"],
                    [["January", "340"], ["February", "295"], ["March", "412"]])
            + "How many books in total were borrowed from the branch over the three months?"),
      choices=["635", "707", "752", "1,047"], correct="D",
      check="340 + 295 + 412 = 1,047."),

 dict(n="C2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The masses, in grams, of five posted letters are 12, 15, 15, 20 and 28. What is the "
            "median of these masses, in grams?"),
      choices=["12", "15", "18", "20"], correct="B",
      check="The middle value of the ordered list is 15."),

 dict(n="C2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A straight fence post is driven into level ground, and the two angles that the post "
            "makes with the ground on either side of it add to 180&deg;. One of these angles "
            "measures 118&deg;. What is the measure, in degrees, of the other angle?"),
      choices=["28", "32", "62", "118"], correct="C",
      check="180 - 118 = 62."),

 dict(n="C2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A triangular sports banner has a base of 18 centimetres and a height of 11 "
            "centimetres. What is the area of the banner, in square centimetres?"),
      answers=["99"],
      check="(1/2)(18)(11) = 99."),

 dict(n="C2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular shipping label measures 8 centimetres by 5 centimetres. What is the "
            "perimeter of the label, in centimetres?"),
      answers=["26"],
      check="2(8 + 5) = 26."),

 dict(n="C2E-22", domain="GT", skill="GT-TR", type="FR",
      stem=("A rectangular gate is 2.4 metres wide and 1.8 metres tall. A straight brace is "
            "fitted from one corner of the gate to the corner diagonally opposite. How many "
            "metres long is the brace?"),
      answers=["3"],
      check="sqrt(2.4^2 + 1.8^2) = sqrt(9) = 3."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="C2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A supplier prints the same delivery charge on an invoice in two ways: as "
            "\\(\\frac{2}{3}(6x-9)\\) dollars and as \\(4x+c\\) dollars, where x is the number "
            "of pallets ordered and c is a constant. The two expressions give the same charge "
            "for every value of x. What is the value of c?"),
      choices=["-6", "-3", "3", "6"], correct="A",
      check="(2/3)(6x-9) = 4x - 6, so c = -6."),

 dict(n="C2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("An accountant values a machine by the linear model \\(V(t)=c-vt\\), where t is the "
            "number of years since purchase and c and v are positive constants. The machine is "
            "valued at $19,400 after 3 years and at $12,200 after 7 years. What was the purchase "
            "price of the machine, in dollars?"),
      choices=["$21,800", "$23,000", "$24,800", "$26,600"], correct="C",
      check="v = 7,200/4 = 1,800 per year, so c = 19,400 + 3(1,800) = 24,800."),

 dict(n="C2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A charity stall sells wristbands for $4 each and mugs for $11 each, and it will "
            "sell exactly 200 items in total. The stall must take in at least $1,500. What is "
            "the least number of mugs the stall must sell?"),
      choices=["96", "100", "105", "112"], correct="B",
      check="4(200-g) + 11g >= 1,500 gives 7g >= 700, so g >= 100."),

 dict(n="C2H-04", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rectangular courtyard is 3 metres longer than it is wide and has an area of 154 "
            "square metres. A stone path 1 metre wide is laid all the way around the outside of "
            "the courtyard. What is the area of the path, in square metres?"),
      choices=["44", "48", "50", "54"], correct="D",
      check="w(w+3) = 154 gives w = 11 and length 14; the outer rectangle is 13 by 16, so the path is 208 - 154 = 54."),

 dict(n="C2H-05", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A laboratory's two conversion steps are modelled by \\(f(x)=x^{2}-4x\\) and "
            "\\(g(x)=x+3\\), applied in that order so that the reading g produces is fed into f. "
            "Which expression is equivalent to \\(f(g(x))\\)?"),
      choices=["\\(x^{2}+2x-3\\)", "\\(x^{2}-4x+3\\)", "\\(x^{2}+2x+9\\)", "\\(x^{2}-x-3\\)"],
      correct="A",
      check="(x+3)^2 - 4(x+3) = x^2 + 2x - 3."),

 dict(n="C2H-06", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("An engineer subtracts one flow rate from another and needs the result as a single "
            "quotient, for \\(x>1\\). Which expression is equivalent to "
            "\\(\\frac{3}{x+2}-\\frac{2}{x-1}\\)?"),
      choices=["\\(\\frac{x+1}{x^{2}+x-2}\\)", "\\(\\frac{x-7}{x^{2}+x-2}\\)",
               "\\(\\frac{1}{x+1}\\)", "\\(\\frac{5x-7}{x^{2}+x-2}\\)"], correct="B",
      check="[3(x-1) - 2(x+2)] / [(x+2)(x-1)] = (x-7)/(x^2+x-2)."),

 dict(n="C2H-07", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A runner covers 12 kilometres on Saturday at a constant speed of x kilometres per "
            "hour, then covers 12 kilometres on Sunday at a constant speed of \\(x+2\\) "
            "kilometres per hour. The two runs take 5 hours in total. What is the value of x?"),
      choices=["2", "3", "4", "6"], correct="C",
      check="12/x + 12/(x+2) = 5 gives 5x^2 - 14x - 24 = 0, whose positive root is 4."),

 dict(n="C2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A materials scientist reduces the quantity \\(\\sqrt[3]{27x^{12}}\\cdot x^{-2}\\), "
            "where \\(x>0\\). Which expression is equivalent to that quantity?"),
      choices=["\\(9x^{2}\\)", "\\(3x^{6}\\)", "\\(3x^{10}\\)", "\\(3x^{2}\\)"], correct="D",
      check="The cube root is 3x^4, and 3x^4 times x^-2 is 3x^2."),

 dict(n="C2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A sealed radiator loses the same fraction of its coolant every hour, so the volume "
            "remaining is \\(A(t)=A_{0}r^{t}\\) litres after t hours, where \\(A_{0}\\) and r "
            "are constants. After 2 hours 72 litres remain, and after 4 hours 40.5 litres "
            "remain. What is the value of \\(A_{0}\\)?"),
      choices=["96", "108", "128", "144"], correct="C",
      check="r^2 = 40.5/72 = 0.5625, so A0 = 72/0.5625 = 128."),

 dict(n="C2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the xy-plane, the line \\(y=2x+c\\) touches the curve \\(y=x^{2}-6x+11\\) at "
            "exactly one point, where c is a constant. What is the value of c?"),
      choices=["-5", "-3", "2", "5"], correct="A",
      check="x^2-8x+(11-c) = 0 has a zero discriminant when 64 = 4(11-c), so c = -5."),

 dict(n="C2H-11", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A workshop records the same batch of components in two ways, as \\(5x+2y=k\\) and "
            "as \\(15x+6y=48\\), where x and y are the numbers of two kinds of component and k "
            "is a constant. Every pair \\((x, y)\\) that satisfies one equation also satisfies "
            "the other. What is the value of k?"),
      choices=["12", "16", "24", "32"], correct="B",
      check="Dividing the second equation by 3 gives 5x + 2y = 16, so k = 16."),

 dict(n="C2H-12", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A polling organisation surveyed 500 randomly selected adults in a city and reported "
            "a mean daily commute time of 27.4 minutes, with an associated margin of error of "
            "1.8 minutes at the 95% confidence level. Which of the following is the most "
            "appropriate conclusion?"),
      choices=["It is plausible that the mean daily commute time of all adults in the city is "
               "between 25.6 and 29.2 minutes.",
               "Every adult in the city has a daily commute time between 25.6 and 29.2 minutes.",
               "Exactly 95% of the adults surveyed have a daily commute time between 25.6 and "
               "29.2 minutes.",
               "The mean daily commute time of all adults in the city must be exactly 27.4 "
               "minutes."], correct="A",
      check="A confidence interval bounds a plausible range for the population mean, not for individuals."),

 dict(n="C2H-13", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A quality inspector weighs two batches of bearings. Batch A contains 30 bearings "
            "with a mean mass of 52 grams, and batch B contains 20 bearings with a mean mass of "
            "62 grams. What is the mean mass, in grams, of all 50 bearings?"),
      choices=["55", "56", "57", "58"], correct="B",
      check="(30(52) + 20(62))/50 = 2,800/50 = 56."),

 dict(n="C2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A foundry casts an alloy in which the ratio of the mass of copper to the mass of "
            "zinc is 3 to 5. The foundry has 84 kilograms of copper and 120 kilograms of zinc "
            "and no other source of either metal. What is the greatest mass of the alloy, in "
            "kilograms, that the foundry can cast?"),
      choices=["192", "204", "224", "240"], correct="A",
      check="Copper allows 84(8/3) = 224 kg, zinc allows 120(8/5) = 192 kg; zinc is the limit."),

 dict(n="C2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives a bakery's revenue, in dollars, in each quarter of one year."
            + table(["Quarter", "Revenue ($)"],
                    [["First", "18,400"], ["Second", "21,160"],
                     ["Third", "19,800"], ["Fourth", "24,150"]])
            + "Suppose revenue rises from the fourth quarter to the next quarter by the same "
              "percent as it rose from the first quarter to the second. What would the next "
              "quarter's revenue be, in dollars?"),
      choices=["$26,565.00", "$27,772.50", "$28,175.00", "$29,000.00"], correct="B",
      check="The first-to-second rise is 2,760/18,400 = 15%, and 24,150(1.15) = 27,772.50."),

 dict(n="C2H-16", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle ABC, point D lies on side AB and point E lies on side AC so that "
            "segment DE is parallel to side BC. Given that \\(AD=6\\), \\(DB=9\\) and "
            "\\(DE=8\\), what is the length of side BC?"),
      choices=["12", "15", "20", "24"], correct="C",
      check="AD:AB = 6:15 = 2:5, so BC = 8(5/2) = 20."),

 dict(n="C2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A solid metal cylinder of radius 3 centimetres and height 16 centimetres is melted "
            "down and recast, with no loss of metal, as a solid cone of radius 6 centimetres. "
            "What is the height of the cone, in centimetres?"),
      choices=["6", "9", "12", "16"], correct="C",
      check="Cylinder volume 144 pi = (1/3) pi (36) h, so h = 12."),

 dict(n="C2H-18", domain="GT", skill="GT-TR", type="MC",
      stem=("In triangle ABC, angle C measures 90&deg; and \\(\\sin A=\\frac{20}{29}\\). What is "
            "the value of \\(\\cos B\\)?"),
      choices=["\\(\\frac{21}{29}\\)", "\\(\\frac{20}{21}\\)", "\\(\\frac{29}{20}\\)",
               "\\(\\frac{20}{29}\\)"], correct="D",
      check="Angles A and B are complementary, so cos B = sin A = 20/29."),

 dict(n="C2H-19", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Volunteers at a food bank pack exactly 100 boxes. A standard box takes 4 minutes to "
            "pack and a family box takes 7 minutes, and the volunteers have at most 560 minutes "
            "of packing time. What is the greatest number of family boxes the volunteers can "
            "pack?"),
      choices=["45", "48", "50", "53"], correct="D",
      check="4(100-f) + 7f <= 560 gives 3f <= 160, so f <= 53.3 and f = 53."),

 dict(n="C2H-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A courier's price for a delivery is a fixed booking fee plus a constant charge for "
            "each kilometre travelled. A 14-kilometre delivery costs $23.60 and a 22-kilometre "
            "delivery costs $32.40. What is the cost, in dollars, of a 35-kilometre delivery?"),
      answers=["46.70", "46.7"],
      check="Rate = 8.80/8 = 1.10 per km; fee = 23.60 - 15.40 = 8.20; 8.20 + 35(1.10) = 46.70."),

 dict(n="C2H-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("In a quiz league a team gains 5 points for each correct answer and loses 2 points "
            "for each incorrect answer. One team attempted all 40 questions and finished with "
            "137 points. How many questions did that team answer correctly?"),
      answers=["31"],
      check="5c - 2(40-c) = 137 gives 7c = 217, so c = 31."),

 dict(n="C2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A grain silo is built as a cylinder of radius 4 metres and height 10 metres, topped "
            "by a cone of radius 4 metres and height 3 metres. The total volume of the silo can "
            "be written as \\(V\\pi\\) cubic metres. What is the value of V?"),
      answers=["176"],
      check="160 pi from the cylinder plus 16 pi from the cone gives 176 pi."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
