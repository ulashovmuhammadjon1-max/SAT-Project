#!/usr/bin/env python3
"""
Original Math content for Test 25 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Nearly every item makes a rate, a constant, a
                unit price or an unknown be recovered first and only then
                used — two or three steps throughout. Clearly harder than
                Module 2 (Easy), clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step: one operation, no recovery step. This is
                the lower branch of the adaptive split.
  MODULE_2_HARD hard: parameters in place of numbers, symbolic answer choices,
                a function defined through a composed argument, a system
                conditioned on a constant, an inequality chain, a radical
                equation with an extraneous root, and geometry that chains two
                relationships together.

Every setting sits inside Test 25's assigned thematic territory — papermaking
and pulp mills, dye works, ink and pigment grinding, bookbinding, and paper
marbling.

The territory is split so that no setting appears in both Module 1 and either
Module 2 branch. A student sees Module 1 plus one Module 2 branch, and the same
scene turning up twice in a sitting reads as a repeat even when the mathematics
is different:

  Module 1 only        papermaking and pulp — the beater, the vat and couching
                       crew, the machine's wire and dryer section, the reel,
                       grammage, reams and quires — and the bindery: cases, the
                       guillotine, trimming.
  Module 2 branches    the dye house — madder, indigo, alum, skeins — ink and
                       pigment grinding on the slab and under the muller, and
                       paper marbling: the trough, the comb, the floated
                       colours.

Pass 4 of verify_math_test25.py enforces that split with a keyword check.
Keywords with an everyday English sense are deliberately NOT in that list:
"ink", "size", "leaf", "board", "gathering", "ground", "press" and "sheet" all
mean something ordinary as well as something in this trade, and a checker that
over-matches is worse than no checker because it trains you to ignore it.

House style follows Test 1/2 (see CLAUDE.md): stems are bare HTML, simple
inline math stays plain text, data tables are real <table> markup, and every
piece of LaTeX is typed by hand. No bulk conversion step was used anywhere in
this file, and there are no images: the geometry items are worded so that they
are fully determined without a picture.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">{}</th>')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ----------------------------------------------------------------- Module 1
# Papermaking and the bindery. Upper-medium: recover a value, then use it.
MODULE_1 = [

 dict(n="M1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a hand paper mill one couching crew starts work at seven o'clock and lays down 8 "
            "sheets each minute. A second crew starts fifteen minutes later and lays down 11 sheets "
            "each minute. How many minutes after the second crew starts will the two crews have laid "
            "down the same total number of sheets?"),
      choices=["40", "45", "55", "75"], correct="A",
      check="With t minutes counted from the second crew's start, 8(t+15) = 11t gives 3t = 120 and "
            "t = 40."),

 dict(n="M1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A bindery's charge for a run of book cases is a linear function of the number of cases "
            "in the run. The table gives the charge for two runs."
            + table(["Cases in the run", "Charge (dollars)"], [["40", "286"], ["100", "562"]])
            + "What is the charge, in dollars, for a run of 150 cases?"),
      choices=["$690", "$792", "$846", "$920"], correct="B",
      check="The charge rises by (562-286)/(100-40) = 4.6 dollars a case, so a run of 150 costs "
            "286 + 4.6(150-40) = 792 dollars."),

 dict(n="M1-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The counter on a paper machine's reel shows the total length of paper wound onto it. At "
            "9:00 the counter read 4,180 metres. The machine ran at a steady 260 metres per minute "
            "until 9:20, when it was slowed to a new steady speed. At 10:00 the counter read 15,380 "
            "metres. At what speed, in metres per minute, did the machine run after 9:20?"),
      answers=["150"],
      check="From 9:00 to 9:20 the reel took 20(260) = 5,200 metres, reaching 9,380. The remaining "
            "15,380 - 9,380 = 6,000 metres were wound in 40 minutes, so the speed was 150."),

 dict(n="M1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("Reams of paper are packed 5 to a carton, and a full carton weighs 12.5 kilograms. The "
            "cartons are stacked on a pallet weighing 18 kilograms, and the hoist that lifts the "
            "loaded pallet is rated for a total of at most 500 kilograms. What is the greatest "
            "number of reams that can be lifted on one pallet?"),
      choices=["176", "185", "190", "200"], correct="C",
      check="12.5c + 18 <= 500 gives c <= 38.56, so at most 38 whole cartons, which hold "
            "38(5) = 190 reams."),

 dict(n="M1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Stuff leaving the beater is 4% fibre by mass, the rest being water. Before it reaches "
            "the machine it is diluted with water until it is 0.5% fibre by mass. How many kilograms "
            "of water must be added to 120 kilograms of the stuff leaving the beater?"),
      choices=["600", "720", "780", "840"], correct="D",
      check="The 120 kilograms carry 4.8 kilograms of fibre. At 0.5% the same fibre needs a total "
            "mass of 4.8/0.005 = 960 kilograms, so 960 - 120 = 840 kilograms of water are added."),

 dict(n="M1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The moisture content of the web falls linearly across the dryer section of a paper "
            "machine. At the fourth cylinder the moisture content is 46%, and at the tenth cylinder "
            "it is 22%. At which cylinder does this model give a moisture content of 6%?"),
      choices=["14", "16", "18", "22"], correct="A",
      check="The fall is (22-46)/(10-4) = -4 percentage points a cylinder, so 46 - 4(n-4) = 6 gives "
            "n = 14."),

 dict(n="M1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A stationer sells paper by the ream at $9.00 and by the quire at $0.60. On one day he "
            "sells all 40 of the reams he holds and takes at least $540 altogether. What is the "
            "least number of quires he can have sold that day?"),
      choices=["240", "300", "360", "420"], correct="B",
      check="The reams bring 40(9) = 360 dollars, so 0.6q >= 540 - 360 = 180 and q >= 300."),

 dict(n="M1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A square sheet has an area of \\(x^{2}-14x+49\\) square centimetres, where x is greater "
            "than 7. Which expression gives the perimeter of the sheet, in centimetres?"),
      choices=["2x - 14", "4x - 14", "4x - 28", "4x + 28"], correct="C",
      check="The area is the perfect square (x-7)^2, so each side is x-7 and the perimeter is "
            "4(x-7) = 4x-28."),

 dict(n="M1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of a quadratic function f."
            + table(["x", "f(x)"], [["1", "18"], ["3", "6"], ["5", "6"], ["7", "18"]])
            + "In the xy-plane, what is the x-coordinate of the vertex of the graph of y = f(x)?"),
      choices=["1", "2", "3", "4"], correct="D",
      check="A quadratic takes equal values at points equidistant from its axis, and f(3) = f(5), "
            "so the axis is x = (3+5)/2 = 4."),

 dict(n="M1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("For a certain paper machine the number n of sheets spoiled during a shift is modelled "
            "by \\(n=\\frac{1}{4}v^{2}-3v+90\\), where v is the machine speed in metres per minute. "
            "At what speed does this model give 106 spoiled sheets?"),
      choices=["16", "24", "32", "40"], correct="A",
      check="Multiplying by 4 gives v^2 - 12v + 360 = 424, so v^2 - 12v - 64 = 0 and "
            "(v-16)(v+4) = 0. Only v = 16 is a possible speed."),

 dict(n="M1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In the xy-plane the graph of \\(y=(x-3)(x+11)\\) crosses the x-axis at two points. What "
            "is the distance between those two points?"),
      choices=["8", "11", "14", "22"], correct="C",
      check="The graph crosses where (x-3)(x+11) = 0, that is at x = 3 and x = -11, and the "
            "distance between those points is 3 - (-11) = 14."),

 dict(n="M1-12", domain="ADV", skill="ADV-EQ", type="FR",
      stem=("If \\(x^{\\frac{3}{2}}=216\\) for a positive number x, what is the value of x?"),
      answers=["36"],
      check="Raising both sides to the power 2/3 gives x = 216^(2/3) = 6^2 = 36."),

 dict(n="M1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("Each pass through the dryer section removes 30% of the water still held in the web. A "
            "web enters the dryers carrying 1,200 grams of water per square metre. How many grams of "
            "water per square metre remain after three passes?"),
      choices=["360", "411.6", "588", "840"], correct="B",
      check="Each pass leaves 70%, so 1,200(0.7)^3 = 1,200(0.343) = 411.6 grams."),

 dict(n="M1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A paper machine runs a web 4.2 metres wide at 320 metres per minute, and the paper it "
            "makes has a grammage of 80 grams per square metre. How many kilograms of paper does the "
            "machine make in one hour?"),
      choices=["1,075.2", "4,300.8", "5,376.0", "6,451.2"], correct="D",
      check="In an hour the web runs 320(60) = 19,200 metres, covering 19,200(4.2) = 80,640 square "
            "metres, which at 80 grams a square metre is 6,451,200 grams, or 6,451.2 kilograms."),

 dict(n="M1-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean grammage of eight sample sheets was 79.5 grams per square metre. A ninth sheet "
            "was then weighed, and the mean grammage of all nine sheets was 80.0 grams per square "
            "metre. What was the grammage, in grams per square metre, of the ninth sheet?"),
      choices=["84.0", "85.5", "88.0", "92.0"], correct="A",
      check="The nine sheets total 9(80.0) = 720 and the first eight total 8(79.5) = 636, so the "
            "ninth is 720 - 636 = 84."),

 dict(n="M1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table shows the number of reams sold and the price per ream for four grades of "
            "paper sold by a mill in one week."
            + table(["Grade", "Reams sold", "Price per ream"],
                    [["Blotting", "310", "$5.60"], ["Cartridge", "95", "$18.00"],
                     ["Laid", "140", "$12.50"], ["Wove", "220", "$8.00"]])
            + "For which grade was the total amount taken in the week greatest?"),
      choices=["Blotting", "Cartridge", "Laid", "Wove"], correct="D",
      check="The takings are 1,736, 1,710, 1,750 and 1,760 dollars, so wove is greatest."),

 dict(n="M1-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The price of a ream of cartridge paper rose by 15% in the spring and then fell by 20% "
            "in the autumn. After both changes a ream cost $11.04. What did a ream cost before the "
            "rise?"),
      choices=["$10.80", "$12.00", "$12.50", "$13.80"], correct="B",
      check="The two changes multiply the price by 1.15(0.80) = 0.92, so the original price is "
            "11.04/0.92 = 12.00 dollars."),

 dict(n="M1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A mill inspected 400 sheets and recorded the grade of each sheet and whether it carried "
            "a visible defect."
            + table(["Grade", "With a defect", "Without a defect"],
                    [["Cartridge", "18", "132"], ["Laid", "27", "93"], ["Wove", "15", "115"]])
            + "One of the sheets carrying a defect is chosen at random. What is the probability that "
              "it is a laid sheet?"),
      choices=["\\(\\frac{27}{400}\\)", "\\(\\frac{3}{20}\\)", "\\(\\frac{9}{40}\\)",
               "\\(\\frac{9}{20}\\)"], correct="D",
      check="60 of the 400 sheets carry a defect and 27 of those are laid, so the probability is "
            "27/60 = 9/20."),

 dict(n="M1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("Paper 0.10 millimetres thick is wound tightly onto a core 100 millimetres in diameter "
            "until the outside diameter of the reel is 900 millimetres. The wound paper completely "
            "fills the ring between the two circles. Which of the following is closest to the length "
            "of the paper on the reel, in metres?"),
      choices=["1,571", "3,142", "6,283", "12,566"], correct="C",
      check="The ring has area (pi/4)(900^2 - 100^2) = 200,000pi square millimetres. Dividing by the "
            "0.10-millimetre thickness gives 2,000,000pi millimetres, which is about 6,283 metres."),

 dict(n="M1-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A rectangular sheet measuring 9 centimetres by 12 centimetres is cut along a diagonal. "
            "In one of the two right triangles formed, what is the shortest distance, in centimetres, "
            "from the right-angle corner to the cut edge?"),
      choices=["7.2", "7.5", "9.0", "10.8"], correct="A",
      check="The diagonal is 15 centimetres, and the triangle's area is (1/2)(9)(12) = 54, so the "
            "altitude to the diagonal is 2(54)/15 = 7.2."),

 dict(n="M1-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A bindery's set square is cut as a right triangle KLM with its right angle at L. The "
            "length of KL is 63 millimetres and \\(\\tan K=\\frac{20}{21}\\). What is the perimeter "
            "of the set square, in millimetres?"),
      choices=["150", "183", "210", "246"], correct="C",
      check="tan K = LM/KL, so LM = 63(20/21) = 60 and KM = sqrt(63^2 + 60^2) = 87. The perimeter "
            "is 63 + 60 + 87 = 210."),

 dict(n="M1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A guillotine trims a rectangular sheet by removing 12 millimetres from the fore-edge and "
            "9 millimetres from each of the head and the tail. The trimmed sheet measures 210 "
            "millimetres across from spine to fore-edge and 297 millimetres from head to tail. What "
            "was the area, in square millimetres, of the sheet before trimming?"),
      answers=["69930"],
      check="Untrimmed the sheet was 210 + 12 = 222 millimetres across and 297 + 2(9) = 315 "
            "millimetres from head to tail, so its area was 222(315) = 69,930."),
]


# ------------------------------------------------------------ Module 2 Easy
# The dye house, the ink and pigment slab, and the marbling trough. One step.
MODULE_2_EASY = [

 dict(n="M2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a dye house the cost, in dollars, of dyeing s skeins is given by 4s + 35. Dyeing one "
            "order cost $155. How many skeins were in that order?"),
      choices=["24", "30", "38", "47"], correct="B",
      check="4s + 35 = 155 gives 4s = 120 and s = 30."),

 dict(n="M2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A dyer bought k kilograms of madder root, and the purchase satisfies the equation "
            "7(k - 3) = 42. What is the value of k?"),
      choices=["3", "6", "9", "15"], correct="C",
      check="Dividing by 7 gives k - 3 = 6, so k = 9."),

 dict(n="M2E-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A colourman works dry pigment into oil on a slab. The mass, in grams, of pigment not "
            "yet worked in after m minutes is given by 45 - 3m. How many grams are not yet worked in "
            "after 8 minutes?"),
      choices=["15", "18", "21", "24"], correct="C",
      check="45 - 3(8) = 45 - 24 = 21."),

 dict(n="M2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The mass of ink on a slab, in grams, is modelled by m = 6.5 - 0.4h, where h is the "
            "number of hours since the slab was charged. According to this model, what was the mass "
            "of ink on the slab, in grams, at the moment it was charged?"),
      choices=["0.4", "3.3", "6.1", "6.5"], correct="D",
      check="At h = 0 the model gives m = 6.5."),

 dict(n="M2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A marbler needs n combs, and n satisfies the inequality \\(5n+12>47\\). Which of the "
            "following values of n satisfies that inequality?"),
      choices=["5", "6", "7", "8"], correct="D",
      check="5n > 35 gives n > 7, and 8 is the only listed value greater than 7."),

 dict(n="M2E-06", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A marbling trough is a rectangle with a perimeter of 224 centimetres. Its length is 68 "
            "centimetres. What is its width, in centimetres?"),
      answers=["44"],
      check="2(68 + w) = 224 gives 68 + w = 112 and w = 44."),

 dict(n="M2E-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("For a certain dye bath the quantities p and q are related by p = 3q + 7. If p = 34, what "
            "is the value of q?"),
      choices=["9", "11", "13", "41"], correct="A",
      check="3q = 34 - 7 = 27, so q = 9."),

 dict(n="M2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A colourman's slab holds \\(2x^{3}\\) grams of pigment in each of \\(5x^{4}\\) parcels "
            "set out on the slab. Which expression gives the total mass of pigment, in grams?"),
      choices=["\\(7x^{7}\\)", "\\(10x^{7}\\)", "\\(7x^{12}\\)", "\\(10x^{12}\\)"], correct="B",
      check="The total is 2x^3 times 5x^4, which is 10x^7 because the exponents add."),

 dict(n="M2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A marbler records a morning's total, in grams, as 4a + 9b - a + 2b. Which expression is "
            "equivalent to that total?"),
      choices=["3a + 11b", "3a + 7b", "5a + 11b", "14ab"], correct="A",
      check="4a - a = 3a and 9b + 2b = 11b, so the total is 3a + 11b."),

 dict(n="M2E-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In the xy-plane the graph of \\(y=x^{2}+k\\) passes through the point (3, 14), where k "
            "is a constant. What is the value of k?"),
      choices=["-5", "3", "5", "9"], correct="C",
      check="Substituting the point gives 14 = 3^2 + k, so k = 14 - 9 = 5."),

 dict(n="M2E-11", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The number of skeins a dyer can hang on a drying frame is given by \\(x^{2}+5\\), where "
            "x is the number of rails in the frame. One frame holds 41 skeins. How many rails does "
            "that frame have?"),
      choices=["4", "6", "9", "36"], correct="B",
      check="x^2 + 5 = 41 gives x^2 = 36, and the positive solution is x = 6."),

 dict(n="M2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A colour dropped on a marbling bath spreads so that the area it covers is given by "
            "\\(A(t)=4(3)^{t}\\) square centimetres t seconds after it is dropped. What area, in "
            "square centimetres, does it cover 2 seconds after it is dropped?"),
      choices=["12", "24", "36", "144"], correct="C",
      check="A(2) = 4(3)^2 = 4(9) = 36 square centimetres."),

 dict(n="M2E-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("A cake of dry pigment is a cube whose side length is s centimetres, and "
            "\\(s^{3}=125\\). What is the value of s?"),
      answers=["5"],
      check="125 = 5^3, so s = 5."),

 dict(n="M2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("An ink recipe calls for 7 parts varnish to 3 parts lampblack by mass. How many kilograms "
            "of lampblack are needed to make 40 kilograms of that ink?"),
      choices=["3", "7", "10", "12"], correct="D",
      check="Lampblack is 3 of the 10 parts, so it is (3/10)(40) = 12 kilograms."),

 dict(n="M2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("72 grams of ultramarine costs $54.00. At that rate, what is the cost of 20 grams of "
            "ultramarine?"),
      choices=["$12.00", "$15.00", "$18.00", "$21.60"], correct="B",
      check="54/72 = 0.75 dollars a gram, and 20(0.75) = 15.00 dollars."),

 dict(n="M2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the number of skeins dyed on each of five days."
            + table(["Day", "Skeins dyed"],
                    [["Monday", "23"], ["Tuesday", "31"], ["Wednesday", "18"],
                     ["Thursday", "26"], ["Friday", "31"]])
            + "What is the range of the five values?"),
      choices=["5", "8", "13", "18"], correct="C",
      check="The greatest value is 31 and the least is 18, so the range is 31 - 18 = 13."),

 dict(n="M2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the amount of each of four pigments held in a colourman's store."
            + table(["Pigment", "Kilograms held"],
                    [["Ochre", "46"], ["Vermilion", "9"], ["Verdigris", "17"],
                     ["Lampblack", "28"]])
            + "How many more kilograms of ochre than of verdigris does the store hold?"),
      choices=["17", "29", "37", "46"], correct="B",
      check="46 - 17 = 29 kilograms."),

 dict(n="M2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A dyer's tally for one morning shows 18 skeins dyed indigo and 27 skeins dyed madder. If "
            "one of those skeins is chosen at random, what is the probability that it was dyed "
            "indigo?"),
      choices=["\\(\\frac{2}{5}\\)", "\\(\\frac{3}{5}\\)", "\\(\\frac{2}{3}\\)",
               "\\(\\frac{3}{2}\\)"], correct="A",
      check="18 of the 18 + 27 = 45 skeins were dyed indigo, and 18/45 = 2/5."),

 dict(n="M2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A rectangular block of dry pigment measures 8 centimetres by 5 centimetres by 3 "
            "centimetres. What is the total surface area of the block, in square centimetres?"),
      choices=["62", "79", "120", "158"], correct="D",
      check="The three pairs of faces have areas 8(5) = 40, 8(3) = 24 and 5(3) = 15, so the total "
            "is 2(40 + 24 + 15) = 158 square centimetres."),

 dict(n="M2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular dye tank has a base measuring 50 centimetres by 40 centimetres and is "
            "filled with liquor to a depth of 30 centimetres. What is the volume of the liquor, in "
            "cubic centimetres?"),
      answers=["60000"],
      check="50(40)(30) = 60,000 cubic centimetres."),

 dict(n="M2E-21", domain="GT", skill="GT-LA", type="MC",
      stem=("A marbling comb carries 24 teeth set in a straight line with all the gaps between "
            "neighbouring teeth equal. The distance from the first tooth to the last is 46 "
            "centimetres. What is the distance, in centimetres, between one tooth and the next?"),
      choices=["2", "23", "24", "46"], correct="A",
      check="24 teeth leave 23 gaps between them, and 46/23 = 2 centimetres."),

 dict(n="M2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A marbler's set square is a right triangle in which one of the acute angles measures "
            "45&deg; and the leg adjacent to that angle measures 9 centimetres. What is the length of "
            "the hypotenuse, in centimetres?"),
      choices=["\\(\\frac{9}{2}\\)", "\\(9\\sqrt{2}\\)", "\\(9\\sqrt{3}\\)", "18"],
      correct="B",
      check="The cosine of 45 degrees is the adjacent leg over the hypotenuse, so the hypotenuse is "
            "9 divided by cos 45, which is 9 times the square root of 2."),
]


# ------------------------------------------------------------ Module 2 Hard
MODULE_2_HARD = [

 dict(n="M2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The solution to the system of equations below is the ordered pair (x, y)."
            "<br/>3x + 4y = 26<br/>5x - 2y = 26<br/>"
            "What is the value of x + y?"),
      choices=["4", "6", "8", "12"], correct="C",
      check="Doubling the second equation and adding gives 13x = 78, so x = 6 and y = 2, and "
            "x + y = 8."),

 dict(n="M2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A dye works' costing rule leads to the equation \\(4(x-c)=3x+8\\), where c is a "
            "constant. The solution to this equation is x = 20. What is the value of c?"),
      choices=["2", "3", "7", "12"], correct="B",
      check="Substituting x = 20 gives 4(20 - c) = 68, so 80 - 4c = 68 and c = 3."),

 dict(n="M2H-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane a line passes through the points (p, 2p) and (3p, 8p), where p is a "
            "nonzero constant. What is the slope of the line?"),
      choices=["3", "4", "6", "3p"], correct="A",
      check="The slope is (8p - 2p)/(3p - p) = 6p/2p = 3, and p cancels."),

 dict(n="M2H-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The inequality \\(3x-a>12\\), where a is a constant, is satisfied by exactly those "
            "values of x that are greater than 9. What is the value of a?"),
      choices=["9", "15", "21", "27"], correct="B",
      check="The inequality rearranges to x > (12+a)/3, so (12+a)/3 = 9 gives 12 + a = 27 and "
            "a = 15."),

 dict(n="M2H-05", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The equation \\(2(6x+a)=3(4x-5)+11\\) is true for every value of x, where a is a "
            "constant. What is the value of a?"),
      answers=["-2"],
      check="Both sides carry 12x, so 2a = -15 + 11 = -4 and a = -2."),

 dict(n="M2H-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A skein of yarn of mass w grams takes up dye in the bath, and its finished mass M is "
            "given by \\(M=w\\left(1+\\frac{r}{100}\\right)\\), where r is the percent gain in mass. "
            "Which equation gives r in terms of M and w?"),
      choices=["\\(r=\\frac{100(M-w)}{M}\\)", "\\(r=\\frac{M-w}{100w}\\)",
               "\\(r=\\frac{100(M-w)}{w}\\)", "\\(r=100(M-w)\\)"], correct="C",
      check="Dividing by w gives M/w = 1 + r/100, so r/100 = (M-w)/w and r = 100(M-w)/w."),

 dict(n="M2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The constants x and y satisfy \\(2\\le x\\le 6\\) and \\(1\\le y\\le 4\\). What is the "
            "greatest possible value of \\(\\frac{x-y}{y}\\)?"),
      choices=["1", "2", "3", "5"], correct="D",
      check="The expression equals x/y - 1, which is greatest when x is largest and y smallest, so "
            "the greatest value is 6/1 - 1 = 5."),

 dict(n="M2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f satisfies f(2x - 1) = 6x + 5 for every value of x. What is the value of "
            "f(7)?"),
      choices=["11", "17", "23", "29"], correct="D",
      check="2x - 1 = 7 gives x = 4, so f(7) = 6(4) + 5 = 29."),

 dict(n="M2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The expression \\((3x-4)^{2}-(2x-4)(2x+4)\\) is equivalent to \\(ax^{2}+bx+c\\), "
            "where a, b and c are constants. What is the value of a+b+c?"),
      choices=["-11", "13", "21", "29"], correct="B",
      check="(3x-4)^2 = 9x^2 - 24x + 16 and (2x-4)(2x+4) = 4x^2 - 16, so the difference is "
            "5x^2 - 24x + 32 and a + b + c = 5 - 24 + 32 = 13."),

 dict(n="M2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the xy-plane the graph of \\(y=x^{2}+bx+c\\) passes through the point (0, 12) and "
            "has its vertex on the line x = 5, where b and c are constants. What is the value of b?"),
      choices=["-25", "-20", "-12", "-10"], correct="D",
      check="The vertex of y = x^2 + bx + c lies at x = -b/2, so -b/2 = 5 and b = -10. The point "
            "(0, 12) fixes c = 12 but does not affect b."),

 dict(n="M2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The mass of pigment still too coarse to use after t hours under the muller is modelled "
            "by \\(m(t)=A(0.8)^{t}\\), where m is in grams and A is a constant. After 4 hours 204.8 "
            "grams are still too coarse. What is the value of A?"),
      choices=["256", "320", "500", "640"], correct="C",
      check="0.8^4 = 0.4096, and A(0.4096) = 204.8 gives A = 500."),

 dict(n="M2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The expression (x+a)(x+b) is equal to \\(x^{2}+11x+30\\) for every value of x, where a "
            "and b are constants and a is greater than b. What is the value of a-b?"),
      choices=["1", "5", "6", "11"], correct="A",
      check="a and b multiply to 30 and add to 11, so they are 6 and 5, and a - b = 1."),

 dict(n="M2H-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("One solution of the equation \\(x^{2}-kx+18=0\\) is 3, where k is a constant. What is "
            "the other solution?"),
      answers=["6"],
      check="The two solutions multiply to 18, so the other is 18/3 = 6. (Their sum is then 9, "
            "which makes k = 9.)"),

 dict(n="M2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dye recipe calls for madder and alum in the ratio 5 to 2 by mass. A dyer holds 30 "
            "kilograms of madder and 14 kilograms of alum. What is the greatest total mass, in "
            "kilograms, of a mixture in that ratio that the dyer can make?"),
      choices=["35", "42", "44", "49"], correct="B",
      check="The madder allows 30/5 = 6 shares and the alum allows 14/2 = 7 shares, so 6 shares of "
            "7 kilograms each can be made, a total of 42 kilograms."),

 dict(n="M2H-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean of a set of 7 readings is 24. Each reading is multiplied by 3, and then 5 is "
            "subtracted from each product. What is the mean of the resulting set of 7 values?"),
      choices=["67", "72", "77", "82"], correct="A",
      check="Multiplying every value by 3 multiplies the mean by 3, and subtracting 5 from every "
            "value subtracts 5 from the mean, so the new mean is 3(24) - 5 = 67."),

 dict(n="M2H-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of skeins dyed in each of three colours at two dye works "
            "during one season."
            + table(["Colour", "Old works", "New works"],
                    [["Indigo", "81", "126"], ["Madder", "54", "93"], ["Weld", "45", "51"]])
            + "Of the skeins dyed at the old works, what percentage were dyed indigo?"),
      choices=["18%", "30%", "45%", "55%"], correct="C",
      check="The old works dyed 81 + 54 + 45 = 180 skeins, and 81/180 = 0.45, or 45%."),

 dict(n="M2H-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Two grades of ink are blended. One costs $18 a kilogram and the other costs $30 a "
            "kilogram, and the blend costs $22 a kilogram. What fraction of the blend, by mass, is "
            "the dearer grade?"),
      choices=["\\(\\frac{1}{4}\\)", "\\(\\frac{1}{3}\\)", "\\(\\frac{1}{2}\\)",
               "\\(\\frac{2}{3}\\)"], correct="B",
      check="If a fraction f of the blend is the dearer grade, 30f + 18(1-f) = 22 gives 12f = 4 and "
            "f = 1/3."),

 dict(n="M2H-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A box holds 5 cakes of vermilion and 7 cakes of ochre. Two cakes are taken from the box "
            "at random, one after the other and without replacement. What is the probability that "
            "the two cakes taken are of different pigments?"),
      choices=["\\(\\frac{35}{132}\\)", "\\(\\frac{7}{22}\\)", "\\(\\frac{35}{66}\\)",
               "\\(\\frac{7}{12}\\)"], correct="C",
      check="Vermilion then ochre has probability (5/12)(7/11) and ochre then vermilion the same, "
            "so the total is 2(35/132) = 35/66."),

 dict(n="M2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A cylindrical can of radius r and height h is completely full of ink. All the ink is "
            "poured into a second, taller cylindrical can whose radius is 2r. To what depth does the "
            "ink stand in the second can?"),
      choices=["\\(\\frac{h}{4}\\)", "\\(\\frac{h}{2}\\)", "\\(\\frac{3h}{4}\\)",
               "\\(\\frac{4h}{3}\\)"], correct="A",
      check="The volume pi r^2 h fills a can of base area pi(2r)^2 = 4 pi r^2, so the depth is "
            "h/4."),

 dict(n="M2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("In the xy-plane a circle has its centre at (3, -2) and passes through the point "
            "(11, 4). What is the length of the radius of the circle?"),
      choices=["6", "10", "14", "20"], correct="B",
      check="The radius is the distance from (3,-2) to (11,4), which is sqrt(8^2 + 6^2) = "
            "sqrt(100) = 10."),

 dict(n="M2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A marbler's comb blank is cut as a right triangle ABC with its right angle at C. The "
            "length of AB is 20 centimetres and \\(\\sin A=\\frac{3}{5}\\). What is the area of the "
            "blank, in square centimetres?"),
      choices=["48", "60", "96", "120"], correct="C",
      check="sin A = BC/AB gives BC = 20(3/5) = 12, so AC = sqrt(400-144) = 16 and the area is "
            "(1/2)(12)(16) = 96."),

 dict(n="M2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A conical heap of dry pigment has a base of radius 30 centimetres and a height of 40 "
            "centimetres. The volume of the heap is \\(k\\pi\\) cubic centimetres. What is the value "
            "of k?"),
      answers=["12000"],
      check="The volume is (1/3)pi(30^2)(40) = 12,000 pi cubic centimetres, so k = 12,000."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
