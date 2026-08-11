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
                a composed function, a conditioned system, a discriminant-style
                condition, a two-way table and a weighted mean.

Test 26's assigned thematic territory is bell founding, campanology and change
ringing, organ building, pipe voicing, carillons, tuning and temperament. A
student sits Module 1 plus exactly ONE Module 2 branch, so the territory is
partitioned and no scene is met twice:

  MODULE_1      the bell foundry — bell metal and the crucible, the casting
                pit and the loam mould, turning a bell on the tuning lathe,
                the headstock, shear legs.
  MODULE_2_EASY the ringing chamber — change ringing, the band, practice
                night, quarter peals, striking competitions, rope and sally.
  MODULE_2_HARD organ building and carillons — flue and reed pipes, voicing,
                ranks and scaling, the clavier, equal temperament, semitones.

Settings that the production bank already uses were found by screen.py and
avoided rather than re-skinned: Test 13 M1S Q1 (a two-equation system for
handbell/tower-bell bronze), Test 18 M1S Q18 (the mean of a ring of bells with
the heaviest removed), Test 14 M1S Q6 (plain and dodging changes at 4 s and
7 s), Test 18 M2E Q2/Q10 and M2H Q20, Test 15 M2E Q14.

Twenty-three first drafts were discarded as template repeats after screening —
the reasons are recorded in MANIFEST.md. Almost all of them scored BELOW the
0.75 reject line, which is why every candidate was read rather than scored.

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
      choices=["$150", "$300", "$486", "$972"], correct="D",
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
      choices=["$3,000", "$3,400", "$3,520", "$3,880"], correct="B",
      check="The price a kilogram is 480/80 = 6 and the fixed sum is 1,480 - 180(6) = 400, so 500(6) + 400 = 3,400."),

 dict(n="H1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A bell is tuned by taking passes off the inside of its wall on a lathe. The thickness "
            "of the wall at the soundbow is a linear function of the number of passes taken. After "
            "6 passes the wall was 41.4 millimetres thick, and after 15 passes it was 36.0 "
            "millimetres thick. After how many passes is the wall 32.4 millimetres thick?"),
      choices=["12", "15", "18", "21"], correct="D",
      check="The wall thins by 5.4/9 = 0.6 mm a pass, so the thickness is 45 - 0.6n and 32.4 gives n = 21."),

 dict(n="H1-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A founder has $12,500 to spend on one order. Before any metal is bought, $1,300 must "
            "go on loam, firewood and preparing the casting pit. Bell metal costs $16 a kilogram, "
            "and each bell in the order takes 240 kilograms of metal. What is the greatest number "
            "of complete bells the founder can pay for?"),
      choices=["2", "3", "4", "5"], correct="A",
      check="12,500 - 1,300 = 11,200 dollars buys 11,200/16 = 700 kilograms, and 700/240 is 2 whole bells."),

 dict(n="H1-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A founder casts a set of six bells whose masses, from lightest to heaviest, increase "
            "by the same number of kilograms from one bell to the next. The lightest bell is 152 "
            "kilograms and each bell is 84 kilograms heavier than the one before it. What is the "
            "total mass of the six bells, in kilograms?"),
      choices=["2,172", "2,256", "2,592", "3,432"], correct="A",
      check="The heaviest is 152 + 5(84) = 572, and six bells averaging (152+572)/2 = 362 give 2,172."),

 dict(n="H1-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A founder casts two bells from one melt. The larger bell has 4 times the mass of the "
            "smaller bell. If 90 kilograms of metal were moved from the larger bell to the smaller "
            "bell, the two bells would have equal masses. What is the mass, in kilograms, of the "
            "larger bell?"),
      answers=["240"],
      check="x + 90 = 4x - 90 gives x = 60 for the smaller bell, so the larger bell is 240 kilograms."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A founder's costing sheet carries the expression \\(\\frac{x^{2}-9}{x^{2}+7x+12}\\) . "
            "For x greater than 3, which of the following is equal to that expression?"),
      choices=["\\(\\frac{x+3}{x+4}\\)", "\\(\\frac{x-3}{x-4}\\)", "\\(\\frac{x+3}{x-4}\\)",
               "\\(\\frac{x-3}{x+4}\\)"], correct="D",
      check="The numerator is (x-3)(x+3) and the denominator is (x+3)(x+4), so the factor x+3 cancels."),

 dict(n="H1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("When a founder tunes n bells at one setting of the lathe, the cost of finishing each "
            "bell, in dollars, is modelled by \\(C(n)=n^{2}-36n+520\\) . According to this model, "
            "what is the least cost of finishing one bell?"),
      choices=["$98", "$124", "$160", "$196"], correct="D",
      check="The least value is at n = 36/2 = 18, and 324 - 648 + 520 = 196."),

 dict(n="H1-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The number of minutes x for which a crucible is held at pouring heat satisfies "
            "\\(\\frac{18}{x}=x-3\\) . What is the positive value of x?"),
      choices=["6", "9", "12", "18"], correct="A",
      check="Multiplying by x gives x^2 - 3x - 18 = 0, whose roots are 6 and -3, and only 6 is positive."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("Before tuning begins, 640 grams of metal stand above the finished profile of a bell. "
            "Each pass on the lathe removes 8 percent of the metal that still stands above that "
            "profile. Which expression gives the mass of metal, in grams, still above the profile "
            "after n passes?"),
      choices=["\\(640(0.92)^{n}\\)", "\\(640(1.08)^{n}\\)", "\\(640(0.08)^{n}\\)",
               "\\(640-0.08n\\)"], correct="A",
      check="Removing 8 percent leaves 92 percent, so the mass is multiplied by 0.92 once for each pass."),

 dict(n="H1-12", domain="ADV", skill="ADV-EQ", type="FR",
      stem=("The product \\((3x-4)(2x+7)\\) is equivalent to \\(6x^{2}+bx-28\\) , where b is a "
            "constant. What is the value of b?"),
      answers=["13"],
      check="The x terms are 21x and -8x, so b = 21 - 8 = 13."),

 dict(n="H1-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A founder's model for the cost of finishing a batch is \\(f(x)=(x-3)(x-11)\\) . In "
            "the xy-plane the curve \\(y=f(x)\\) is a parabola. What is the x-coordinate of the "
            "vertex of that parabola?"),
      choices=["5", "6", "7", "11"], correct="C",
      check="The curve meets the x-axis at 3 and 11, and the vertex lies halfway between them at 7."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Bell metal has a density of 8.7 grams for each cubic centimetre. A bell is poured, "
            "and 4 percent of the metal poured is then turned off on the tuning lathe, leaving a "
            "finished bell of mass 522 kilograms. What volume of metal, in cubic centimetres, was "
            "poured?"),
      choices=["60,000", "62,500", "65,250", "67,875"], correct="B",
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
      stem=("The table gives the mass of each of four bells a foundry cast last year and the price "
            "the foundry charged for it. For which bell was the price for each kilogram of mass "
            "the lowest?"
            + table(["Bell", "Mass (kg)", "Price charged"],
                    [["Bell A", "240", "$1,560"], ["Bell B", "360", "$2,232"],
                     ["Bell C", "480", "$2,832"], ["Bell D", "600", "$3,660"]])),
      choices=["Bell A", "Bell B", "Bell C", "Bell D"], correct="C",
      check="The four prices a kilogram are 6.50, 6.20, 5.90 and 6.10 dollars, and Bell C is the lowest."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Of the 240 castings a foundry made last year, 18 were rejected for a flawed lip and "
            "12 were rejected for a blowhole; 3 castings had both faults. One of the 240 castings "
            "is selected at random. What is the probability that it was rejected for at least one "
            "of these two faults?"),
      choices=["\\(\\frac{1}{20}\\)", "\\(\\frac{3}{40}\\)", "\\(\\frac{9}{80}\\)",
               "\\(\\frac{1}{8}\\)"], correct="C",
      check="18 + 12 - 3 = 27 castings had at least one fault, and 27/240 = 9/80."),

 dict(n="H1-19", domain="GT", skill="GT-TR", type="MC",
      stem=("A bell is lifted onto its headstock with a pair of shear legs. Each leg is a straight "
            "timber 7.5 metres long, the two feet rest on level ground, the tops of the legs meet "
            "at a point, and each leg makes an angle of 68&deg; with the ground. How far apart are "
            "the feet of the two legs, to the nearest tenth of a metre?"),
      choices=["2.8", "5.6", "7.0", "13.9"], correct="B",
      check="Each foot is 7.5 cos 68 degrees from the point below the apex, so the feet are 15 cos 68 = 5.6 metres apart."),

 dict(n="H1-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A bell frame is braced by a triangle ABC in which angle B is a right angle, the "
            "length of AB is 10 and the length of BC is 24. Point M is the midpoint of side AC. "
            "What is the length of BM?"),
      choices=["5", "12", "13", "26"], correct="C",
      check="AC is 26 by the Pythagorean theorem, and the midpoint of the hypotenuse is 13 from all three vertices."),

 dict(n="H1-21", domain="GT", skill="GT-AV", type="MC",
      stem=("The headstock a bell hangs from is an oak beam 1.4 metres long whose cross-section is "
            "a square of side 22 centimetres. Oak has a density of 0.72 grams for each cubic "
            "centimetre. What is the mass of the beam, in kilograms, to the nearest tenth?"),
      choices=["33.9", "48.8", "67.8", "135.5"], correct="B",
      check="140(22)(22) = 67,760 cubic centimetres, and 67,760(0.72) = 48,787.2 grams, or 48.8 kilograms."),

 dict(n="H1-22", domain="GT", skill="GT-AV", type="MC",
      stem=("The inside of a crucible is a cylinder 42 centimetres across and 60 centimetres deep. "
            "Bell metal fills the crucible to within 8 centimetres of the top. What is the volume "
            "of the metal, in cubic centimetres, in terms of \\(\\pi\\) ?"),
      choices=["\\(8{,}820\\pi\\)", "\\(11{,}466\\pi\\)", "\\(22{,}932\\pi\\)",
               "\\(26{,}460\\pi\\)"], correct="C",
      check="The radius is 21 and the depth of metal is 52, so the volume is 21 squared times 52 times pi."),
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
      stem=("On practice night a band rang three touches of the same length and one touch of 120 "
            "changes, 528 changes in all. How many changes were in each of the three touches of "
            "equal length?"),
      choices=["120", "136", "176", "216"], correct="B",
      check="528 - 120 = 408 changes were shared equally between three touches, and 408/3 = 136."),

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
      stem=("A learner's mark in a striking test improves by the same number of marks each week. "
            "In week 2 the learner scored 11 marks and in week 6 the learner scored 27 marks. By "
            "how many marks does the learner's score improve each week?"),
      choices=["2", "4", "8", "16"], correct="B",
      check="(27 - 11)/(6 - 2) = 16/4 = 4."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LE", type="MC",
      stem=("The tower fund held $1,240. New bell ropes cost $85 each, and after buying r of them "
            "the fund held $815. What is the value of r?"),
      choices=["3", "4", "5", "9"], correct="C",
      check="1,240 - 85r = 815 gives 85r = 425 and r = 5."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A ringing master writes the number of blows struck in a touch as \\(6x^{2}+15x\\) . "
            "Which of the following is that expression in factored form?"),
      choices=["\\(3x(2x+5)\\)", "\\(3(2x^{2}+5)\\)", "\\(3x(2x^{2}+5x)\\)", "\\(6x(x+15)\\)"],
      correct="A",
      check="3x is the greatest common factor, and 6x^2/3x = 2x while 15x/3x = 5."),

 dict(n="H2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of ringers a tower can call on in week w of a recruiting drive is modelled "
            "by \\(A(w)=w^{2}-5w+40\\) . What number does this model give for week 6?"),
      choices=["40", "42", "44", "46"], correct="D",
      check="36 - 30 + 40 = 46."),

 dict(n="H2E-10", domain="ADV", skill="ADV-NE", type="FR",
      stem=("In the equation \\(x^{2}=3x\\) , the value of x is not 0. What is the value of x?"),
      answers=["3"],
      check="Dividing both sides by x, which is not 0, leaves x = 3."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A tower keeps its bell fund in an account, and the balance in the account after t "
            "years is \\(B(t)=1{,}800(1.04)^{t}\\) dollars. What is the balance, in dollars, at "
            "the moment the account is opened?"),
      choices=["$1,800", "$1,804", "$1,872", "$4,680"], correct="A",
      check="At the moment the account is opened t is 0, and 1.04 to the power 0 is 1, so the balance is 1,800."),

 dict(n="H2E-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A ringing master records the number of blows in a course as \\((x+6)^{2}\\) . Which "
            "of the following is equivalent to that expression?"),
      choices=["\\(x^{2}+36\\)", "\\(x^{2}+12x+36\\)", "\\(x^{2}+6x+36\\)", "\\(x^{2}+12x+12\\)"],
      correct="B",
      check="(x+6)(x+6) = x^2 + 6x + 6x + 36 = x^2 + 12x + 36."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives the number of changes a band had rung after each of the first three "
            "minutes of a touch. The number of changes rung is a linear function of the number of "
            "minutes. How many changes had the band rung after 4 minutes?"
            + table(["Minutes", "1", "2", "3"], [["Changes rung", "7", "12", "17"]])),
      choices=["17", "20", "22", "24"], correct="C",
      check="The count rises by 5 each minute, so after 4 minutes it is 17 + 5 = 22."),

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
      choices=["19", "24", "26", "27"], correct="D",
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
      choices=["\\(\\frac{1}{6}\\)", "\\(\\frac{1}{5}\\)", "\\(\\frac{1}{4}\\)",
               "\\(\\frac{3}{4}\\)"], correct="C",
      check="12/48 = 1/4."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A rope chest in the ringing chamber holds 0.36 cubic metres. The floor of the chest "
            "is a rectangle measuring 1.2 metres by 0.5 metres. What is the height of the chest, "
            "in metres?"),
      choices=["0.15", "0.3", "0.6", "0.9"], correct="C",
      check="The floor area is 0.6 square metres, and 0.36 divided by 0.6 is 0.6 metres."),

 dict(n="H2E-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A ringing chamber has 8 bell ropes, and the points at which they come through the "
            "ceiling are equally spaced round a circle. What is the measure, in degrees, of the "
            "angle at the centre of that circle between two ropes that are next to each other?"),
      choices=["36", "45", "60", "135"], correct="B",
      check="A full turn of 360 degrees is divided into 8 equal parts, and 360/8 = 45."),

 dict(n="H2E-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A bell rope 8 metres long runs straight from the pulley to the ringer's hands and "
            "makes an angle of 12&deg; with the vertical. Which expression gives the vertical "
            "distance, in metres, from the pulley down to the ringer's hands?"),
      choices=["\\(8\\sin 12^{\\circ}\\)", "\\(\\frac{8}{\\cos 12^{\\circ}}\\)",
               "\\(8\\tan 12^{\\circ}\\)", "\\(8\\cos 12^{\\circ}\\)"], correct="D",
      check="The vertical distance is the side adjacent to the 12 degree angle, so it is 8 cos 12 degrees."),

 dict(n="H2E-22", domain="GT", skill="GT-AV", type="MC",
      stem=("The lower end of a bell rope is coiled into a circle of radius 14 centimetres on the "
            "floor. What is the circumference of that circle, in centimetres, in terms of "
            "\\(\\pi\\) ?"),
      choices=["\\(14\\pi\\)", "\\(21\\pi\\)", "\\(28\\pi\\)", "\\(196\\pi\\)"], correct="C",
      check="The circumference is 2 pi r, and 2(14) = 28."),
]

# ---------------------------------------------------------- Module 2 (Hard)
# Organ building and carillons: flue and reed pipes, voicing, ranks and
# scaling, the clavier, equal temperament and semitones.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A voicer takes f hours over each flue pipe and r hours over each reed pipe. One "
            "week's work and the next week's work give the system of equations below.<br/>"
            "3f + 2r = 51<br/>5f + 4r = 93<br/>What is the value of r?"),
      choices=["9", "12", "15", "21"], correct="B",
      check="Doubling the first equation gives 6f + 4r = 102; subtracting the second leaves f = 9, and then r = 12."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The keys of a carillon clavier lie on a straight line in the xy-plane that passes "
            "through the points \\((a,\\ 3a)\\) and \\((3a,\\ 11a)\\) , where a is a positive "
            "constant. The same line passes through the point \\((7a,\\ y)\\) . What is the value "
            "of y in terms of a?"),
      choices=["\\(19a\\)", "\\(23a\\)", "\\(27a\\)", "\\(31a\\)"], correct="C",
      check="The slope is 8a/2a = 4, so from (3a, 11a) a further 4a in x adds 16a, giving y = 27a."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("An organ builder has 240 hours of shop time and $6,400 for materials. Each flue pipe "
            "takes 3 hours and $50 of material, and each reed pipe takes 5 hours and $160 of "
            "material. The specification requires at least twice as many flue pipes as reed pipes. "
            "What is the greatest number of reed pipes the builder can make?"),
      choices=["12", "16", "18", "21"], correct="D",
      check="Making exactly twice as many flue pipes uses the least of each resource: 11r hours at most 240 "
            "gives r at most 21, and 260r dollars at most 6,400 gives r at most 24."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A voicer's rule relating two ranks of pipes gives the equation "
            "\\(\\frac{3}{x-4}=\\frac{5}{x+2}\\) . What is the value of x?"),
      choices=["7", "11", "13", "17"], correct="C",
      check="Cross-multiplying gives 3x + 6 = 5x - 20, so 2x = 26 and x = 13."),

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
      stem=("For x greater than 2, the expression \\(\\frac{3}{x-2}-\\frac{2}{x+1}\\) can be "
            "written as a single fraction whose denominator is \\(x^{2}-x-2\\) . What is the "
            "numerator of that fraction?"),
      choices=["\\(x-7\\)", "\\(x+7\\)", "\\(5x-1\\)", "\\(5x+7\\)"], correct="B",
      check="3(x+1) - 2(x-2) = 3x + 3 - 2x + 4 = x + 7."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NE", type="FR",
      stem=("The two solutions of the equation \\(x^{2}-16x+k=0\\) differ by 6, and k is a "
            "constant. What is the value of k?"),
      answers=["55"],
      check="The solutions sum to 16 and differ by 6, so they are 11 and 5, and k is their product, 55."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In equal temperament the octave is divided into twelve equal steps, so a pipe n "
            "semitones above a pipe of frequency F sounds a frequency of "
            "\\(F\\left(2^{\\frac{n}{12}}\\right)\\) . A rank contains a pipe 19 semitones above a "
            "given pipe and a pipe 7 semitones above the same given pipe. The frequency of the "
            "first of these is how many times the frequency of the second?"),
      choices=["2", "4", "\\(2^{\\frac{13}{12}}\\)", "\\(2^{\\frac{19}{7}}\\)"], correct="A",
      check="The ratio is 2 to the power 19/12 divided by 2 to the power 7/12, which is 2 to the power 1."),

 dict(n="H2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A voicer's scaling rule stores lengths as "
            "\\(\\frac{a^{\\frac{5}{6}}}{a^{\\frac{1}{3}}}\\) , where a is a positive constant. "
            "Which of the following is equal to that quotient?"),
      choices=["\\(a^{\\frac{1}{3}}\\)", "\\(a^{\\frac{1}{2}}\\)", "\\(a^{\\frac{5}{18}}\\)",
               "\\(a^{\\frac{7}{6}}\\)"], correct="B",
      check="Subtracting the exponents gives 5/6 - 2/6 = 1/2."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the xy-plane, the circle \\(x^{2}+y^{2}=45\\) and the line \\(y=2x\\) meet at two "
            "points. What is the product of the x-coordinates of those two points?"),
      choices=["\\(-27\\)", "\\(-18\\)", "\\(-9\\)", "3"], correct="C",
      check="Substituting gives 5x^2 = 45, so x is 3 or -3 and the product is -9."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A carillon has n bells whose masses total m kilograms. A further bell, of mass "
            "\\(\\frac{3m}{n}\\) kilograms, is added to the carillon. Which expression gives the "
            "mean mass, in kilograms, of the bells the carillon then has?"),
      choices=["\\(\\frac{3m}{n+1}\\)", "\\(\\frac{m+3}{n+1}\\)", "\\(\\frac{m(n+3)}{n}\\)",
               "\\(\\frac{m(n+3)}{n(n+1)}\\)"], correct="D",
      check="The new total is m + 3m/n = m(n+3)/n, shared between n + 1 bells."),

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
      check="The fee was multiplied by 1.08 and then by 1.05, so it was 1,701 divided by 1.134, or 1,500."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A rank of 30 pipes has a mean speaking length of 48 centimetres. The 12 tin-rich "
            "pipes in the rank have a mean speaking length of 60 centimetres. What is the mean "
            "speaking length, in centimetres, of the other 18 pipes in the rank?"),
      choices=["36", "40", "44", "54"], correct="B",
      check="30(48) - 12(60) = 1,440 - 720 = 720 centimetres over 18 pipes, giving 40."),

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
      stem=("In right triangle ABC the right angle is at C, and \\(\\tan A=\\frac{a}{b}\\) , where "
            "a and b are positive constants. Which expression gives \\(\\sin A\\) ?"),
      choices=["\\(\\frac{a}{\\sqrt{a^{2}+b^{2}}}\\)", "\\(\\frac{b}{\\sqrt{a^{2}+b^{2}}}\\)",
               "\\(\\frac{a}{a+b}\\)", "\\(\\frac{\\sqrt{a^{2}+b^{2}}}{a}\\)"], correct="A",
      check="Taking the legs as a and b, the hypotenuse is the square root of a squared plus b squared."),

 dict(n="H2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("A circle has a radius of 25 centimetres. A chord of this circle lies 20 centimetres "
            "from the centre of the circle. What is the length of the chord, in centimetres?"),
      choices=["12", "20", "24", "30"], correct="D",
      check="Half the chord, the distance 20 and the radius 25 form a right triangle, so half the chord is 15."),

 dict(n="H2H-21", domain="GT", skill="GT-AV", type="MC",
      stem=("An organ pipe is made as an open cylinder of sheet metal with no metal at either end, "
            "so the metal used is the curved surface only. A second pipe is made with twice the "
            "radius of the first and half the length of the first. The area of metal in the second "
            "pipe is how many times the area of metal in the first?"),
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
