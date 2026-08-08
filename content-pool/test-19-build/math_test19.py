#!/usr/bin/env python3
"""
Original Math content for Test 19 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium and deliberately hard. Nearly every item makes a
                constant, a rate, a unit price or an unknown be recovered
                first and only then used — two or three steps throughout.
                Clearly harder than Module 2 (Easy), clearly below Module 2
                (Hard).
  MODULE_2_EASY genuinely one-step — one operation, no recovery step. This is
                the lower branch of the adaptive split.
  MODULE_2_HARD hard: parameters instead of numbers, structural and symbolic
                answer choices, a composed function, a system conditioned on
                constants, inequality chains, an absolute-value equation, and
                geometry that chains two relationships together.

Every setting sits inside Test 19's assigned thematic territory — peat cutting
and turbary, tanning and leatherwork, windmill and watermill grinding,
charcoal burning, basket making and osier beds, thatching, lime burning, eel
traps and fish weirs, fen drainage and pumping, saltmarsh grazing, withy beds,
sluice gates, reed cutting and hurdle making.

The settings are split so that no setting appears in both Module 1 and either
Module 2 branch: a student sees Module 1 plus one Module 2 branch, and the
same peat bank turning up twice in one sitting reads as a repeat even when the
mathematics is different.

  Module 1 only        peat/turbary, tanning, charcoal burning, thatching,
                       eel traps and weirs, saltmarsh grazing, sluice gates
  Module 2 branches    windmill/watermill grinding, basket making and osier
                       beds, lime burning, fen drainage and pumping, withy
                       beds, reed cutting, hurdle making

House style follows Test 1/2 (see CLAUDE.md): stems are bare HTML, simple
inline math stays plain text, data tables are real <table> markup, and all
LaTeX is typed by hand. No bulk conversion step was used anywhere in this
file.
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
      stem=("A peat cutter worked the first 3 hours of the day at 240 turves an hour and then, as "
            "the bank grew wetter, at 180 turves an hour for the rest of the day. By the end of the "
            "day 1,440 turves had been cut. For how many hours did the cutter work altogether?"),
      choices=["4", "6", "7", "8"], correct="C",
      check="The first 3 hours yield 720 turves, so 180h = 720 more takes h = 4 further hours, and "
            "3 + 4 = 7 hours in all."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In a charcoal burner's stack the rings of billets are counted upward from the ground, "
            "and the number of billets falls by the same amount from each ring to the next. The "
            "third ring holds 70 billets and the eighth ring holds 40 billets. How many billets "
            "does the twelfth ring hold?"),
      choices=["10", "16", "22", "28"], correct="B",
      check="The fall per ring is (40-70)/(8-3) = -6 billets, so the twelfth ring holds "
            "70 - 6(12-3) = 16."),

 dict(n="H1-03", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tannery buys shredded oak bark by the sack. One merchant charges a delivery fee of "
            "$65 and then $18 for each sack; a second merchant charges no delivery fee but $23 for "
            "each sack. For one particular order the two merchants would charge exactly the same "
            "amount. What is that amount?"),
      choices=["$234", "$260", "$286", "$299"], correct="D",
      check="65 + 18s = 23s gives s = 13 sacks, and 13($23) = $299."),

 dict(n="H1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A grazier holds a licence for a saltmarsh of 46 hectares which permits at most 2.5 "
            "ewes per hectare, and under the licence each lamb counts as half a ewe. The grazier "
            "already runs 74 ewes on the marsh. What is the greatest number of lambs the grazier "
            "may add without breaking the licence?"),
      choices=["74", "78", "82", "86"], correct="C",
      check="The licence allows 46(2.5) = 115 ewes, and 74 + 0.5L <= 115 gives L <= 82."),

 dict(n="H1-05", domain="ALG", skill="ALG-LE", type="FR",
      stem=("An eel fisher sets 56 traps in all, spread over the upper, middle and lower reaches of "
            "a river. The middle reach holds 3 times as many traps as the upper reach, and the "
            "lower reach holds 6 more traps than the upper reach. How many traps are set in the "
            "lower reach?"),
      answers=["16"],
      check="With u traps in the upper reach, u + 3u + (u+6) = 56 gives u = 10, so the lower reach "
            "holds 16."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A tannery bought 40 sacks of coarse bark at $12 a sack and a number of sacks of fine "
            "bark at $20 a sack. Taking every sack bought together, the average cost worked out at "
            "$15 a sack. How many sacks of fine bark did the tannery buy?"),
      choices=["20", "24", "28", "30"], correct="B",
      check="40(12) + 20f = 15(40+f) gives 5f = 120 and f = 24."),

 dict(n="H1-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The discharge through a sluice gate is a linear function of the head of water standing "
            "behind it. The table gives two readings taken by the keeper."
            + table(["Head of water (metres)", "Discharge (cubic metres per second)"],
                    [["0.5", "3.4"], ["2.0", "7.0"]])
            + "What head of water, in metres, does this relationship give for a discharge of 10.6 "
              "cubic metres per second?"),
      choices=["3.0", "3.5", "4.4", "4.8"], correct="B",
      check="The rate is (7.0-3.4)/(2.0-0.5) = 2.4 and the discharge at zero head is "
            "3.4 - 0.5(2.4) = 2.2, so 2.4H + 2.2 = 10.6 gives H = 3.5."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A charcoal burner models the mass of charcoal lost to the flue, in kilograms, as "
            "\\(L(x)=2x^{2}-20x+63\\), where x is the number of hours the stack has been alight. "
            "Which expression is equivalent to \\(L(x)\\) and shows the least possible loss as a "
            "constant?"),
      choices=["\\(2(x-5)^{2}+13\\)", "\\(2(x-5)^{2}-13\\)", "\\(2(x-10)^{2}+13\\)",
               "\\(2(x-5)^{2}+63\\)"], correct="A",
      check="Taking 2 out of the first two terms gives 2(x-5)^2 - 50 + 63, which is 2(x-5)^2 + 13."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of elvers passing an eel weir in a week is modelled by "
            "\\(N(w)=N_{0}b^{w}\\), where w is the number of the week and \\(N_{0}\\) and b are "
            "constants. The model gives 180 elvers in week 2 and 1,440 elvers in week 5. How many "
            "elvers does the model give for week 4?"),
      choices=["360", "540", "720", "960"], correct="C",
      check="Three weeks multiply the count by 1,440/180 = 8, so b = 2, and week 4 is 1,440/2 = "
            "720."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The floor of a sluice channel is modelled in the xy-plane by the curve "
            "\\(y=x^{2}-8x+20\\), and the surface of the water is modelled by the line y=5. The "
            "line meets the curve at two points. What is the distance between those two points?"),
      choices=["2", "3", "4", "5"], correct="A",
      check="x^2 - 8x + 20 = 5 gives x = 3 and x = 5, and the two points share the same y, so they "
            "are 2 apart."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A tannery's drum controller turns a dial reading x into a drum speed "
            "\\(f(x)=\\frac{2x+k}{x-3}\\), where k is a constant and \\(x>3\\). A dial reading of 5 "
            "gives a speed of 7. What speed does a dial reading of 4 give?"),
      choices=["8", "10", "12", "14"], correct="C",
      check="(10+k)/2 = 7 gives k = 4, so f(4) = (8+4)/(4-3) = 12."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A tannery's cutting plan gives the area of a hide panel, in square decimetres, as "
            "\\((3x+m)(2x-5)\\), where m is a constant. The same area is also given by "
            "\\(6x^{2}-9x-15\\) for every value of x. What is the value of m?"),
      choices=["3", "5", "9", "15"], correct="A",
      check="Expanding gives 6x^2 + (2m-15)x - 5m, so 2m - 15 = -9 and -5m = -15 both give m = 3."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A gauge fitted at an eel weir gives readings x that satisfy "
            "\\(x^{4}-13x^{2}+36=0\\). What is the greatest value of x that satisfies this "
            "equation?"),
      choices=["2", "2.5", "3", "6"], correct="C",
      check="Treating x^2 as the unknown gives x^2 = 4 or x^2 = 9, so the four readings are -3, -2, "
            "2 and 3."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A freshly cut turf weighs 5 kilograms and loses 64% of its mass while it dries on the "
            "bank. A cart carries 400 dried turves. What is the mass, in kilograms, of the cart's "
            "load?"),
      choices=["500", "640", "700", "720"], correct="D",
      check="A dried turf keeps 36% of 5 kilograms, which is 1.8 kilograms, and 400(1.8) = 720."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A thatcher needs 9 bundles of straw for every 2 square metres of roof, and straw is "
            "delivered in loads of 120 bundles. A roof measures 14 metres by 6 metres. What is the "
            "least number of loads the thatcher must order to cover the roof?"),
      choices=["3", "4", "5", "7"], correct="B",
      check="The roof is 84 square metres, which needs 84(9)/2 = 378 bundles, and 378/120 = 3.15, "
            "so 4 loads."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of turves cut and the hours worked by each of four gangs on "
            "one peat moor."
            + table(["Gang", "Turves cut", "Hours worked"],
                    [["Turf gang", "2,760", "6"], ["Moor gang", "3,150", "7"],
                     ["Hill gang", "2,000", "5"], ["Bank gang", "3,840", "8"]])
            + "How many more turves per hour did the fastest gang cut than the slowest gang?"),
      choices=["20", "40", "60", "80"], correct="D",
      check="The four rates are 460, 450, 400 and 480 turves per hour, and 480 - 400 = 80."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A tanner recorded the masses of 12 hides and found their mean to be 25 kilograms. One "
            "hide had been entered as 18 kilograms when its true mass was 42 kilograms. Using the "
            "corrected figure, what is the mean mass, in kilograms, of the 12 hides?"),
      answers=["27"],
      check="The recorded total was 12(25) = 300, the corrected total is 300 - 18 + 42 = 324, and "
            "324/12 = 27."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the result of one night's fishing, in which every trap set was "
            "recorded as either holding eels or empty."
            + table(["Reach", "Held eels", "Empty"],
                    [["Upper", "45", "15"], ["Lower", "75", "65"]])
            + "One of the traps that held eels is picked at random. What is the probability that it "
              "was set in the lower reach?"),
      choices=["\\(\\frac{3}{8}\\)", "\\(\\frac{5}{8}\\)", "\\(\\frac{5}{12}\\)",
               "\\(\\frac{15}{28}\\)"], correct="B",
      check="45 + 75 = 120 traps held eels and 75 of them were in the lower reach, so the "
            "probability is 75/120 = 5/8."),

 dict(n="H1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("On a surveyor's plan of a saltmarsh, a fence runs straight from the point (2, -3) to "
            "the point (14, 13), and one unit on the plan stands for one metre. A gate post stands "
            "at the midpoint of the fence. How many metres of fence run from the point (2, -3) to "
            "the gate post?"),
      choices=["10", "13", "14", "20"], correct="A",
      check="The fence is the square root of 12^2 + 16^2, which is 20 metres, and the post is half "
            "way along it."),

 dict(n="H1-20", domain="GT", skill="GT-AV", type="MC",
      stem=("The concrete apron below a sluice gate is a rectangle 18 metres long and 7 metres "
            "wide. A rectangular opening 12 metres long and 2.5 metres wide is left in the middle "
            "of it for the channel, and the rest of the apron is paved. How many square metres of "
            "the apron are paved?"),
      choices=["60", "66", "84", "96"], correct="D",
      check="The apron covers 18(7) = 126 square metres and the opening takes 12(2.5) = 30 of "
            "them, leaving 96."),

 dict(n="H1-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A stop plank rests against the vertical face of a sluice weir, with its lower end on "
            "the level floor of the channel. The plank is 12 metres long and makes an angle of "
            "60&deg; with the face of the weir. How many metres up the face of the weir does the "
            "top of the plank reach?"),
      choices=["6", "\\(6\\sqrt{3}\\)", "9", "12"], correct="A",
      check="The face of the weir is the side adjacent to the 60 degree angle, so the reach is "
            "12 cos 60, which is 6 metres."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A charcoal burner covers a circular floor of radius 3 metres with a mound of earth in "
            "the shape of a hemisphere. The volume of the mound is \\(k\\pi\\) cubic metres. What "
            "is the value of k?"),
      answers=["18"],
      check="A hemisphere of radius 3 has volume (2/3) times pi times 27, which is 18 pi."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A fen pumping engine lifts 24 cubic metres of water each minute. At that rate, how "
            "many cubic metres does the engine lift in 7 minutes?"),
      choices=["144", "156", "168", "192"], correct="C",
      check="24(7) = 168."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A hurdle maker charges 14h dollars for an order of h hurdles. One order came to $322. "
            "How many hurdles were in that order?"),
      choices=["21", "23", "26", "28"], correct="B",
      check="322/14 = 23."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A withy bed carried 1,400 usable rods after 2 years and 3,000 usable rods after 6 "
            "years, and the stock grew by the same number of rods each year. By how many rods did "
            "the stock grow each year?"),
      choices=["250", "320", "350", "400"], correct="D",
      check="(3,000-1,400)/(6-2) = 400."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A reed cutter has already cut 130 bundles and now cuts 24 more bundles each day. Which "
            "expression gives the total number of bundles cut d days from now?"),
      choices=["\\(24d+130\\)", "\\(130d+24\\)", "\\(154d\\)", "\\(130-24d\\)"], correct="A",
      check="Add 24 bundles for each of the d days to the 130 already cut."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A lime kiln must never be charged with more than 2,400 kilograms of limestone. Which "
            "inequality gives all the possible masses m, in kilograms, of a charge?"),
      choices=["\\(m<2{,}400\\)", "\\(m\\le 2{,}400\\)", "\\(m\\ge 2{,}400\\)",
               "\\(m>2{,}400\\)"], correct="B",
      check="No more than 2,400 allows 2,400 itself and anything below it."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A miller's day tally gives the system<br/>a+b=40<br/>a-b=6<br/>where a and b are the "
            "numbers of sacks of two grains ground that day. What is the value of a?"),
      answers=["23"],
      check="Adding the two equations gives 2a = 46, so a = 23."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A basket maker works out the charge for an order as C=9n+24, where C is the charge in "
            "dollars and n is the number of baskets in the order. What does 24 represent in this "
            "model?"),
      choices=["The charge, in dollars, made for each basket in the order.",
               "A fixed charge, in dollars, made once on every order whatever its size.",
               "The number of baskets that can be had for $9.",
               "The greatest charge, in dollars, that can be made for one order."],
      correct="B",
      check="24 does not change with n, so it is charged once for the order however many baskets "
            "it holds."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A basket maker uses \\(4x+15\\) rods for the base of a basket and \\(6x-7\\) rods for "
            "its sides. Which expression gives the total number of rods used for the basket?"),
      choices=["\\(10x+8\\)", "\\(10x+22\\)", "\\(10x-8\\)", "\\(24x-105\\)"], correct="A",
      check="(4x+15) + (6x-7) = 10x + 8."),

 dict(n="H2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A reed cutter models the number of bundles cut on day n as \\(P(n)=n^{2}+4n\\). How "
            "many bundles does the model give for day 6?"),
      choices=["40", "52", "60", "72"], correct="C",
      check="6^2 + 4(6) = 36 + 24 = 60."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A hurdle maker's cutting rule leads to the equation \\(x^{2}+5x-24=0\\), which has two "
            "solutions. What is the greater of the two solutions?"),
      choices=["-24", "-8", "-3", "3"], correct="D",
      check="The equation factors as (x+8)(x-3) = 0, so the solutions are -8 and 3."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A lime kiln's draught is rated by \\(R(t)=\\frac{48}{t}+5\\), where t is the number of "
            "hours since the kiln was lit. What is the rating 6 hours after lighting?"),
      choices=["11", "13", "15", "53"], correct="B",
      check="48/6 + 5 = 8 + 5 = 13."),

 dict(n="H2E-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A millwright's gearing calculation uses the product \\((3x^{4})(5x^{3})\\). Which "
            "expression is equivalent to that product?"),
      choices=["\\(15x^{7}\\)", "\\(15x^{12}\\)", "\\(8x^{7}\\)", "\\(8x^{12}\\)"], correct="A",
      check="Multiply 3 by 5 and add the exponents 4 and 3."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The mass of water left in a stack of drying reed is modelled by "
            "\\(M(h)=640\\left(\\frac{1}{2}\\right)^{h}\\) kilograms, where h is the number of days "
            "of drying. What mass does the model give after 3 days?"),
      choices=["20", "40", "64", "80"], correct="D",
      check="640 halved three times is 320, then 160, then 80."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("An osier bed yielded 450 rods, and 18% of them were rejected as too brittle. How many "
            "rods were rejected?"),
      choices=["45", "72", "81", "90"], correct="C",
      check="0.18(450) = 81."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A watermill grinds 3 sacks of flour from every 8 bushels of wheat. At that rate, how "
            "many sacks of flour does it grind from 96 bushels of wheat?"),
      answers=["36"],
      check="96/8 = 12 lots of 3 sacks, which is 36 sacks."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A workshop sorts the hurdles it makes into four grades, as the table records."
            + table(["Grade", "Hurdles"],
                    [["Fine", "46"], ["Standard", "58"], ["Coarse", "39"], ["Rough", "67"]])
            + "How many hurdles did the workshop sort altogether?"),
      choices=["190", "200", "210", "220"], correct="C",
      check="46 + 58 + 39 + 67 = 210."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("On seven days a fen pumping station logged 14, 9, 12, 20, 11, 9 and 17 hours of "
            "pumping. What is the median of the seven figures?"),
      choices=["9", "12", "13", "14"], correct="B",
      check="In order the figures are 9, 9, 11, 12, 14, 17, 20, and the fourth of seven is 12."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Of 40 hurdles offered for inspection, 24 passed. What fraction of the hurdles failed?"),
      choices=["\\(\\frac{2}{5}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{2}{3}\\)",
               "\\(\\frac{1}{4}\\)"], correct="A",
      check="40 - 24 = 16 failed, and 16/40 = 2/5."),

 dict(n="H2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("Three braces meet at one point in the middle of a hurdle, and the three angles they "
            "make around that point measure 145&deg;, 132&deg; and x&deg;. What is the value of x?"),
      choices=["53", "63", "73", "83"], correct="D",
      check="Angles round a point total 360 degrees, and 360 - 145 - 132 = 83."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="MC",
      stem=("A rectangular reed store covers 84 square metres of ground and is 12 metres long. How "
            "wide, in metres, is the store?"),
      choices=["6", "6.5", "7", "8"], correct="C",
      check="84/12 = 7."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A hurdle maker's yard gate is a semicircle whose straight edge is 8 metres long. The "
            "area of the gate is \\(k\\pi\\) square metres. What is the value of k?"),
      answers=["8"],
      check="The straight edge is the diameter, so the radius is 4, a whole circle of radius 4 has "
            "area 16 pi, and half of that is 8 pi."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("In a right triangle set out to square a lime kiln's flue, the side opposite angle A is "
            "7 metres long and the hypotenuse is 25 metres long. What is the value of "
            "\\(\\sin A\\)?"),
      choices=["\\(\\frac{7}{25}\\)", "\\(\\frac{24}{25}\\)", "\\(\\frac{7}{24}\\)",
               "\\(\\frac{25}{7}\\)"], correct="A",
      check="The sine of an angle is the opposite side over the hypotenuse, which is 7/25."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A fen drainage board's costing sheet gives the system<br/>px+4y=26<br/>3x-qy=1<br/>"
            "where p and q are constants. The solution of this system is x=2 and y=5. What is the "
            "value of p+q?"),
      choices=["3", "4", "5", "7"], correct="B",
      check="2p + 20 = 26 gives p = 3, and 6 - 5q = 1 gives q = 1, so p + q = 4."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A wind engine's daily output is a linear function g of the number of hours x that the "
            "sails turn. It is known that g(2)=7 and g(10)=31. For what value of x does this "
            "function give g(x)=100?"),
      choices=["25", "29", "31", "33"], correct="D",
      check="The rate is (31-7)/(10-2) = 3 and g(x) = 3x + 1, so 3x + 1 = 100 gives x = 33."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A lime kiln's charge x, in tonnes, must satisfy \\(3\\le\\frac{2x-5}{4}\\le 7\\). What "
            "is the greatest possible value of x?"),
      choices=["8.5", "12.5", "14.5", "16.5"], correct="D",
      check="Multiplying through by 4 gives 12 <= 2x-5 <= 28, so 8.5 <= x <= 16.5."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a watermill, grinding 4 sacks of wheat together with 3 sacks of barley takes 62 "
            "minutes, and grinding 6 sacks of wheat together with 5 sacks of barley takes 98 "
            "minutes. At the same rates, how many minutes does grinding 5 sacks of wheat together "
            "with 4 sacks of barley take?"),
      choices=["80", "84", "90", "98"], correct="A",
      check="The system gives 8 minutes a sack for wheat and 10 for barley, so 5(8) + 4(10) = 80."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The number of usable rods standing in a withy bed t years after planting is modelled "
            "by \\(S(t)=p-qt\\), where p and q are positive constants. In terms of p and q, after "
            "how many years does the model give half as many usable rods as at planting?"),
      choices=["\\(\\frac{2p}{q}\\)", "\\(\\frac{p}{q}\\)", "\\(\\frac{q}{2p}\\)",
               "\\(\\frac{p}{2q}\\)"], correct="D",
      check="At planting the stock is p, so p - qt = p/2 gives qt = p/2 and t = p/(2q)."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A basket maker has 26 hours of working time and must finish exactly 40 baskets in it. "
            "A round basket takes 20 minutes to weave and a square basket takes 45 minutes. What is "
            "the greatest number of square baskets the maker can finish within the working time?"),
      choices=["30", "32", "34", "39"], correct="A",
      check="26 hours is 1,560 minutes, and 20(40-s) + 45s <= 1,560 gives 25s <= 760, so s <= 30.4 "
            "and at most 30 square baskets."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("Setting the gearing of a windmill leads to the equation "
            "\\(\\frac{2x+7}{3}-\\frac{x-4}{2}=5\\). What is the value of x?"),
      answers=["4"],
      check="Multiplying through by 6 gives 2(2x+7) - 3(x-4) = 30, which is x + 26 = 30."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A millwright's two adjustments to a pair of stones are modelled by \\(f(x)=4x+1\\) and "
            "\\(g(x)=x^{2}-3x\\). Which expression is equivalent to \\(g(f(x))-f(g(x))\\)?"),
      choices=["\\(12x^{2}+8x-1\\)", "\\(12x^{2}+8x-3\\)", "\\(12x^{2}-8x-3\\)",
               "\\(20x^{2}-4x-1\\)"], correct="B",
      check="g(f(x)) is 16x^2 - 4x - 2 and f(g(x)) is 4x^2 - 12x + 1, and subtracting the second "
            "from the first leaves 12x^2 + 8x - 3."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("An osier grader's ratio is \\(\\frac{6x+19}{x+3}\\), where \\(x>0\\). This ratio can "
            "be written as \\(6+\\frac{k}{x+3}\\), where k is a constant. What is the value of k?"),
      choices=["-1", "0", "1", "3"], correct="C",
      check="6(x+3) is 6x+18, so the ratio is 6 plus a remainder of 1 over x+3."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A lime burner's charging rule reduces to the equation \\(9^{x+1}=27^{x-1}\\). What is "
            "the value of x?"),
      choices=["5", "6", "8", "11"], correct="A",
      check="Writing both sides as powers of 3 gives 2x+2 = 3x-3, so x = 5."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A lime kiln's fuel use is modelled by \\(f(x)=x^{2}+px+q\\), where p and q are "
            "constants and x is the number of hours since lighting. The model takes its least value "
            "when x=5, and it gives f(1)=9. What is the value of q?"),
      choices=["9", "14", "18", "25"], correct="C",
      check="The least value sits at x = -p/2, so p = -10, and 1 - 10 + q = 9 gives q = 18."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A hurdle maker's scaling rule uses the expression \\(2x^{3}+3x^{2}-8x-12\\). Which "
            "expression is equivalent to it?"),
      choices=["\\((x-2)^{2}(2x+3)\\)", "\\((x-3)(x+2)(2x+2)\\)", "\\((x^{2}+4)(2x-3)\\)",
               "\\((x-2)(x+2)(2x+3)\\)"], correct="D",
      check="Grouping gives x^2(2x+3) - 4(2x+3), which is (x^2-4)(2x+3), and x^2-4 factors "
            "further."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A tolerance condition on a mill's gearing gives the equation \\(|2x-7|=x+1\\). What is "
            "the sum of all the solutions of this equation?"),
      choices=["6", "8", "10", "16"], correct="C",
      check="2x-7 = x+1 gives 8 and 7-2x = x+1 gives 2; both make x+1 positive, so the sum is 10."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A gang of 6 reed cutters clears a bed in 15 days, every cutter working at the same "
            "steady rate. To clear a bed of the same size in 9 days, how many cutters must be added "
            "to the gang?"),
      choices=["4", "5", "6", "10"], correct="A",
      check="The work is 6(15) = 90 cutter-days, so 9 days needs 90/9 = 10 cutters, which is 4 more "
            "than the 6 already in the gang."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the result of inspecting every hurdle made at two workshops in one "
            "month."
            + table(["Workshop", "Passed", "Failed"],
                    [["Osier Green", "168", "32"], ["Sedge Fen", "108", "42"]])
            + "At the workshop with the greater proportion of hurdles failed, how many more hurdles "
              "failed than at the other workshop?"),
      choices=["8", "10", "12", "14"], correct="B",
      check="Osier Green failed 32 of 200, which is 16%, and Sedge Fen failed 42 of 150, which is "
            "28%, so the greater proportion is Sedge Fen and 42 - 32 = 10."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives, for each of four withy beds, the number of rods cut in one season and "
            "the percentage of those rods rejected as unusable."
            + table(["Bed", "Rods cut", "Rejected"],
                    [["Willow Ham", "4,200", "15%"], ["Long Drove", "3,800", "6%"],
                     ["North Rhyne", "4,500", "21%"], ["Sedge Bank", "4,000", "11%"]])
            + "Which bed yielded the greatest number of usable rods?"),
      choices=["Willow Ham", "Long Drove", "North Rhyne", "Sedge Bank"], correct="B",
      check="The usable counts are 3,570, 3,572, 3,555 and 3,560, so Long Drove yielded the most "
            "despite cutting the second fewest."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A crate holds 9 white osier rods and 6 brown osier rods. Two rods are taken from the "
            "crate at random, one after the other, and the first is not put back. What is the "
            "probability that both rods taken are brown?"),
      answers=["1/7"],
      check="The first rod is brown with probability 6 out of 15 and the second with probability 5 "
            "out of 14, and the product of those is 1/7."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A watermill keeps 1 sack in every 16 it grinds as its toll and returns the rest to the "
            "customers. In one week the mill kept 27 sacks as toll. How many sacks did the mill "
            "return to its customers that week?"),
      choices=["405", "416", "432", "459"], correct="A",
      check="27 sacks of toll means 27(16) = 432 sacks ground, of which 432 - 27 = 405 went back."),

 dict(n="H2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("Limestone standing in a lime kiln's cylindrical shaft to a depth of 4 metres fills "
            "\\(36\\pi\\) cubic metres of the shaft. The burner then tips in enough limestone to "
            "raise the level by a further 1.5 metres. How many cubic metres of limestone were "
            "tipped in?"),
      choices=["\\(9\\pi\\)", "\\(12\\pi\\)", "\\(13.5\\pi\\)", "\\(18\\pi\\)"], correct="C",
      check="4 pi r^2 = 36 pi gives r^2 = 9, so each extra metre of depth is 9 pi and 1.5 metres is "
            "13.5 pi."),

 dict(n="H2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A hurdle maker's diagonal brace makes a right triangle whose two shorter sides are in "
            "the ratio 3 to 4 and whose longest side is 45 centimetres. What is the area, in square "
            "centimetres, of that triangle?"),
      choices=["405", "486", "540", "648"], correct="B",
      check="The sides are 27, 36 and 45, and half of 27 times 36 is 486."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A millwright sets out a right triangle whose hypotenuse is 26 centimetres long and in "
            "which \\(\\sin A=\\frac{5}{13}\\), where A is one of the acute angles. What is the "
            "area, in square centimetres, of that triangle?"),
      choices=["60", "96", "120", "156"], correct="C",
      check="The side opposite A is 10 and the other leg is 24, so the area is half of 10 times 24, "
            "which is 120."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A lime kiln's charging ramp is a bank of earth 20 metres long whose cross-section is "
            "the same all the way along: a right triangle whose two legs are in the ratio 3 to 4, "
            "the shorter of them being 1.5 metres. How many cubic metres of earth are in the ramp?"),
      answers=["30"],
      check="The legs are 1.5 and 2.0 metres, so the cross-section is 1.5 square metres and the "
            "ramp holds 1.5(20) = 30 cubic metres."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
