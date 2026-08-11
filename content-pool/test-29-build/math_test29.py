#!/usr/bin/env python3
"""
Original Math content for Test 29 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item makes a rate, a constant, a
                unit price or an unknown be recovered first and only then used;
                two or three steps throughout.
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard: parameters instead of numbers, symbolic answer choices, a
                conditioned system, a composed function, an extraneous root, an
                integer count over a compound inequality, and geometry needing
                two relationships chained.

Test 29's thematic territory is the building trades that begin where the stone
leaves the ground: brickworks and kilns, tile making, plasterwork and lath,
stonemasonry and tracery, scaffolding and hoists. The territory is SPLIT across
the adaptive branches, because a student sees Module 1 and exactly one Module 2
module:

  Module 1          brickworks, brick kilns and firing, plasterwork and lath
  Module 2 (both)   tile making, stonemasonry and tracery, scaffolding and hoists

No setting keyword may cross that line; verify_math_test29.py pass 4 enforces
it with word-boundary-safe matching.

House style follows Test 1/2 (see CLAUDE.md): bare HTML stems, simple inline
maths left as plain text, real <table> markup for every data table, &deg; as an
entity, every \\( \\) typed by hand. No bulk conversion step was used anywhere
in this file. No images: every figure is either a real table or worded so that
it is fully determined without a picture.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ---------------------------------------------------------------- Module 1
# Brickworks, brick kilns and firing; plasterwork, lath and rendering.
MODULE_1 = [
 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A plasterer gauges a coarse mix from lime putty and sand in the proportion 1 barrow of "
            "putty to every 3 barrows of sand. A ceiling took 96 barrows of the gauged mix "
            "altogether. Lime putty costs $14 a barrow and sand costs $6 a barrow. What was the "
            "cost, in dollars, of the material for that ceiling?"),
      choices=["576", "768", "960", "1,152"], correct="B",
      check="One barrow in four is putty, so 24 barrows at 14 and 72 at 6 give 336 + 432 = 768."),

 dict(n="H1-02", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The number of green bricks still standing in a drying shed d days after the moulding "
            "gang stopped work is 15,400 - 620d. On which day does the shed first hold fewer than "
            "4,000 green bricks?"),
      choices=["17", "18", "19", "20"], correct="C",
      check="15,400 - 620d < 4,000 gives d > 18.38, so the first whole day is day 19."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("During the early part of a firing the temperature inside a brick kiln rises as a "
            "linear function of the number of hours since the fires were lit. The temperature was "
            "520&deg;C after 4 hours and 1,020&deg;C after 9 hours. After how many hours does the "
            "same model give a temperature of 1,220&deg;C?"),
      choices=["10", "11", "12", "13"], correct="B",
      check="500 degrees over 5 hours is 100 per hour, so the model is 100h + 120 and 1,220 gives h = 11."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A brickyard sends out bricks in carts and in lorries. Every cart carries 480 bricks and "
            "every lorry carries 2,100 bricks. On one day 25 vehicles left the yard and they carried "
            "23,340 bricks between them. How many of those vehicles were carts?"),
      choices=["7", "9", "14", "18"], correct="D",
      check="480c + 2,100(25 - c) = 23,340 gives 1,620c = 29,160 and c = 18 carts."),

 dict(n="H1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A plasterer's price for running a cornice is a linear function of the length of the run. "
            "A run of 12 metres is priced at $438 and a run of 20 metres at $690. At the same rates, "
            "what is the price, in dollars, of a run of 32 metres?"),
      choices=["1,008", "1,044", "1,068", "1,104"], correct="C",
      check="252 dollars over 8 metres is 31.50 a metre, leaving 438 - 378 = 60 fixed; 32(31.5) + 60 = 1,068."),

 dict(n="H1-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Green bricks are set in a kiln in bungs of 800 bricks each, and every bung must be "
            "complete. A firing is worth lighting only if the kiln holds at least 30,000 bricks, and "
            "the kiln cannot hold more than 34,000. How many different whole numbers of bungs meet "
            "both conditions?"),
      choices=["4", "5", "6", "8"], correct="B",
      check="800b is between 30,000 and 34,000 for b from 37.5 to 42.5, so b is 38, 39, 40, 41 or 42."),

 dict(n="H1-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{6x^{2}+19x+15}{2x+3}\\) for "
            "\\(x\\ne-\\frac{3}{2}\\) ?"),
      choices=["3x+5", "3x+3", "2x+5", "6x+5"], correct="A",
      check="6x^2 + 19x + 15 factors as (2x+3)(3x+5), and the (2x+3) cancels."),

 dict(n="H1-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The head of a kiln doorway is cut to a parabola. Its height above the floor, in "
            "centimetres, is \\(h(x)=-\\frac{1}{20}(x-90)^{2}+180\\), where x is the horizontal "
            "distance in centimetres from one jamb. How wide is the doorway at floor level, in "
            "centimetres?"),
      choices=["60", "90", "110", "120"], correct="D",
      check="h = 0 gives (x-90)^2 = 3,600, so x = 30 or x = 150 and the width is 120."),

 dict(n="H1-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Each day in a drying shed removes the same fraction of whatever water a stack of green "
            "bricks still holds. One stack held 240 kilograms of water when it was set down and "
            "122.88 kilograms at the end of the third day. How many kilograms of water did it hold "
            "at the end of the first day?"),
      choices=["120", "153.6", "192", "216"], correct="C",
      check="240r^3 = 122.88 gives r^3 = 0.512 and r = 0.8, so after one day 240(0.8) = 192."),

 dict(n="H1-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("For the function g, \\(g(x)=a(x-3)(x+7)\\), where a is a constant. If \\(g(1)=-48\\), "
            "what is the value of \\(g(0)\\) ?"),
      choices=["-63", "-21", "21", "63"], correct="A",
      check="g(1) = a(-2)(8) = -16a = -48 gives a = 3, and g(0) = 3(-3)(7) = -63."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A plasterer works out the volume of finishing coat for a wall from "
            "\\(V=\\frac{Lht}{1000}\\), where V is in cubic metres, L and h are the length and "
            "height of the wall in metres and t is the thickness of the coat in millimetres. Which "
            "expression gives t in terms of the other quantities?"),
      choices=["\\(\\frac{1000V}{Lh}\\)", "\\(\\frac{Lh}{1000V}\\)", "\\(\\frac{V}{1000Lh}\\)",
               "\\(\\frac{VLh}{1000}\\)"], correct="A",
      check="Multiplying by 1,000 and dividing by Lh gives t = 1000V/(Lh)."),

 dict(n="H1-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the xy-plane the graphs of \\(y=x^{2}-6x+13\\) and \\(y=2x-2\\) meet at two points. "
            "What is the sum of the x-coordinates of those two points?"),
      choices=["3", "5", "8", "15"], correct="C",
      check="x^2 - 6x + 13 = 2x - 2 gives x^2 - 8x + 15 = 0, whose roots 3 and 5 sum to 8."),

 dict(n="H1-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Six moulders working an 8-hour day moulded 2,400 green bricks. Working at the same rate "
            "for each moulder, how many green bricks would nine moulders mould in a 10-hour day?"),
      choices=["3,600", "4,500", "5,400", "6,000"], correct="B",
      check="2,400/(6 times 8) = 50 bricks per moulder-hour, and 9(10)(50) = 4,500."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of bricks drawn from each of four kilns after one firing and "
            "the percentage of those bricks that were wasters. For which kiln was the number of "
            "sound bricks greatest?"
            + table(["Kiln", "Bricks drawn", "Wasters"],
                    [["Ashcombe", "34,000", "8%"],
                     ["Bewley", "30,000", "2%"],
                     ["Cullen", "36,000", "15%"],
                     ["Draycote", "32,000", "5%"]])),
      choices=["Ashcombe", "Bewley", "Cullen", "Draycote"], correct="A",
      check="Sound bricks are 31,280, 29,400, 30,600 and 30,400, so Ashcombe is greatest."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A firing drew 24,000 bricks. Of those, 6 per cent were wasters and were thrown out. Of "
            "the bricks that remained, one in every eight was graded a second and the rest were "
            "graded first quality. How many bricks were graded first quality?"),
      choices=["18,048", "19,200", "19,560", "19,740"], correct="D",
      check="24,000(0.94) = 22,560 sound bricks, and seven eighths of 22,560 is 19,740."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Six firings at a brickyard used 14, 17, 12, 19, 15 and 21 tonnes of coal. A seventh "
            "firing then used 16 tonnes. By how many tonnes did the median of the list change when "
            "the seventh figure was added?"),
      choices=["0", "0.5", "1", "1.5"], correct="A",
      check="The first six sort to 12, 14, 15, 17, 19, 21 with median 16; adding 16 keeps the median at 16."),

 dict(n="H1-17", domain="GT", skill="GT-LA", type="MC",
      stem=("A lath is nailed diagonally across the corner of a rectangular door opening. It meets "
            "the jamb at a point 45 centimetres below the head and meets the head at a point 108 "
            "centimetres from that jamb. The lath is then cut 6 centimetres longer at each end so "
            "that it can be nailed. What is the length, in centimetres, of the piece of lath cut?"),
      choices=["117", "121", "125", "129"], correct="D",
      check="The diagonal is sqrt(45^2 + 108^2) = 117, and 117 + 6 + 6 = 129."),

 dict(n="H1-18", domain="GT", skill="GT-TR", type="MC",
      stem=("A brickyard chimney stands vertically on level ground. From a point on the ground 48 "
            "metres from the foot of the chimney, the angle of elevation of the top has a tangent "
            "of \\(\\frac{5}{12}\\). What is the straight-line distance, in metres, from that point "
            "to the top of the chimney?"),
      choices=["20", "52", "60", "68"], correct="B",
      check="The height is 48(5/12) = 20, and sqrt(48^2 + 20^2) = 52."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The inside of a brick kiln is a rectangular box 9 metres long, 4 metres wide and 3 "
            "metres high to the springing, and above it sits a crown in the form of half a cylinder "
            "of the same 9-metre length whose diameter is the 4-metre width. What is the total "
            "volume inside the kiln, in cubic metres?"),
      choices=["\\(108+9\\pi\\)", "\\(108+12\\pi\\)", "\\(108+18\\pi\\)", "\\(108+36\\pi\\)"],
      correct="C",
      check="The box is 9(4)(3) = 108 and the half-cylinder is (1/2)pi(2^2)(9) = 18 pi."),

 dict(n="H1-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A firing began with 8 tonnes of coal at the kiln, burned at a steady rate. After 30 "
            "hours of firing, 5.6 tonnes were left. The firing must be stopped while 1.6 tonnes are "
            "still in reserve. For how many hours in total can the firing run?"),
      answers=["80"],
      check="2.4 tonnes in 30 hours is 0.08 a hour, and 6.4/0.08 = 80 hours."),

 dict(n="H1-21", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("At a brickyard the day gang moulded a mean of 1,860 green bricks a day over 6 days, and "
            "the night gang moulded a mean of 1,410 a day over 4 days. What is the mean number of "
            "green bricks moulded a day over all 10 of those days?"),
      answers=["1680"],
      check="6(1,860) + 4(1,410) = 11,160 + 5,640 = 16,800, and 16,800/10 = 1,680."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A brick wall is to be 22 metres long, 2.7 metres high and 0.34 metres thick. Each brick "
            "together with its share of the mortar occupies 0.0017 cubic metres of the wall. How "
            "many bricks does the wall take?"),
      answers=["11880"],
      check="22(2.7)(0.34) = 20.196 cubic metres, and 20.196/0.0017 = 11,880."),
]


# ------------------------------------------------------------ Module 2 (Easy)
# Tile making, stonemasonry and tracery, scaffolding and hoists.
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A pallet held 480 plain tiles. Seven equal barrow loads were taken off it and 165 tiles "
            "were left. How many tiles were in each barrow load?"),
      choices=["35", "45", "55", "63"], correct="B",
      check="480 - 165 = 315, and 315/7 = 45."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An empty crate has a mass of 8 kilograms, and each ridge tile packed into it has a mass "
            "of 3 kilograms. The full crate has a mass of 71 kilograms. How many ridge tiles are in "
            "the crate?"),
      choices=["21", "23", "24", "26"], correct="A",
      check="3t + 8 = 71 gives 3t = 63 and t = 21."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The total mass, in kilograms, of a scaffold tower built n lifts high is given by "
            "46n + 120. What is the total mass, in kilograms, of a tower built 5 lifts high?"),
      choices=["166", "236", "350", "580"], correct="C",
      check="46(5) + 120 = 230 + 120 = 350."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A hoist raises a load at a constant speed. The load was 9 metres above the ground 2 "
            "seconds after the hoist started and 21 metres above the ground 6 seconds after it "
            "started. How many metres does the load rise each second?"),
      choices=["1", "2", "2.5", "3"], correct="D",
      check="(21 - 9)/(6 - 2) = 12/4 = 3 metres a second."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Which value of x satisfies the inequality 4x - 5 > 19 ?"),
      choices=["4", "5", "6", "7"], correct="D",
      check="4x > 24 gives x > 6, and 7 is the only listed value greater than 6."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tile press turns out 180 tiles every 4 minutes. At that rate, how many tiles does it "
            "turn out in 15 minutes?"),
      choices=["45", "540", "675", "720"], correct="C",
      check="180/4 = 45 tiles a minute, and 45(15) = 675."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A mason's cart may carry a load of no more than 750 kilograms. Each dressed stone has a "
            "mass of 60 kilograms. What is the greatest number of dressed stones the cart may carry "
            "in one load?"),
      choices=["11", "12", "13", "15"], correct="B",
      check="750/60 = 12.5, so 12 whole stones can be carried."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to 3(2x + 7) - 4x ?"),
      choices=["2x+21", "2x+7", "6x+21", "10x+21"], correct="A",
      check="6x + 21 - 4x = 2x + 21."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\((x+6)(x+2)\\) ?"),
      choices=["\\(x^{2}+6x+12\\)", "\\(x^{2}+2x+12\\)", "\\(x^{2}+8x+12\\)", "\\(x^{2}+12x+8\\)"],
      correct="C",
      check="The outer and inner products give 6x + 2x = 8x, and 6(2) = 12."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=x^{2}-5\\). What is the value of \\(f(4)\\) ?"),
      choices=["11", "16", "21", "27"], correct="A",
      check="4^2 - 5 = 16 - 5 = 11."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("If \\((n-9)(n+4)=0\\) and n is positive, what is the value of n ?"),
      choices=["-4", "4", "5", "9"], correct="D",
      check="The solutions are 9 and -4, and only 9 is positive."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of x and the corresponding values of the function f. For "
            "which value of x is \\(f(x)=12\\) ?"
            + table(["x", "f(x)"], [["2", "3"], ["4", "12"], ["6", "27"], ["8", "48"]])),
      choices=["2", "4", "6", "8"], correct="B",
      check="The row whose second entry is 12 has x = 4."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("If \\(\\sqrt{x}=13\\), what is the value of x ?"),
      choices=["26", "144", "169", "196"], correct="C",
      check="Squaring both sides gives x = 169."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("At a tileworks, 3 of every 8 tiles made are pantiles. In a batch of 240 tiles, how many "
            "are pantiles?"),
      choices=["90", "96", "120", "150"], correct="A",
      check="Three eighths of 240 is 90."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of tiles drawn from the presses at four tileworks in one "
            "week. How many more tiles did Marlow draw than Penhale?"
            + table(["Tileworks", "Tiles drawn"],
                    [["Kelby", "4,200"], ["Marlow", "5,600"], ["Penhale", "3,900"],
                     ["Rowan", "4,800"]])),
      choices=["1,400", "1,700", "2,100", "2,600"], correct="B",
      check="5,600 - 3,900 = 1,700."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Four dressed stones have masses of 62, 70, 74 and 84 kilograms. What is the median of "
            "these four masses, in kilograms?"),
      choices=["70", "72", "74", "78"], correct="B",
      check="The two middle values are 70 and 74, and their mean is 72."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Of the 340 tiles carried up a scaffold in one morning, 15 per cent were broken. How "
            "many of those tiles were broken?"),
      choices=["34", "44", "48", "51"], correct="D",
      check="0.15(340) = 51."),

 dict(n="H2E-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A circular stone roundel has a radius of 30 centimetres. What is its area, in square "
            "centimetres?"),
      choices=["\\(30\\pi\\)", "\\(60\\pi\\)", "\\(900\\pi\\)", "\\(3600\\pi\\)"], correct="C",
      check="pi r^2 with r = 30 gives 900 pi."),

 dict(n="H2E-19", domain="GT", skill="GT-TR", type="MC",
      stem=("In a right triangle, the side opposite one of the acute angles has a length of 7 and "
            "the hypotenuse has a length of 25. What is the sine of that acute angle?"),
      choices=["\\(\\frac{24}{25}\\)", "\\(\\frac{7}{25}\\)", "\\(\\frac{7}{24}\\)",
               "\\(\\frac{25}{7}\\)"], correct="B",
      check="Sine is the opposite side over the hypotenuse, so it is 7/25."),

 dict(n="H2E-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("Five loads of stone brought to a mason's yard had masses of 340, 380, 300, 360 and 420 "
            "kilograms. What is the mean mass, in kilograms, of a load?"),
      answers=["360"],
      check="The five masses total 1,800, and 1,800/5 = 360."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A block of stone is a cube with edges of 40 centimetres. What is the volume of the "
            "block, in cubic centimetres?"),
      answers=["64000"],
      check="40 cubed is 64,000."),

 dict(n="H2E-22", domain="GT", skill="GT-LA", type="FR",
      stem=("A triangular timber bracket under a scaffold platform has two of its angles measuring "
            "47&deg; and 68&deg;. What is the measure, in degrees, of its third angle?"),
      answers=["65"],
      check="180 - 47 - 68 = 65."),
]


# ------------------------------------------------------------ Module 2 (Hard)
# Tile making, stonemasonry and tracery, scaffolding and hoists.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("For two numbers x and y, \\(x+y=13\\) and \\(x^{2}-y^{2}=91\\). What is the value of "
            "\\(x-y\\) ?"),
      choices=["3", "7", "13", "91"], correct="B",
      check="x^2 - y^2 = (x+y)(x-y), so 13(x-y) = 91 and x - y = 7."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the system of equations below, c is a constant and the system has no solution."
            "<br/>\\(2x-3y=7\\)<br/>\\(4x+cy=9\\)<br/>What is the value of c ?"),
      choices=["-6", "-2", "2", "6"], correct="A",
      check="No solution needs the left sides proportional, so c/(-3) = 4/2 and c = -6."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, a line passes through the points \\((a,2a)\\) and \\((3a,8a)\\), where "
            "a is a positive constant. What is the slope of that line?"),
      choices=["1", "2", "3", "6"], correct="C",
      check="(8a - 2a)/(3a - a) = 6a/2a = 3, whatever positive a is."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("How many integers n satisfy both 5n - 7 > 18 and 3n + 4 \\(\\le\\) 61 ?"),
      choices=["12", "13", "14", "15"], correct="C",
      check="n > 5 and n <= 19 give n from 6 to 19, which is 14 integers."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, a line of slope \\(-\\frac{3}{4}\\) passes through the point "
            "\\((8,-1)\\). What is the y-coordinate of the point at which the line crosses the "
            "y-axis?"),
      choices=["-7", "1", "5", "11"], correct="C",
      check="-1 = -3/4(8) + b gives b = -1 + 6 = 5."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A dressed stone and the pallet under it have a combined mass of m kilograms, and the "
            "stone is 4 times as heavy as the pallet. In terms of m, what is the mass of the stone, "
            "in kilograms?"),
      choices=["\\(\\frac{4m}{5}\\)", "\\(\\frac{m}{5}\\)", "\\(\\frac{3m}{4}\\)",
               "\\(\\frac{5m}{4}\\)"], correct="A",
      check="With pallet p the total is 5p = m, so the stone 4p is 4m/5."),

 dict(n="H2H-07", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g are defined by \\(f(x)=3x-4\\) and \\(g(x)=x^{2}+c\\), where c is "
            "a constant. If \\(f(g(2))=11\\), what is the value of c ?"),
      choices=["-1", "1", "3", "5"], correct="B",
      check="f(g(2)) = 3(4 + c) - 4 = 8 + 3c = 11 gives c = 1."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("What is the solution to the equation \\(\\sqrt{5x+11}=x+1\\) ?"),
      choices=["-2", "3", "5", "7"], correct="C",
      check="Squaring gives x^2 - 3x - 10 = 0 with roots 5 and -2; -2 fails the original equation."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A winch working alone raises a stone to the top of a tower in u minutes, and a second "
            "winch working alone raises the same stone in v minutes. Working together at those "
            "rates, the two winches raise the stone in how many minutes?"),
      choices=["\\(\\frac{uv}{u+v}\\)", "\\(\\frac{u+v}{uv}\\)", "\\(\\frac{u+v}{2}\\)",
               "\\(\\frac{2}{u+v}\\)"], correct="A",
      check="The combined rate is 1/u + 1/v = (u+v)/(uv), and the time is its reciprocal."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In the xy-plane, the graph of \\(y=x^{2}+bx+c\\), where b and c are constants, has its "
            "lowest point at \\((4,-9)\\). What is the value of \\(b+c\\) ?"),
      choices=["-1", "1", "7", "15"], correct="A",
      check="y = (x-4)^2 - 9 = x^2 - 8x + 7, so b = -8, c = 7 and b + c = -1."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("What value of x satisfies \\(\\frac{27^{x}}{9^{x-1}}=243\\) ?"),
      choices=["2", "3", "5", "6"], correct="B",
      check="3^(3x) over 3^(2x-2) is 3^(x+2), and 243 is 3^5, so x + 2 = 5 and x = 3."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The expression \\(x^{2}+kx+36\\), where k is a constant, is the square of a binomial. "
            "If k is negative, what is the value of k ?"),
      choices=["-12", "-6", "6", "12"], correct="A",
      check="(x - 6)^2 = x^2 - 12x + 36, so the negative value of k is -12."),

 dict(n="H2H-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A gang of w masons cuts b blocks in d days, every mason working at the same steady "
            "rate. At that rate, how many blocks would a gang of 2w masons cut in 3d days?"),
      choices=["\\(\\frac{2b}{3}\\)", "3b", "5b", "6b"], correct="D",
      check="Twice the masons for three times the days is six times the work, or 6b blocks."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean mass of 7 dressed blocks is 84 kilograms. When one more block is added to the "
            "set, the mean mass of the 8 blocks is 87 kilograms. What is the mass, in kilograms, of "
            "the block that was added?"),
      choices=["87", "96", "108", "120"], correct="C",
      check="8(87) - 7(84) = 696 - 588 = 108."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of stones cut and the number rejected at four banker shops "
            "in one month. At which shop was the greatest percentage of the stones cut rejected?"
            + table(["Banker shop", "Stones cut", "Stones rejected"],
                    [["Alder", "250", "12"], ["Brent", "180", "9"],
                     ["Corve", "320", "18"], ["Dell", "400", "20"]])),
      choices=["Alder", "Brent", "Corve", "Dell"], correct="C",
      check="The rates are 4.8%, 5%, 5.625% and 5%, so Corve is highest."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The number of tiles a press turned out in a week fell by 12 per cent from one week to "
            "the next, and then rose by 25 per cent in the week after that, ending at 3,300 tiles. "
            "How many tiles did the press turn out in the first of those three weeks?"),
      choices=["2,904", "3,000", "3,300", "3,750"], correct="B",
      check="0.88(1.25) = 1.10, and 3,300/1.10 = 3,000."),

 dict(n="H2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A stone finial is made of a cube of edge 30 centimetres with a right pyramid set "
            "squarely on its top face. The pyramid's base is that whole top face and its apex is 40 "
            "centimetres above it. What is the total volume of the finial, in cubic centimetres?"),
      choices=["21,000", "27,000", "36,000", "39,000"], correct="D",
      check="27,000 for the cube plus (1/3)(900)(40) = 12,000 for the pyramid gives 39,000."),

 dict(n="H2H-18", domain="GT", skill="GT-LA", type="MC",
      stem=("A two-centred head for a tracery light is struck with two circular arcs, each of radius "
            "equal to the span and each centred on one of the two springing points, so that the two "
            "arcs meet at the apex. The span is 2.4 metres. What is the height of the apex above "
            "the line joining the springing points, in metres?"),
      choices=["\\(1.2\\sqrt{2}\\)", "\\(1.2\\sqrt{3}\\)", "\\(2.4\\sqrt{2}\\)",
               "\\(2.4\\sqrt{3}\\)"], correct="B",
      check="The two springings and the apex form an equilateral triangle of side 2.4, whose height is 1.2 sqrt(3)."),

 dict(n="H2H-19", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC the right angle is at C, and \\(\\sin A=\\frac{20}{29}\\). What "
            "is the value of \\(\\tan A\\) ?"),
      choices=["\\(\\frac{20}{29}\\)", "\\(\\frac{21}{29}\\)", "\\(\\frac{21}{20}\\)",
               "\\(\\frac{20}{21}\\)"], correct="D",
      check="The third side is sqrt(29^2 - 20^2) = 21, so tan A = 20/21."),

 dict(n="H2H-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A set of 12 measurements has a mean of 25. Every measurement in the set is then "
            "increased by 4, and each result is doubled. What is the mean of the 12 numbers that "
            "result?"),
      answers=["58"],
      check="Adding 4 takes the mean to 29 and doubling takes it to 58."),

 dict(n="H2H-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The numbers x and y satisfy 3x + 4y = 41 and 5x - 2y = 25. What is the value of "
            "x + y ?"),
      answers=["12"],
      check="Doubling the second and adding gives 13x = 91, so x = 7, y = 5 and x + y = 12."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A stone corbel is cut from a rectangular block 45 centimetres long, 22 centimetres wide "
            "and 18 centimetres deep. A rectangular notch running the whole 45-centimetre length, 8 "
            "centimetres wide and 6 centimetres deep, is cut out of one edge. What is the volume of "
            "the finished corbel, in cubic centimetres?"),
      answers=["15660"],
      check="45(22)(18) = 17,820 and the notch is 45(8)(6) = 2,160, leaving 15,660."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
