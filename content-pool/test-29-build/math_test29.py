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
      stem=("A plasterer gauges a coarse mix from lime putty and sand in the proportion of 1 barrow "
            "of putty to every 3 barrows of sand. A ceiling took 96 barrows of the gauged mix "
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
      stem=("During the early part of a firing the temperature inside a brick kiln rises as a linear "
            "function of the number of hours since the fires were lit. The temperature was "
            "520&deg;C after 4 hours and 1,020&deg;C after 9 hours. After how many hours does that "
            "model give a temperature of 1,220&deg;C?"),
      choices=["10", "11", "12", "13"], correct="B",
      check="500 degrees over 5 hours is 100 an hour, so the model is 100h + 120 and 1,220 gives h = 11."),

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
            "both of those conditions?"),
      choices=["4", "5", "6", "8"], correct="B",
      check="800b lies between 30,000 and 34,000 for b from 37.5 to 42.5, so b is 38, 39, 40, 41 or 42."),

 dict(n="H1-07", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("At a brickyard the cost of firing n thousand bricks is \\(0.5n^{2}+13n\\) dollars, and "
            "the money taken for them is \\(0.5n^{2}+31n-54\\) dollars. Which expression gives the "
            "brickyard's profit, in dollars, on n thousand bricks?"),
      choices=["18n-54", "18n+54", "\\(n^{2}+18n-54\\)", "44n-54"], correct="A",
      check="Subtracting the cost from the money taken cancels the squared terms and leaves 18n - 54."),

 dict(n="H1-08", domain="ADV", skill="ADV-NE", type="MC",
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
      stem=("The waste from a kiln is modelled by the function g, where \\(g(x)=a(x-3)(x+7)\\) and a "
            "is a constant. If \\(g(1)=-48\\), what is the value of \\(g(0)\\) ?"),
      choices=["-63", "-21", "21", "63"], correct="A",
      check="g(1) = a(-2)(8) = -16a = -48 gives a = 3, and g(0) = 3(-3)(7) = -63."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A plasterer works out the volume of finishing coat for a wall from "
            "\\(V=\\frac{Lht}{1000}\\), where V is in cubic metres, L and h are the length and "
            "height of the wall in metres, and t is the thickness of the coat in millimetres. Which "
            "expression gives t in terms of the other quantities?"),
      choices=["\\(\\frac{1000V}{Lh}\\)", "\\(\\frac{Lh}{1000V}\\)", "\\(\\frac{V}{1000Lh}\\)",
               "\\(\\frac{VLh}{1000}\\)"], correct="A",
      check="Multiplying by 1,000 and dividing by Lh gives t = 1000V/(Lh)."),

 dict(n="H1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The fuel bill for a kiln firing that runs for t hours is \\(0.4t^{2}-16t+800\\) dollars. "
            "For what number of hours is that fuel bill least?"),
      choices=["10", "16", "20", "25"], correct="C",
      check="The least value of a quadratic with a positive leading coefficient is at t = 16/(2(0.4)) = 20."),

 dict(n="H1-13", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Six moulders working an 8-hour day moulded 2,400 green bricks. Working at that same "
            "rate for each moulder, how many green bricks would nine moulders mould in a 10-hour "
            "day?"),
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
      check="The sound bricks are 31,280, 29,400, 30,600 and 30,400, so Ashcombe is greatest."),

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
      stem=("A firing began with 8 tonnes of coal at the kiln, burned at a steady rate. After 30 "
            "hours of firing, 5.6 tonnes were left. The firing must be stopped while 1.6 tonnes are "
            "still in reserve. For how many hours in total can the firing run?"),
      answers=["80"],
      check="2.4 tonnes in 30 hours is 0.08 an hour, and 6.4/0.08 = 80 hours."),

 dict(n="H1-21", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("At a brickyard the day gang moulded a mean of 1,860 green bricks a day over 6 days, and "
            "the night gang moulded a mean of 1,410 a day over 4 days. What is the mean number of "
            "green bricks moulded a day over all 10 of those days?"),
      answers=["1680"],
      check="6(1,860) + 4(1,410) = 11,160 + 5,640 = 16,800, and 16,800/10 = 1,680."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A brick flue shaft is a hollow square-section column 12 metres high. Its outside "
            "cross-section is a square of side 1.3 metres and the flue running up the middle of it "
            "is a square of side 0.9 metres, both of them the whole height of the shaft. How many "
            "cubic metres of brickwork does the shaft contain?"),
      answers=["10.56"],
      check="(1.3^2 - 0.9^2)(12) = (1.69 - 0.81)(12) = 0.88(12) = 10.56."),
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
      stem=("A scaffold tower built n lifts high has a total mass, in kilograms, of 46n + 120. Which "
            "of the following is the best interpretation of the number 120 in this context?"),
      choices=["Each lift adds 120 kilograms to the mass of the tower.",
               "A tower 120 lifts high has a mass of 46 kilograms.",
               "A tower with no lifts erected has a mass of 120 kilograms.",
               "The mass of the tower rises by 120 kilograms for every 46 lifts."],
      correct="C",
      check="Setting n = 0 leaves 120 kilograms, which is the tower before any lift is erected."),

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
      stem=("On a drawing of a tracery window, 3 centimetres represents 2 metres. A mullion drawn 12 "
            "centimetres long represents an actual length of how many metres?"),
      choices=["4", "6", "8", "18"], correct="C",
      check="12/3 = 4 lots of 3 centimetres, and 4(2) = 8 metres."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A hoist may raise a total load of at most 400 kilograms, and the cradle it lifts has a "
            "mass of 55 kilograms. Which inequality gives the possible total mass t, in kilograms, "
            "of the tiles placed in the cradle?"),
      choices=["\\(t\\le 345\\)", "\\(t\\ge 345\\)", "\\(t\\le 455\\)", "\\(t\\ge 455\\)"],
      correct="A",
      check="The tiles and the cradle together must not exceed 400, so t is at most 400 - 55 = 345."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A scaffolder's charge for a job, in dollars, is 3(2x + 7) - 4x, where x is the number "
            "of lifts erected. Which expression is equivalent to that charge?"),
      choices=["2x+21", "2x+7", "6x+21", "10x+21"], correct="A",
      check="6x + 21 - 4x = 2x + 21."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("At a tileworks the number of sound tiles left after sorting is 7x - 2(x - 4), where x "
            "is the number of racks sorted. That number equals ax + 8 for every value of x, where a "
            "is a constant. What is the value of a ?"),
      choices=["3", "5", "7", "9"], correct="B",
      check="7x - 2x + 8 = 5x + 8, so a = 5."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("At a tileworks the mass, in kilograms, of a stack of x quarry tiles is given by "
            "\\(m(x)=2.4x+5\\). What is the mass, in kilograms, of a stack of 15 quarry tiles?"),
      choices=["36", "38", "41", "45"], correct="C",
      check="2.4(15) + 5 = 36 + 5 = 41."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A pallet of tiles is built up in layers, and after x layers it holds \\(6(2)^{x}\\) "
            "tiles. If the pallet holds 96 tiles, how many layers have been laid?"),
      choices=["3", "4", "5", "16"], correct="B",
      check="6(2)^x = 96 gives 2^x = 16, so x = 4."),

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
      stem=("At a tileworks the number of crates needed to pack x tiles is given by "
            "\\(c(x)=\\frac{x}{24}\\). How many crates are needed to pack 288 tiles?"),
      choices=["12", "24", "264", "312"], correct="A",
      check="288/24 = 12."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("At a tileworks, 3 of every 8 tiles made are pantiles. In a batch of 240 tiles, how many "
            "are pantiles?"),
      choices=["90", "96", "120", "150"], correct="A",
      check="Three eighths of 240 is 90."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of tiles drawn from the presses at four tileworks in one "
            "week. According to the table, how many tiles altogether were drawn that week?"
            + table(["Tileworks", "Tiles drawn"],
                    [["Kelby", "4,200"], ["Marlow", "5,600"], ["Penhale", "3,900"],
                     ["Rowan", "4,800"]])),
      choices=["14,600", "17,900", "18,500", "19,400"], correct="C",
      check="4,200 + 5,600 + 3,900 + 4,800 = 18,500."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("On a pallet the ratio of plain tiles to ridge tiles is 7 to 2. If the pallet holds 63 "
            "plain tiles, how many ridge tiles does it hold?"),
      choices=["14", "18", "22", "28"], correct="B",
      check="63/7 = 9 lots of the ratio, and 9(2) = 18 ridge tiles."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Of the 340 tiles carried up a scaffold in one morning, 15 per cent were broken. How "
            "many of those tiles were broken?"),
      choices=["34", "44", "48", "51"], correct="D",
      check="0.15(340) = 51."),

 dict(n="H2E-18", domain="GT", skill="GT-AV", type="MC",
      stem=("A hoist rope is wound on a drum whose radius is 25 centimetres. How far, in "
            "centimetres, does the load rise during one complete turn of the drum?"),
      choices=["\\(25\\pi\\)", "\\(35\\pi\\)", "\\(50\\pi\\)", "\\(625\\pi\\)"], correct="C",
      check="One turn winds on the circumference, 2 pi (25) = 50 pi."),

 dict(n="H2E-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A scaffold standard rises vertically 9 metres from the ground, and a ledger runs "
            "horizontally 12 metres from the foot of that standard. A brace is fixed from the top of "
            "the standard to the far end of the ledger. What is the tangent of the angle the brace "
            "makes with the standard?"),
      choices=["\\(\\frac{3}{4}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{4}{5}\\)",
               "\\(\\frac{4}{3}\\)"], correct="D",
      check="At the top of the standard the opposite side is the 12-metre ledger and the adjacent side the 9-metre standard, so the tangent is 12/9 = 4/3."),

 dict(n="H2E-20", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("Five loads of stone brought to a mason's yard had masses of 340, 380, 300, 360 and 420 "
            "kilograms. What is the mean mass, in kilograms, of a load?"),
      answers=["360"],
      check="The five masses total 1,800, and 1,800/5 = 360."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("The inside of a stone cistern is a rectangular box 1.2 metres long, 0.5 metres wide and "
            "0.4 metres deep. Given that 1 cubic metre is 1,000 litres, how many litres does the "
            "cistern hold when it is full?"),
      answers=["240"],
      check="1.2(0.5)(0.4) = 0.24 cubic metres, and 0.24(1,000) = 240 litres."),

 dict(n="H2E-22", domain="GT", skill="GT-LA", type="FR",
      stem=("A mason checks whether the corner of a stone plinth is square by measuring 60 "
            "centimetres from the corner along one edge and 80 centimetres from the corner along "
            "the other. If the corner is exactly square, how many centimetres apart are the two "
            "marks?"),
      answers=["100"],
      check="sqrt(60^2 + 80^2) = sqrt(10,000) = 100."),
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
      stem=("The function f gives the height, in centimetres, of a scaffold platform after x lifts "
            "have been erected, and \\(f(x)=2x+7\\). A second function g is defined by "
            "\\(g(x)=f(x-3)\\). Which expression defines g ?"),
      choices=["2x-3", "2x+1", "2x+4", "2x+13"], correct="B",
      check="f(x-3) = 2(x-3) + 7 = 2x - 6 + 7 = 2x + 1."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The time a winch takes to raise a stone varies inversely as the square of the gear "
            "ratio set on it. At a gear ratio of 3 the winch takes 40 seconds to raise a "
            "particular stone. How many seconds does it take to raise that same stone at a gear "
            "ratio of 6 ?"),
      choices=["10", "20", "80", "160"], correct="A",
      check="Time times the square of the ratio is constant at 40(9) = 360, and 360/36 = 10 seconds."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A winch working alone raises a stone to the top of a tower in u minutes, and a second "
            "winch working alone raises the same stone in v minutes. Working together at those "
            "rates, the two winches raise the stone in how many minutes?"),
      choices=["\\(\\frac{uv}{u+v}\\)", "\\(\\frac{u+v}{uv}\\)", "\\(\\frac{u+v}{2}\\)",
               "\\(\\frac{2}{u+v}\\)"], correct="A",
      check="The combined rate is 1/u + 1/v = (u+v)/(uv), and the time is its reciprocal."),

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
      check="The rejection rates are 4.8, 5, 5.625 and 5 per cent, so Corve is the greatest."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The number of tiles a press turned out in a week fell by 12 per cent from one week to "
            "the next, and then rose by 25 per cent in the week after that, ending at 3,300 tiles. "
            "How many tiles did the press turn out in the first of those three weeks?"),
      choices=["2,904", "3,000", "3,300", "3,750"], correct="B",
      check="0.88(1.25) = 1.10, and 3,300/1.10 = 3,000."),

 dict(n="H2H-17", domain="GT", skill="GT-AV", type="MC",
      stem=("A stone finial is made of a cube of edge 30 centimetres with a right pyramid set "
            "squarely on its top face. The pyramid's base is that whole top face and its apex "
            "stands 40 centimetres above it. What is the total volume of the finial, in cubic "
            "centimetres?"),
      choices=["21,000", "27,000", "36,000", "39,000"], correct="D",
      check="27,000 for the cube plus (1/3)(900)(40) = 12,000 for the pyramid gives 39,000."),

 dict(n="H2H-18", domain="GT", skill="GT-LA", type="MC",
      stem=("A two-centred head for a tracery light is struck with two circular arcs, each of radius "
            "equal to the span and each centred on one of the two springing points, so that the two "
            "arcs meet at the apex. The span is 2.4 metres. What is the height of the apex above "
            "the line joining the two springing points, in metres?"),
      choices=["\\(1.2\\sqrt{2}\\)", "\\(1.2\\sqrt{3}\\)", "\\(2.4\\sqrt{2}\\)",
               "\\(2.4\\sqrt{3}\\)"], correct="B",
      check="The two springings and the apex form an equilateral triangle of side 2.4, whose height is 1.2 sqrt(3)."),

 dict(n="H2H-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A hoist gantry has a horizontal jib 5.2 metres long. A straight tie runs from the outer "
            "end of the jib to a point on the vertical mast above the root of the jib, and the tie "
            "makes an angle with the jib whose cosine is \\(\\frac{13}{15}\\). What is the length of "
            "the tie, in metres?"),
      choices=["4.5", "5.2", "5.8", "6"], correct="D",
      check="The jib is the adjacent side, so 5.2/L = 13/15 and L = 5.2(15)/13 = 6."),

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
