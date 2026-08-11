#!/usr/bin/env python3
"""
Original Math content for Test 27 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Nearly every item makes a rate, a constant, a
                dimension or an unknown be recovered first and only then used;
                two or three steps throughout. Clearly harder than Module 2
                (Easy) and clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
                One operation, no recovery step.
  MODULE_2_HARD hard. Parameters in place of numbers, symbolic answer choices,
                a system conditioned on a coefficient, an absolute-value
                inequality resolved to an interval, a nonlinear system, a
                radical equation with an extraneous root, and geometry that
                chains similarity to an area scale factor.

Every setting is drawn from Test 27's assigned thematic territory. The
territory is split across modules so that no setting can reach a student
twice — a student sees Module 1 plus one Module 2 branch:

  Module 1        ice harvesting, ice houses and ice ponds; salt pans,
                  salterns and the evaporating house; root cellars and
                  earth-covered stores.
  Module 2 (both) fish curing, smokehouses and smoking racks; cheese caves,
                  affinage, turning and brushing.

Neighbouring territories deliberately avoided: dairying belongs to Test 17, so
nothing here touches milking, herds or creameries — the cheese work starts at
the cave door. Peat and lime burning (Test 19), quarrying (Test 18) and
maritime freight (Test 16) are likewise left alone.

Templates rejected during drafting, after reading the nearest banked stems
rather than trusting a similarity number (see MANIFEST.md for the full list):
brine concentration/mixture of any kind (Test 12 M2H Q14 is a tannery brine
mixture; Test 7 M2H Q21 the 20%/50% classic), a salt-pan depth-vs-time table
(Test 16 M1S Q3), a conical salt pile reshaped (Test 13 M2H Q22), a cheese
cylinder whose height is tied to its diameter (Test 17 M2H Q18), the
first-unit-then-additional-unit cost equation (three banked instances), a
misrecorded value corrected mean (Test 19 M1S Q17), a leave-one-out mean
(Test 18 M1S Q18), DE parallel to BC in triangle ABC (Test 9 M2H Q18),
f(g(k)) composition (Test 7 M2H Q7), an infinitely-many-solutions coefficient
(Test 9 M2H Q1), a ramp of given slope length and rise (Test 9 M1S Q19), and a
rectangle whose length is stated relative to its width with a given area
(Test 20 M1S Q9).

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
      stem=("A saltworks draws its salt from an east pan and a west pan. In one season the two "
            "pans together gave 4,160 kilograms of salt, and the east pan gave 260 kilograms more "
            "than twice what the west pan gave. How many kilograms of salt did the east pan give "
            "that season?"),
      choices=["1,300", "1,560", "2,600", "2,860"], correct="D",
      check="w + (2w + 260) = 4,160 gives w = 1,300, so the east pan gave 2(1,300) + 260 = 2,860."),

 dict(n="H1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An ice merchant may hire a horse sledge for the whole season at 48 pounds and then "
            "pay 0.60 pound for each block it carries, or pay a jobbing carter 1.35 pounds a block "
            "with no hire to pay. For how many blocks carried in a season would the two "
            "arrangements cost the same?"),
      choices=["36", "48", "52", "64"], correct="D",
      check="48 + 0.60b = 1.35b leaves 0.75b = 48, so b = 64."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A saltworks watches two evaporating pans. The mass of salt drawn from the first, in "
            "kilograms, is 18d + 40 after d days of drying. The second pan gives 24 kilograms a "
            "day and already held 16 kilograms of salt when the drying began. After how many days "
            "of drying have the two pans given equal masses of salt?"),
      choices=["3", "4", "6", "8"], correct="B",
      check="The second pan gives 24d + 16, and 18d + 40 = 24d + 16 leaves 6d = 24, so d = 4."),

 dict(n="H1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("An ice house is drawn down at a steady rate through the summer. On the 8th day of the "
            "summer it held 186 tonnes of ice, and on the 26th day it held 132 tonnes. On which "
            "day of the summer does this rate leave the ice house empty?"),
      choices=["62", "64", "70", "74"], correct="C",
      check="54 tonnes go in 18 days, so 3 tonnes a day, and 186 - 3(d - 8) = 0 gives d = 70."),

 dict(n="H1-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A saltworks pays 560 pounds in fixed costs for a season and a further 0.35 pound for "
            "every bushel of salt it draws, and it sells every bushel it draws for 2.40 pounds. "
            "What is the least number of bushels the works must draw and sell for the season's "
            "profit to be at least 900 pounds?"),
      choices=["685", "713", "720", "736"], correct="B",
      check="2.40b - (560 + 0.35b) is at least 900 once 2.05b is at least 1,460, so b is at least "
            "712.19 and the least whole number of bushels is 713."),

 dict(n="H1-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The mass of ice left in a store, in tonnes, is modelled by M = 310 - 4.6w, where w is "
            "the number of weeks since the store was closed. The store is emptied and swept as "
            "soon as no more than 15 percent of its original mass is left. After how many whole "
            "weeks is the store emptied and swept?"),
      choices=["47", "52", "57", "58"], correct="D",
      check="15 percent of 310 is 46.5, and 310 - 4.6w is at most 46.5 once w is at least 57.28, "
            "so the store is emptied in week 58."),

 dict(n="H1-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("An ice gang cuts blocks in two sizes: a large block has a mass of 42 kilograms and a "
            "small block a mass of 26 kilograms. In one day the gang cut 96 blocks with a combined "
            "mass of 3,232 kilograms. How many large blocks did the gang cut that day?"),
      answers=["46"],
      check="42L + 26(96 - L) = 3,232 leaves 16L = 736, so L = 46."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A saltworks estimates the tonnage it will draw from p pans as \\((5p+6)(2p-3)\\). "
            "Which expression is equivalent to this estimate?"),
      choices=["\\(10p^{2}-3p-18\\)", "\\(10p^{2}+3p-18\\)", "\\(10p^{2}-3p+18\\)",
               "\\(10p^{2}+27p-18\\)"], correct="A",
      check="Multiplying out gives 10p squared minus 15p plus 12p minus 18, which is 10p squared "
            "minus 3p minus 18."),

 dict(n="H1-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A packer's rule of thumb puts the number of ice blocks a chamber will take at "
            "\\(\\left(\\frac{8n^{6}}{27}\\right)^{\\frac{2}{3}}\\), where n is a measure of the "
            "chamber. Which expression is equivalent to this rule for \\(n>0\\)?"),
      choices=["\\(\\frac{4n^{4}}{9}\\)", "\\(\\frac{4n^{9}}{9}\\)", "\\(\\frac{16n^{4}}{9}\\)",
               "\\(\\frac{4n^{4}}{3}\\)"], correct="A",
      check="The cube root of 8 is 2 and of 27 is 3, each squared gives 4 over 9, and n to the "
            "sixth raised to two thirds is n to the fourth."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The mass of salt left undissolved on the floor of a pan, in kilograms, is modelled by "
            "\\(S(h)=h^{2}-18h+96\\), where h is the number of hours since the brine was let in "
            "and \\(0\\le h\\le 9\\). After how many hours does this model give 24 kilograms?"),
      choices=["4", "6", "8", "12"], correct="B",
      check="h squared minus 18h plus 72 equals 0 factors as (h - 6)(h - 12), and only h = 6 lies "
            "in the interval given."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The ice remaining in a store is modelled by "
            "\\(T(w)=240\\left(\\frac{3}{4}\\right)^{w}\\) tonnes, where w is the number of weeks "
            "since the store was closed. According to this model, how many tonnes of ice are lost "
            "during the second week alone?"),
      choices=["45", "60", "75", "105"], correct="A",
      check="The model gives 180 tonnes after one week and 135 after two, so the second week alone "
            "costs 45 tonnes."),

 dict(n="H1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of hours a pan of brine takes to dry out is modelled by "
            "\\(t=9\\sqrt{d}\\), where d is the depth of the brine in centimetres. A pan takes 63 "
            "hours to dry out. What is the depth, in centimetres, of brine in that pan?"),
      choices=["7", "42", "49", "56"], correct="C",
      check="9 times the square root of d equals 63 gives a square root of 7, so d = 49."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("The number of blocks an ice gang cuts in one shift is modelled by "
            "\\(B(s)=-s^{2}+22s-40\\), where s is the number of sawyers in the gang. What is the "
            "greatest number of sawyers for which this model gives a positive number of blocks?"),
      answers=["19"],
      check="The model is positive between the roots of s squared minus 22s plus 40, which are 2 "
            "and 20, so the greatest whole number of sawyers is 19."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the tonnage of ice cut into each of four ice houses one winter and "
            "the tonnage still fit to deliver at the end of the following summer. "
            + table(["Ice house", "Tonnes cut in", "Tonnes delivered"],
                    [["Ashwell", "480", "396"], ["Barrow", "350", "301"],
                     ["Cranford", "620", "496"], ["Deeping", "540", "459"]])
            + " Which ice house lost the greatest percentage of the ice cut into it?"),
      choices=["Ashwell", "Barrow", "Cranford", "Deeping"], correct="C",
      check="The losses are 17.5, 14, 20 and 15 percent, so Cranford lost the greatest share."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("An ice warden measured the thickness of the ice on a pond on each of 41 days one "
            "winter and recorded the number of days at each thickness. "
            + table(["Thickness (cm)", "Number of days"],
                    [["14", "5"], ["15", "9"], ["16", "12"], ["17", "8"], ["18", "7"]])
            + " What is the median of the 41 recorded thicknesses, in centimetres?"),
      choices=["15", "16", "17", "18"], correct="B",
      check="With 41 days the median is the 21st value, and the running totals 5, 14 and 26 put "
            "the 21st value at 16 centimetres."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Ice is cut into blocks measuring 0.5 metre by 0.4 metre by 0.3 metre, and this ice "
            "has a mass of 920 kilograms for each cubic metre. A sledge may carry a load of at "
            "most 1,150 kilograms. What is the greatest number of whole blocks the sledge may "
            "carry at once?"),
      choices=["18", "19", "20", "21"], correct="C",
      check="A block is 0.06 cubic metre and so 55.2 kilograms, and 1,150 divided by 55.2 is "
            "20.83, so 20 blocks may go on."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table classifies the 300 crates held in a root cellar in April by what they hold "
            "and by whether the roots in them are still sound. "
            + table(["", "Sound", "Sprouted", "Total"],
                    [["Potatoes", "168", "42", "210"], ["Turnips", "63", "27", "90"],
                     ["Total", "231", "69", "300"]])
            + " One crate is selected at random from the crates of potatoes. What is the "
              "probability that the roots in the selected crate are still sound?"),
      choices=["\\(\\frac{4}{5}\\)", "\\(\\frac{7}{10}\\)", "\\(\\frac{77}{100}\\)",
               "\\(\\frac{14}{25}\\)"], correct="A",
      check="168 of the 210 crates of potatoes are sound, and 168 over 210 reduces to 4 over 5."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("In one season a saltworks pumped 46,000 cubic metres of sea water into its pans and "
            "drew 1,472 tonnes of salt from them. Working at the same yield, how many cubic metres "
            "of sea water must the works pump to draw 1,840 tonnes of salt?"),
      choices=["46,000", "51,750", "55,200", "57,500"], correct="D",
      check="1,840 is 1.25 times 1,472, and 1.25 times 46,000 cubic metres is 57,500."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The floor of a root cellar is a rectangle measuring 4.5 metres by 3.2 metres. It is "
            "given an even layer of dry sand over the whole of its area, and 2.16 cubic metres of "
            "sand are used. What is the depth, in metres, of the layer of sand?"),
      choices=["0.12", "0.15", "0.18", "0.24"], correct="B",
      check="The floor is 14.4 square metres, and 2.16 divided by 14.4 is 0.15."),

 dict(n="H1-20", domain="GT", skill="GT-LA", type="MC",
      stem=("An ice house has a square floor of side 16 metres. A straight partition runs from one "
            "corner of the floor to the middle point of a side that does not meet that corner. "
            "What is the length, in metres, of the partition?"),
      choices=["\\(4\\sqrt{5}\\)", "\\(8\\sqrt{5}\\)", "\\(8\\sqrt{3}\\)", "20"],
      correct="B",
      check="The partition is the hypotenuse of a right triangle with legs 16 and 8, and the square "
            "root of 320 is 8 root 5."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A root cellar is roofed over and then covered with a layer of earth 0.4 metre thick "
            "spread evenly over a rectangular area 6 metres by 4.5 metres. The earth is brought up "
            "in carts, and one cart holds 0.9 cubic metre. How many cartloads of earth does the "
            "covering take?"),
      answers=["12"],
      check="6 times 4.5 times 0.4 is 10.8 cubic metres, and 10.8 divided by 0.9 is 12."),

 dict(n="H1-22", domain="GT", skill="GT-TR", type="MC",
      stem=("An ice saw is set into the ice at an acute angle A to the surface of the pond, and "
            "the setting gauge gives \\(\\tan A=\\frac{7}{24}\\). What is the value of "
            "\\(\\sin A\\)?"),
      choices=["\\(\\frac{7}{25}\\)", "\\(\\frac{24}{25}\\)", "\\(\\frac{25}{24}\\)",
               "\\(\\frac{7}{24}\\)"], correct="A",
      check="A right triangle with legs 7 and 24 has hypotenuse 25, so the sine of A is 7 over 25."),
]

# ---------------------------------------------------------- Module 2 (Easy)
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The number of herring still hanging on a smokehouse rack h hours after the fire is "
            "lit is given by 340 - 12h. How many herring are still hanging 9 hours after the fire "
            "is lit?"),
      choices=["108", "196", "232", "268"], correct="C",
      check="340 minus 12 times 9 is 340 minus 108, which is 232."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A curer packs smoked herring 8 to a box. After packing as many full boxes as "
            "possible from 236 herring, 4 herring were left over. How many full boxes did the "
            "curer pack?"),
      choices=["24", "27", "28", "29"], correct="D",
      check="236 less the 4 left over is 232, and 232 divided by 8 is 29."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A cheese cave takes 9 wheels in each row on its shelves. How many rows does it take "
            "to hold 153 wheels, with every row filled?"),
      answers=["17"],
      check="153 divided by 9 is 17."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The mass of a cheese wheel, in kilograms, w weeks after it is carried into the cave "
            "is given by m = 4.6 - 0.05w. What is the mass of a wheel, in kilograms, 12 weeks "
            "after it is carried in?"),
      choices=["3.4", "3.8", "4.0", "4.6"], correct="C",
      check="4.6 minus 0.05 times 12 is 4.6 minus 0.6, which is 4.0."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The number of herring a smokehouse can hang is given by 6r + 24, where r is the "
            "number of extra rails fitted above the hearth. Which is the best interpretation of "
            "the 24 in this expression?"),
      choices=["The number of herring the smokehouse can hang before any extra rail is fitted",
               "The number of herring each extra rail lets the smokehouse hang",
               "The greatest number of extra rails the smokehouse will take",
               "The number of herring the smokehouse loses for each extra rail fitted"],
      correct="A",
      check="Setting r to 0 leaves 24, the number hung with no extra rail fitted."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A smoking rack may carry a load of at most 45 kilograms. Herring are hung on it in "
            "strings, and each string has a mass of 3 kilograms. What is the greatest number of "
            "strings the rack may carry?"),
      choices=["9", "12", "14", "15"], correct="D",
      check="45 divided by 3 is 15."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A curer charges, in pence, 7f + 40 to smoke f fish for a customer. What does the "
            "curer charge, in pence, to smoke 22 fish?"),
      choices=["154", "180", "194", "234"], correct="C",
      check="7 times 22 is 154, and 154 plus 40 is 194."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A curer works out a load's rate figure as \\(15p+35\\). Which expression is "
            "equivalent to this figure?"),
      choices=["\\(3(5p+7)\\)", "\\(5(3p+7)\\)", "\\(5(3p+35)\\)", "\\(15(p+35)\\)"],
      correct="B",
      check="5 divides both 15p and 35, leaving 3p and 7."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A cheese cave's air-change figure is written as \\(\\sqrt{81b^{4}}\\), where "
            "\\(b>0\\). Which expression is equivalent to this figure?"),
      choices=["\\(9b^{2}\\)", "\\(9b^{4}\\)", "\\(18b^{2}\\)", "\\(81b^{2}\\)"], correct="A",
      check="The square root of 81 is 9 and the square root of b to the fourth is b squared."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of days a cheese wheel needs in the cave is modelled by "
            "\\(\\frac{120}{x}\\), where x is the number of degrees Celsius by which the cave "
            "stands above freezing. How many days does the model give when x is 8?"),
      choices=["8", "10", "12", "15"], correct="D",
      check="120 divided by 8 is 15."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A curer's smoke index x satisfies \\(x^{3}=125\\). What is the value of the smoke "
            "index?"),
      choices=["5", "25", "41", "375"], correct="A",
      check="The cube root of 125 is 5."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="FR",
      stem=("The number of minutes of smoking a curer allows at draught setting x is "
            "\\(\\frac{200}{x+3}\\). How many minutes does this allow at draught setting 7?"),
      answers=["20"],
      check="7 plus 3 is 10, and 200 divided by 10 is 20."),

 dict(n="H2E-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A cheese cave's shelf plan uses the expression \\(4y^{2}-36\\). Which expression is "
            "equivalent to this?"),
      choices=["\\(4(y-3)^{2}\\)", "\\(4(y-3)(y+3)\\)", "\\(4(y-6)(y+6)\\)",
               "\\((2y-6)(2y+18)\\)"], correct="B",
      check="Taking out 4 leaves y squared minus 9, which factors as (y - 3)(y + 3)."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of herring smoked at each of four smokehouses in one week. "
            + table(["Smokehouse", "Herring smoked"],
                    [["Fennhaven", "2,140"], ["Garrow", "3,480"],
                     ["Halden", "2,905"], ["Ivory Quay", "3,260"]])
            + " Which smokehouse smoked the greatest number of herring that week?"),
      choices=["Fennhaven", "Garrow", "Halden", "Ivory Quay"], correct="B",
      check="3,480 is the largest of the four figures, and it belongs to Garrow."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Of the 60 cheese wheels in a cave, 12 are wrapped in cloth and the rest are left "
            "bare. What percent of the wheels in the cave are wrapped in cloth?"),
      choices=["12%", "15%", "20%", "25%"], correct="C",
      check="12 divided by 60 is 0.2, which is 20 percent."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A smokehouse burns 2.5 kilograms of oak chips every hour it is alight. How many "
            "kilograms of chips does it burn in a firing that lasts 14 hours?"),
      choices=["16.5", "28", "35", "56"], correct="C",
      check="2.5 times 14 is 35."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the number of cheese wheels put into each grade at one cave's grading "
            "in March. "
            + table(["Grade", "Number of wheels"],
                    [["Prime", "36"], ["Second", "27"], ["Kitchen", "17"]])
            + " What fraction of the wheels graded in March were put into the prime grade?"),
      choices=["\\(\\frac{9}{20}\\)", "\\(\\frac{9}{25}\\)", "\\(\\frac{4}{9}\\)",
               "\\(\\frac{27}{80}\\)"], correct="A",
      check="36 of 80 wheels were prime, and 36 over 80 reduces to 9 over 20."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of cheese wheels standing on each of the four shelves of "
            "one cave. "
            + table(["Shelf", "Wheels standing"],
                    [["Top", "46"], ["Second", "38"],
                     ["Third", "52"], ["Bottom", "29"]])
            + " How many wheels are standing in the cave altogether?"),
      choices=["148", "155", "165", "173"], correct="C",
      check="46 plus 38 plus 52 plus 29 is 165."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The roof space of a smokehouse is a prism 6 metres long whose end is a triangle with "
            "a base of 4 metres and a height of 1.5 metres. What is the volume, in cubic metres, "
            "of the roof space?"),
      choices=["18", "24", "27", "36"], correct="A",
      check="The triangle is 3 square metres, and 3 times 6 is 18."),

 dict(n="H2E-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A smoke baffle is cut as a triangle whose three angles measure 3n&deg;, 4n&deg; and "
            "5n&deg;. What is the value of n?"),
      choices=["12", "15", "18", "20"], correct="B",
      check="The three angles add to 180, so 12n = 180 and n = 15."),

 dict(n="H2E-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A smokehouse chimney is a hollow prism 7 metres tall whose inside cross-section is a "
            "square of side 0.9 metre. What is the volume, in cubic metres, of the space inside "
            "the chimney?"),
      answers=["5.67"],
      check="0.9 squared is 0.81, and 0.81 times 7 is 5.67."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A cheese cave's ramp is the hypotenuse of a right triangle, and it is 18 metres long. "
            "The ramp makes an angle of 30&deg; with the level floor. What is the length, in "
            "metres, of the side opposite the 30&deg; angle?"),
      choices=["6", "9", "12", "15"], correct="B",
      check="The side opposite a 30 degree angle is half the hypotenuse, and half of 18 is 9."),
]

# ---------------------------------------------------------- Module 2 (Hard)
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A curer's loading rule is the pair of equations \\(ax+4y=26\\) and \\(3x-2y=5\\), "
            "where a is a constant, x is the number of racks of herring and y the number of racks "
            "of mackerel. The pair has the solution in which \\(x=3\\). What is the value of a?"),
      choices=["2", "4", "5", "6"], correct="D",
      check="Putting x = 3 into 3x - 2y = 5 gives y = 2, and then 3a + 8 = 26 gives a = 6."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A smokehouse fires n batches of fish one after another. Each batch takes t hours in "
            "the smoke, and the hearth must be left to cool for c hours between one batch and the "
            "next. Which expression gives the total number of hours from the moment the first "
            "batch goes in to the moment the last batch comes out?"),
      choices=["\\(nt+(n-1)c\\)", "\\(nt+nc\\)", "\\((n-1)t+nc\\)", "\\(n(t+c)-t\\)"],
      correct="A",
      check="There are n spells of smoking and only n - 1 gaps, since no cooling follows the last "
            "batch."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A curer's two smoking ovens hold 348 fish between them. If 40 fish were moved from "
            "the larger oven to the smaller, the larger would still hold 26 more fish than the "
            "smaller. How many fish does the larger oven hold?"),
      answers=["227"],
      check="Moving 40 across changes the difference by 80, so the true difference is 106, and "
            "348 plus 106 halved is 227."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("On a plan of a cheese cave a straight line passes through the points \\((a,3a)\\) and "
            "\\((3a,11a)\\), where a is a positive constant. The line crosses the vertical axis at "
            "the point \\((0,b)\\). What is the value of b in terms of a?"),
      choices=["\\(-a\\)", "\\(a\\)", "\\(-4a\\)", "\\(3a\\)"], correct="A",
      check="The slope is 8a over 2a, which is 4, and 3a = 4a + b gives b = -a."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A cheese cave will accept a wheel only if its mass m, in kilograms, satisfies "
            "\\(\\left|m-38\\right|\\le 2.5\\). Which of the following gives every acceptable mass?"),
      choices=["\\(35.5\\le m\\le 40.5\\)", "\\(35.5\\le m\\le 38\\)",
               "\\(m\\le 35.5\\) or \\(m\\ge 40.5\\)", "\\(38\\le m\\le 40.5\\)"], correct="A",
      check="The condition says m is within 2.5 of 38, which is every mass from 35.5 to 40.5."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A cheese cave's shelf survey uses a line in the xy-plane whose equation is "
            "\\(y=px+q\\). The line passes through \\((0,-5)\\) and is parallel to the line "
            "through \\((1,5)\\) and "
            "\\((4,17)\\). What is the value of \\(p+q\\)?"),
      choices=["\\(-9\\)", "\\(-1\\)", "\\(3\\)", "\\(9\\)"], correct="B",
      check="The slope of the second line is 12 over 3, which is 4, and passing through (0, -5) "
            "makes q equal -5, so p + q is -1."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Hanging one herring in a smokehouse takes 0.4 minute and hanging one mackerel takes "
            "0.7 minute. A curer will spend no more than 280 minutes hanging fish, and must hang "
            "at least 300 herring. What is the greatest number of mackerel the curer can hang?"),
      choices=["212", "228", "240", "400"], correct="B",
      check="300 herring take 120 minutes, leaving at most 160 minutes, and 160 divided by 0.7 is "
            "228.57, so 228 mackerel."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("An affineur's turning schedule uses the function \\(f(x)=2x^{2}-5\\). For a positive "
            "constant a it is known that \\(f(a)=45\\). What is the value of \\(f(2a)\\)?"),
      choices=["\\(90\\)", "\\(175\\)", "\\(180\\)", "\\(195\\)"], correct="D",
      check="2a squared minus 5 equal to 45 gives a = 5, and f(10) is 200 minus 5, which is 195."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A curer's timing rule is written as \\(x^{2}+14x+58\\). Which expression is "
            "equivalent to this rule?"),
      choices=["\\((x+7)^{2}+9\\)", "\\((x+7)^{2}-9\\)", "\\((x+7)^{2}+58\\)",
               "\\((x+14)^{2}-138\\)"], correct="A",
      check="Half of 14 is 7, and 7 squared is 49, so the rule is (x + 7) squared plus 58 minus 49."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("An affineur's spacing rule uses the expression \\(4x^{2}+kx+49\\), where k is a "
            "positive constant, and this expression is the square of a binomial. What is the value "
            "of k?"),
      choices=["\\(14\\)", "\\(21\\)", "\\(26\\)", "\\(28\\)"], correct="D",
      check="The square of 2x plus 7 is 4x squared plus 28x plus 49, so k is 28."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of wheels ripening in a cave is modelled by "
            "\\(N(t)=N_{0}\\cdot 3^{\\frac{t}{5}}\\), where \\(N_{0}\\) is the number at the start "
            "and t is the number of days since then. According to this model, by what factor is "
            "the number multiplied over a stretch of 20 days?"),
      choices=["\\(12\\)", "\\(27\\)", "\\(60\\)", "\\(81\\)"], correct="D",
      check="20 days is 4 stretches of 5 days, so the factor is 3 to the fourth, which is 81."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="FR",
      stem=("A curer's damper gauge reports a positive reading x for which "
            "\\(x^{2}+\\frac{1}{x^{2}}=23\\). What is the value of \\(x+\\frac{1}{x}\\)?"),
      answers=["5"],
      check="Squaring x plus its reciprocal gives 23 plus 2, which is 25, and the positive square "
            "root is 5."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A smokehouse's output, in fish, is modelled by \\(P(x)=-3x^{2}+42x-135\\), where x is "
            "the number of hours the hearth is kept alight. The model gives an output of 0 at two "
            "values of x. What is the positive difference between those two values?"),
      choices=["\\(2\\)", "\\(3\\)", "\\(4\\)", "\\(9\\)"], correct="C",
      check="Dividing by -3 leaves x squared minus 14x plus 45, whose roots are 5 and 9."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A cheese cave holds 45 wheels whose mean mass is 4.2 kilograms. A further w wheels, "
            "each of mass exactly 6 kilograms, are carried in, and the mean mass of all the wheels "
            "in the cave is then 4.5 kilograms. What is the value of w?"),
      choices=["6", "9", "12", "15"], correct="B",
      check="189 plus 6w equals 4.5 times (45 + w), which leaves 1.5w equal to 13.5, so w = 9."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A smokehouse working with 3 racks cures 45 fish an hour, and the number of fish cured "
            "in an hour varies directly with the number of racks in use. How many hours does the "
            "smokehouse take to cure 1,200 fish when 5 racks are in use?"),
      choices=["12", "16", "20", "27"], correct="B",
      check="Each rack cures 15 fish an hour, so 5 racks cure 75 an hour, and 1,200 divided by 75 "
            "is 16."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of cheese wheels in each mass class at one cave's weighing "
            "of 80 wheels. "
            + table(["Mass class (kg)", "Number of wheels"],
                    [["3.0 to 3.4", "12"], ["3.5 to 3.9", "23"],
                     ["4.0 to 4.4", "31"], ["4.5 to 4.9", "14"]])
            + " Which mass class contains the median mass of the 80 wheels?"),
      choices=["3.0 to 3.4", "3.5 to 3.9", "4.0 to 4.4", "4.5 to 4.9"], correct="C",
      check="The median lies between the 40th and 41st wheels, and the running totals 12, 35 and "
            "66 put both of them in the class from 4.0 to 4.4."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table classifies the 240 cheese wheels in one affineur's care by the cave they "
            "ripen in and by the grade they were given. "
            + table(["", "Prime", "Second", "Total"],
                    [["Upper cave", "84", "36", "120"], ["Lower cave", "45", "75", "120"],
                     ["Total", "129", "111", "240"]])
            + " One wheel is selected at random from the wheels in the upper cave. What is the "
              "probability that the selected wheel was graded prime?"),
      choices=["\\(\\frac{7}{10}\\)", "\\(\\frac{7}{20}\\)", "\\(\\frac{43}{80}\\)",
               "\\(\\frac{28}{43}\\)"], correct="A",
      check="84 of the 120 wheels in the upper cave are prime, and 84 over 120 reduces to 7 over "
            "10."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A cheese cave holds Tomme wheels and Beaufort wheels in the ratio 5 to 3. After 48 "
            "more Beaufort wheels are carried in, the two kinds stand in the ratio 5 to 4. How "
            "many Tomme wheels are in the cave?"),
      choices=["144", "180", "192", "240"], correct="D",
      check="With 5k Tomme and 3k Beaufort, 4(5k) = 5(3k + 48) gives k = 48, so there are 240 "
            "Tomme wheels."),

 dict(n="H2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A smokehouse hood is a cone with no base, open to the room below. Its rim is a circle "
            "of radius 60 centimetres, and the slanting sheet metal runs 100 centimetres from the "
            "rim to the point at the top. What is the area, in square centimetres, of the sheet "
            "metal in the hood?"),
      choices=["\\(1{,}200\\pi\\)", "\\(3{,}000\\pi\\)", "\\(4{,}800\\pi\\)",
               "\\(6{,}000\\pi\\)"], correct="D",
      check="The curved surface of a cone is pi times radius times slant height, which is 60 times "
            "100 times pi."),

 dict(n="H2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("On a plan, a smoke baffle is a triangle with vertices at \\((0,0)\\), \\((12,0)\\) "
            "and \\((12,5)\\), and one unit on the plan stands for one centimetre. A second baffle "
            "is similar to the first, and the longest side of the second baffle is 39 centimetres. "
            "What is the area, in square centimetres, of the second baffle?"),
      choices=["90", "180", "270", "390"], correct="C",
      check="The first baffle has legs 12 and 5 and so a hypotenuse of 13 and an area of 30, the "
            "similarity ratio is 3, and area scales by 9."),

 dict(n="H2H-21", domain="GT", skill="GT-AV", type="FR",
      stem=("A smoking chamber is a rectangular room 12 metres long, 7 metres wide and 3 metres "
            "high. Four brick piers stand in it, each running from the floor to the ceiling and "
            "each 0.5 metre by 0.5 metre in cross-section. What is the volume, in cubic metres, of "
            "the space left inside the chamber?"),
      answers=["249"],
      check="The room is 252 cubic metres and each pier takes 0.75 cubic metre, so four piers take "
            "3."),

 dict(n="H2H-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A cheese cave's corner brace is a right triangle ABC whose right angle is at C. In "
            "this brace the length of AC is 3 times the length of BC. What is the value of "
            "\\(\\tan A\\)?"),
      choices=["\\(\\frac{1}{3}\\)", "\\(3\\)", "\\(\\frac{1}{\\sqrt{10}}\\)",
               "\\(\\frac{3}{\\sqrt{10}}\\)"], correct="A",
      check="The tangent of A is the side opposite over the side adjacent, which is BC over AC, "
            "or one third."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
