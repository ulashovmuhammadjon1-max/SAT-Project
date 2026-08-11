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
                a function defined piecewise or through a shifted argument, a
                border quadratic, an inverse variation, a probability that has
                to be rebuilt after the box changes, and geometry that chains
                two relationships together.

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

REPAIR PASS (this build). 34 of the original 66 drafts were rewritten as
genuine template repeats of questions already live in production. Only two of
the 34 scored at or above the 0.75 reject line; the rest were found by READING
the flagged matches and, in eleven cases, by grepping the bank for the
mechanism rather than for the words — a repeat that changes its setting words
scores LOW precisely because it changed the words. The worst offenders scored
0.37 (7(k-3)=42 against Test 6's 7(k-2)=63), 0.39 (a 5-to-2 ratio limited by
stock, against Test 14's identical 5-to-2 ratio limited by stock) and 0.44
(pouring one cylinder into a wider one, against Test 18's silo). Six more —
M1-04, M1-05, M1-13, M1-15, M1-16 and M2E-08 — never scored above 0.30 against
their true twins at all. See MANIFEST.md for the full table.
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
      stem=("A guillotine operator is paid $16 for each of the first 35 hours worked in a week and "
            "$24 for each hour worked beyond 35. In one week the operator was paid $824. How many "
            "hours did the operator work that week?"),
      choices=["44", "46", "49", "52"], correct="B",
      check="The first 35 hours pay 35(16) = 560 dollars, leaving 824 - 560 = 264 dollars at 24 "
            "dollars an hour, which is 11 further hours, so 46 hours in all."),

 dict(n="M1-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("The counter on a paper machine's reel shows the total length of paper wound onto it. At "
            "9:00 the counter read 4,180 metres. The machine ran at a steady 260 metres per minute "
            "until 9:20, when it was slowed to a new steady speed. At 10:00 the counter read 15,380 "
            "metres. At what speed, in metres per minute, did the machine run after 9:20?"),
      answers=["150"],
      check="From 9:00 to 9:20 the reel took 20(260) = 5,200 metres, reaching 9,380. The remaining "
            "15,380 - 9,380 = 6,000 metres were wound in 40 minutes, so the speed was 150."),

 dict(n="M1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The first four reels run on a paper machine averaged 940 metres of paper each. What is "
            "the least number of metres the fifth reel must run if the five reels are to average at "
            "least 960 metres each?"),
      choices=["980", "1,000", "1,040", "1,160"], correct="C",
      check="Five reels averaging 960 metres total 4,800 metres, and the first four total "
            "4(940) = 3,760, so the fifth must run at least 4,800 - 3,760 = 1,040 metres."),

 dict(n="M1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two fifths of the sheets on a pallet are cartridge and the rest are wove. There are 84 "
            "more wove sheets than cartridge sheets on the pallet. How many sheets are on the "
            "pallet?"),
      choices=["140", "168", "210", "420"], correct="D",
      check="Wove is three fifths and cartridge two fifths of the pallet, so the difference is one "
            "fifth of the pallet. One fifth is 84, so the pallet holds 420 sheets."),

 dict(n="M1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A pallet holds 5 times as many blotting reams as cartridge reams. After 36 blotting "
            "reams are taken off the pallet, it holds 3 times as many blotting reams as cartridge "
            "reams. How many cartridge reams are on the pallet?"),
      choices=["12", "18", "24", "90"], correct="B",
      check="With c cartridge reams, 5c - 36 = 3c gives 2c = 36 and c = 18."),

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
      stem=("A bindery's cost, in dollars, of a run of n cases is \\(n^{2}+18n\\), and the bindery is "
            "paid 63n dollars for the run. For how many cases does the payment for a run exactly "
            "cover its cost?"),
      choices=["18", "45", "63", "81"], correct="B",
      check="n^2 + 18n = 63n gives n^2 = 45n, and since n is positive, n = 45."),

 dict(n="M1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined so that \\(f(x)=3x+7\\) when x is less than 5, and "
            "\\(f(x)=x^{2}-4\\) when x is 5 or greater. What is the value of f(6) - f(2)?"),
      choices=["19", "23", "25", "45"], correct="A",
      check="6 is 5 or greater, so f(6) = 36 - 4 = 32; 2 is less than 5, so f(2) = 6 + 7 = 13. The "
            "difference is 32 - 13 = 19."),

 dict(n="M1-12", domain="ADV", skill="ADV-EQ", type="FR",
      stem=("For every positive value of x, \\(\\frac{x^{a}}{x^{3}}=x^{12}\\), where a is a constant. "
            "What is the value of a?"),
      answers=["15"],
      check="Dividing powers of the same base subtracts the exponents, so a - 3 = 12 and a = 15."),

 dict(n="M1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=x^{2}+2x\\). What is the average rate of change of "
            "f as x increases from 1 to 5?"),
      choices=["6", "8", "10", "32"], correct="B",
      check="f(5) = 35 and f(1) = 3, so the average rate of change is (35-3)/(5-1) = 32/4 = 8."),

 dict(n="M1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A paper machine runs a web 4.2 metres wide at 320 metres per minute, and the paper it "
            "makes has a grammage of 80 grams per square metre. How many kilograms of paper does the "
            "machine make in one hour?"),
      choices=["1,075.2", "4,300.8", "5,376.0", "6,451.2"], correct="D",
      check="In an hour the web runs 320(60) = 19,200 metres, covering 19,200(4.2) = 80,640 square "
            "metres, which at 80 grams a square metre is 6,451,200 grams, or 6,451.2 kilograms."),

 dict(n="M1-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The grammages recorded for five sheets were 78, 79, 80, 81 and 96 grams per square "
            "metre. The reading of 96 was afterwards found to be a misprint for 82, and the record "
            "was corrected. Which statement correctly describes the effect of that correction on the "
            "five readings?"),
      choices=["The mean decreases and the median is unchanged.",
               "The mean is unchanged and the median decreases.",
               "Both the mean and the median decrease.",
               "Both the mean and the median are unchanged."], correct="A",
      check="The mean falls from 414/5 = 82.8 to 400/5 = 80, while the middle reading is 80 both "
            "before and after the correction."),

 dict(n="M1-16", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of reams of three of the four grades a mill sold in one week."
            + table(["Grade", "Reams sold"],
                    [["Blotting", "310"], ["Cartridge", "95"], ["Wove", "220"]])
            + "The mill sold 765 reams altogether that week, the rest of them laid paper, and laid "
              "paper sells at $12.50 a ream. What amount did the mill take for the laid paper it "
              "sold that week?"),
      choices=["$875.00", "$1,187.50", "$1,750.00", "$3,875.00"], correct="C",
      check="The three grades shown account for 310 + 95 + 220 = 625 reams, so 765 - 625 = 140 reams "
            "were laid, and 140(12.50) = 1,750 dollars."),

 dict(n="M1-17", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Cartridge paper is sold in a box of 12 reams for $198 and in a box of 20 reams for $310. "
            "How many dollars less does one ream cost when it is bought in the larger box?"),
      choices=["$0.50", "$1.00", "$1.50", "$2.00"], correct="B",
      check="A ream costs 198/12 = 16.50 dollars in the smaller box and 310/20 = 15.50 dollars in "
            "the larger, a difference of 1.00 dollar."),

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
      stem=("In triangle ABC the measures of the three angles are in the ratio 2 to 3 to 7. What is "
            "the measure, in degrees, of the largest of the three angles?"),
      choices=["30", "45", "90", "105"], correct="D",
      check="The three parts total 12, and 180/12 = 15, so the largest angle measures 7(15) = 105."),

 dict(n="M1-21", domain="GT", skill="GT-TR", type="MC",
      stem=("Right triangles ABC and DEF have their right angles at C and at F, and "
            "\\(\\tan A=\\tan D\\). In triangle ABC the length of AC is 15 and the length of BC is 8. "
            "In triangle DEF the length of DF is 45. What is the length of EF?"),
      choices=["16", "20", "24", "40"], correct="C",
      check="tan A = BC/AC = 8/15 and tan D = EF/DF = EF/45, so EF = 45(8/15) = 24."),

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
      stem=("A dye house's tally sheet leads to the equation \\(\\frac{3x+1}{4}=7\\). What is the "
            "value of x?"),
      choices=["7", "9", "11", "27"], correct="B",
      check="Multiplying by 4 gives 3x + 1 = 28, so 3x = 27 and x = 9."),

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
      stem=("A marbler needs n combs, where n is greater than 4 and 3n is less than 21. Which of the "
            "following could be the value of n?"),
      choices=["3", "4", "6", "8"], correct="C",
      check="3n < 21 gives n < 7, and with n > 4 the value must be 5 or 6. Only 6 is listed."),

 dict(n="M2E-06", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A marbling trough holds 5 litres more than twice what a size pan holds, and the trough "
            "holds 47 litres. How many litres does the size pan hold?"),
      answers=["21"],
      check="2p + 5 = 47 gives 2p = 42 and p = 21."),

 dict(n="M2E-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("For a certain dye bath the quantities p and q are related by p = 3q + 7. If p = 34, what "
            "is the value of q?"),
      choices=["9", "11", "13", "41"], correct="A",
      check="3q = 34 - 7 = 27, so q = 9."),

 dict(n="M2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A colourman sets out cakes of pigment in a square block with \\(x+7\\) rows and "
            "\\(x+7\\) cakes in each row. Which expression gives the total number of cakes in the "
            "block?"),
      choices=["\\(x^{2}+49\\)", "\\(x^{2}+7x+49\\)", "\\(x^{2}+14x+49\\)", "2x + 14"],
      correct="C",
      check="The total is (x+7)(x+7), and expanding gives x^2 + 14x + 49."),

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
      stem=("In the xy-plane the graph of \\(y=x^{2}-9\\) crosses the x-axis at (a, 0) and at (b, 0), "
            "where a is less than b. What is the value of b?"),
      choices=["-9", "-3", "3", "9"], correct="C",
      check="x^2 - 9 = 0 gives x = -3 or x = 3, and the greater of the two is 3."),

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
      stem=("Of the 60 skeins in one delivery, 45 were dyed madder. What fraction of the delivery was "
            "dyed madder?"),
      choices=["\\(\\frac{1}{4}\\)", "\\(\\frac{2}{3}\\)", "\\(\\frac{3}{4}\\)",
               "\\(\\frac{4}{3}\\)"], correct="C",
      check="45 of 60 is 45/60, which is 3/4."),

 dict(n="M2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The masses, in grams, of seven cakes of pigment are 24, 31, 24, 40, 24, 31 and 52. What "
            "is the mode of these seven masses, in grams?"),
      choices=["24", "28", "31", "52"], correct="A",
      check="24 occurs three times, more often than any other mass, so the mode is 24."),

 dict(n="M2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the amount of each of four pigments held in a colourman's store."
            + table(["Pigment", "Kilograms held"],
                    [["Ochre", "46"], ["Vermilion", "9"], ["Verdigris", "17"],
                     ["Lampblack", "28"]])
            + "How many kilograms of pigment does the store hold altogether?"),
      choices=["82", "91", "100", "118"], correct="C",
      check="46 + 9 + 17 + 28 = 100 kilograms."),

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
      stem=("A marbler's corner brace is a right triangle whose two legs measure 14 centimetres and 9 "
            "centimetres. What is the area, in square centimetres, of the brace?"),
      answers=["63"],
      check="The area of a right triangle is half the product of its legs, so it is "
            "(1/2)(14)(9) = 63 square centimetres."),

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
      stem=("A dye works makes a standing charge of $90 for a season and then charges $6 for each "
            "skein dyed. A rival works makes no standing charge and charges $9 for each skein dyed. "
            "For how many skeins dyed in a season do the two works charge the same amount?"),
      choices=["10", "15", "30", "45"], correct="C",
      check="90 + 6s = 9s gives 3s = 90 and s = 30."),

 dict(n="M2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A dye works' costing rule leads to the equation \\(4(x-c)=3x+8\\), where c is a "
            "constant. The solution to this equation is x = 20. What is the value of c?"),
      choices=["2", "3", "7", "12"], correct="B",
      check="Substituting x = 20 gives 4(20 - c) = 68, so 80 - 4c = 68 and c = 3."),

 dict(n="M2H-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane a line has its x-intercept at the point (12, 0) and its y-intercept at "
            "the point (0, -8). For what value of x does this line pass through the point (x, -2)?"),
      choices=["3", "6", "9", "10"], correct="C",
      check="The slope is (0-(-8))/(12-0) = 2/3, so the line is y = (2/3)x - 8. Setting y = -2 gives "
            "(2/3)x = 6 and x = 9."),

 dict(n="M2H-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The inequality \\(3x-a>12\\), where a is a constant, is satisfied by exactly those "
            "values of x that are greater than 9. What is the value of a?"),
      choices=["9", "15", "21", "27"], correct="B",
      check="The inequality rearranges to x > (12+a)/3, so (12+a)/3 = 9 gives 12 + a = 27 and "
            "a = 15."),

 dict(n="M2H-05", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A dye vat is filled through a pipe that runs 18 litres a minute, while a waste cock lets "
            "11 litres a minute away. Both run from the moment the empty vat is opened. After how "
            "many minutes does the vat hold 154 litres?"),
      answers=["22"],
      check="The vat gains 18 - 11 = 7 litres a minute, and 154/7 = 22 minutes."),

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
      stem=("A marbled panel 24 centimetres by 18 centimetres is mounted so that a border of the same "
            "width runs all the way round it, and the mounted rectangle covers 616 square "
            "centimetres. What is the width of the border, in centimetres?"),
      choices=["2", "4", "5", "11"], correct="A",
      check="(24+2w)(18+2w) = 616 gives 4w^2 + 84w - 184 = 0, that is w^2 + 21w - 46 = 0, so "
            "(w+23)(w-2) = 0 and the positive width is 2."),

 dict(n="M2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In the xy-plane the graph of \\(y=f(x)\\) has an x-intercept at the point (6, 0). The "
            "graph of \\(y=f(x-4)\\) has an x-intercept at the point (a, 0). What is the value of a?"),
      choices=["2", "4", "10", "24"], correct="C",
      check="f(x-4) is zero when x - 4 = 6, that is when x = 10, so the shifted graph crosses the "
            "x-axis at (10, 0)."),

 dict(n="M2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A colourman's roller setting is a positive number x for which "
            "\\(x+\\frac{1}{x}=5\\). What is the value of \\(x^{2}+\\frac{1}{x^{2}}\\)?"),
      choices=["21", "23", "25", "27"], correct="B",
      check="Squaring both sides of x + 1/x = 5 gives x^2 + 2 + 1/x^2 = 25, so "
            "x^2 + 1/x^2 = 23."),

 dict(n="M2H-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("One solution of the equation \\(x^{2}-kx+18=0\\) is 3, where k is a constant. What is "
            "the other solution?"),
      answers=["6"],
      check="The two solutions multiply to 18, so the other is 18/3 = 6. (Their sum is then 9, "
            "which makes k = 9.)"),

 dict(n="M2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The time a batch of pigment takes to grind varies inversely with the number of mullers "
            "set to work on it. Four mullers grind a batch in 15 hours. How many hours do six mullers "
            "take to grind a batch of the same size?"),
      choices=["8", "10", "12", "22.5"], correct="B",
      check="Inverse variation makes the product of mullers and hours constant, so 4(15) = 6t gives "
            "t = 60/6 = 10 hours."),

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
      stem=("A box holds 60 cakes of colour, and the probability that a cake drawn from it at random "
            "is vermilion is \\(\\frac{2}{5}\\). How many ochre cakes must be added to the box so "
            "that the probability of drawing a vermilion cake becomes \\(\\frac{1}{3}\\)?"),
      choices=["6", "12", "18", "24"], correct="B",
      check="The box holds (2/5)(60) = 24 vermilion cakes. Adding k ochre cakes makes the "
            "probability 24/(60+k), and setting that equal to 1/3 gives 60 + k = 72 and k = 12."),

 dict(n="M2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A square dye tray of side 20 centimetres has the largest possible circle marked on its "
            "floor. What is the area, in square centimetres, of the part of the floor that is inside "
            "the square but outside the circle?"),
      choices=["\\(100-25\\pi\\)", "\\(400-20\\pi\\)", "\\(400-100\\pi\\)",
               "\\(400-400\\pi\\)"], correct="C",
      check="The square has area 400 and the largest circle inside it has radius 10 and area 100pi, "
            "so the region between them has area 400 - 100pi."),

 dict(n="M2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A marbler's triangular scraper has two sides measuring 9 centimetres and 14 centimetres. "
            "Which of the following could be the length, in centimetres, of its third side?"),
      choices=["4", "5", "18", "23"], correct="C",
      check="The third side must be greater than 14 - 9 = 5 and less than 14 + 9 = 23, and 18 is the "
            "only listed length strictly between them."),

 dict(n="M2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A marbler's comb is cut as an isosceles triangle whose two equal sides each measure 26 "
            "centimetres and whose base measures 48 centimetres. What is the sine of one of the two "
            "equal base angles of that triangle?"),
      choices=["\\(\\frac{5}{13}\\)", "\\(\\frac{5}{12}\\)", "\\(\\frac{12}{13}\\)",
               "\\(\\frac{13}{5}\\)"], correct="A",
      check="The perpendicular from the apex halves the base, giving a right triangle with "
            "hypotenuse 26 and one leg 24, so the other leg is 10 and the sine of a base angle is "
            "10/26 = 5/13."),

 dict(n="M2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("A dye vat is a rectangular tank 80 centimetres long and 50 centimetres wide. Liquor is "
            "run into the empty tank at 24 litres a minute for 5 minutes. To what depth, in "
            "centimetres, does the liquor then stand? (1 litre is 1,000 cubic centimetres.)"),
      answers=["30"],
      check="The tank receives 24(5) = 120 litres, which is 120,000 cubic centimetres. The base "
            "covers 80(50) = 4,000 square centimetres, so the depth is 120,000/4,000 = 30."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
