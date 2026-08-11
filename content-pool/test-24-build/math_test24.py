#!/usr/bin/env python3
"""
Original Math content for Test 24 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Nearly every item makes a rate, a constant, a
                unit price or an unknown be recovered first and only then used;
                two or three steps throughout. Clearly harder than Module 2
                (Easy) and clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
                One operation, no recovery step.
  MODULE_2_HARD hard. Parameters in place of numbers, symbolic answer choices,
                a composed function given only its composition, a system
                conditioned on a constant, a parameterised inequality, and
                geometry needing two relationships chained.

Thematic territory for Test 24 is the rope and canvas trades: ropewalks and
cordage, twine spinning, hemp dressing and hackling, net making, sailmaking
lofts, canvas and tarpaulin, rigging and knotwork. It is deliberately kept off
Test 16's maritime/textile ground — no ships, voyages, cargo, looms, weaving or
cloth mills appear anywhere below.

**The territory is split across the adaptive boundary.** A student sees Module
1 and exactly one Module 2 branch, so a setting used in both would show the
same scene twice in one sitting:

    Module 1              ropewalk, cordage, hemp dressing and hackling,
                          twine spinning, strand and hawser laying, tar kettle
    Module 2 (both)       net making and mesh gauges, sailmaking lofts, canvas
                          and tarpaulin, rigging, splices, blocks and thimbles

`verify_math_test24.py` pass 4 enforces that split with a keyword check whose
keywords are chosen so they cannot collide — "tarpaulin" and "tar kettle" are
listed separately precisely because a bare "tar" prefix would match both.

House style follows Test 1/2 (see CLAUDE.md): simple inline arithmetic stays
plain text, `\\( \\)` is reserved for fractions, exponents, radicals and
subscripts, every data table is real `<table>` markup, and `&deg;` goes in as
an entity. All LaTeX is typed by hand; no bulk conversion step was used
anywhere in this file.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ============================================================== Module 1
# Upper-medium. Settings: ropewalk, cordage, hemp dressing, twine spinning,
# strand and hawser laying, tar kettle.
MODULE_1 = [
 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A ropewalk lays a warp of 720 fathoms using three grades of yarn. The number of "
            "fathoms of medium yarn is 40 more than the number of fathoms of light yarn, and the "
            "number of fathoms of heavy yarn is half the number of fathoms of light yarn. How "
            "many fathoms of heavy yarn are in the warp?"),
      choices=["136", "168", "272", "312"], correct="A",
      check="L + (L+40) + L/2 = 720 gives 2.5L = 680, so L = 272 and the heavy yarn is 136."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A twine spinner is paid a fixed sum for each day worked plus a further fixed sum for "
            "each pound of twine spun beyond the daily quota. On a day when she spun 14 pounds "
            "beyond the quota she was paid $89, and on a day when she spun 22 pounds beyond the "
            "quota she was paid $113. How much is she paid, in dollars, on a day when she spins 9 "
            "pounds beyond the quota?"),
      choices=["68", "74", "77", "89"], correct="B",
      check="$24 more for 8 more pounds is $3 a pound, so the fixed sum is 89 - 42 = 47 and "
            "47 + 27 = 74."),

 dict(n="H1-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Each bale of raw hemp yields 38 pounds of long fibre once it has been hackled. A "
            "ropewalk already holds 216 pounds of long fibre and needs at least 910 pounds in "
            "all. What is the least number of bales it must hackle?"),
      choices=["16", "17", "18", "19"], correct="D",
      check="910 - 216 = 694 pounds still wanted, and 694/38 is about 18.3, so 19 bales."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A foreman writes the equation 6(y - 4) = 2y + 44 to find the number y of yarns in one "
            "strand of a cable. A hawser is laid from 3 such strands. How many yarns are in the "
            "hawser?"),
      choices=["17", "34", "51", "68"], correct="C",
      check="6y - 24 = 2y + 44 gives 4y = 68 and y = 17, so three strands hold 51 yarns."),

 dict(n="H1-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Tar drawn off a kettle cools at a constant rate. Its temperature was 220&deg;F four "
            "minutes after it was drawn off and 172&deg;F sixteen minutes after it was drawn off. "
            "According to this model, how many minutes after it was drawn off is the tar at "
            "100&deg;F?"),
      choices=["30", "34", "40", "46"], correct="B",
      check="48 degrees lost in 12 minutes is 4 a minute; 220 - 4(t-4) = 100 gives t = 34."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A ropewalk turns out light line at 30 fathoms an hour and heavy line at 18 fathoms an "
            "hour, and it makes only one of the two at any moment. In a 9-hour day it produced 222 "
            "fathoms of line in all. For how many hours of that day was it making heavy line?"),
      answers=["4"],
      check="30a + 18b = 222 with a + b = 9 gives 270 - 12b = 222, so b = 4."),

 dict(n="H1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A hand cart may carry a load of at most 512 pounds. It is already carrying 146 pounds "
            "of gear, and 40 spools weighing 0.8 pounds each are put aboard. Each coil of twine "
            "added after that weighs 3.5 pounds. What is the greatest number of coils the cart can "
            "carry?"),
      choices=["88", "92", "94", "95"], correct="D",
      check="512 - 146 - 32 = 334 pounds spare and 334/3.5 is about 95.4, so 95 coils."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For the cordage sizes used at one ropewalk, the difference "
            "\\((4n+3)^{2}-(16n^{2}+5)\\) gives the number of extra yarns needed to close a "
            "strand of size n. Which expression is equivalent to that difference?"),
      choices=["24n - 4", "24n + 4", "24n + 14", "12n + 4"], correct="B",
      check="(4n+3)^2 = 16n^2 + 24n + 9, and subtracting 16n^2 + 5 leaves 24n + 4."),

 dict(n="H1-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The breaking strain S, in pounds, of a tarred yarn after d days of exposure on the "
            "walk is modelled by \\(S=240-\\frac{d^{2}}{80}\\) for \\(0\\le d\\le 80\\). After how "
            "many days does the model give a breaking strain of 195 pounds?"),
      choices=["45", "60", "75", "80"], correct="B",
      check="d^2/80 = 45 gives d^2 = 3600, so d = 60 within the stated range."),

 dict(n="H1-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A slack length of cordage is hung between two posts 8 metres apart. Its height above "
            "the floor, in centimetres, at a point x metres from the left-hand post is given by "
            "\\(h(x)=2x^{2}-16x+46\\) for \\(0\\le x\\le 8\\). What is the least height above the "
            "floor reached by the cordage, in centimetres?"),
      choices=["14", "16", "30", "46"], correct="A",
      check="The vertex is at x = 4 and h(4) = 32 - 64 + 46 = 14."),

 dict(n="H1-11", domain="ADV", skill="ADV-EQ", type="FR",
      stem=("For all \\(y\\ne-\\frac{8}{3}\\), the expression \\(\\frac{9y^{2}-64}{3y+8}\\) is "
            "equivalent to \\(3y-c\\), where c is a constant. What is the value of c?"),
      answers=["8"],
      check="9y^2 - 64 = (3y+8)(3y-8), so the quotient is 3y - 8 and c = 8."),

 dict(n="H1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f gives the weight, in pounds, of a coil of cordage that is x fathoms "
            "long, where f(x) = 2.4x + 11. For a certain coil, f(x) = 131. What is the value of "
            "f(x + 25) for that same coil?"),
      choices=["131", "156", "185", "191"], correct="D",
      check="Adding 25 fathoms adds 2.4(25) = 60 pounds, and 131 + 60 = 191."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("A cordage line is stretched between two posts. Its sag y, in millimetres, at a point "
            "x metres from the left-hand post is \\(y=90-(x-6)^{2}\\) for \\(0\\le x\\le 12\\). "
            "What is the greatest value of x at which the sag is 65 millimetres?"),
      answers=["11"],
      check="(x-6)^2 = 25 gives x = 1 or x = 11, and 11 is the greater."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Twine is measured out in hanks, and one hank is 840 yards. A spinner produces 7 hanks "
            "in 4 hours. Working at that same rate, how many yards of twine does the spinner "
            "produce in a 9-hour day?"),
      choices=["11,760", "12,600", "13,230", "17,640"], correct="C",
      check="7 hanks is 5,880 yards in 4 hours, so 1,470 yards an hour and 1,470(9) = 13,230."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A bale of raw hemp loses 35 percent of its weight while it is retted, and the "
            "remainder then loses a further 20 percent of its weight while it is hackled. The "
            "dressed fibre that is left weighs 195 pounds. What was the weight, in pounds, of the "
            "bale of raw hemp?"),
      choices=["312", "340", "375", "420"], correct="C",
      check="0.65(0.80) = 0.52 of the original remains, and 195/0.52 = 375."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean breaking load of the first 6 sample yarns cut from a run of cordage was 42 "
            "pounds. A seventh sample was then cut, and its breaking load was 70 pounds. What is "
            "the mean breaking load, in pounds, of all 7 samples?"),
      choices=["46", "48", "52", "56"], correct="A",
      check="6(42) = 252, and (252 + 70)/7 = 46."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of pounds of dressed hemp drawn from store by each of four "
            "ropewalks in one week, together with the number of fathoms of cordage each one laid "
            "in that week. " +
            table(["Ropewalk", "Pounds of hemp", "Fathoms laid"],
                  [["Ashcombe", "480", "1,200"],
                   ["Bardsley", "520", "1,352"],
                   ["Coldharbour", "640", "1,536"],
                   ["Denhurst", "700", "1,890"]]) +
            " Which ropewalk laid the greatest number of fathoms per pound of hemp drawn?"),
      choices=["Ashcombe", "Bardsley", "Coldharbour", "Denhurst"], correct="D",
      check="The ratios are 2.5, 2.6, 2.4 and 2.7, so Denhurst is greatest."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A foreman recorded the number of strands that broke during each of 7 runs of a "
            "ropewalk: 4, 9, 6, 4, 11, 7, and 4. What is the positive difference between the "
            "median and the mode of these 7 numbers?"),
      choices=["1", "2", "3", "5"], correct="B",
      check="Ordered, the runs are 4, 4, 4, 6, 7, 9, 11; the median is 6, the mode is 4, and the "
            "difference is 2."),

 dict(n="H1-19", domain="GT", skill="GT-LA", type="MC",
      stem=("A hemp stack is braced by two straight stays, each of which runs from a point on a "
            "vertical post down to a stake in level ground. The first stay runs from the top of "
            "the post, 24 feet above the ground, to a stake 10 feet from the foot of the post. The "
            "second stay runs from a point 8 feet above the ground on the same post to a stake 6 "
            "feet from the foot of the post on the opposite side. What is the combined length, in "
            "feet, of the two stays?"),
      choices=["30", "32", "34", "36"], correct="D",
      check="Two right triangles give hypotenuses of 26 and 10 feet, and 26 + 10 = 36."),

 dict(n="H1-20", domain="GT", skill="GT-TR", type="MC",
      stem=("A straight stay 41 feet long runs from a stake in level ground to a point 40 feet up "
            "a vertical post. What is the sine of the angle the stay makes with the ground?"),
      choices=["\\(\\frac{40}{41}\\)", "\\(\\frac{40}{9}\\)", "\\(\\frac{9}{41}\\)",
               "\\(\\frac{9}{40}\\)"], correct="A",
      check="The side opposite that angle is the 40-foot rise and the hypotenuse is 41, so the "
            "sine is 40/41."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="MC",
      stem=("Twine is wound onto a bobbin whose barrel is a right circular cylinder 9 centimetres "
            "long and 4 centimetres in diameter. The wound twine covers the whole length of the "
            "barrel and forms a cylindrical shell whose outer diameter is 10 centimetres. What is "
            "the volume, in cubic centimetres, of the wound twine?"),
      choices=["\\(81\\pi\\)", "\\(189\\pi\\)", "\\(225\\pi\\)", "\\(756\\pi\\)"], correct="B",
      check="9(pi)(5^2 - 2^2) = 9(pi)(21) = 189 pi."),

 dict(n="H1-22", domain="GT", skill="GT-LA", type="MC",
      stem=("Two straight rails of a ropewalk are parallel to one another, and a single straight "
            "stay crosses both of them. The angle the stay makes with the first rail measures "
            "(4x + 15)&deg;, and the corresponding angle it makes with the second rail measures "
            "(6x - 25)&deg;. What is the measure, in degrees, of the supplement of that angle?"),
      choices=["65", "75", "85", "95"], correct="C",
      check="Corresponding angles are equal, so 4x + 15 = 6x - 25 gives x = 20 and an angle of 95 "
            "degrees, whose supplement is 85 degrees."),
]

# ============================================================== Module 2 (Easy)
# One step throughout. Settings: net making and mesh gauges, sailmaking lofts,
# canvas and tarpaulin, rigging and thimbles.
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A net maker uses the equation 8n + 17 = 121 to find the number n of meshes in one row "
            "of a net. What is the value of n?"),
      choices=["9", "11", "12", "13"], correct="D",
      check="8n = 104, so n = 13."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A net maker knots 26 meshes each hour. At that rate, how many meshes does the net "
            "maker knot in 7 hours?"),
      choices=["156", "172", "182", "196"], correct="C",
      check="26(7) = 182."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A net maker begins with 480 meshes still to knot and knots the same number each day. "
            "The number M of meshes still to knot after d days is given by M = 480 - 32d. How many "
            "meshes does the net maker knot each day?"),
      choices=["15", "32", "448", "480"], correct="B",
      check="The coefficient of d is the number knotted each day, which is 32."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A sailmaker uses the equation 5(t - 3) = 40 to find the number t of tabling strips "
            "cut from a roll of canvas. What is the value of t?"),
      answers=["11"],
      check="t - 3 = 8, so t = 11."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A sailmaker will use a needle of gauge w only if \\(4w+5<33\\). Which of the following "
            "values of w satisfies that condition?"),
      choices=["6", "7", "8", "9"], correct="A",
      check="4w < 28 gives w < 7, and 6 is the only listed value below 7."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A roll of tarpaulin holds 240 square feet of material, and each cover cut from it "
            "uses 18 square feet. After c covers have been cut, 96 square feet are left. What is "
            "the value of c?"),
      choices=["2", "4", "6", "8"], correct="D",
      check="240 - 18c = 96 gives 18c = 144 and c = 8."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A finished net weighs 4 pounds for each square metre of netting in it, and its frame "
            "weighs 11 pounds. The whole net must weigh no more than 96 pounds. What is the "
            "greatest whole number of square metres of netting the net can contain?"),
      choices=["19", "20", "21", "22"], correct="C",
      check="(96 - 11)/4 = 21.25, so 21 whole square metres."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to 3(2k + 7) - 5k ?"),
      choices=["k + 21", "k + 7", "11k + 21", "11k + 7"], correct="A",
      check="6k + 21 - 5k = k + 21."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to (x + 6)(x + 4) ?"),
      choices=["\\(x^{2}+24\\)", "\\(x^{2}+10x+10\\)", "\\(x^{2}+24x+10\\)",
               "\\(x^{2}+10x+24\\)"], correct="D",
      check="x^2 + 4x + 6x + 24 = x^2 + 10x + 24."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the equation (m - 9)(m + 5) = 0, what is the positive value of m that satisfies "
            "the equation?"),
      choices=["4", "5", "9", "14"], correct="C",
      check="The solutions are 9 and -5, and 9 is the positive one."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of x and the corresponding values of the function f. " +
            table(["x", "f(x)"],
                  [["1", "15"], ["2", "8"], ["3", "0"], ["4", "-6"]]) +
            " For which value of x in the table is f(x) equal to 0 ?"),
      choices=["1", "2", "3", "4"], correct="C",
      check="The table pairs x = 3 with f(x) = 0."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="FR",
      stem=("The function f is defined by f(x) = 7x - 6. What is the value of f(4)?"),
      answers=["22"],
      check="7(4) - 6 = 22."),

 dict(n="H2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For y > 0, which expression is equivalent to \\(\\frac{y^{11}}{y^{4}}\\)?"),
      choices=["\\(y^{3}\\)", "\\(y^{7}\\)", "\\(y^{15}\\)", "\\(y^{44}\\)"], correct="B",
      check="Subtracting exponents gives y^(11-4) = y^7."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A net contains 96 meshes arranged in 8 rows, with the same number of meshes in each "
            "row. How many meshes are in each row?"),
      choices=["8", "12", "16", "88"], correct="B",
      check="96/8 = 12."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A net loft holds 180 floats, and 30 percent of them are made of cork. How many of the "
            "floats are made of cork?"),
      choices=["54", "60", "126", "150"], correct="A",
      check="0.30(180) = 54."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of nets repaired at each of four lofts during one season. " +
            table(["Loft", "Nets repaired"],
                  [["Halstow", "34"], ["Kingsdown", "51"], ["Marden", "29"], ["Newlyn", "47"]]) +
            " Which loft repaired the greatest number of nets?"),
      choices=["Halstow", "Kingsdown", "Marden", "Newlyn"], correct="B",
      check="51 is the greatest of the four counts, and it belongs to Kingsdown."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A sailmaker measured the width, in inches, of five strips of canvas: 14, 18, 11, 20, "
            "and 17. What is the mean of these five widths?"),
      choices=["13", "14", "15", "16"], correct="D",
      check="The five widths total 80, and 80/5 = 16."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A box holds 45 sail needles, and 18 of them are bone. One needle is drawn from the "
            "box at random. What is the probability that the needle drawn is bone?"),
      choices=["\\(\\frac{2}{5}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{2}{9}\\)",
               "\\(\\frac{18}{27}\\)"], correct="A",
      check="18/45 = 2/5."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A tarpaulin is a rectangle 14 feet long and 9 feet wide. What is its area, in square "
            "feet?"),
      choices=["23", "46", "126", "252"], correct="C",
      check="14(9) = 126."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A net is stowed in a chest in the shape of a rectangular box 4 feet long, 3 feet "
            "wide, and 2 feet deep. What is the volume of the chest, in cubic feet?"),
      answers=["24"],
      check="4(3)(2) = 24."),

 dict(n="H2E-21", domain="GT", skill="GT-LA", type="MC",
      stem=("A triangular sail has one corner measuring 38&deg; and a second corner measuring "
            "64&deg; . What is the measure, in degrees, of the third corner?"),
      choices=["78", "82", "102", "116"], correct="A",
      check="180 - 38 - 64 = 78."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A right triangular sail has legs of length 8 feet and 15 feet and a hypotenuse of "
            "length 17 feet. What is the sine of the angle opposite the 8-foot leg?"),
      choices=["\\(\\frac{8}{17}\\)", "\\(\\frac{15}{17}\\)", "\\(\\frac{8}{15}\\)",
               "\\(\\frac{17}{8}\\)"], correct="A",
      check="Sine is the opposite leg over the hypotenuse, which is 8/17."),
]

# ============================================================== Module 2 (Hard)
# Parameters, symbolic choices, a composition given only through f(g(x)), a
# system conditioned on a constant, a parameterised inequality, chained
# geometry. Settings: sailmaking lofts, canvas and tarpaulin, rigging, splices,
# blocks and thimbles, net making.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the system of equations below, a is a constant.<br/>ax + 6y = 15<br/>4x + 3y = 9"
            "<br/>If the system has no solution, what is the value of a ?"),
      choices=["-8", "2", "4", "8"], correct="D",
      check="No solution needs equal coefficient ratios with unequal constants: a/4 = 6/3 gives "
            "a = 8, and 15/9 is not 2."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In a sail loft's cutting plan, a straight edge passes through the points (-2, 11) and "
            "(6, -5) . Which of the following points also lies on that edge?"),
      choices=["(3, 2)", "(0, 9)", "(8, -8)", "(10, -13)"], correct="D",
      check="The slope is -16/8 = -2 and the line is y = -2x + 7, which gives y = -13 at x = 10."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("In the inequality \\(px-8\\le 3x+12\\), p is a constant, and the solution to the "
            "inequality is \\(x\\ge-4\\). What is the value of p ?"),
      choices=["-5", "-2", "2", "5"], correct="B",
      check="(p-3)x <= 20; reversing the inequality needs p - 3 < 0, and 20/(p-3) = -4 gives "
            "p - 3 = -5, so p = -2."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="FR",
      stem=("Three lengths of rope are to be spliced together. Taken two at a time, the first and "
            "second measure 34 feet in all, the second and third measure 47 feet in all, and the "
            "first and third measure 39 feet in all. What is the length, in feet, of the third "
            "rope?"),
      answers=["26"],
      check="Adding all three pairs gives twice the total, so the total is 60 and the third is "
            "60 - 34 = 26."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A sail loft's charge C, in dollars, for a sail of area A square feet is a linear "
            "function of A. A sail of 120 square feet is charged $510 and a sail of 200 square "
            "feet is charged $750. Which equation gives C in terms of A ?"),
      choices=["C = 3A + 150", "C = 3A + 90", "C = 3.75A + 60", "C = 4.05A"], correct="A",
      check="$240 more for 80 more square feet is $3 each, and 510 - 360 = 150."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A finished canvas panel is accepted only if its width w, in inches, satisfies "
            "\\(\\lvert w-34.5\\rvert\\le 0.8\\). What is the least width, in inches, that is "
            "accepted?"),
      choices=["33.5", "33.7", "34.5", "35.3"], correct="B",
      check="The width lies between 34.5 - 0.8 and 34.5 + 0.8, so the least accepted width is "
            "33.7."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A rigger buys blocks and thimbles, paying the same price for every block and the same "
            "price for every thimble. An order of 5 blocks and 8 thimbles costs $137, and an order "
            "of 8 blocks and 5 thimbles costs $149. What is the total cost, in dollars, of one "
            "block together with one thimble?"),
      choices=["22", "24", "26", "44"], correct="A",
      check="Adding the two orders gives 13 blocks and 13 thimbles for $286, so one of each is "
            "286/13 = 22."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g satisfy f(x) = 2x + 7 and f(g(x)) = 6x - 1 for every value of "
            "x. Which expression gives g(x) ?"),
      choices=["3x - 4", "3x + 4", "3x - 8", "6x - 8"], correct="A",
      check="2g(x) + 7 = 6x - 1 gives 2g(x) = 6x - 8 and g(x) = 3x - 4."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For a two-part tackle, the combined stretch k of the falls is related to the "
            "individual stretches p and q by \\(\\frac{1}{k}=\\frac{1}{p}+\\frac{1}{q}\\), where "
            "p, q and k are all positive. Which expression gives k in terms of p and q ?"),
      choices=["\\(\\frac{p+q}{pq}\\)", "\\(\\frac{pq}{p+q}\\)", "\\(\\frac{pq}{p-q}\\)",
               "\\(\\frac{p+q}{2}\\)"], correct="B",
      check="1/k = (q+p)/(pq), so k = pq/(p+q)."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rectangular panel of canvas has an area of 96 square feet and a perimeter of 44 "
            "feet. What is the length, in feet, of its longer side?"),
      choices=["8", "12", "14", "16"], correct="D",
      check="Length plus width is 22 and their product is 96, so the sides are 16 and 6."),

 dict(n="H2H-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For a > 0, which expression is equivalent to \\(\\sqrt{50a^{7}}\\)?"),
      choices=["\\(5a^{3}\\sqrt{2}\\)", "\\(5a^{3}\\sqrt{2a}\\)", "\\(5a^{4}\\sqrt{2}\\)",
               "\\(25a^{3}\\sqrt{2a}\\)"], correct="B",
      check="50a^7 = 25 a^6 times 2a, and the square root of that is 5 a^3 root(2a)."),

 dict(n="H2H-12", domain="ADV", skill="ADV-NF", type="FR",
      stem=("The function f is defined by \\(f(x)=x^{2}-14x+53\\). The least value of f occurs at "
            "x = a, and that least value is b. What is the value of a + b ?"),
      answers=["11"],
      check="The vertex is at x = 7 and f(7) = 49 - 98 + 53 = 4, so a + b = 11."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The expression \\(x^{2}-10x+k\\), where k is a constant, can be written in the form "
            "\\((x-5)^{2}-9\\). What is the value of k ?"),
      choices=["-9", "9", "14", "16"], correct="D",
      check="(x-5)^2 - 9 = x^2 - 10x + 25 - 9 = x^2 - 10x + 16, so k = 16."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A sail loft blends its canvas yarn from 3 parts flax costing $2.40 a pound and 2 "
            "parts cotton costing $1.65 a pound, by weight. What is the cost, in dollars, of one "
            "pound of the blend?"),
      choices=["1.95", "2.03", "2.10", "2.25"], correct="C",
      check="(3(2.40) + 2(1.65))/5 = 10.50/5 = 2.10."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Two seamers working together, each at a constant rate, finish a suit of canvas in 12 "
            "hours. Working alone at that same constant rate, the first seamer would finish it in "
            "20 hours. Working alone, how many hours would the second seamer take to finish it?"),
      choices=["30", "32", "36", "48"], correct="A",
      check="1/12 - 1/20 = 1/30, so the second seamer alone takes 30 hours."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the results of an inspection of 180 finished sails, sorted by the "
            "loft that made them. " +
            table(["", "Passed", "Returned", "Total"],
                  [["Eastgate loft", "74", "16", "90"],
                   ["Westgate loft", "63", "27", "90"],
                   ["Total", "137", "43", "180"]]) +
            " One of the returned sails is selected at random. What is the probability that the "
            "sail selected was made at the Westgate loft?"),
      choices=["\\(\\frac{16}{43}\\)", "\\(\\frac{27}{43}\\)", "\\(\\frac{27}{90}\\)",
               "\\(\\frac{43}{180}\\)"], correct="B",
      check="43 sails were returned and 27 of them came from Westgate, so the probability is "
            "27/43."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A second rectangular sail is cut so that its length is 20 percent greater than the "
            "length of a first sail and its width is 15 percent less than the width of the first "
            "sail. The area of the second sail is what percent of the area of the first sail?"),
      choices=["95", "98", "102", "105"], correct="C",
      check="1.20(0.85) = 1.02, which is 102 percent."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the finished length L, in inches, of a seam sewn with n stitches, for "
            "four values of n. " +
            table(["n", "L"],
                  [["12", "30"], ["20", "46"], ["28", "62"], ["36", "78"]]) +
            " Which equation gives the relationship between L and n for the values in the table?"),
      choices=["L = 2n + 6", "L = 2n + 30", "L = 2.5n", "L = 1.6n + 10"], correct="A",
      check="L rises 16 for every 8 stitches, so the rate is 2, and 30 - 2(12) = 6."),

 dict(n="H2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A length of canvas hose is a right circular cylinder with inner radius r and length "
            "L. A second length of canvas hose is a right circular cylinder with inner radius 2r "
            "and length \\(\\frac{L}{3}\\). The volume enclosed by the second hose is how many "
            "times the volume enclosed by the first?"),
      choices=["\\(\\frac{1}{3}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{3}{4}\\)",
               "\\(\\frac{4}{3}\\)"], correct="D",
      check="The volume scales by 2^2 for the radius and by 1/3 for the length, giving 4/3."),

 dict(n="H2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle ABC, point D lies on side AB and point E lies on side AC, and segment DE "
            "is parallel to side BC. The length of AD is 6, the length of DB is 9, and the length "
            "of DE is 8. What is the length of BC ?"),
      choices=["12", "16", "20", "24"], correct="C",
      check="AB/AD = 15/6 = 2.5, and the triangles are similar, so BC = 2.5(8) = 20."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A straight stay makes an acute angle \\(\\theta\\) with level ground, and "
            "\\(\\tan\\theta=\\frac{7}{24}\\). What is the value of \\(\\sin\\theta\\)?"),
      choices=["\\(\\frac{7}{24}\\)", "\\(\\frac{7}{25}\\)", "\\(\\frac{24}{25}\\)",
               "\\(\\frac{25}{7}\\)"], correct="B",
      check="A 7-24-25 right triangle gives a hypotenuse of 25, so the sine is 7/25."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A triangular sail has a base of 18 feet and a height of 24 feet. A second triangular "
            "sail is similar to the first, and its base is 27 feet. What is the area, in square "
            "feet, of the second sail?"),
      answers=["486"],
      check="The first sail has area 216, the scale factor is 1.5, and 216(1.5)^2 = 486."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
