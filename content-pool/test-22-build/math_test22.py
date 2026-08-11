#!/usr/bin/env python3
"""
Original Math content for Test 22 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item makes a rate, a constant, a
                unit mass or an unknown be recovered first and only then used —
                two or three steps throughout. Clearly harder than Module 2
                (Easy), clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step: one operation, no recovery step. This is
                the lower branch of the adaptive split.
  MODULE_2_HARD hard: parameters instead of numbers, symbolic and structural
                answer choices, a function composed with an unknown inner
                function, a conditioned quadratic, an inequality solved into a
                region, and geometry that chains two relationships.

Test 22's assigned thematic territory is beekeeping and apiaries, honey
extraction, sugar refining, beet processing, confectionery boiling, and
beeswax and candle making. The territory is split across the adaptive
boundary, because a student sees Module 1 plus exactly ONE Module 2 branch and
a setting reused across that boundary shows the same scene twice in one
sitting:

  Module 1        beekeeping, apiaries and honey extraction — hives, supers,
                  frames, brood, swarming, pollination hire, uncapping,
                  settling tanks, refractometers, jars.
  Module 2 Easy   sugar refining and beet processing — weighbridges,
                  diffusers, cossettes, filter beds, refined sacks, syrup
                  grading.
  Module 2 Hard   confectionery boiling and beeswax and candle making — boiling
                  pans, trays of sweets, dipping, moulds, wicks, wax slabs.

verify_math_test22.py enforces that split with a keyword pass, and re-derives
every answer below with sympy from the question itself rather than from the
`check` note.

House style follows Test 1/2 (see CLAUDE.md): stems are bare HTML, simple
inline math stays plain text, data tables are real <table> markup, `&deg;` and
friends go in as entities, and every piece of LaTeX in this file was typed by
hand. No bulk conversion step was used anywhere.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ================================================================= Module 1
# Beekeeping, apiaries and honey extraction. Upper-medium: recover something,
# then use it.
MODULE_1 = [
 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A beekeeper is paid one fixed amount for each colony placed in an orchard and a "
            "different fixed amount for each colony placed on a field of oilseed. Placing 9 "
            "colonies in orchards and 5 colonies on oilseed earned $1,930, and placing 6 colonies "
            "in orchards and 11 colonies on oilseed earned $2,176. How much is earned by placing "
            "one colony in an orchard together with one colony on oilseed?"),
      choices=["$266", "$278", "$284", "$300"], correct="A",
      check="9a+5b=1930 and 6a+11b=2176 give a=150 and b=116, so one of each earns 266."),

 dict(n="H1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Two hives stand on weighing platforms, and each gains mass at its own constant rate "
            "while a nectar flow lasts. The table gives the mass of each hive on three days of one "
            "flow."
            + table(["Day of the flow", "Mass of hive A (kg)", "Mass of hive B (kg)"],
                    [["2", "41", "62"], ["5", "47", "65"], ["9", "55", "69"]])
            + "If both hives keep gaining at these rates, on which day of the flow do the two "
              "hives have the same mass?"),
      choices=["21", "22", "23", "24"], correct="C",
      check="Hive A gains 2 kg a day and hive B gains 1 kg a day, so their masses are 2d+37 and "
            "d+60; 2d+37 = d+60 gives d = 23."),

 dict(n="H1-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A beekeeper must extract at least 900 kilograms of honey during a five-day week. "
            "On the first three days 168, 205 and 149 kilograms were extracted. If an equal mass "
            "is extracted on each of the last two days, at least how many kilograms must be "
            "extracted on each of those two days?"),
      choices=["165", "172", "181", "189"], correct="D",
      check="522 kg have been extracted, so 2e >= 900 - 522 = 378 and e >= 189 kilograms."),

 dict(n="H1-04", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The number of frames a brood box holds is 1 more than twice the number a shallow "
            "super holds. A hive made up of one brood box and three shallow supers holds 41 frames "
            "altogether. How many frames does the brood box hold?"),
      answers=["17"],
      check="With s frames in a super the brood box holds 2s+1, and (2s+1)+3s = 41 gives s = 8 and "
            "a brood box of 17 frames."),

 dict(n="H1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A refractometer reading r is turned into the water content w, as a percentage, of a "
            "sample of honey by \\(w=\\frac{r-38}{19}\\). Which equation gives r in terms of w?"),
      choices=["\\(r=19w+38\\)", "\\(r=19w-38\\)", "\\(r=\\frac{w+38}{19}\\)",
               "\\(r=19(w+38)\\)"], correct="A",
      check="Multiplying by 19 gives 19w = r-38, so r = 19w+38."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two people uncap frames of honey at constant rates, one at 15 frames an hour and the "
            "other at 25 frames an hour. The first begins at once and the second begins 2 hours "
            "later, and between them they uncap 310 frames. For how many hours has the first "
            "person been working when the 310th frame is uncapped?"),
      choices=["7", "8", "9", "10"], correct="C",
      check="15t + 25(t-2) = 310 gives 40t = 360 and t = 9 hours."),

 dict(n="H1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A colony is to be fed until its winter stores are more than 18 kilograms but no more "
            "than 22 kilograms. The colony now holds 9.5 kilograms of stores, and each feed adds "
            "exactly 1.5 kilograms. How many different numbers of feeds meet the requirement?"),
      choices=["2", "3", "4", "5"], correct="B",
      check="9.5 + 1.5n > 18 gives n > 5.67 and 9.5 + 1.5n <= 22 gives n <= 8.33, so n is 6, 7 or "
            "8 — three values."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For \\(w>2\\), which expression is equivalent to \\(\\frac{8w^{3}-27}{2w-3}\\)?"),
      choices=["\\(4w^{2}+6w+9\\)", "\\(4w^{2}-6w+9\\)", "\\(4w^{2}+9\\)",
               "\\(2w^{2}+3w+9\\)"], correct="A",
      check="8w^3-27 factors as (2w-3)(4w^2+6w+9), so the quotient is 4w^2+6w+9."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The time t, in minutes, that a full settling tank of honey takes to cool to the "
            "temperature of the room is modelled by \\(t=k\\sqrt{m}\\), where m is the mass of "
            "honey in the tank in kilograms and k is a constant. A tank holding 16 kilograms cools "
            "in 60 minutes. How many minutes does this model give for a tank holding 36 "
            "kilograms?"),
      choices=["60", "75", "80", "90"], correct="D",
      check="60 = k times 4 gives k = 15, and 15 times 6 = 90 minutes."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("One solution of the equation \\(x^{2}+px+72=0\\) is 4, and p is a constant. What is "
            "the value of p?"),
      choices=["-22", "-18", "18", "22"], correct="A",
      check="Substituting x = 4 gives 16 + 4p + 72 = 0, so 4p = -88 and p = -22."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of capped brood cells in a colony is multiplied by the same factor over "
            "every 12-day period. A colony had 2,700 capped cells on day 12 and 8,100 capped cells "
            "on day 24. How many capped cells does this model give for day 0?"),
      choices=["300", "450", "900", "2,700"], correct="C",
      check="The factor over 12 days is 8,100/2,700 = 3, so day 0 held 2,700/3 = 900 cells."),

 dict(n="H1-12", domain="ADV", skill="ADV-NE", type="FR",
      stem=("In the equation \\(\\frac{6}{x-2}=\\frac{4}{x-4}\\), what is the value of x?"),
      answers=["8"],
      check="Cross-multiplying gives 6(x-4) = 4(x-2), so 2x = 16 and x = 8."),

 dict(n="H1-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A beekeeper's forage index x for one season satisfies \\(4^{x}=7\\), where x is a "
            "constant. For that same season, what is the value of \\(4^{2x+1}\\)?"),
      choices=["28", "196", "392", "784"], correct="B",
      check="4^(2x+1) = (4^x)^2 times 4 = 49 times 4 = 196."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("One extraction run separates a colony's crop into light honey and dark honey in the "
            "ratio 7 to 3 by mass. The run yielded 148 kilograms more light honey than dark honey. "
            "What was the total mass, in kilograms, of the crop?"),
      choices=["296", "370", "444", "518"], correct="B",
      check="With 7u and 3u kilograms, 4u = 148 gives u = 37, so the crop is 10u = 370 kilograms."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Honey runs from a settling tank through a tap at 4.5 litres per minute, and this "
            "honey has a mass of 1.44 kilograms per litre. What mass of honey, in kilograms, runs "
            "from the tap in 25 minutes?"),
      choices=["112.5", "144", "150", "162"], correct="D",
      check="4.5(25) = 112.5 litres, and 112.5(1.44) = 162 kilograms."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the honey taken from each of four apiaries in two successive seasons."
            + table(["Apiary", "First season (kg)", "Second season (kg)"],
                    [["Alder", "240", "294"], ["Byre", "180", "225"],
                     ["Coppice", "350", "420"], ["Dell", "150", "195"]])
            + "At which apiary was the percentage increase from the first season to the second the "
              "greatest?"),
      choices=["Alder", "Byre", "Coppice", "Dell"], correct="D",
      check="The increases are 22.5%, 25%, 20% and 30%, so Dell is the greatest."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean mass of the 12 full supers in a load is 25 kilograms. One super with a mass "
            "of 36 kilograms is taken off the load. What is the mean mass, in kilograms, of the "
            "supers that remain?"),
      choices=["23", "24", "24.5", "25"], correct="B",
      check="The total is 12(25) = 300 kg; (300-36)/11 = 24 kilograms."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A crate holds 40 jars of honey, 25 of them clear and 15 of them set. Three of the "
            "clear jars and 5 of the set jars carry an export label. One jar is selected at random "
            "from the jars that carry no export label. What is the probability that the selected "
            "jar is set?"),
      choices=["\\(\\frac{5}{16}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{3}{8}\\)",
               "\\(\\frac{15}{32}\\)"], correct="A",
      check="22 clear and 10 set jars carry no label, so the probability is 10/32 = 5/16."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The end wall of a honey house is a trapezoid whose parallel sides are 6 metres and 10 "
            "metres long and whose height is 3.5 metres. The building is 12 metres long and its "
            "cross-section is the same all the way along. What is the volume, in cubic metres, of "
            "the building?"),
      choices=["252", "308", "336", "420"], correct="C",
      check="The cross-section has area (6+10)/2 times 3.5 = 28 m^2, and 28(12) = 336 m^3."),

 dict(n="H1-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A rectangular apiary enclosure measures 24 metres by 45 metres, and a straight path "
            "runs from one corner of the enclosure to the opposite corner. Fencing costs $14 per metre, and "
            "the whole perimeter and the path are to be fenced. What is the total cost?"),
      choices=["$1,932", "$2,646", "$2,730", "$3,024"], correct="B",
      check="The diagonal is the square root of 24^2+45^2 = 2601, which is 51; the perimeter is "
            "138, so 189(14) = 2,646 dollars."),

 dict(n="H1-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In a right triangle, the hypotenuse is 3.4 metres long and one of the legs is 1.6 "
            "metres long. What is the tangent of the angle formed by the hypotenuse and that "
            "leg?"),
      choices=["\\(\\frac{8}{17}\\)", "\\(\\frac{15}{17}\\)", "\\(\\frac{15}{8}\\)",
               "\\(\\frac{17}{8}\\)"], correct="C",
      check="The other leg is the square root of 3.4^2-1.6^2 = 9, which is 3, so the tangent is "
            "3/1.6 = 15/8."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A settling tank is a cylinder of radius 25 centimetres standing on its base. Honey "
            "with a volume of \\(6{,}250\\pi\\) cubic centimetres is poured into the empty tank. "
            "What is the depth, in centimetres, of the honey in the tank?"),
      answers=["10"],
      check="The base area is 625 pi, and 6,250 pi divided by 625 pi is a depth of 10 cm."),
]


# ============================================================ Module 2 Easy
# Sugar refining and beet processing. Strictly one step.
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A weighbridge ticket shows that a lorry carrying b tonnes of beet has a total mass of "
            "b+14 tonnes. One ticket reads 39 tonnes. What is the value of b?"),
      choices=["14", "25", "39", "53"], correct="B",
      check="b + 14 = 39 gives b = 25."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The mass of sugar, in kilograms, recovered from t tonnes of beet at a refinery is "
            "given by S(t)=152t. How many kilograms of sugar does this model give for 25 tonnes of "
            "beet?"),
      choices=["3,800", "3,952", "4,180", "4,560"], correct="A",
      check="152(25) = 3,800 kilograms."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A weighbridge subtracts a fixed tare of 9 kilograms from the gross mass of every "
            "sack of beet pulp to give its net mass. One sack has a net mass of 41 kilograms. "
            "What is that sack's gross mass, in kilograms?"),
      choices=["32", "41", "50", "59"], correct="C",
      check="The gross mass g satisfies g - 9 = 41, so g = 50 kilograms."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The solutions of the inequality \\(7x+4\\le39\\) are exactly the values of x that "
            "are at most k. What is the value of k?"),
      choices=["4", "5", "6", "7"], correct="B",
      check="7x <= 35 gives x <= 5, so k = 5."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A refinery's stock of raw sugar, in tonnes, t days after a shipment arrives is given "
            "by S(t)=2,400-85t. By how many tonnes does the stock fall each day?"),
      choices=["85", "340", "2,315", "2,400"], correct="A",
      check="The coefficient of t is -85, so the stock falls by 85 tonnes a day."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A refinery's evaporators burn 340 litres of fuel oil for every hour they run. For "
            "how many hours do they run to burn 2,720 litres of fuel oil?"),
      answers=["8"],
      check="340h = 2,720 gives h = 8 hours."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A refinery must process at least 480 tonnes of beet this week and has already "
            "processed 315 tonnes. What is the least number of further tonnes it must process this "
            "week?"),
      choices=["135", "145", "155", "165"], correct="D",
      check="480 - 315 = 165 tonnes."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A rectangular filter bed has an area, in square metres, of \\(6x^{2}+15x\\). Which "
            "expression gives that area written as a product of two factors?"),
      choices=["\\(3x(2x+15)\\)", "\\(6x(x+5)\\)", "\\(3x(2x+5)\\)", "\\(3(2x+5)\\)"],
      correct="C",
      check="3x divides both terms, and 6x^2+15x = 3x(2x+5)."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A square screen used to grade sugar crystals has sides of length \\(2x+7\\) "
            "centimetres. Which expression gives the area of the screen, in square centimetres?"),
      choices=["\\(4x^{2}+49\\)", "\\(2x^{2}+14x+49\\)", "\\(4x^{2}+28x+49\\)",
               "\\(4x^{2}+14x+49\\)"], correct="C",
      check="(2x+7)^2 = 4x^2 + 28x + 49."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The graph of \\(y=(x-6)(x+2)\\) in the xy-plane is a parabola. What is the "
            "x-coordinate of the vertex of that parabola?"),
      choices=["-2", "2", "4", "6"], correct="B",
      check="The parabola meets the x-axis at 6 and -2, and its vertex sits midway between them, "
            "at x = 2."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("What is the positive solution of the equation \\((n-9)(n+4)=0\\)?"),
      choices=["-9", "-4", "4", "9"], correct="D",
      check="The solutions are 9 and -4, and the positive one is 9."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of x and the corresponding values of the function f."
            + table(["x", "f(x)"], [["1", "5"], ["2", "11"], ["3", "19"], ["4", "29"]])
            + "What is the value of f(4)-f(1)?"),
      choices=["14", "18", "24", "29"], correct="C",
      check="f(4) = 29 and f(1) = 5, so the difference is 24."),

 dict(n="H2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For y&gt;0, the expression \\(\\frac{y^{11}}{y^{4}}\\) is equal to which of the "
            "following?"),
      choices=["\\(y^{7}\\)", "\\(y^{15}\\)", "\\(y^{44}\\)", "\\(y^{3}\\)"], correct="A",
      check="Dividing powers of the same base subtracts the exponents: 11 - 4 = 7."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A diffuser processes 1,260 kilograms of beet cossettes in 9 hours at a constant rate. "
            "How many kilograms does it process in one hour?"),
      answers=["140"],
      check="1,260 divided by 9 is 140 kilograms an hour."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A consignment of beet has a mass of 650 tonnes, and 18% of that mass is sugar. What "
            "is the mass, in tonnes, of sugar in the consignment?"),
      choices=["108", "110", "117", "130"], correct="C",
      check="0.18(650) = 117 tonnes."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the mass of beet refined in each of four weeks."
            + table(["Week", "Beet refined (tonnes)"],
                    [["1", "840"], ["2", "960"], ["3", "1,020"], ["4", "880"]])
            + "In how many of these weeks was more than 900 tonnes of beet refined?"),
      choices=["1", "2", "3", "4"], correct="B",
      check="Only weeks 2 and 3 exceed 900 tonnes, so the answer is 2."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Five sacks of refined sugar were weighed, and their mean mass was 50 kilograms. What "
            "is the total mass, in kilograms, of the five sacks?"),
      choices=["150", "200", "250", "300"], correct="C",
      check="The total is 5 times the mean, which is 250 kilograms."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("Of 80 syrup samples tested at a refinery, 28 were graded fine. What fraction of the "
            "samples tested were graded fine?"),
      answers=["7/20", "0.35", ".35"],
      check="28/80 simplifies to 7/20, which is 0.35."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A circular filter bed has a diameter of 12 metres. What is the area, in square "
            "metres, of the filter bed?"),
      choices=["\\(6\\pi\\)", "\\(12\\pi\\)", "\\(24\\pi\\)", "\\(36\\pi\\)"], correct="D",
      check="The radius is 6 metres, so the area is 36 pi square metres."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="MC",
      stem=("The rim of a circular juice vat is 36 metres round. What is the length, in metres, "
            "of the part of that rim cut off by a central angle of 90&deg;?"),
      choices=["9", "12", "18", "24"], correct="A",
      check="A central angle of 90 degrees cuts off a quarter of the rim, which is 9 metres."),

 dict(n="H2E-21", domain="GT", skill="GT-LA", type="MC",
      stem=("In the xy-plane, the endpoints of a segment are the points (4, 1) and (4, 13). What "
            "is the length of the segment?"),
      choices=["6", "8", "10", "12"], correct="D",
      check="The endpoints share an x-coordinate, so the length is 13 - 1 = 12."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("In a right triangle, the leg opposite the angle x is 20 units long and the leg "
            "adjacent to the angle x is 21 units long. What is the value of \\(\\tan x\\)?"),
      choices=["\\(\\frac{20}{21}\\)", "\\(\\frac{21}{20}\\)", "\\(\\frac{20}{29}\\)",
               "\\(\\frac{21}{29}\\)"], correct="A",
      check="The tangent is the opposite leg over the adjacent leg, which is 20/21."),
]


# ============================================================ Module 2 Hard
# Confectionery boiling, beeswax and candle making. Parameters, symbolic
# answers and chained relationships.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The solution to the system of equations 2x+3y=12 and 5x+ay=25, where a is a "
            "constant, is the ordered pair (3, 2). What is the value of a?"),
      choices=["5", "7", "10", "15"], correct="A",
      check="Substituting (3, 2) into 5x+ay=25 gives 15 + 2a = 25, so a = 5."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The cost C, in dollars, of boiling one batch of sweets is C=an+b, where n is the "
            "number of trays filled from the batch and a and b are positive constants. Which "
            "expression gives n in terms of C, a and b?"),
      choices=["\\(\\frac{C+b}{a}\\)", "\\(\\frac{C}{a}-b\\)", "\\(\\frac{C-b}{a}\\)",
               "\\(\\frac{C-a}{b}\\)"], correct="C",
      check="an = C-b, so n = (C-b)/a."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("How many integer values of n satisfy \\(-5<3n-8\\le13\\)?"),
      choices=["6", "7", "8", "9"], correct="A",
      check="3n-8 > -5 gives n > 1 and 3n-8 <= 13 gives n <= 7, so n runs from 2 to 7: six values."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, a line passes through the points (a, 2a) and (6a, 5a), where a is a "
            "positive constant. What is the slope of the line?"),
      choices=["\\(\\frac{2}{5}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{5}{3}\\)",
               "\\(\\frac{7}{5}\\)"], correct="B",
      check="The slope is (5a-2a)/(6a-a) = 3a/5a = 3/5."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two moulds fill candles at constant rates. Working together they fill 180 candles in "
            "4 hours, and the faster mould working on its own fills 180 candles in 6 hours. How "
            "many hours would the slower mould take to fill 180 candles on its own?"),
      choices=["12", "15", "18", "24"], correct="A",
      check="Together the rate is 45 an hour and the faster mould is 30 an hour, so the slower is "
            "15 an hour and takes 180/15 = 12 hours."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Which inequality gives all the values of x for which \\(\\frac{2x-5}{3}\\ge x-6\\)?"),
      choices=["\\(x\\le\\frac{23}{5}\\)", "\\(x\\ge-13\\)", "\\(x\\ge13\\)", "\\(x\\le13\\)"],
      correct="D",
      check="2x-5 >= 3x-18 gives 13 >= x, that is x <= 13."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A slab of boiled sugar is cut into equal pieces of the same mass. If every piece "
            "were 3 grams heavier, the slab would make exactly 40 pieces; if every piece were 2 "
            "grams lighter, it would make exactly 60 pieces. What is the mass, in grams, of the "
            "whole slab?"),
      answers=["600"],
      check="With a piece of p grams, 40(p+3) = 60(p-2) gives p = 12, and the slab is 40(15) = "
            "600 grams."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by f(x)=3x-2. If \\(f(g(x))=6x+7\\) for every value of x, "
            "which expression defines g(x)?"),
      choices=["\\(2x+9\\)", "\\(6x+9\\)", "\\(\\frac{6x+5}{3}\\)", "\\(2x+3\\)"], correct="D",
      check="3g(x)-2 = 6x+7 gives 3g(x) = 6x+9 and g(x) = 2x+3."),

 dict(n="H2H-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The two solutions of the equation \\(x^{2}-14x+q=0\\), where q is a constant, differ "
            "by 6. What is the value of q?"),
      choices=["40", "45", "49", "58"], correct="A",
      check="The solutions add to 14 and differ by 6, so they are 10 and 4 and q = 40."),

 dict(n="H2H-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which single fraction is equal to \\(\\frac{1}{a}-\\frac{1}{a+3}\\) when a is a "
            "positive constant?"),
      choices=["\\(\\frac{-3}{a(a+3)}\\)", "\\(\\frac{3}{a(a+3)}\\)", "\\(\\frac{1}{3}\\)",
               "\\(\\frac{2a+3}{a(a+3)}\\)"], correct="B",
      check="The common denominator gives ((a+3)-a)/(a(a+3)) = 3/(a(a+3))."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The mass, in grams, of molten wax left in a pouring vessel t minutes after pouring "
            "begins is modelled by \\(m(t)=A\\cdot2^{-\\frac{t}{6}}\\), where A is a constant. "
            "Given that m(0)=48 and m(t)=6, what is the value of t?"),
      choices=["12", "15", "18", "24"], correct="C",
      check="A = 48, and 48 times 2^(-t/6) = 6 gives 2^(-t/6) = 1/8, so t/6 = 3 and t = 18."),

 dict(n="H2H-12", domain="ADV", skill="ADV-NE", type="FR",
      stem=("The solutions of the equation \\(x^{2}-10x+18=0\\) can be written in the form "
            "\\(5\\pm\\sqrt{k}\\), where k is a constant. What is the value of k?"),
      answers=["7"],
      check="Completing the square gives (x-5)^2 = 7, so k = 7."),

 dict(n="H2H-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The quotient \\(\\frac{\\sqrt{50a^{5}}}{\\sqrt{2a}}\\), where a is a positive "
            "constant, is equal to which of the following?"),
      choices=["\\(25a^{4}\\)", "\\(5a^{3}\\)", "\\(5a^{2}\\)", "\\(10a^{2}\\)"], correct="C",
      check="The quotient of the radicals is the square root of 25a^4, which is 5a^2 for a > 0."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A single boiling pan boils away w litres of water in h hours at a constant rate. "
            "Working at that same rate, how many hours do two such pans together take to boil away "
            "3w litres of water?"),
      choices=["\\(\\frac{2h}{3}\\)", "\\(\\frac{3h}{4}\\)", "6h", "\\(\\frac{3h}{2}\\)"],
      correct="D",
      check="One pan boils away w/h litres an hour, so two boil away 2w/h, and 3w divided by 2w/h "
            "is 3h/2 hours."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean of a list of 6 numbers is m. Every number in the list is increased by 4, and "
            "each result is then doubled. What is the mean of the new list, in terms of m?"),
      choices=["2m+4", "2m+8", "2m+2", "m+8"], correct="B",
      check="Adding 4 raises the mean to m+4, and doubling gives 2(m+4) = 2m+8."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives, for each of four lines of boiled sweets, the number of batches made "
            "in a season and the number of those batches rejected at inspection."
            + table(["Line", "Batches made", "Batches rejected"],
                    [["Almond", "250", "18"], ["Barley", "180", "15"],
                     ["Clove", "320", "22"], ["Damson", "140", "12"]])
            + "For which line was the greatest proportion of the batches made rejected?"),
      choices=["Almond", "Barley", "Clove", "Damson"], correct="D",
      check="The proportions are 0.072, 0.083, 0.069 and 0.086, so Damson is the greatest."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A candle burns down c centimetres in each hour it is alight. Which expression gives "
            "the number of hours a candle of length L centimetres burns before it is reduced to a "
            "stub of length s centimetres, where L is greater than s?"),
      choices=["\\(\\frac{L+s}{c}\\)", "\\(\\frac{L-s}{c}\\)", "\\(\\frac{c}{L-s}\\)",
               "\\(c(L-s)\\)"], correct="B",
      check="The candle loses L-s centimetres at c centimetres an hour, so it burns (L-s)/c hours."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the results of inspecting 300 boiled sweets of two shapes."
            + table(["Shape", "Passed", "Failed"],
                    [["Drop", "132", "18"], ["Bar", "126", "24"]])
            + "One of the sweets that failed inspection is selected at random. What is the "
              "probability that the selected sweet is a bar?"),
      choices=["\\(\\frac{2}{25}\\)", "\\(\\frac{4}{25}\\)", "\\(\\frac{3}{7}\\)",
               "\\(\\frac{4}{7}\\)"], correct="D",
      check="42 sweets failed and 24 of them are bars, so the probability is 24/42 = 4/7."),

 dict(n="H2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A solid wax cone is cut through by a plane that is parallel to its base and lies "
            "halfway between the base and the apex. The piece above the cut is itself a cone. "
            "What fraction of the whole cone's volume does that upper piece hold?"),
      choices=["\\(\\frac{1}{8}\\)", "\\(\\frac{1}{6}\\)", "\\(\\frac{1}{4}\\)",
               "\\(\\frac{1}{2}\\)"], correct="A",
      check="The upper cone is similar to the whole cone with every length halved, so its volume "
            "is (1/2)^3 = 1/8 of the whole."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular slab of wax measures 30 centimetres by 24 centimetres by 5 "
            "centimetres. It is melted down without loss and cast into cubes of edge 4 "
            "centimetres. What is the greatest number of whole cubes that can be cast?"),
      answers=["56"],
      check="The slab is 3,600 cm^3 and each cube is 64 cm^3, and 3,600/64 = 56.25, so 56 whole "
            "cubes."),

 dict(n="H2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In a right triangle, the sine of one of the acute angles is \\(\\frac{5}{13}\\). What "
            "is the tangent of that same angle?"),
      choices=["\\(\\frac{12}{13}\\)", "\\(\\frac{13}{12}\\)", "\\(\\frac{5}{12}\\)",
               "\\(\\frac{12}{5}\\)"], correct="C",
      check="The remaining leg is 12, so the tangent is 5/12."),

 dict(n="H2H-22", domain="GT", skill="GT-LA", type="MC",
      stem=("In the xy-plane, the line through the points (1, 4) and (5, k), where k is a "
            "constant, is perpendicular to the line y=-2x+9. What is the value of k?"),
      choices=["2", "4", "6", "8"], correct="C",
      check="A line perpendicular to a line of slope -2 has slope 1/2, so (k-4)/(5-1) = 1/2 and "
            "k = 6."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
