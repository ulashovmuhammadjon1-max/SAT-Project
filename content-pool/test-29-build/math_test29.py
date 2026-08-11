#!/usr/bin/env python3
"""
Original Math content for Test 29 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item makes a rate, a constant, a
                unit price or an unknown be recovered first and only then used;
                two or three steps throughout.
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
  MODULE_2_HARD hard: parameters instead of numbers, symbolic answer choices, a
                function defined by a shift of another, a biquadratic, a
                two-rate charge, an integer count over a compound inequality,
                and geometry needing two relationships chained.

Test 29's thematic territory is the building trades that begin where the stone
leaves the ground: brickworks and kilns, tile making, plasterwork and lath,
stonemasonry and tracery, scaffolding and hoists. The territory is SPLIT across
the adaptive branches, because a student sees Module 1 and exactly one Module 2
module:

  Module 1          brickworks, brick kilns and firing, plasterwork and lath
  Module 2 (both)   tile making, stonemasonry and tracery, scaffolding and hoists

No setting keyword may cross that line; verify_math_test29.py pass 4 enforces
it with word-boundary-safe matching.

Every stem carries enough of its own setting to be recognisable. That is not
only house style: a bare stem such as "Which expression is equivalent to ...?"
is nearly all boilerplate, and its token signature collides with every other
bare stem in the bank. Six first drafts scored above 0.75 against production for
that reason alone, and several more were genuine template repeats hiding under a
low score. See MANIFEST.md for the full list.

House style follows Test 1/2 (see CLAUDE.md): bare HTML stems, simple inline
maths left as plain text, real <table> markup for every data table, &deg; as an
entity, every \\( \\) typed by hand. No bulk conversion step was used anywhere
in this file. No images: every figure is a real table, and every geometry item
is worded so that it is fully determined without a picture.
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
      stem=("A carter is paid $14 for every day he works at a brickyard and, on top of that, $9 for "
            "every load of green bricks he carries to the kilns. In a week in which he worked 6 days "
            "he was paid $624 altogether. How many loads did he carry that week?"),
      choices=["60", "66", "69", "72"], correct="A",
      check="The 6 days are worth 84 dollars, leaving 540 dollars at 9 a load, so 60 loads."),

 dict(n="H1-02", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The number of green bricks still standing in a drying shed d days after the moulding "
            "gang stopped work is 15,400 - 620d. On which day does the shed first hold fewer than "
            "4,000 green bricks?"),
      choices=["17", "18", "19", "20"], correct="C",
      check="15,400 - 620d < 4,000 gives d > 18.38, so the first whole day is day 19."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Two kilns are lit on the same morning, each with 30 tonnes of coal at its mouth. The "
            "first burns coal steadily at 0.6 tonnes an hour and the second steadily at 0.45 tonnes "
            "an hour. After how many hours of burning does the first kiln have 9 tonnes less coal "
            "left than the second?"),
      choices=["40", "45", "50", "60"], correct="D",
      check="The two amounts left are 30 - 0.6h and 30 - 0.45h, whose difference 0.15h equals 9 at h = 60."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Three fifths of the green bricks standing in a drying shed were set in a kiln. Then 480 "
            "of the bricks still in the shed were carted to a second shed, and 1,120 green bricks "
            "were left standing in the first. How many green bricks were standing in the shed before "
            "any were moved?"),
      choices=["4,000", "4,800", "5,200", "6,400"], correct="A",
      check="Two fifths of the start, less 480, is 1,120, so two fifths is 1,600 and the start is 4,000."),

 dict(n="H1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A plasterer gauges every batch of coarse stuff so that 3s + 2p = 96, where s is the "
            "number of barrows of sand and p the number of barrows of lime putty in the batch. One "
            "batch is gauged with 4 more barrows of sand than another batch. How many fewer barrows "
            "of lime putty does that batch use?"),
      choices=["2", "3", "6", "8"], correct="C",
      check="Raising s by 4 raises 3s by 12, so 2p must fall by 12 and p falls by 6."),

 dict(n="H1-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A moulder is held to an output that averages at least 1,200 green bricks a day over a "
            "five-day week. On the first four days of one week he moulded 1,150, 1,240, 1,090 and "
            "1,275 bricks. What is the least number of green bricks he can mould on the fifth day "
            "and still meet that condition?"),
      choices=["1,200", "1,225", "1,245", "1,260"], correct="C",
      check="Five days at a mean of 1,200 need 6,000 altogether, and the first four came to 4,755."),

 dict(n="H1-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("At a brickyard the cost of firing n thousand bricks is \\(0.5n^{2}+13n\\) dollars, and "
            "the money taken for them is \\(0.5n^{2}+31n-54\\) dollars. Which expression gives the "
            "brickyard's profit, in dollars, on n thousand bricks?"),
      choices=["18n-54", "18n+54", "\\(n^{2}+18n-54\\)", "44n-54"], correct="A",
      check="Subtracting the cost from the money taken cancels the squared terms and leaves 18n - 54."),

 dict(n="H1-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A moulding gang has 540 thousand green bricks to mould for a contract. If the gang "
            "moulded 3 thousand more bricks each day than it now plans to, it would finish the "
            "contract 9 days earlier than it now plans to. How many thousand bricks a day does the "
            "gang now plan to mould?"),
      choices=["9", "12", "15", "18"], correct="B",
      check="540/n - 540/(n+3) = 9 clears to n^2 + 3n - 180 = 0, whose positive root is 12."),

 dict(n="H1-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Two brick piers stand on the same footing. One is 4 metres taller than the other, and "
            "the sum of the squares of their two heights, each in metres, is 106. How many metres "
            "tall is the shorter pier?"),
      choices=["3", "5", "6", "7"], correct="B",
      check="x^2 + (x+4)^2 = 106 gives x^2 + 4x - 45 = 0, whose positive root is 5."),

 dict(n="H1-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The depth of scale on the inside of a brick flue, in millimetres, is modelled by "
            "\\(s(t)=0.6t^{2}+2t\\), where t is the number of years since the flue was built. What "
            "is the average rate of change of this model, in millimetres a year, from the fourth "
            "year to the tenth year?"),
      choices=["8.4", "9.6", "10.4", "12.2"], correct="C",
      check="s(10) = 80 and s(4) = 17.6, and their difference over 6 years is 10.4 a year."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A plasterer's estimating rule gives the number of laths a panel takes as "
            "\\(x^{2}+18x+c\\), where x is the width of the panel in feet and c is a constant. That "
            "expression is the square of a binomial for every value of x. What is the value of c ?"),
      choices=["9", "36", "72", "81"], correct="D",
      check="(x+9)^2 = x^2 + 18x + 81 is the only square with an 18x term, so c = 81."),

 dict(n="H1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A plasterer's drying model is the function f defined by \\(f(x)=x^{2}-9x\\), where x "
            "is the number of hours since the coat was laid. The model takes the same value at k "
            "hours as it does at k+3 hours. What is the value of k ?"),
      choices=["2", "3", "4.5", "6"], correct="B",
      check="f(k+3) - f(k) = 6k - 18, which is 0 only at k = 3."),

 dict(n="H1-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A brickyard buys its coal either in loads of 12 tonnes costing $960 or in loads of 20 "
            "tonnes costing $1,560. How many dollars less does a tonne of coal cost in the larger "
            "load than in the smaller?"),
      choices=["2", "3", "4", "6"], correct="A",
      check="960/12 = 80 a tonne and 1,560/20 = 78 a tonne, a difference of 2."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A chimney stack was measured at the end of each week while it was being built, and the "
            "table gives the height reached. During which week did the stack rise by the greatest "
            "number of metres?"
            + table(["End of week", "Height of stack (m)"],
                    [["1", "6.4"], ["2", "12.1"], ["3", "17.2"], ["4", "23.5"], ["5", "28.0"]])),
      choices=["Week 2", "Week 3", "Week 4", "Week 5"], correct="C",
      check="The weekly rises are 5.7, 5.1, 6.3 and 4.5 metres, and the greatest is in week 4."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A firing drew 24,000 bricks. Of those, 6 per cent were wasters and were thrown out. Of "
            "the bricks that remained, one in every eight was graded a second and the rest were "
            "graded first quality. How many bricks were graded first quality?"),
      choices=["18,048", "19,200", "19,560", "19,740"], correct="D",
      check="24,000(0.94) = 22,560 sound bricks, and seven eighths of 22,560 is 19,740."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Six firings at a brickyard used 14, 17, 12, 19, 15 and 21 tonnes of coal. A seventh "
            "firing then used 16 tonnes. By how many tonnes did the median of the list change when "
            "the seventh figure was added to it?"),
      choices=["0", "0.5", "1", "1.5"], correct="A",
      check="The first six sort to 12, 14, 15, 17, 19, 21 with median 16; adding 16 keeps the median at 16."),

 dict(n="H1-17", domain="GT", skill="GT-LA", type="MC",
      stem=("A lath is nailed diagonally across the corner of a rectangular door opening. It meets "
            "the jamb at a point 45 centimetres below the head and meets the head at a point 108 "
            "centimetres from that jamb. The lath is cut 6 centimetres longer at each end so that "
            "it can be nailed. What is the length, in centimetres, of the piece of lath cut?"),
      choices=["117", "121", "125", "129"], correct="D",
      check="The diagonal is sqrt(45^2 + 108^2) = 117, and 117 + 6 + 6 = 129."),

 dict(n="H1-18", domain="GT", skill="GT-TR", type="MC",
      stem=("The two sloping sides of a brick gable are equal, and each makes an angle with the "
            "horizontal whose tangent is \\(\\frac{7}{24}\\). The gable is 14.4 metres wide at its "
            "base. How long, in metres, is each of its sloping sides?"),
      choices=["6.9", "7.5", "8.4", "9.6"], correct="B",
      check="Half the base is 7.2, the rise is 7.2(7/24) = 2.1, and sqrt(7.2^2 + 2.1^2) = 7.5."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The inside of a brick kiln is a rectangular box 9 metres long, 4 metres wide and 3 "
            "metres high to the springing, and above that sits a crown in the form of half a "
            "cylinder of the same 9-metre length whose diameter is the 4-metre width. What is the "
            "total volume inside the kiln, in cubic metres?"),
      choices=["\\(108+9\\pi\\)", "\\(108+12\\pi\\)", "\\(108+18\\pi\\)", "\\(108+36\\pi\\)"],
      correct="C",
      check="The box holds 9(4)(3) = 108 and the half-cylinder (1/2)pi(2^2)(9) = 18 pi."),

 dict(n="H1-20", domain="ALG", skill="ALG-LE", type="FR",
      stem=("Of the bricks drawn from one kiln, one third were graded commons and one quarter were "
            "graded facings. The remaining 250 bricks were graded seconds. How many bricks were "
            "drawn from the kiln?"),
      answers=["600"],
      check="Commons and facings take 7/12 of the draw, so the 250 seconds are 5/12 of it and the draw is 600."),

 dict(n="H1-21", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("Of the 400 bricks drawn from a kiln, 15 per cent were wasters and the rest were sound. "
            "One of those 400 bricks is picked at random. What is the probability that the brick "
            "picked is not a waster?"),
      answers=["0.85", "17/20", ".85"],
      check="340 of the 400 bricks are sound, and 340/400 = 0.85."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A room is 5.4 metres long, 4.2 metres wide and 2.5 metres high, and its four walls are "
            "to be plastered. A doorway 2 metres high and 0.9 metres wide is cut in one of the "
            "walls and is not plastered. How many square metres of plastering does the room take?"),
      answers=["46.2"],
      check="The four walls are 2(5.4+4.2)(2.5) = 48 square metres, less the 1.8 of the doorway."),
]


# ------------------------------------------------------------ Module 2 (Easy)
# Tile making, stonemasonry and tracery, scaffolding and hoists.
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A pallet held 480 plain tiles. Seven equal barrow loads were taken off it and 165 tiles "
            "were left on it. How many tiles were in each barrow load?"),
      choices=["35", "45", "55", "63"], correct="B",
      check="480 - 165 = 315, and 315/7 = 45."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An empty crate has a mass of 8 kilograms, and each ridge tile packed into it has a mass "
            "of 3 kilograms. The full crate has a mass of 71 kilograms. How many ridge tiles are in "
            "the crate?"),
      choices=["21", "23", "24", "26"], correct="A",
      check="3t + 8 = 71 gives 3t = 63 and t = 21."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The table gives three values of the linear function h, which a tiler uses to work out "
            "the number of battens a roof takes."
            + table(["x", "h(x)"], [["2", "11"], ["4", "17"], ["6", "23"]])
            + " What is the value of h(8) ?"),
      choices=["26", "27", "29", "31"], correct="C",
      check="h rises by 6 for every rise of 2 in x, so h(8) = 23 + 6 = 29."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A hoist raises a load at a constant speed. The load was 9 metres above the ground 2 "
            "seconds after the hoist started and 21 metres above the ground 6 seconds after it "
            "started. How many metres does the load rise each second?"),
      choices=["1", "2", "2.5", "3"], correct="D",
      check="(21 - 9)/(6 - 2) = 12/4 = 3 metres a second."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A mason is paid $22 for every stone he dresses. What is the least whole number of "
            "stones he must dress for his pay to be more than $300 ?"),
      choices=["13", "14", "15", "16"], correct="B",
      check="22s > 300 gives s > 13.6, so 14 stones is the least whole number."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tiler's rule for the number x of tiles in one row makes 7x - 12 = 4x + 27 true. "
            "What is the value of x ?"),
      choices=["5", "9", "13", "15"], correct="C",
      check="Taking 4x from both sides gives 3x - 12 = 27, so 3x = 39 and x = 13."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The number of tiles x that may be sent up in one lift of a hoist satisfies "
            "\\(5x+8\\le 78\\). What is the greatest number of tiles that may be sent up in one "
            "lift?"),
      choices=["14", "15", "16", "17"], correct="A",
      check="5x is at most 70, so x is at most 14."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("On a mason's cutting list the numbers a and b of two sizes of stone satisfy "
            "2a + 3b = 17. What is the value of 6a + 9b ?"),
      choices=["17", "34", "51", "68"], correct="C",
      check="6a + 9b is 3 times 2a + 3b, so it is 3(17) = 51."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("At a tileworks the number of sound tiles left after sorting is 7x - 2(x - 4), where x "
            "is the number of racks sorted. That number equals ax + 8 for every value of x, where a "
            "is a constant. What is the value of a ?"),
      choices=["3", "5", "7", "9"], correct="B",
      check="7x - 2x + 8 = 5x + 8, so a = 5."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function h is defined by \\(h(x)=(x-2)(x+6)\\). For which values of x is "
            "\\(h(x)=0\\) ?"),
      choices=["-6 and -2", "-6 and 2", "-2 and 6", "2 and 6"], correct="B",
      check="A product is zero only when a factor is, so x - 2 = 0 or x + 6 = 0."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Tiles are stacked in a square, x tiles along each side, so that the stack holds "
            "\\(x^{2}\\) tiles altogether. One such stack holds 196 tiles. How many tiles are there "
            "along each side of it?"),
      choices=["12", "14", "16", "98"], correct="B",
      check="x^2 = 196 and x is positive, so x = 14."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function p gives the price, in dollars, of n ridge tiles, and \\(p(n)=1.75n\\). "
            "Which statement is the best interpretation of \\(p(40)=70\\) ?"),
      choices=["One ridge tile costs $40.",
               "The price of 70 ridge tiles is $40.",
               "One ridge tile costs $70.",
               "The price of 40 ridge tiles is $70."],
      correct="D",
      check="p takes a number of tiles and returns a price, so p(40) = 70 prices 40 tiles at $70."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f gives the number of minutes a hoist takes to raise x crates of tiles, "
            "and \\(f(6)=19\\). Which point must lie on the graph of \\(y=f(x)\\) in the xy-plane?"),
      choices=["(0, 19)", "(19, 0)", "(19, 6)", "(6, 19)"], correct="D",
      check="f(6) = 19 says the input 6 is paired with the output 19, which is the point (6, 19)."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Two thirds of the tiles on a pallet are plain tiles, and one quarter of the plain tiles "
            "on that pallet are graded seconds. What fraction of all the tiles on the pallet are "
            "plain tiles graded seconds?"),
      choices=["\\(\\frac{1}{12}\\)", "\\(\\frac{1}{8}\\)", "\\(\\frac{1}{6}\\)",
               "\\(\\frac{5}{12}\\)"], correct="C",
      check="A quarter of two thirds is one sixth."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of tiles of each kind stacked on one pallet. What fraction "
            "of the tiles on the pallet are ridge tiles?"
            + table(["Kind of tile", "Number on the pallet"],
                    [["Plain", "180"], ["Pantile", "96"], ["Ridge", "72"], ["Valley", "12"]])),
      choices=["\\(\\frac{1}{12}\\)", "\\(\\frac{1}{8}\\)", "\\(\\frac{1}{6}\\)",
               "\\(\\frac{1}{5}\\)"], correct="D",
      check="The pallet holds 360 tiles and 72 of them are ridge tiles, so the fraction is 1/5."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A pallet holds 480 plain tiles and 120 ridge tiles and no others. The number of plain "
            "tiles on the pallet is how many times the number of ridge tiles?"),
      choices=["2", "3", "4", "5"], correct="C",
      check="480/120 = 4."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("On seven working days a hoist gang broke 4, 2, 5, 2, 6, 2 and 7 tiles. Which number of "
            "broken tiles was recorded on more of those days than any other?"),
      choices=["2", "4", "5", "7"], correct="A",
      check="2 appears on three of the seven days and every other figure appears once."),

 dict(n="H2E-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A hoist rope is wound on a drum whose radius is 25 centimetres. How far, in "
            "centimetres, does the load rise during one complete turn of the drum?"),
      choices=["\\(25\\pi\\)", "\\(35\\pi\\)", "\\(50\\pi\\)", "\\(625\\pi\\)"], correct="C",
      check="One turn winds on the circumference, 2 pi (25) = 50 pi."),

 dict(n="H2E-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A guy rope runs in a straight line from the head of a hoist mast to a peg in level "
            "ground. The head of the mast is 15 metres above the ground, and the tangent of the "
            "angle the rope makes with the ground is \\(\\frac{5}{2}\\). How many metres from the "
            "foot of the mast is the peg?"),
      choices=["6", "7.5", "12", "37.5"], correct="A",
      check="The tangent is the 15-metre rise over the distance, so the distance is 15 divided by 5/2, or 6."),

 dict(n="H2E-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("On seven days a mason's yard received 12, 9, 15, 8, 20, 14 and 6 loads of stone. How "
            "many of those seven figures are greater than the mean of the seven?"),
      answers=["3"],
      check="The seven loads total 84, so the mean is 12, and 15, 20 and 14 stand above it."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A circular sinking is cut in the top face of a stone plinth, and the sinking measures "
            "42 centimetres across. The area of the sinking is \\(k\\pi\\) square centimetres. "
            "What is the value of k ?"),
      answers=["441"],
      check="The radius is 21 centimetres, so the area is 21 squared times pi."),

 dict(n="H2E-22", domain="GT", skill="GT-LA", type="FR",
      stem=("A straight joint runs across the top of a stone plinth. On one side of the joint the "
            "angle between the joint and a set square measures \\((3x+20)\\)&deg;, and on the other "
            "side the angle between them measures \\((2x-5)\\)&deg;. The two angles together make a "
            "straight line. What is the value of x ?"),
      answers=["33"],
      check="(3x+20) + (2x-5) = 180 gives 5x + 15 = 180 and x = 33."),
]


# ------------------------------------------------------------ Module 2 (Hard)
# Tile making, stonemasonry and tracery, scaffolding and hoists.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two lengths x and y, in centimetres, cut from a stone bed satisfy \\(x+y=13\\) and "
            "\\(x^{2}-y^{2}=91\\). What is the value of \\(x-y\\) ?"),
      choices=["3", "7", "13", "91"], correct="B",
      check="x^2 - y^2 = (x+y)(x-y), so 13(x-y) = 91 and x - y = 7."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A mason is paid d dollars for each of the first 20 stones he dresses in a week, and "
            "half that rate for every stone he dresses after the first 20. In terms of d, how much "
            "is he paid for dressing 32 stones in a week?"),
      choices=["26d", "28d", "30d", "32d"], correct="A",
      check="20d for the first 20 and 12(d/2) = 6d for the other 12 gives 26d."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("On a mason's setting-out grid a straight cutting line passes through the points "
            "\\((a,2a)\\) and \\((3a,8a)\\), where a is a positive constant. What is the slope of "
            "that cutting line?"),
      choices=["1", "2", "3", "6"], correct="C",
      check="(8a - 2a)/(3a - a) = 6a/(2a) = 3 for every positive a."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A tileworks numbers its press settings with integers n. How many integers n satisfy "
            "both 5n - 7 > 18 and 3n + 4 \\(\\le\\) 61 ?"),
      choices=["12", "13", "14", "15"], correct="C",
      check="n > 5 and n at most 19 give n from 6 to 19, which is 14 integers."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("On a mason's setting-out plan a straight cutting line has the equation \\(px+qy=r\\), "
            "where p, q and r are positive constants. What is the x-coordinate of the point at "
            "which the cutting line crosses the x-axis?"),
      choices=["\\(\\frac{q}{p}\\)", "\\(\\frac{p}{r}\\)", "\\(\\frac{r}{q}\\)",
               "\\(\\frac{r}{p}\\)"], correct="D",
      check="Putting y = 0 gives px = r, so x = r/p."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A dressed stone and the pallet under it have a combined mass of m kilograms, and the "
            "stone is 4 times as heavy as the pallet. In terms of m, what is the mass of the stone, "
            "in kilograms?"),
      choices=["\\(\\frac{4m}{5}\\)", "\\(\\frac{m}{5}\\)", "\\(\\frac{3m}{4}\\)",
               "\\(\\frac{5m}{4}\\)"], correct="A",
      check="With pallet p the total is 5p = m, so the stone, 4p, is 4m/5."),

 dict(n="H2H-07", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A tileworks writes its press-wear index as the function f defined by "
            "\\(f(x)=\\frac{2x+5}{x^{2}-49}\\). For which values of x is f not defined?"),
      choices=["-7 and 7", "-7 only", "7 only", "\\(-\\frac{5}{2}\\) only"], correct="A",
      check="f is undefined exactly where the denominator vanishes, at x = 7 and x = -7."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A tileworks models the bow of a pressed tile by the function f defined by "
            "\\(f(x)=x^{2}-6x+5\\). For how many values of x does \\(f(x)=-4\\) ?"),
      choices=["None", "Exactly one", "Exactly two", "More than two"], correct="B",
      check="f(x) + 4 = (x-3)^2, which is zero only at x = 3, so there is exactly one value."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A mason's setting-out rule gives an offset as \\((\\sqrt{y}+3)(\\sqrt{y}-3)\\), "
            "where y is a measured length and \\(y\\ge 0\\). Which expression is equivalent to "
            "that offset?"),
      choices=["\\(y+9\\)", "\\(y-6\\)", "\\(y-6\\sqrt{y}+9\\)", "\\(y-9\\)"],
      correct="D",
      check="The two factors are conjugates, so their product is y - 9."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A tileworks models the waste from a press by \\(f(x)=x^{2}-6x+c\\), where c is a "
            "constant and x is the number of hours the press has run. The least value f ever takes "
            "is 4. What is the value of c ?"),
      choices=["-5", "4", "13", "22"], correct="C",
      check="f(x) = (x-3)^2 + c - 9, whose least value is c - 9; setting c - 9 = 4 gives c = 13."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A tileworks records a clay stiffness index s for which \\(3^{2s}=7\\). What is the "
            "value of \\(3^{6s}\\) ?"),
      choices=["343", "441", "2,187", "2,401"], correct="A",
      check="3^(6s) is the cube of 3^(2s), so it is 7^3 = 343."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("On a mason's template the expression \\((2x+5)(x-3)-(x-3)(x+1)\\) gives a length in "
            "centimetres. That expression is equivalent to \\((x-3)(ax+b)\\), where a and b are "
            "constants. What is the value of \\(a+b\\) ?"),
      choices=["3", "5", "7", "11"], correct="B",
      check="Taking out (x-3) leaves (2x+5)-(x+1) = x+4, so a = 1, b = 4 and a + b = 5."),

 dict(n="H2H-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A gang of w masons cuts b blocks in d days, every mason working at the same steady "
            "rate. At that rate, how many blocks would a gang of 2w masons cut in 3d days?"),
      choices=["\\(\\frac{2b}{3}\\)", "3b", "5b", "6b"], correct="D",
      check="Twice the masons for three times the days is six times the work, or 6b blocks."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The masses of the 9 dressed blocks in one load were recorded, and the median of the 9 "
            "masses was 84 kilograms. At most how many of those 9 masses could have been less than "
            "84 kilograms?"),
      choices=["3", "4", "5", "8"], correct="B",
      check="The median is the 5th of the 9 sorted masses, so at most the 4 below it can be smaller."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A tileworks charges for a delivery by a rule of the form \\(C=a+bn\\), where n is the "
            "number of crates delivered, C is the charge in dollars, and a and b are constants. The "
            "table gives what four deliveries were charged, and exactly one of them was not charged "
            "by that rule. Which delivery was not?"
            + table(["Crates delivered", "Charge ($)"],
                    [["4", "86"], ["7", "137"], ["10", "188"], ["12", "220"]])),
      choices=["The delivery of 4 crates", "The delivery of 7 crates",
               "The delivery of 10 crates", "The delivery of 12 crates"], correct="D",
      check="The first three sit on C = 18 + 17n, which gives 222 for 12 crates, not 220."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("In a mason's yard the ratio of dressed stones to rough stones is 3 to 5. After 40 more "
            "dressed stones are brought into the yard, and no rough stones are brought in or taken "
            "away, that ratio becomes 5 to 7. How many stones were in the yard before the 40 were "
            "brought in?"),
      choices=["280", "420", "560", "640"], correct="C",
      check="(3k+40)/(5k) = 5/7 gives k = 70, so the yard held 3(70) + 5(70) = 560."),

 dict(n="H2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A stone column is a right circular cylinder 3.6 metres tall whose base is 0.8 metres "
            "across. Its curved surface, but neither of its flat ends, is to be tooled. How many "
            "square metres of surface is that?"),
      choices=["\\(1.44\\pi\\)", "\\(2.88\\pi\\)", "\\(5.76\\pi\\)", "\\(11.52\\pi\\)"],
      correct="B",
      check="The curved surface is 2 pi r h with r = 0.4 and h = 3.6, which is 2.88 pi."),

 dict(n="H2H-18", domain="GT", skill="GT-LA", type="MC",
      stem=("A two-centred head for a tracery light is struck with two circular arcs, each of radius "
            "equal to the span and each centred on one of the two springing points, so that the two "
            "arcs meet at the apex. The span is 2.4 metres. What is the height of the apex above "
            "the line joining the two springing points, in metres?"),
      choices=["\\(1.2\\sqrt{2}\\)", "\\(1.2\\sqrt{3}\\)", "\\(2.4\\sqrt{2}\\)",
               "\\(2.4\\sqrt{3}\\)"], correct="B",
      check="The two springings and the apex form an equilateral triangle of side 2.4, whose height is 1.2 sqrt(3)."),

 dict(n="H2H-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A raking shore is propped against a wall so that it rises 1 metre for every 4 metres it "
            "runs out from the foot of the wall. What is the sine of the angle the shore makes with "
            "the level ground?"),
      choices=["\\(\\frac{1}{4}\\)", "\\(\\frac{4}{17}\\)", "\\(\\frac{\\sqrt{17}}{17}\\)",
               "\\(\\frac{4\\sqrt{17}}{17}\\)"], correct="C",
      check="The shore is the hypotenuse of a 1 by 4 right triangle, of length sqrt(17), so the sine is 1/sqrt(17)."),

 dict(n="H2H-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A set of 12 measurements taken at a tileworks has a mean of 25. Every measurement in "
            "the set is then increased by 4, and each result is doubled. What is the mean of the 12 "
            "numbers that result?"),
      answers=["58"],
      check="Adding 4 takes the mean to 29, and doubling takes it to 58."),

 dict(n="H2H-21", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A mason's rule sets the number x of stones in a course so that "
            "\\(\\frac{3}{x-2}=\\frac{5}{x+6}\\). What is the value of x ?"),
      answers=["14"],
      check="Cross-multiplying gives 3x + 18 = 5x - 10, so 2x = 28 and x = 14."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A stone corbel is cut from a rectangular block 45 centimetres long, 22 centimetres wide "
            "and 18 centimetres deep. A rectangular notch running the whole 45-centimetre length, 8 "
            "centimetres wide and 6 centimetres deep, is cut out of one edge. What is the volume of "
            "the finished corbel, in cubic centimetres?"),
      answers=["15660"],
      check="45(22)(18) = 17,820, the notch is 45(8)(6) = 2,160, and 17,820 - 2,160 = 15,660."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
