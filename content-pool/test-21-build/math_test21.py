#!/usr/bin/env python3
"""
Original Math content for Test 21 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium, deliberately harder than a stock Module 1.
                Nearly every item makes a constant, a rate, a unit price or an
                unknown be recovered first and only then used; two or three
                steps throughout. Clearly harder than Module 2 (Easy) and
                clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
                One operation, no recovery step.
  MODULE_2_HARD hard. Parameters in place of numbers, structural and symbolic
                answer choices, a composed function, a system conditioned on a
                constant, an inequality chain resolved to an integer count, and
                geometry that chains two relationships.

Every setting is drawn from Test 21's assigned thematic territory. The
territory is split across modules so that no setting can reach a student
twice — a student sees Module 1 plus one Module 2 branch:

  Module 1        vineyards and grape harvesting, wheelwrighting and
                  cartwrighting, rain gauges and weather stations, tobacco
                  curing barns, harness making, hay ricks and balers, seed
                  cleaning and grading.
  Module 2 (both) silk rearing and reeling, spectacle grinding, observatory
                  domes and telescope mountings, photographic plates,
                  darkroom work and contact sheets, carriage springs.

House style follows Test 1/2 — see CLAUDE.md. All LaTeX is typed by hand; no
bulk conversion step was used anywhere in this file.
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
      stem=("In one week a picking crew worked its way along the rows of a vineyard, taking 3 more "
            "rows of Riesling vines than of Pinot vines and 47 rows in all. Each Riesling row gave "
            "210 kilograms of grapes and each Pinot row gave 260 kilograms. How many kilograms of "
            "grapes did the crew take that week?"),
      choices=["10,810", "10,970", "11,120", "11,280"], correct="B",
      check="47 rows split as 25 Riesling and 22 Pinot, so 25(210) + 22(260) = 10,970."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A rain gauge at a weather station was not emptied overnight. Rain then fell at a "
            "steady rate all morning: the gauge held 7 millimetres of water at 11 in the morning "
            "and 16 millimetres at 2 in the afternoon. Which equation gives the depth d, in "
            "millimetres, of water in the gauge h hours after 9 in the morning?"),
      choices=["d=3h+1", "d=3h+7", "d=3h-1", "d=h+5"], correct="A",
      check="9 millimetres over 3 hours is 3 an hour, and 7 at h=2 puts the starting depth at 1."),

 dict(n="H1-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A saddler's stitching horse will hold a strap no more than 210 centimetres long. Every "
            "strap is cut 18 centimetres longer than 4 times the length of the billet that will be "
            "sewn to it. What is the greatest possible length, in centimetres, of a billet whose "
            "strap the stitching horse will hold?"),
      choices=["36", "42", "45", "48"], correct="D",
      check="4b + 18 is at most 210, so 4b is at most 192 and b is at most 48."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A cartwright's yard holds 3 times as many cart wheels as dray wheels. After 24 cart "
            "wheels are sold and 6 dray wheels are bought, the yard holds twice as many cart wheels "
            "as dray wheels. How many dray wheels did the yard hold at the start?"),
      choices=["30", "33", "36", "42"], correct="C",
      check="3d - 24 = 2(d + 6) gives d = 36."),

 dict(n="H1-05", domain="ALG", skill="ALG-LF", type="FR",
      stem=("Bales were carried out of a mown field at a steady rate. Three hours after the loading "
            "began 264 bales were still in the field, and seven hours after it began 148 were still "
            "in the field. How many bales were in the field when the loading began?"),
      answers=["351"],
      check="116 bales went in 4 hours, so 29 an hour, and 264 + 3(29) = 351."),

 dict(n="H1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The air in a tobacco curing barn warms at a constant rate once the flues are lit. Two "
            "hours after lighting a thermometer in the barn read 46 degrees Celsius, and five hours "
            "after lighting it read 64 degrees Celsius. The leaf is taken down when the thermometer "
            "reads 100 degrees Celsius. How many hours after lighting is the leaf taken down?"),
      choices=["9", "10", "11", "12"], correct="C",
      check="18 degrees over 3 hours is 6 an hour, and 46 + 6(t - 2) = 100 gives t = 11."),

 dict(n="H1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A seed cleaner passes a batch only if it carries at most 4 grams of chaff for each "
            "kilogram of seed. A batch of 45 kilograms of seed carries 294 grams of chaff, and each "
            "further run through the cleaner takes out 36 grams of chaff. What is the least number "
            "of further runs that will bring the batch within the limit?"),
      choices=["1", "2", "3", "4"], correct="D",
      check="The limit is 45(4) = 180 grams, and 294 - 36r is at most 180 once r reaches 4."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A vineyard estimates the trellis wire needed for n rows, in metres, as "
            "\\((3n+4)^{2}-\\left(9n^{2}+7\\right)\\). Which expression is equivalent to this "
            "estimate?"),
      choices=["24n+9", "24n+23", "24n-9", "9n+9"], correct="A",
      check="(3n+4)^2 = 9n^2 + 24n + 16, and taking away 9n^2 + 7 leaves 24n + 9."),

 dict(n="H1-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The number of frost-free days in a year at a weather station is modelled by "
            "\\(F(a)=180-\\frac{a^{2}}{500}\\), where a is the station's height above sea level in "
            "metres and \\(0<a<300\\). At what height, in metres, does this model give 135 "
            "frost-free days?"),
      choices=["60", "90", "120", "150"], correct="D",
      check="a^2/500 = 45 gives a^2 = 22,500, so a = 150."),

 dict(n="H1-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The area of leaf on a young vine, in square centimetres, is modelled by "
            "\\(A(w)=24(1.5)^{w}\\), where w is the number of weeks since bud break. According to "
            "this model, by what percent does the leaf area grow over any two-week stretch?"),
      choices=["50%", "100%", "125%", "225%"], correct="C",
      check="Two weeks multiply the area by 1.5 squared, which is 2.25, a growth of 125 percent."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The volume of must a vineyard's press yields in one pressing varies directly with the "
            "square of the diameter of the press's ram. A press whose ram is 30 centimetres across "
            "yields 45 litres in a pressing. How many litres does a press whose ram is 40 "
            "centimetres across yield in a pressing?"),
      choices=["60", "72", "80", "90"], correct="C",
      check="45 = k(30)^2 gives k = 0.05, and 0.05(40)^2 = 80."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A wheelwright sets the dish of a wheel by the rule \\(D=\\frac{r(s-2)}{4}\\), where r "
            "is the rim radius, s is the number of spokes and D is the dish. Which expression gives "
            "s in terms of D and r?"),
      choices=["\\(\\frac{4D}{r}+2\\)", "\\(\\frac{4D+2}{r}\\)", "\\(\\frac{4D}{r}-2\\)",
               "\\(\\frac{D}{4r}+2\\)"], correct="A",
      check="4D = r(s-2), so s - 2 = 4D/r and s = 4D/r + 2."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The ripeness of a vineyard's grapes, measured in degrees Brix, is modelled by "
            "\\(S(d)=d^{2}-4d+15\\), where d counts the days after veraison and "
            "\\(0\\le d\\le 30\\). At what value of d does this model reach 75 degrees Brix?"),
      choices=["4", "6", "8", "10"], correct="D",
      check="d^2 - 4d - 60 = 0 factors as (d-10)(d+6), and only d = 10 lies in the range."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A vineyard pays its pickers $4 for each lug box filled, and a full lug box holds 9 "
            "kilograms of grapes. How many dollars is a picker paid for a day on which that picker "
            "brings in 738 kilograms of grapes?"),
      choices=["246", "328", "369", "410"], correct="B",
      check="738/9 = 82 lug boxes, and 82(4) = 328."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("After 12 percent of the leaf hung in a tobacco curing barn was thrown out as trash, "
            "2,024 kilograms were left. How many kilograms of leaf were hung in the barn?"),
      choices=["2,266", "2,300", "2,432", "2,530"], correct="B",
      check="2,024 is 88 percent of the leaf hung, and 2,024/0.88 = 2,300."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the depth of rain, in millimetres, that four weather stations "
            "measured in May and in June."
            + table(["Weather station", "Rainfall in May (mm)", "Rainfall in June (mm)"],
                    [["Ashdown", "62", "91"], ["Braylea", "78", "96"],
                     ["Cowden", "45", "83"], ["Denbrook", "70", "102"]])
            + "For the station whose rainfall rose by the greatest amount from May to June, what "
              "was the total rainfall, in millimetres, over the two months?"),
      choices=["128", "153", "172", "174"], correct="A",
      check="The rises are 29, 18, 38 and 32 millimetres, so Cowden rose most, and 45 + 83 = 128."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the seed lots a merchant tested last season, classified by crop and by "
            "whether the lot passed the germination test."
            + table(["Crop", "Passed", "Failed"],
                    [["Clover", "100", "20"], ["Ryegrass", "130", "50"],
                     ["Timothy", "70", "30"]])
            + "Every lot that failed will be tested a second time. What percent of all the lots in "
              "the table will be tested a second time?"),
      choices=["20%", "25%", "30%", "33%"], correct="B",
      check="100 lots failed out of 400 lots in all, and 100/400 = 25 percent."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("In one vineyard 14 rows gave a mean of 205 kilograms of grapes each, and 6 further "
            "rows gave a mean of 240 kilograms each. What was the mean yield, in kilograms, of "
            "these 20 rows?"),
      answers=["215.5"],
      check="14(205) + 6(240) = 4,310 kilograms over 20 rows, and 4,310/20 = 215.5."),

 dict(n="H1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A harness maker cuts a triangular gusset with two sides of equal length and a third "
            "side that is 7 centimetres shorter than each of the equal sides. The three sides "
            "together measure 71 centimetres. What is the length, in centimetres, of the shortest "
            "side of the gusset?"),
      choices=["19", "23", "26", "33"], correct="A",
      check="3s - 7 = 71 gives an equal side of 26, so the third side is 26 - 7 = 19."),

 dict(n="H1-20", domain="GT", skill="GT-TR", type="MC",
      stem=("A vineyard row runs straight up a slope, rising 25 metres over a horizontal run of 60 "
            "metres. What is the value of the sine of the angle at which the row meets the "
            "horizontal?"),
      choices=["\\(\\frac{5}{12}\\)", "\\(\\frac{5}{13}\\)", "\\(\\frac{12}{13}\\)",
               "\\(\\frac{13}{5}\\)"], correct="B",
      check="The row itself measures 65 metres, so the sine is 25/65 = 5/13."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="MC",
      stem=("A rain gauge catches rain in a funnel whose circular mouth is 20 centimetres across, "
            "and every drop that lands in the funnel runs down into a cylindrical measuring tube 4 "
            "centimetres across. After a shower in which 1.2 centimetres of rain fell, how many "
            "centimetres deep does the water stand in the measuring tube?"),
      choices=["6", "24", "30", "48"], correct="C",
      check="The mouth's area is 25 times the tube's, so the depth is 25(1.2) = 30 centimetres."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A hay rick is built as a rectangular block 9 metres long, 5 metres wide and 4 metres "
            "high, carrying on top of it a prism whose triangular cross-section is 5 metres wide at "
            "its base and 2 metres tall. What is the total volume of the rick, in cubic metres?"),
      answers=["225"],
      check="9(5)(4) = 180 cubic metres below, and (1/2)(5)(2)(9) = 45 above, so 225 in all."),
]


# ------------------------------------------------------------ Module 2 Easy
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An observatory's dome shutter is opened by turning a crank. The number of turns t "
            "needed satisfies 6t+14=92. What is the value of t?"),
      choices=["11", "13", "15", "18"], correct="B",
      check="6t = 78, so t = 13."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A silk reeler winds 45 grams of raw silk onto each skein. How many grams of raw silk "
            "are wound onto 16 skeins?"),
      choices=["720", "760", "805", "845"], correct="A",
      check="45(16) = 720."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A carriage spring stands 260 millimetres high when nothing rests on it, and it settles "
            "3 millimetres lower for each sack loaded onto it. Which expression gives the height of "
            "the spring, in millimetres, once s sacks have been loaded?"),
      choices=["260-3s", "260+3s", "3s-260", "257s"], correct="A",
      check="Start at 260 and take away 3 for each of the s sacks."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A carriage spring's deflection is modelled in the xy-plane by the line y=7x+4. This "
            "line crosses the y-axis at the point (0, k). What is the value of k?"),
      choices=["-7", "-4", "4", "7"], correct="C",
      check="Putting x = 0 into y = 7x + 4 leaves y = 4."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A lens polisher's speed setting x satisfies \\(3x-8>16\\). Which of the following "
            "could be the value of x?"),
      choices=["6", "7", "8", "9"], correct="D",
      check="3x > 24 means x > 8, and 9 is the only listed value above 8."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A spring maker's stock of 320 steel strips falls by 24 strips each day. After how many "
            "days are 152 strips left?"),
      choices=["4", "5", "6", "7"], correct="D",
      check="320 - 152 = 168, and 168/24 = 7."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A rack in a silk-reeling shed holds at most 24 skeins, and 9 skeins are on it already. "
            "What is the greatest number of further skeins that can be put on the rack?"),
      choices=["13", "15", "17", "33"], correct="B",
      check="24 - 9 = 15."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A silk mill writes its cost estimate as \\(4(3k+5)-7k\\), where k is the number of "
            "reels running. Which expression is equivalent to this estimate?"),
      choices=["\\(5k+20\\)", "\\(5k+5\\)", "\\(12k+20\\)", "\\(19k+20\\)"], correct="A",
      check="4(3k) - 7k = 5k and 4(5) = 20."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The area of a telescope maker's baffle, in square centimetres, is "
            "\\(x^{2}+9x+20\\). Which expression is equivalent to this area?"),
      choices=["\\((x+2)(x+10)\\)", "\\((x+4)(x+5)\\)", "\\((x+1)(x+20)\\)",
               "\\((x-4)(x-5)\\)"], correct="B",
      check="4 and 5 add to 9 and multiply to 20."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of the function f, which records a telescope drive's "
            "error."
            + table(["x", "f(x)"], [["1", "12"], ["2", "5"], ["3", "0"], ["4", "-3"]])
            + "For which value of x does \\(f(x)=0\\)?"),
      choices=["1", "2", "3", "4"], correct="C",
      check="The table pairs x = 3 with the value 0."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A grinder's design equation is \\((n-7)(n+2)=0\\), where n is a positive number of "
            "grinding passes. What is the value of n?"),
      choices=["2", "5", "7", "9"], correct="C",
      check="The solutions are 7 and -2, and only 7 is positive."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A spectacle maker's power rule is the function g defined by \\(g(x)=\\frac{36}{x}\\), "
            "where x is a focal length in centimetres. What is the value of \\(g(9)\\)?"),
      choices=["\\(\\frac{1}{4}\\)", "2", "3", "4"], correct="D",
      check="36 divided by 9 is 4."),

 dict(n="H2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("An optician writes a magnification ratio as \\(\\frac{x^{9}}{x^{4}}\\), where "
            "\\(x>0\\). Which expression is equivalent to this ratio?"),
      choices=["\\(x^{2}\\)", "\\(x^{5}\\)", "\\(x^{13}\\)", "\\(x^{36}\\)"], correct="B",
      check="Dividing powers of the same base subtracts the exponents, and 9 - 4 = 5."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A silk reeler reels 6 skeins in an hour. Working at this rate, how many hours does the "
            "reeler take to reel 78 skeins?"),
      answers=["13"],
      check="78/6 = 13."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("When raw silk is reeled, the ratio of the mass of reeled silk to the mass of waste is "
            "5 to 2. How many kilograms of waste are produced alongside 140 kilograms of reeled "
            "silk?"),
      choices=["14", "35", "40", "56"], correct="D",
      check="140 divided by 5 is 28, and 28(2) = 56."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of clear nights an observatory recorded in each of four "
            "months."
            + table(["Month", "Clear nights"],
                    [["January", "14"], ["February", "9"], ["March", "17"], ["April", "12"]])
            + "In how many of these months were there more than 12 clear nights?"),
      choices=["0", "1", "2", "3"], correct="C",
      check="Only January with 14 and March with 17 exceed 12, so 2 months."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of lens blanks ground and the number rejected at each of "
            "four benches last week."
            + table(["Bench", "Blanks ground", "Blanks rejected"],
                    [["Alder", "120", "7"], ["Birch", "96", "11"],
                     ["Cedar", "140", "5"], ["Dunn", "88", "9"]])
            + "At which bench were the most blanks rejected?"),
      choices=["Alder", "Birch", "Cedar", "Dunn"], correct="B",
      check="The rejected counts are 7, 11, 5 and 9, and 11 is the greatest."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A rearing tray holds 45 cocoons, and 18 of them are double cocoons. One of the 45 "
            "cocoons is picked at random. What is the probability that it is a double cocoon? Give "
            "the answer as a fraction in lowest terms."),
      answers=["2/5"],
      check="18 out of 45 reduces to 2/5."),

 dict(n="H2E-19", domain="GT", skill="GT-LA", type="MC",
      stem=("In the xy-plane the midpoint of the segment joining the points (2, -5) and (10, 1) is "
            "the point (a, b). What is the value of a+b?"),
      choices=["-4", "0", "4", "8"], correct="C",
      check="The midpoint is (6, -2), and 6 + (-2) = 4."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="MC",
      stem=("The shutter opening of an observatory dome is a semicircle of radius 4 metres. What is "
            "the area of this opening, in square metres?"),
      choices=["\\(8\\pi\\)", "\\(16\\pi\\)", "\\(32\\pi\\)", "\\(64\\pi\\)"], correct="A",
      check="Half of pi times 4 squared is 8 pi."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A lens-grinding template is a triangle with a base of 26 centimetres and a height of 9 "
            "centimetres. What is the area of this template, in square centimetres?"),
      answers=["117"],
      check="Half of 26 times 9 is 117."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A mounting bracket is a right triangle ABC with its right angle at C. In this bracket "
            "\\(\\tan A=\\frac{5}{12}\\) and AC=24 centimetres. What is the length of BC, in "
            "centimetres?"),
      choices=["5", "6", "10", "12"], correct="C",
      check="The tangent of A is BC/AC, so BC = 24(5/12) = 10."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A darkroom mixes a developer from x litres of one stock solution and y litres of "
            "another, and the mixture must satisfy both of the following conditions."
            "<br/>2x+5y=31<br/>4x-3y=23<br/>What is the value of \\(\\frac{x}{y}\\)?"),
      choices=["\\(\\frac{3}{8}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{5}{3}\\)",
               "\\(\\frac{8}{3}\\)"], correct="D",
      check="The conditions give y = 3 and x = 8, so the ratio is 8/3."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The two setting circles of a telescope mounting are drawn in the xy-plane as "
            "perpendicular lines. One of them is the line \\(4x-6y=15\\); the other passes through "
            "the point \\((8,-1)\\). What is the y-coordinate of the y-intercept of the second "
            "line?"),
      choices=["-13", "-1", "11", "23"], correct="C",
      check="The first line has slope 2/3, so the second has slope -3/2, and -1 + (3/2)(8) = 11."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A spectacle grinder's setting x must satisfy both \\(7x-4>3x+16\\) and "
            "\\(2x+5\\le 41\\). How many integer values of x satisfy both conditions?"),
      choices=["12", "13", "14", "18"], correct="B",
      check="The conditions give x > 5 and x at most 18, so the integers 6 through 18, which is 13 "
            "values."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A darkroom's stop bath is made up of 3 parts water to 1 part acid by volume. How many "
            "litres of water must be stirred into 8 litres of this stop bath so that the result is "
            "5 parts water to 1 part acid?"),
      choices=["1", "2", "3", "4"], correct="D",
      check="8 litres holds 6 of water and 2 of acid; 5 parts water to 2 of acid is 10, so 4 more "
            "litres of water are needed."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="FR",
      stem=("A telescope drive's setting error is a linear function f for which \\(f(3)=-2\\) and "
            "\\(f(9)=16\\). For what value of x does \\(f(x)=40\\)?"),
      answers=["17"],
      check="18 over 6 gives a slope of 3, and -2 + 3(x - 3) = 40 gives x = 17."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A darkroom thermometer's tolerance is described by \\(\\left|2x-9\\right|=13\\), an "
            "equation with two solutions. What is the sum of those two solutions?"),
      choices=["4", "9", "13", "22"], correct="B",
      check="The solutions are 11 and -2, which add to 9."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A darkroom worker has 240 minutes of bench time. Each contact sheet takes 6 minutes to "
            "print and each enlargement takes 14 minutes, and the worker must print at least 12 "
            "enlargements. What is the greatest number of contact sheets the worker can print in "
            "the 240 minutes?"),
      choices=["10", "12", "14", "16"], correct="B",
      check="12 enlargements take 168 minutes, leaving 72 minutes, and 72/6 = 12."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A darkroom's dilution rule is the function f defined by \\(f(x)=\\frac{60}{x+3}\\). "
            "For some number a it happens that \\(f(a)=5\\). What is the value of \\(f(a-6)\\)?"),
      choices=["3", "5", "6", "10"], correct="D",
      check="60/(a+3) = 5 gives a = 9, and f(3) = 60/6 = 10."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A spectacle grinder's curvature model \\(2x^{2}-12x+23\\) is rewritten in the form "
            "\\(2(x-h)^{2}+j\\), where h and j are constants. What is the value of \\(h+j\\)?"),
      choices=["5", "8", "11", "14"], correct="B",
      check="Completing the square gives 2(x-3)^2 + 5, so h = 3 and j = 5."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A telescope maker's focal relation is \\(\\frac{18}{x}+x=11\\), an equation with two "
            "solutions. What is the greater of the two solutions?"),
      choices=["2", "3", "6", "9"], correct="D",
      check="Multiplying through by x gives x^2 - 11x + 18 = 0, so x is 2 or 9."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A silk mill's throwing ratio satisfies \\(\\frac{8^{x}}{4^{x-3}}=32\\). What is the "
            "value of x?"),
      choices=["-1", "1", "2", "5"], correct="A",
      check="In base 2 the left side is 2 raised to x+6, so x + 6 = 5 and x = -1."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A spring maker writes the compliance of a leaf spring as "
            "\\(\\frac{3}{x}+\\frac{2}{x+1}\\), for \\(x>0\\). Which expression is equivalent to "
            "this compliance?"),
      choices=["\\(\\frac{5x+3}{x^{2}+x}\\)", "\\(\\frac{6}{x^{2}+x}\\)",
               "\\(\\frac{5x+3}{2x+1}\\)", "\\(\\frac{5}{2x+1}\\)"], correct="A",
      check="Over the common denominator x(x+1) the numerator is 3(x+1) + 2x = 5x + 3."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("An observatory dome's profile is modelled by \\(f(x)=x^{2}-8x+21\\). Exactly one value "
            "of x other than 2 gives \\(f(x)=f(2)\\). What is that value of x?"),
      choices=["3", "5", "6", "10"], correct="C",
      check="The parabola is symmetric about x = 4, and 2 is 2 to the left of 4, so 6 matches it."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A list of 8 exposure times has a mean of 34 seconds. Two further exposure times are "
            "added to the list, and the mean of the 10 times is 39.2 seconds. One of the two times "
            "added is 58 seconds. What is the other, in seconds?"),
      choices=["58", "60", "62", "66"], correct="C",
      check="The 10 times total 392 seconds and the first 8 total 272, so the two added total 120 "
            "and the other is 62."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the plates exposed at an observatory over one season, classified by "
            "the instrument used and by whether the plate proved usable."
            + table(["Instrument", "Usable", "Not usable"],
                    [["Astrograph", "84", "26"], ["Refractor", "96", "44"],
                     ["Coelostat", "60", "40"]])
            + "One of the usable plates is selected at random. What is the probability that it was "
              "exposed with the astrograph?"),
      choices=["\\(\\frac{7}{20}\\)", "\\(\\frac{6}{25}\\)", "\\(\\frac{21}{50}\\)",
               "\\(\\frac{42}{125}\\)"], correct="A",
      check="240 plates proved usable and 84 of them came from the astrograph, and 84/240 = 7/20."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A silk mill's output was 5,000 kilograms in its first year. The output rose by 6 "
            "percent in the second year and then fell by 6 percent in the third. What was the "
            "output, in kilograms, in the third year?"),
      choices=["4,964", "4,982", "5,000", "5,018"], correct="B",
      check="5,000(1.06) = 5,300, and 5,300(0.94) = 4,982."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A contact printer works at a steady rate, turning out 200 prints in 3 hours and 20 "
            "minutes. At this rate, how many prints does it turn out in 5 hours and 15 minutes?"),
      choices=["252", "280", "300", "315"], correct="D",
      check="200 prints in 200 minutes is 1 a minute, and 5 hours 15 minutes is 315 minutes."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A drawer holds 40 photographic plates, of which 15 have not been exposed. Three of the "
            "unexposed plates are taken out of the drawer. If one of the plates still in the drawer "
            "is then chosen at random, what is the probability that it has not been exposed?"),
      answers=["12/37"],
      check="12 unexposed plates are left among 37 plates in the drawer."),

 dict(n="H2H-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A telescope's finder bracket is a right triangle whose vertices sit at the points "
            "A(-3, 2), B(5, 2) and C(5, 8) of the xy-plane, with the right angle at B. The point M "
            "is the midpoint of side AC. What is the length of the segment BM?"),
      choices=["3", "4", "5", "6"], correct="C",
      check="M is (1, 5), and the distance from (5, 2) to (1, 5) is 5."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="MC",
      stem=("An observatory dome is a hemisphere whose curved surface area is \\(72\\pi\\) square "
            "metres. What is the volume of this hemisphere, in cubic metres?"),
      choices=["\\(72\\pi\\)", "\\(108\\pi\\)", "\\(144\\pi\\)", "\\(288\\pi\\)"], correct="C",
      check="Two pi r squared equals 72 pi gives r = 6, and two thirds of pi times 216 is 144 pi."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC the right angle is at B, and \\(\\cos A=\\frac{7}{25}\\). What "
            "is the value of \\(\\sin C\\)?"),
      choices=["\\(\\frac{7}{25}\\)", "\\(\\frac{7}{24}\\)", "\\(\\frac{24}{25}\\)",
               "\\(\\frac{25}{7}\\)"], correct="A",
      check="Angles A and C are complementary, so the sine of C equals the cosine of A."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A darkroom tank is a rectangular box with a square base and a height of 30 "
            "centimetres, and it holds 12,000 cubic centimetres. The inside of the base and the "
            "insides of the four walls are lined with felt. How many square centimetres of felt "
            "does the lining take?"),
      answers=["2800"],
      check="The base is 400 square centimetres, so its side is 20, and 400 + 4(20)(30) = 2,800."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
