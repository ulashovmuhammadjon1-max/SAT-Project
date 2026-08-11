#!/usr/bin/env python3
"""
Original Math content for Test 26 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item makes a constant, a rate, a
                density or an unknown be recovered first and only then used;
                two or three steps throughout.
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
                One operation, no recovery step.
  MODULE_2_HARD hard: parameters in place of numbers, symbolic answer choices,
                a composed function, a conditioned system, a discriminant
                condition, a two-way table and a weighted mean.

Test 26's assigned thematic territory is bell founding, campanology and change
ringing, organ building, pipe voicing, carillons, tuning and temperament. A
student sits Module 1 plus exactly ONE Module 2 branch, so the territory is
partitioned and no scene is met twice:

  MODULE_1      the bell foundry — bell metal and the crucible, the casting
                pit and the loam mould, turning a bell on the tuning lathe,
                the headstock and the hanging of a bell, shear legs.
  MODULE_2_EASY the ringing chamber — change ringing, the band, practice
                night, quarter peals, striking competitions, rope and sally.
  MODULE_2_HARD organ building and carillons — flue and reed pipes, voicing,
                the windchest, the clavier, equal temperament and semitones.

Three settings that the production bank already uses were checked and
deliberately avoided rather than re-skinned (screen.py found them):
  Test 13 M1S Q1  a two-equation system for handbell/tower-bell bronze
  Test 18 M1S Q18 the mean of a ring of bells with the heaviest removed
  Test 14 M1S Q6  plain and dodging changes at 4 s and 7 s
  Test 18 M2E Q2/Q10, M2H Q20, Test 15 M2E Q14 (tin into copper; a bell-cost
  quadratic evaluated; a cylinder ingot with h = 2r; a struck fork decaying
  exponentially)

House style follows Test 1/2 (CLAUDE.md): bare HTML stems, simple inline maths
left as plain text, real <table> markup for every data table, &deg; as an
entity, function names escaped inside math mode. Every \\( \\) span in this
file was typed by hand; no bulk conversion step was used anywhere.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ---------------------------------------------------------------- Module 1
# The bell foundry: bell metal, the casting pit, the tuning lathe, hanging.
MODULE_1 = [
 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A bell founder weighs the three fittings that go with a new bell. The headstock is "
            "12 kilograms more than three times the mass of the clapper, and the crown staple is "
            "half the mass of the clapper. The three fittings weigh 237 kilograms together. "
            "Machining the headstock is charged at $6 for each kilogram of its mass. How much is "
            "charged for machining the headstock?"),
      choices=["$150", "$300", "$972", "$1,422"], correct="C",
      check="c + (3c+12) + c/2 = 237 gives c = 50, so the headstock is 162 kilograms and 162(6) = 972."),

 dict(n="H1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A charge of bell metal is made up of copper and tin only. The charge contains 4 "
            "kilograms more than five times as much copper as tin, and the whole charge weighs "
            "646 kilograms. Tin costs $26 a kilogram. What is the cost of the tin in the charge?"),
      choices=["$2,782", "$2,808", "$14,014", "$16,796"], correct="A",
      check="t + (5t+4) = 646 gives t = 107 kilograms of tin, and 107(26) = 2,782."),

 dict(n="H1-03", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A foundry quotes for a bell by charging a fixed sum for the loam mould and then a "
            "fixed price for each kilogram of bell metal, so the quote is a linear function of the "
            "mass of the bell. The table gives three of the foundry's quotes. What does the "
            "foundry quote for a bell of mass 500 kilograms?"
            + table(["Mass of bell (kg)", "Quote"],
                    [["180", "$1,480"], ["260", "$1,960"], ["340", "$2,440"]])),
      choices=["$2,920", "$3,000", "$3,400", "$3,880"], correct="C",
      check="The price a kilogram is 480/80 = 6 and the fixed sum is 1,480 - 180(6) = 400, so 500(6) + 400 = 3,400."),

 dict(n="H1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A bell is tuned by taking passes off the inside of its wall on a lathe. The thickness "
            "of the wall at the soundbow is a linear function of the number of passes taken. After "
            "6 passes the wall was 41.4 millimetres thick, and after 15 passes it was 36.0 "
            "millimetres thick. After how many passes is the wall 32.4 millimetres thick?"),
      choices=["18", "21", "24", "27"], correct="B",
      check="The wall thins by 5.4/9 = 0.6 mm a pass, so the thickness is 45 - 0.6n and 32.4 gives n = 21."),

 dict(n="H1-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A founder has $12,500 to spend on one order. Before any metal is bought, $1,300 must "
            "go on loam, firewood and the casting pit. Bell metal costs $16 a kilogram, and each "
            "bell in the order takes 240 kilograms of metal. What is the greatest number of "
            "complete bells the founder can pay for?"),
      choices=["2", "3", "4", "5"], correct="A",
      check="12,500 - 1,300 = 11,200 dollars buys 11,200/16 = 700 kilograms, and 700/240 is 2 whole bells."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A founder casts a set of six bells whose masses, from lightest to heaviest, increase "
            "by the same number of kilograms from one bell to the next. The lightest bell is 152 "
            "kilograms and each bell is 84 kilograms heavier than the one before it. What is the "
            "total mass of the six bells, in kilograms?"),
      choices=["1,952", "2,172", "2,256", "2,592"], correct="B",
      check="The heaviest is 152 + 5(84) = 572, and six bells averaging (152+572)/2 = 362 give 2,172."),

 dict(n="H1-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A founder casts two bells from one melt. The larger bell has 4 times the mass of the "
            "smaller bell. If 90 kilograms of metal were moved from the larger bell to the smaller "
            "bell, the two bells would have equal masses. What is the mass, in kilograms, of the "
            "larger bell?"),
      answers=["240"],
      check="x + 90 = 4x - 90 gives x = 60 for the smaller bell, so the larger bell is 240 kilograms."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{6x^{2}+13x-5}{2x+5}\\) , where "
            "\\(x\\ne -\\frac{5}{2}\\) ?"),
      choices=["\\(2x+5\\)", "\\(3x+1\\)", "\\(6x-1\\)", "\\(3x-1\\)"], correct="D",
      check="6x^2 + 13x - 5 factors as (2x+5)(3x-1), so cancelling 2x+5 leaves 3x-1."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("When a founder tunes n bells at one setting of the lathe, the cost of finishing each "
            "bell, in dollars, is modelled by \\(C(n)=n^{2}-36n+520\\). According to this model, "
            "what is the least cost of finishing one bell?"),
      choices=["$160", "$196", "$260", "$324"], correct="B",
      check="The least value is at n = 36/2 = 18, and 324 - 648 + 520 = 196."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("What is the solution to the equation \\(\\sqrt{x+31}=x+1\\) ?"),
      choices=["\\(-6\\)", "3", "5", "18"], correct="C",
      check="Squaring gives x^2 + x - 30 = 0, whose roots are 5 and -6; only 5 satisfies the original equation."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("Before tuning begins, 640 grams of metal stand above the finished profile of a bell. "
            "Each pass on the lathe removes 8 percent of the metal that still stands above that "
            "profile. Which expression gives the mass of metal, in grams, still above the profile "
            "after n passes?"),
      choices=["\\(640(0.92)^{n}\\)", "\\(640(1.08)^{n}\\)", "\\(640(0.08)^{n}\\)",
               "\\(640-0.08n\\)"], correct="A",
      check="Removing 8 percent leaves 92 percent, so the mass is multiplied by 0.92 once for each pass."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="FR",
      stem=("For the polynomial \\(f(x)=2x^{3}+ax^{2}-11x+6\\) , where a is a constant, "
            "\\(f(3)=0\\) . What is the value of a?"),
      answers=["-3"],
      check="54 + 9a - 33 + 6 = 0 gives 9a = -27 and a = -3."),

 dict(n="H1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives the value of the function f at each of five values of x. What is the "
            "value of \\(f(f(2))\\) ?"
            + table(["x", "1", "2", "3", "4", "5"], [["f(x)", "3", "5", "1", "2", "4"]])),
      choices=["1", "2", "4", "5"], correct="C",
      check="f(2) = 5 and f(5) = 4."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Bell metal has a density of 8.7 grams for each cubic centimetre. A bell is poured, "
            "and 4 percent of the metal poured is then turned off on the tuning lathe, leaving a "
            "finished bell of mass 522 kilograms. What volume of metal, in cubic centimetres, was "
            "poured?"),
      choices=["60,000", "62,400", "62,500", "65,250"], correct="C",
      check="522/0.96 = 543.75 kilograms were poured, and 543,750 grams divided by 8.7 is 62,500 cubic centimetres."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Before casting a bell of mass 1,216 kilograms, a founder makes a model of it in the "
            "same metal, with every length one quarter of the corresponding length on the bell. "
            "What is the mass of the model, in kilograms?"),
      choices=["4.75", "19", "76", "304"], correct="B",
      check="Every length is scaled by 1/4, so the volume and the mass are scaled by (1/4)^3 = 1/64, and 1,216/64 = 19."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A tuning lathe takes 45 grams of metal off a bell each minute that it runs. The lathe "
            "is run for 7 hours on each working day. How many working days does it take to remove "
            "113.4 kilograms of metal?"),
      answers=["6"],
      check="45 grams a minute for 420 minutes is 18,900 grams, so 18.9 kilograms a day, and 113.4/18.9 = 6."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("A foundry cast four sets of bells last year. The table gives, for each set, the "
            "number of castings made and the number of those castings rejected for flaws. For "
            "which set was the greatest percentage of the castings rejected?"
            + table(["Set", "Castings made", "Castings rejected"],
                    [["Set A", "45", "6"], ["Set B", "60", "9"],
                     ["Set C", "36", "5"], ["Set D", "72", "11"]])),
      choices=["Set A", "Set B", "Set C", "Set D"], correct="D",
      check="The four rates are 6/45 = 13.3, 9/60 = 15.0, 5/36 = 13.9 and 11/72 = 15.3 percent, and Set D is greatest."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Of the 240 castings a foundry made last year, 18 were rejected for a flawed lip and "
            "12 were rejected for a blowhole; 3 castings had both faults. One of the 240 castings "
            "is selected at random. What is the probability that it was rejected for at least one "
            "of these two faults?"),
      choices=["\\(\\frac{1}{20}\\)", "\\(\\frac{3}{40}\\)", "\\(\\frac{9}{80}\\)",
               "\\(\\frac{1}{8}\\)"], correct="C",
      check="18 + 12 - 3 = 27 castings had at least one fault, and 27/240 = 9/80."),

 dict(n="H1-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A bell is lifted into a tower on a pair of shear legs. Each leg is a straight timber "
            "7.5 metres long, the two feet rest on level ground, the tops of the legs meet at a "
            "point, and each leg makes an angle of 68&deg; with the ground. How far apart are the "
            "feet of the two legs, to the nearest tenth of a metre?"),
      choices=["2.8", "5.6", "7.0", "13.9"], correct="B",
      check="Each foot is 7.5 cos 68 degrees from the point below the apex, so the feet are 15 cos 68 = 5.6 metres apart."),

 dict(n="H1-20", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle ABC, point D lies on side AB and point E lies on side AC, and segment DE "
            "is parallel to side BC. The length of AD is 12, the length of DB is 8, and the length "
            "of DE is 18. What is the length of BC?"),
      choices=["12", "24", "27", "30"], correct="D",
      check="AD/AB = 12/20 = 3/5 and the triangles are similar, so BC = 18(5/3) = 30."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="MC",
      stem=("The headstock a bell hangs from is an oak beam 1.4 metres long whose cross-section is "
            "a square of side 22 centimetres. Oak has a density of 0.72 grams for each cubic "
            "centimetre. What is the mass of the beam, in kilograms, to the nearest tenth?"),
      choices=["4.9", "33.9", "48.8", "67.8"], correct="C",
      check="140(22)(22) = 67,760 cubic centimetres, and 67,760(0.72) = 48,787.2 grams, or 48.8 kilograms."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="MC",
      stem=("A cylindrical ingot of bell metal has a radius of 6 centimetres and a height of 25 "
            "centimetres. The ingot is melted down and recast as a solid cube of the same metal. "
            "What is the edge length of the cube, in centimetres, to the nearest tenth?"),
      choices=["13.0", "14.1", "15.0", "30.0"], correct="B",
      check="The volume is 900 pi, about 2,827.43 cubic centimetres, and its cube root is 14.1."),
]

# ---------------------------------------------------------- Module 2 (Easy)
# The ringing chamber: change ringing, the band, practice night, striking.
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("On practice night each member of the band rang 5 touches and the visitors rang 13 "
            "touches between them. A total of 63 touches were rung. How many members does the "
            "band have?"),
      choices=["10", "13", "15", "50"], correct="A",
      check="5b + 13 = 63 gives 5b = 50 and b = 10."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A quarter peal of 1,260 changes was rung at a steady rate of 42 changes each minute. "
            "How many minutes did the quarter peal take?"),
      answers=["30"],
      check="1,260 divided by 42 is 30 minutes."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LE", type="MC",
      stem=("If \\(4(x-7)=36\\) , what is the value of x?"),
      choices=["2", "9", "16", "29"], correct="C",
      check="Dividing by 4 gives x - 7 = 9, so x = 16."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("At a striking competition each band starts with 100 marks and loses 3 marks for every "
            "fault the judges record, so a band with f faults scores S = 100 - 3f marks. How many "
            "marks does a band with 14 faults score?"),
      choices=["14", "42", "55", "58"], correct="D",
      check="100 - 3(14) = 100 - 42 = 58."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The ringing chamber holds at most 15 people at one time. There are already 6 people "
            "in the chamber. Which inequality gives all possible numbers n of further people who "
            "may come up into the chamber?"),
      choices=["\\(n\\le 9\\)", "\\(n\\le 6\\)", "\\(n\\ge 9\\)", "\\(n\\le 15\\)"], correct="A",
      check="6 + n is at most 15, so n is at most 9."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, a line passes through the points (2, 11) and (6, 27). What is the "
            "slope of this line?"),
      choices=["2", "4", "8", "16"], correct="B",
      check="(27 - 11)/(6 - 2) = 16/4 = 4."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("If \\(9-2x=-7\\) , what is the value of x?"),
      choices=["\\(-8\\)", "\\(-1\\)", "1", "8"], correct="D",
      check="-2x = -16, so x = 8."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\((x+7)(x-3)\\) ?"),
      choices=["\\(x^{2}+4x-21\\)", "\\(x^{2}-4x-21\\)", "\\(x^{2}+10x-21\\)",
               "\\(x^{2}+4x+21\\)"], correct="A",
      check="x^2 - 3x + 7x - 21 = x^2 + 4x - 21."),

 dict(n="H2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function g is defined by \\(g(x)=x^{2}-5x\\) . What is the value of "
            "\\(g(-3)\\) ?"),
      choices=["\\(-24\\)", "\\(-6\\)", "6", "24"], correct="D",
      check="9 - (-15) = 9 + 15 = 24."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NE", type="FR",
      stem=("What is the positive solution to the equation \\(x^{2}-144=0\\) ?"),
      answers=["12"],
      check="x^2 = 144, so the positive solution is 12."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function N is defined by \\(N(t)=4(3)^{t}\\) . What is the value of "
            "\\(N(3)\\) ?"),
      choices=["36", "64", "108", "216"], correct="C",
      check="3 cubed is 27, and 4(27) = 108."),

 dict(n="H2E-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\((5x^{2})(2x^{3})\\) ?"),
      choices=["\\(7x^{5}\\)", "\\(7x^{6}\\)", "\\(10x^{5}\\)", "\\(10x^{6}\\)"], correct="C",
      check="5(2) = 10 and the exponents add to give x^5."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives three values of the linear function g. What is the value of "
            "\\(g(4)\\) ?"
            + table(["x", "1", "2", "3"], [["g(x)", "7", "12", "17"]])),
      choices=["20", "22", "24", "27"], correct="B",
      check="The function increases by 5 for each increase of 1 in x, so g(4) = 17 + 5 = 22."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A band rang 36 changes in 4 minutes at a steady rate. How many changes did the band "
            "ring each minute?"),
      choices=["4", "9", "32", "144"], correct="B",
      check="36 divided by 4 is 9."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="FR",
      stem=("A tower keeps a list of 340 ringers who have rung there. Of these, 15 percent have "
            "rung a full peal in the tower. How many of the ringers on the list have rung a full "
            "peal in the tower?"),
      answers=["51"],
      check="15 percent of 340 is 0.15(340) = 51."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A tower captain recorded the number of ringers present on each of seven practice "
            "nights: 24, 31, 19, 27, 22, 35, 29. What is the median of these seven numbers?"),
      choices=["24", "27", "29", "31"], correct="B",
      check="In order the numbers are 19, 22, 24, 27, 29, 31, 35, and the fourth is 27."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of ringers who came to practice night at each of four "
            "towers. How many more ringers came to Barford than to Abbotsbury?"
            + table(["Tower", "Ringers"],
                    [["Abbotsbury", "19"], ["Barford", "30"],
                     ["Chelworth", "23"], ["Dunmow", "26"]])),
      choices=["11", "13", "15", "19"], correct="A",
      check="30 - 19 = 11."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Of the 48 ringers at a district meeting, 12 had rung a full peal. One of the 48 "
            "ringers is selected at random. What is the probability that the ringer selected had "
            "rung a full peal?"),
      choices=["\\(\\frac{1}{6}\\)", "\\(\\frac{1}{4}\\)", "\\(\\frac{1}{3}\\)",
               "\\(\\frac{3}{4}\\)"], correct="B",
      check="12/48 = 1/4."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The wheel that carries a bell rope is a circle of radius 0.6 metres. What is the "
            "circumference of this circle, in metres?"),
      choices=["\\(0.36\\pi\\)", "\\(0.6\\pi\\)", "\\(1.2\\pi\\)", "\\(2.4\\pi\\)"], correct="C",
      check="The circumference is 2 pi r, and 2(0.6) = 1.2."),

 dict(n="H2E-20", domain="GT", skill="GT-LA", type="MC",
      stem=("In a triangle, two of the interior angles measure 47&deg; and 68&deg;. What is the "
            "measure of the third interior angle?"),
      choices=["65&deg;", "68&deg;", "115&deg;", "133&deg;"], correct="A",
      check="180 - 47 - 68 = 65."),

 dict(n="H2E-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC, the right angle is at C, the length of AB is 17, and the "
            "length of BC is 8. What is the value of \\(\\sin A\\) ?"),
      choices=["\\(\\frac{8}{15}\\)", "\\(\\frac{8}{17}\\)", "\\(\\frac{15}{17}\\)",
               "\\(\\frac{17}{8}\\)"], correct="B",
      check="Angle A is opposite BC and AB is the hypotenuse, so sin A = 8/17."),

 dict(n="H2E-22", domain="GT", skill="GT-AV", type="MC",
      stem=("A circle has a radius of 5 centimetres. What is the area of this circle, in square "
            "centimetres?"),
      choices=["\\(5\\pi\\)", "\\(10\\pi\\)", "\\(25\\pi\\)", "\\(100\\pi\\)"], correct="C",
      check="The area is pi r squared, and 5 squared is 25."),
]

# ---------------------------------------------------------- Module 2 (Hard)
# Organ building and carillons: flue and reed pipes, voicing, the windchest,
# the clavier, equal temperament and semitones.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A voicer takes f hours over each flue pipe and r hours over each reed pipe. One "
            "week's work and the next week's work give the system of equations below.<br/>"
            "3f + 2r = 51<br/>5f + 4r = 93<br/>What is the value of r?"),
      choices=["9", "12", "15", "21"], correct="B",
      check="Doubling the first equation gives 6f + 4r = 102; subtracting the second leaves f = 9, and then r = 12."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, a line passes through the points \\((a,\\ 3a)\\) and "
            "\\((3a,\\ 11a)\\) , where a is a positive constant. What is the y-coordinate of the "
            "y-intercept of this line, in terms of a?"),
      choices=["\\(-a\\)", "\\(a\\)", "\\(-4a\\)", "\\(3a\\)"], correct="A",
      check="The slope is 8a/2a = 4, and 3a - 4(a) = -a."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("An organ builder has 240 hours of shop time and $6,400 for materials. Each flue pipe "
            "takes 3 hours and $50 of material, and each reed pipe takes 5 hours and $160 of "
            "material. The specification requires at least twice as many flue pipes as reed pipes. "
            "What is the greatest number of reed pipes the builder can make?"),
      choices=["12", "16", "18", "21"], correct="D",
      check="Taking exactly twice as many flue pipes uses the least of both resources: 11r hours at most 240 "
            "gives r at most 21, and 260r dollars at most 6,400 gives r at most 24."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the system of equations below, k is a constant and the system has infinitely many "
            "solutions.<br/>6x + ky = 18<br/>9x + 12y = 27<br/>What is the value of k?"),
      choices=["4", "8", "12", "18"], correct="B",
      check="Multiplying the first equation by 3/2 gives 9x + 1.5ky = 27, so 1.5k = 12 and k = 8."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The function h is linear, and a is a positive constant. If \\(h(2)=5a\\) and "
            "\\(h(6)=13a\\) , what is the value of \\(h(10)\\) in terms of a?"),
      choices=["\\(17a\\)", "\\(19a\\)", "\\(21a\\)", "\\(26a\\)"], correct="C",
      check="The slope is 8a/4 = 2a, so h(10) = 13a + 4(2a) = 21a."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LE", type="FR",
      stem=("Three ranks on an organ contain 183 pipes between them. The second rank contains 12 "
            "more pipes than the first rank, and the third rank contains 9 fewer pipes than three "
            "times the first rank. How many pipes does the third rank contain?"),
      answers=["99"],
      check="p + (p+12) + (3p-9) = 183 gives 5p = 180 and p = 36, so the third rank has 3(36) - 9 = 99."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("What is the greatest integer value of x that satisfies "
            "\\(\\frac{2x-5}{3}\\le\\frac{x+4}{2}\\) ?"),
      choices=["11", "17", "22", "34"], correct="C",
      check="Multiplying by 6 gives 4x - 10 at most 3x + 12, so x is at most 22."),

 dict(n="H2H-08", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g are defined by \\(f(x)=x^{2}+5x\\) and \\(g(x)=x-3\\) . Which "
            "expression is equivalent to \\(f(g(x))\\) ?"),
      choices=["\\(x^{2}-x-6\\)", "\\(x^{2}-6x+9\\)", "\\(x^{2}+5x-3\\)",
               "\\(x^{2}-11x+24\\)"], correct="A",
      check="(x-3)^2 + 5(x-3) = x^2 - 6x + 9 + 5x - 15 = x^2 - x - 6."),

 dict(n="H2H-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{3}{x-2}-\\frac{2}{x+1}\\) , where "
            "\\(x\\ne 2\\) and \\(x\\ne -1\\) ?"),
      choices=["\\(\\frac{1}{x^{2}-x-2}\\)", "\\(\\frac{x+7}{x^{2}-x-2}\\)",
               "\\(\\frac{5x-1}{x^{2}-x-2}\\)", "\\(\\frac{x-7}{x^{2}-x-2}\\)"], correct="B",
      check="3(x+1) - 2(x-2) = x + 7 over the common denominator (x-2)(x+1) = x^2 - x - 2."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="FR",
      stem=("In the equation \\(2x^{2}+bx+72=0\\) , b is a positive constant and the equation has "
            "exactly one real solution. What is the value of b?"),
      answers=["24"],
      check="One real solution needs b^2 - 4(2)(72) = 0, so b^2 = 576 and the positive value is 24."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In equal temperament the octave is divided into twelve equal steps, so a pipe n "
            "semitones above a pipe of frequency F sounds a frequency of "
            "\\(F\\left(2^{\\frac{n}{12}}\\right)\\) . A rank contains a pipe 19 semitones above a "
            "given pipe and a pipe 7 semitones above the same given pipe. The frequency of the "
            "first of these is how many times the frequency of the second?"),
      choices=["2", "4", "\\(2^{\\frac{13}{12}}\\)", "\\(2^{\\frac{19}{7}}\\)"], correct="A",
      check="The ratio is 2^(19/12) divided by 2^(7/12), which is 2^(12/12) = 2."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\(\\frac{a^{\\frac{5}{6}}}{a^{\\frac{1}{3}}}\\) , "
            "where a is a positive constant?"),
      choices=["\\(a^{\\frac{1}{3}}\\)", "\\(a^{\\frac{1}{2}}\\)", "\\(a^{\\frac{5}{18}}\\)",
               "\\(a^{\\frac{7}{6}}\\)"], correct="B",
      check="Subtracting the exponents gives 5/6 - 2/6 = 1/2."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The graph of \\(x^{2}+y^{2}=45\\) and the graph of \\(y=2x\\) intersect at two "
            "points in the xy-plane. What is the product of the x-coordinates of these two "
            "points?"),
      choices=["\\(-27\\)", "\\(-18\\)", "\\(-9\\)", "3"], correct="C",
      check="Substituting gives 5x^2 = 45, so x = 3 or x = -3 and the product is -9."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A carillon has n bells whose masses total m kilograms. A further bell, of mass "
            "\\(\\frac{3m}{n}\\) kilograms, is added to the carillon. Which expression gives the "
            "mean mass, in kilograms, of the bells the carillon then has?"),
      choices=["\\(\\frac{3m}{n+1}\\)", "\\(\\frac{m+3}{n+1}\\)", "\\(\\frac{m(n+3)}{n}\\)",
               "\\(\\frac{m(n+3)}{n(n+1)}\\)"], correct="D",
      check="The new total is m + 3m/n = m(n+3)/n over n + 1 bells."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the 330 pipes of an organ, classified by the kind of pipe and by the "
            "metal the pipe is made from. One of the 330 pipes is selected at random. Given that "
            "the pipe selected is a reed pipe, what is the probability that it is made of "
            "tin-rich metal?"
            + table(["", "Tin-rich", "Lead-rich", "Total"],
                    [["Flue pipes", "84", "156", "240"],
                     ["Reed pipes", "63", "27", "90"],
                     ["Total", "147", "183", "330"]])),
      choices=["\\(\\frac{7}{33}\\)", "\\(\\frac{3}{10}\\)", "\\(\\frac{3}{7}\\)",
               "\\(\\frac{7}{10}\\)"], correct="D",
      check="Of the 90 reed pipes, 63 are tin-rich, and 63/90 = 7/10."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A tuner's fee for one visit rose by 8 percent one year and then by a further 5 "
            "percent the next year, bringing it to $1,701. What was the fee before the two rises?"),
      choices=["$1,500", "$1,530", "$1,559", "$1,650"], correct="A",
      check="The fee was multiplied by 1.08 and then by 1.05, so it was 1,701/1.134 = 1,500."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A voicer measured the mouth width of each of 20 pipes and found the mean of the 20 "
            "measurements to be 32.4 millimetres. One of the measurements was then found to have "
            "been recorded as 19.2 millimetres when it should have been 9.2 millimetres. What is "
            "the mean of the 20 measurements once this one is corrected?"),
      choices=["31.4", "31.5", "31.9", "32.9"], correct="C",
      check="The total falls from 20(32.4) = 648 to 638, and 638/20 = 31.9."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of pipes in each of three ranks of an organ and the mean "
            "speaking length of the pipes in that rank. What is the mean speaking length, in "
            "centimetres, of all 100 of these pipes?"
            + table(["Rank", "Number of pipes", "Mean speaking length (cm)"],
                    [["Open Diapason", "50", "96"], ["Principal", "30", "60"],
                     ["Fifteenth", "20", "30"]])),
      choices=["62", "72", "78", "95"], correct="B",
      check="50(96) + 30(60) + 20(30) = 7,200 centimetres over 100 pipes, giving 72."),

 dict(n="H2H-19", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC, the right angle is at C and \\(\\sin A=\\frac{5}{13}\\) . "
            "What is the value of \\(\\cos B\\) ?"),
      choices=["\\(\\frac{5}{13}\\)", "\\(\\frac{5}{12}\\)", "\\(\\frac{12}{13}\\)",
               "\\(\\frac{13}{5}\\)"], correct="A",
      check="Angles A and B are complementary in a right triangle, so cos B equals sin A, which is 5/13."),

 dict(n="H2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A circle has a radius of 25 centimetres. A chord of this circle lies 20 centimetres "
            "from the centre of the circle. What is the length of the chord, in centimetres?"),
      choices=["12", "20", "24", "30"], correct="D",
      check="Half the chord, the distance 20 and the radius 25 form a right triangle, so half the chord is 15."),

 dict(n="H2H-21", domain="GT", skill="GT-AV", type="MC",
      stem=("An organ pipe is made as an open cylinder of sheet metal, with no metal at either "
            "end, so the metal used is the curved surface only. A second pipe is made with twice "
            "the radius of the first and half the length of the first. The area of metal in the "
            "second pipe is how many times the area of metal in the first?"),
      choices=["\\(\\frac{1}{2}\\)", "1", "2", "4"], correct="B",
      check="The curved surface is 2 pi r L, and doubling r while halving L leaves the product unchanged."),

 dict(n="H2H-22", domain="GT", skill="GT-AV", type="FR",
      stem=("The resonator of a reed pipe is a solid cone. A plane parallel to the base of the "
            "cone cuts it at the midpoint of its axis, separating a smaller cone at the top. What "
            "fraction of the volume of the whole cone is the volume of the smaller cone?"),
      answers=["1/8", "0.125"],
      check="Every length in the smaller cone is half the corresponding length, so the volume ratio is (1/2)^3 = 1/8."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
