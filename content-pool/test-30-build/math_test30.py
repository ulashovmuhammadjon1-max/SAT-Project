#!/usr/bin/env python3
"""
Original Math content for Test 30 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Nearly every item makes a rate, a constant, a
                unit price or an unknown be recovered first and only then used;
                two or three steps throughout. Clearly harder than Module 2
                (Easy) and clearly below Module 2 (Hard).
  MODULE_2_EASY genuinely one-step — the lower branch of the adaptive split.
                One operation, no recovery step.
  MODULE_2_HARD hard. Parameters instead of numbers, symbolic answer choices, a
                shifted-function composition, a system read for a product
                rather than for x, an inequality conditioned on a constant, an
                equation with an extraneous root, and geometry needing two
                relationships chained.

Test 30's thematic territory is physic gardens, essential-oil distilling,
apothecary dispensing and weights, herbarium pressing, and seed drying and
storage. The territory is SPLIT ACROSS THE ADAPTIVE BRANCH, because a student
sees Module 1 plus exactly one Module 2 module:

  Module 1              physic gardens and essential-oil distilling
  Module 2 (both)       apothecary dispensing and weights, herbarium pressing,
                        seed drying and storage

verify_math_test30.py pass 4 enforces that split with a keyword check. The
keywords are deliberately chosen to be words that cannot collide with ordinary
English — "alembic", "drachm", "herbarium", "germinat", not "still", "press",
"drying" or "grain", each of which has an everyday sense that would make a
prefix match fire on the wrong module.

Every stem below was screened against the 1,386 production Math stems in
../prod_math_stems.json BEFORE it was written out, and 24 first drafts were
discarded as template repeats — see MANIFEST.md for the list. House style
follows Test 1/2 (see CLAUDE.md): bare HTML stems, simple inline maths as plain
text, \\( \\) reserved for fractions, exponents, radicals and subscripts, real
<table> markup for every data table, and &deg; rather than a raw glyph. All
LaTeX is typed by hand; no bulk conversion step was used anywhere in this file.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = '<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;text-align:left;background:#F4F6F8;">{}</th>'
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# ---------------------------------------------------------------- Module 1
# Physic gardens and essential-oil distilling.
MODULE_1 = [
 dict(n="H1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In a physic garden 40 percent of the beds are given to plants grown for ointments "
            "and the rest to plants grown for infusions. The garden has 33 more infusion beds "
            "than ointment beds. How many beds does the physic garden have altogether?"),
      choices=["165", "198", "220", "264"], correct="A",
      check="Infusion beds less ointment beds is 0.6b - 0.4b = 0.2b, and 0.2b = 33 gives b = 165."),

 dict(n="H1-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A gardener sets young plants out in rows, putting the same number in every row. "
            "Setting out 9 rows would leave 14 plants over, and setting out 11 rows would need 8 "
            "more plants than the gardener has. How many plants does the gardener have?"),
      choices=["103", "113", "121", "128"], correct="B",
      check="9r + 14 = 11r - 8 gives r = 11, so the gardener has 9(11) + 14 = 113 plants."),

 dict(n="H1-03", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A charge of peppermint and a charge of lavender put through an alembic on the same "
            "day weigh 91 kilograms together. The peppermint charge weighs 14 kilograms less "
            "than twice the lavender charge. How many kilograms does the peppermint charge weigh?"),
      choices=["35", "49", "56", "63"], correct="C",
      check="p + l = 91 with p = 2l - 14 gives 3l = 105, so l = 35 and p = 56."),

 dict(n="H1-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A distiller's records show that the volume of oil an alembic yields rises by 3 "
            "millilitres for every extra kilogram of plant material in the charge, and that a "
            "charge of 40 kilograms yields 268 millilitres. According to this relationship, how "
            "many millilitres of oil does a charge of 65 kilograms yield?"),
      choices=["313", "322", "335", "343"], correct="D",
      check="65 - 40 = 25 extra kilograms at 3 millilitres each is 75, and 268 + 75 = 343."),

 dict(n="H1-05", domain="ALG", skill="ALG-LF", type="FR",
      stem=("The mass of oil in a receiver, in grams, t minutes after collection begins is "
            "modelled by m(t)=9t+45. According to this model, how many minutes after collection "
            "begins does the receiver hold 4 times as much oil as it held at the moment "
            "collection began?"),
      answers=["15"],
      check="The model gives 45 grams at t = 0, and 9t + 45 = 180 gives t = 15."),

 dict(n="H1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The table gives the volume of oil an alembic yielded from each of three charges of "
            "lavender. The volume of oil is a linear function of the mass of the charge. Which "
            "equation gives the volume V, in millilitres, of oil yielded by a charge of mass m "
            "kilograms?"
            + table(["Mass of charge (kilograms)", "Oil yielded (millilitres)"],
                    [["20", "148"], ["35", "253"], ["50", "358"]])),
      choices=["V = 8m + 7", "V = 7m + 8", "V = 7m - 8", "V = 6m + 28"], correct="B",
      check="The volume rises 105 millilitres over 15 kilograms, so 7 per kilogram, and "
            "148 - 7(20) = 8."),

 dict(n="H1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A physic garden can obtain a plant in either of two ways. Buying one in costs $6. "
            "Raising them from cuttings instead costs $150 for the frame together with $2 for "
            "each cutting struck. What is the least number of plants for which raising them from "
            "cuttings costs less than buying them in?"),
      choices=["26", "32", "38", "45"], correct="C",
      check="150 + 2n < 6n gives n > 37.5, so the least whole number is 38."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A collar of oiled cloth is cut for the neck of a retort, and the area of cloth it "
            "takes, in square centimetres, is \\((2x+7)^{2}-(2x-7)^{2}\\), where x is a length in "
            "centimetres. Which expression gives that same area for every value of x?"),
      choices=["\\(28x\\)", "\\(98\\)", "\\(8x^{2}+98\\)", "\\(56x\\)"], correct="D",
      check="(2x+7)^2 = 4x^2 + 28x + 49 and (2x-7)^2 = 4x^2 - 28x + 49, and the difference is 56x."),

 dict(n="H1-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A physic garden's planting index is \\(\\frac{x^{2}-49}{x^{2}-11x+28}\\), where x is "
            "the number of beds in a quarter and \\(x\\ne 4\\) and \\(x\\ne 7\\). Which "
            "expression gives that same index?"),
      choices=["\\(\\frac{x+7}{x-4}\\)", "\\(\\frac{x-7}{x+4}\\)", "\\(\\frac{x+7}{x+4}\\)",
               "\\(\\frac{x-4}{x+7}\\)"], correct="A",
      check="The numerator is (x-7)(x+7) and the denominator is (x-7)(x-4), leaving (x+7)/(x-4)."),

 dict(n="H1-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The temperature of a water bath under an alembic, in degrees Celsius, t minutes "
            "after the burner is turned down is modelled by "
            "\\(T(t)=\\frac{1}{4}t^{2}-8t+102\\). What is the least temperature, in degrees "
            "Celsius, that this model gives?"),
      choices=["22", "38", "54", "70"], correct="B",
      check="The vertex is at t = 8/(2 times 1/4) = 16, and T(16) = 64 - 128 + 102 = 38."),

 dict(n="H1-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("In the xy-plane the graph of y=f(x) passes through the point (3, 10). Which point "
            "must lie on the graph of y=f(x-2)+5 ?"),
      choices=["(1, 5)", "(1, 15)", "(5, 15)", "(5, 5)"], correct="C",
      check="Replacing x by x - 2 moves the graph 2 to the right and adding 5 moves it 5 up, "
            "carrying (3, 10) to (5, 15)."),

 dict(n="H1-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A distiller's timing rule is \\(x^{2}-kx+108=0\\), where k is a positive constant. "
            "One solution of the rule is 3 times the other solution. What is the value of k?"),
      choices=["12", "18", "21", "24"], correct="D",
      check="With solutions r and 3r the product is 3r^2 = 108, so r = 6 and k = r + 3r = 24."),

 dict(n="H1-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("Two strengths of an infusion are set equal by the equation "
            "\\(\\frac{5}{x-2}=\\frac{3}{x+4}\\). What value of x satisfies this equation?"),
      choices=["-13", "-7", "7", "13"], correct="A",
      check="Cross-multiplying gives 5x + 20 = 3x - 6, so 2x = -26 and x = -13."),

 dict(n="H1-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The mass of lavender charged into an alembic and the mass of water charged in with "
            "it are always in the ratio 3 to 8. One charge uses 220 kilograms more water than "
            "lavender. How many kilograms of lavender does that charge use?"),
      choices=["88", "132", "176", "352"], correct="B",
      check="The difference is 5 parts, so one part is 44 kilograms and the lavender is 3(44) = 132."),

 dict(n="H1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Lavender for distilling is sold either in trusses of 8 kilograms costing $34 each or "
            "in trusses of 15 kilograms costing $60 each. How many cents less is a kilogram of "
            "lavender bought in the larger truss than in the smaller truss?"),
      choices=["15", "20", "25", "30"], correct="C",
      check="34/8 = 4.25 dollars a kilogram and 60/15 = 4.00, a difference of 0.25 dollars."),

 dict(n="H1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The oil yields, in millilitres, of the first five charges of a season were 34, 41, "
            "47, 52 and 58. A sixth charge was then distilled, and the median of all six yields "
            "was 49.5 millilitres. Which of the following could be the yield, in millilitres, of "
            "the sixth charge?"),
      choices=["38", "44", "50", "55"], correct="D",
      check="For six values the median is the mean of the third and fourth, and only a sixth "
            "value of at least 52 leaves those two as 47 and 52, whose mean is 49.5."),

 dict(n="H1-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("Two lists each record six oil yields in millilitres, and the two lists have the same "
            "mean. The first list is 40, 44, 48, 52, 56, 60 and the second list is 46, 47, 49, "
            "51, 53, 54. Which statement about the standard deviations of the two lists is true?"),
      choices=["The standard deviation of the first list is greater than the standard deviation "
               "of the second list.",
               "The standard deviation of the second list is greater than the standard deviation "
               "of the first list.",
               "The two lists have the same standard deviation.",
               "The standard deviation of each list is zero."], correct="A",
      check="Both lists have a mean of 50, and the first list's values sit further from 50 than "
            "the second list's do."),

 dict(n="H1-18", domain="PSDA", skill="PSDA-DI", type="FR",
      stem=("The table summarises the plants a physic garden raised in one season, by the way "
            "each plant was propagated and by whether it flowered in its first year. What "
            "percentage of all the plants in the table did not flower in their first year?"
            + table(["", "Flowered in first year", "Did not flower", "Total"],
                    [["Raised from cuttings", "120", "80", "200"],
                     ["Raised by division", "80", "40", "120"],
                     ["Total", "200", "120", "320"]])),
      answers=["37.5"],
      check="120 of the 320 plants did not flower, and 120/320 = 0.375."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The head of an alembic is a right circular cone whose base has a radius of 15 "
            "centimetres. The head encloses \\(1{,}125\\pi\\) cubic centimetres. What is the "
            "height of the head, in centimetres?"),
      choices=["9", "15", "25", "45"], correct="B",
      check="(1/3)pi(15^2)h = 75 pi h = 1,125 pi gives h = 15."),

 dict(n="H1-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A raised bed in a physic garden is a rectangular box 3 metres long, 1.2 metres wide "
            "and 0.4 metres deep, and it is filled level to the brim with compost. Compost is "
            "sold in bags each holding 0.06 cubic metres. How many bags are needed to fill the "
            "bed?"),
      answers=["24"],
      check="3(1.2)(0.4) = 1.44 cubic metres, and 1.44/0.06 = 24."),

 dict(n="H1-21", domain="GT", skill="GT-LA", type="MC",
      stem=("A triangular corner bed PQR in a physic garden has PQ equal in length to PR, and "
            "the angle at P measures 44&deg;. A gravel walk runs from Q to a point S on "
            "\\(\\overline{PR}\\) and bisects the angle at Q. What is the measure, in degrees, of "
            "angle PQS?"),
      choices=["34", "44", "68", "90"], correct="A",
      check="The two base angles are each (180 - 44)/2 = 68 degrees, and half of 68 is 34."),

 dict(n="H1-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A brace cut for a cold frame is a right triangle ABC with its right angle at C. In "
            "this brace \\(\\tan A=\\frac{20}{21}\\) and the hypotenuse AB is 29 centimetres "
            "long. What is the area, in square centimetres, of the brace?"),
      choices=["105", "210", "290", "420"], correct="B",
      check="The legs are in the ratio 20 to 21 and 20-21-29 is a right triangle, so the legs "
            "are 20 and 21 and the area is (1/2)(20)(21) = 210."),
]


# ---------------------------------------------------------- Module 2 (Easy)
# Apothecary dispensing and weights, herbarium pressing, seed drying and storage.
MODULE_2_EASY = [
 dict(n="H2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An apothecary divides a 111-gram stock of a powder equally among 8 identical jars "
            "and finds 15 grams left over. How many grams of the powder does each jar hold?"),
      choices=["9", "12", "14", "16"], correct="B",
      check="111 - 15 = 96 grams shared among 8 jars is 12 grams each."),

 dict(n="H2E-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Each drawer of a herbarium cabinet holds 24 mounted sheets. How many mounted sheets "
            "do 15 such drawers hold altogether?"),
      choices=["320", "340", "360", "380"], correct="C",
      check="15(24) = 360."),

 dict(n="H2E-03", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An apothecary's drawer holds 480 pills at the start of a month, and 24 pills are "
            "taken from it each day. After how many days is the drawer empty?"),
      choices=["15", "18", "20", "22"], correct="C",
      check="480/24 = 20."),

 dict(n="H2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The number of specimens still waiting to be mounted in a herbarium is given by "
            "n=190-8d, where d is the number of days since mounting began. How many specimens "
            "are still waiting after 12 days?"),
      choices=["86", "94", "102", "110"], correct="B",
      check="190 - 8(12) = 190 - 96 = 94."),

 dict(n="H2E-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A seed merchant's packing rule gives the number of seeds in a packet as f(g)=9g+40, "
            "where g is the grade number of the seed. How many seeds does this rule give for a "
            "packet of grade 7?"),
      choices=["63", "96", "103", "110"], correct="C",
      check="9(7) + 40 = 63 + 40 = 103."),

 dict(n="H2E-06", domain="ALG", skill="ALG-LF", type="FR",
      stem=("A seed store holds 640 packets and sends out 45 packets in each week. How many "
            "packets are left in the store after 8 weeks?"),
      answers=["280"],
      check="640 - 8(45) = 640 - 360 = 280."),

 dict(n="H2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A seed lot is accepted for storage only if its cleanliness number n satisfies "
            "5n+3&gt;38. Which of the following could be the cleanliness number of an accepted "
            "lot?"),
      choices=["5", "6", "7", "8"], correct="D",
      check="5n + 3 > 38 gives n > 7, and 8 is the only listed value greater than 7."),

 dict(n="H2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The number of grains of powder an apothecary needs for a parcel of k doses is "
            "\\(6(2k-5)+3k\\). Which expression gives that same number of grains for every "
            "value of k?"),
      choices=["\\(15k-30\\)", "\\(9k-30\\)", "\\(15k-5\\)", "\\(12k-30\\)"], correct="A",
      check="6(2k-5) = 12k - 30, and 12k - 30 + 3k = 15k - 30."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A herbarium case holds \\((x+6)(x+4)\\) mounted sheets. Which expression gives that "
            "same number of sheets for every value of x?"),
      choices=["\\(x^{2}+24x+10\\)", "\\(x^{2}+10x+24\\)", "\\(x^{2}+10x+10\\)",
               "\\(x^{2}+24\\)"], correct="B",
      check="(x+6)(x+4) = x^2 + 4x + 6x + 24 = x^2 + 10x + 24."),

 dict(n="H2E-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A seed counter reports a lot size as \\(\\left(3m^{4}\\right)^{2}\\) seeds, where m "
            "is a positive whole number. Which expression gives that same lot size?"),
      choices=["\\(6m^{8}\\)", "\\(9m^{6}\\)", "\\(9m^{8}\\)", "\\(3m^{8}\\)"], correct="C",
      check="Squaring gives 3^2 = 9 and m^(4 times 2) = m^8, so 9m^8."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The moisture content of a seed lot, in percent, is modelled by "
            "\\(M(d)=18-\\frac{d^{2}}{4}\\), where d is the number of days the lot has spent in "
            "the drying room. What moisture content, in percent, does this model give after 6 "
            "days?"),
      choices=["3", "9", "12", "15"], correct="B",
      check="6^2/4 = 9, and 18 - 9 = 9."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The number of specimens a herbarium clerk mounts in a session is modelled by "
            "\\(N(h)=-h^{2}+12h\\), where h is the number of hours the session lasts. How many "
            "specimens does this model give for a session of 5 hours?"),
      choices=["20", "25", "30", "35"], correct="D",
      check="-(5^2) + 12(5) = -25 + 60 = 35."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("An apothecary's balance number x is positive and satisfies \\(x^{2}+3=52\\). What "
            "is the value of x?"),
      choices=["5", "7", "17", "49"], correct="B",
      check="x^2 = 49, and the positive solution is x = 7."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("An apothecary weighs powders with a set of weights in which 1 drachm is 60 grains. "
            "How many grains are there in 7 drachms?"),
      choices=["360", "400", "420", "480"], correct="C",
      check="7(60) = 420."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A lot of 2,400 seeds is divided equally among 16 packets. How many seeds go into "
            "each packet?"),
      choices=["100", "120", "140", "150"], correct="D",
      check="2,400/16 = 150."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("The masses, in grams, of five parcels of dried leaf held in a store are 24, 31, 28, "
            "35 and 27. What is the median of these five masses, in grams?"),
      answers=["28"],
      check="In order the masses are 24, 27, 28, 31, 35, and the middle value is 28."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A herbarium case holds 96 mounted sheets, of which 36 are grasses and 24 are sedges; "
            "the rest are ferns. One sheet is drawn from the case at random. What is the "
            "probability that the sheet drawn is not a grass?"),
      choices=["\\(\\frac{5}{8}\\)", "\\(\\frac{3}{8}\\)", "\\(\\frac{1}{4}\\)",
               "\\(\\frac{3}{4}\\)"], correct="A",
      check="96 - 36 = 60 sheets are not grasses, and 60/96 = 5/8."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of grains in each of four doses an apothecary made up. "
            "What is the difference between the greatest and the least of these numbers of "
            "grains?"
            + table(["Dose", "Grains"],
                    [["Alder", "45"], ["Bryony", "62"], ["Comfrey", "38"], ["Dittany", "57"]])),
      choices=["24", "29", "45", "62"], correct="A",
      check="The greatest is 62 and the least is 38, and 62 - 38 = 24."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A seed drying tray is an open rectangular box 50 centimetres long, 30 centimetres "
            "wide and 6 centimetres deep, and it is filled level to the brim. What is the volume "
            "of seed in the tray, in cubic centimetres?"),
      choices=["900", "1,500", "9,000", "90,000"], correct="C",
      check="50(30)(6) = 9,000."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A herbarium mounting sheet is a rectangle 42 centimetres long and 26 centimetres "
            "wide. What is the perimeter of the sheet, in centimetres?"),
      answers=["136"],
      check="2(42 + 26) = 2(68) = 136."),

 dict(n="H2E-21", domain="GT", skill="GT-LA", type="MC",
      stem=("An apothecary's folding weight rest has the shape of a triangle in which two of the "
            "angles measure 43&deg; and 68&deg;. What is the measure, in degrees, of the third "
            "angle of that triangle?"),
      choices=["49", "59", "62", "69"], correct="D",
      check="180 - 43 - 68 = 69."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A herbarium pressing gauge is a right triangle KLM with its right angle at L. In "
            "this gauge KM is 37 centimetres long and LM is 12 centimetres long. What is the "
            "value of \\(\\cos M\\)?"),
      choices=["\\(\\frac{12}{37}\\)", "\\(\\frac{35}{37}\\)", "\\(\\frac{12}{35}\\)",
               "\\(\\frac{37}{12}\\)"], correct="A",
      check="LM is the leg adjacent to M and KM is the hypotenuse, so cos M = 12/37."),
]


# ---------------------------------------------------------- Module 2 (Hard)
# Apothecary dispensing and weights, herbarium pressing, seed drying and storage.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="FR",
      stem=("An apothecary's tolerance rule is \\(\\left|3x-8\\right|=x+4\\), where x is a "
            "gauge reading. What is the sum of all values of x that satisfy this rule?"),
      answers=["7"],
      check="3x - 8 = x + 4 gives x = 6 and 3x - 8 = -(x+4) gives x = 1; both satisfy the rule, "
            "and 6 + 1 = 7."),

 dict(n="H2H-02", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An apothecary's day book fixes two quantities x and y by y=4x-7 and 2x+3y=35. What "
            "is the value of the product xy?"),
      choices=["13", "21", "28", "36"], correct="D",
      check="2x + 3(4x-7) = 35 gives 14x = 56, so x = 4 and y = 9, and 4(9) = 36."),

 dict(n="H2H-03", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A seed store sent out 620 packets, each either small or large. 30 percent of the "
            "small packets and 45 percent of the large packets came back unopened, and 231 "
            "packets in all came back. How many large packets were sent out?"),
      choices=["260", "300", "320", "380"], correct="B",
      check="With s + l = 620, 0.30(620 - l) + 0.45l = 231 gives 186 + 0.15l = 231, so l = 300."),

 dict(n="H2H-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("Two seed stores are drawn down at constant rates. The first begins with 5,400 "
            "packets and sends out r packets each week, and the second begins with 3,000 packets "
            "and sends out \\(\\frac{r}{3}\\) packets each week. In terms of r, after how many "
            "weeks do the two stores hold the same number of packets?"),
      choices=["\\(\\frac{1{,}200}{r}\\)", "\\(\\frac{2{,}400}{r}\\)",
               "\\(\\frac{3{,}600}{r}\\)", "\\(\\frac{7{,}200}{r}\\)"], correct="C",
      check="5,400 - rw = 3,000 - (r/3)w gives 2,400 = (2r/3)w, so w = 3,600/r."),

 dict(n="H2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("On a herbarium mounting plan a straight line passes through the points (-4, 9) and (8, 3). A "
            "second straight line is parallel to the first and passes through (2, -5). What is "
            "the y-coordinate of the point on the second line whose x-coordinate is 14?"),
      choices=["-11", "-8", "-2", "1"], correct="A",
      check="The slope is (3-9)/(8+4) = -1/2, and -5 - (1/2)(14-2) = -5 - 6 = -11."),

 dict(n="H2H-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A seed grader accepts a reading x whenever "
            "\\(\\frac{2x-7}{3}\\le\\frac{x+1}{2}\\). Which of the following gives all the "
            "readings the grader accepts?"),
      choices=["\\(x\\le 11\\)", "\\(x\\le 17\\)", "\\(x\\ge 11\\)", "\\(x\\ge 17\\)"],
      correct="B",
      check="Multiplying by 6 gives 2(2x-7) <= 3(x+1), so 4x - 14 <= 3x + 3 and x <= 17."),

 dict(n="H2H-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A dispensing tolerance is written \\(ax+12&gt;5x-8\\), where a is a constant, and "
            "the readings x that satisfy it are exactly those with \\(x&lt;5\\). What is the "
            "value of a?"),
      choices=["-5", "-1", "0", "1"], correct="D",
      check="(a-5)x > -20 reverses only when a - 5 is negative, and -20/(a-5) = 5 gives "
            "a - 5 = -4, so a = 1."),

 dict(n="H2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A herbarium records a pressing rate as \\(\\frac{1}{a}-\\frac{1}{b}\\), where a and "
            "b are positive constants. Which expression gives that same rate?"),
      choices=["\\(\\frac{a-b}{ab}\\)", "\\(\\frac{b-a}{ab}\\)", "\\(\\frac{1}{a-b}\\)",
               "\\(\\frac{ab}{b-a}\\)"], correct="B",
      check="Over the common denominator ab the difference is (b - a)/(ab)."),

 dict(n="H2H-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A seed store's dispatch model uses the function f defined by f(x)=3x-7, and a second "
            "function g is defined by g(x)=f(x+4). Which expression gives g(x) for every value "
            "of x?"),
      choices=["\\(3x-11\\)", "\\(3x-3\\)", "\\(3x+12\\)", "\\(3x+5\\)"], correct="D",
      check="f(x+4) = 3(x+4) - 7 = 3x + 12 - 7 = 3x + 5."),

 dict(n="H2H-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=\\frac{a}{x+2}\\), where a is a constant, and "
            "the equation f(x)=x has exactly one real solution. What is the value of a?"),
      choices=["-4", "-1", "1", "4"], correct="B",
      check="a/(x+2) = x gives x^2 + 2x - a = 0, whose discriminant 4 + 4a is zero when a = -1."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=x^{2}+bx+c\\), where b and c are constants. "
            "f(1)=f(9), and the least value f takes is -7. What is the value of c?"),
      choices=["18", "23", "32", "43"], correct="A",
      check="f(1) = f(9) puts the axis at x = 5, so b = -10, and 25 - 50 + c = -7 gives c = 18."),

 dict(n="H2H-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A seed physiologist's calibration satisfies \\(\\sqrt{2x+11}=x-2\\). What is the "
            "value of x?"),
      choices=["-1", "3", "7", "9"], correct="C",
      check="Squaring gives x^2 - 6x - 7 = 0, so x = 7 or x = -1, and x = -1 makes the right "
            "side negative, so only x = 7 works."),

 dict(n="H2H-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A germination index x is positive and satisfies \\(x^{4}-13x^{2}+36=0\\). What is "
            "the sum of all the possible values of x?"),
      choices=["5", "6", "13", "25"], correct="A",
      check="Writing u = x^2 gives u = 4 or u = 9, so the positive x are 2 and 3, and 2 + 3 = 5."),

 dict(n="H2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A seed store held 3,600 packets. During the first year it dispatched 40 percent of "
            "them and then took in 600 new packets, and during the second year it dispatched 25 "
            "percent of whatever it held at the start of that year. How many packets did the "
            "store hold at the end of the second year?"),
      choices=["1,890", "2,070", "2,160", "2,340"], correct="B",
      check="3,600(0.6) = 2,160, then 2,160 + 600 = 2,760, and 2,760(0.75) = 2,070."),

 dict(n="H2H-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("Four clerks working together mount 3 herbarium sheets every 5 minutes. Working at "
            "that same rate for each clerk, how many clerks are needed to mount 63 sheets in 35 "
            "minutes?"),
      choices=["6", "8", "9", "12"], correct="D",
      check="Four clerks mount 21 sheets in 35 minutes, and 63 is 3 times 21, so 3(4) = 12 "
            "clerks are needed."),

 dict(n="H2H-16", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("In one germination trial 240 seeds of a first variety and 160 seeds of a second "
            "variety were sown. 85 percent of the first variety's seeds and 70 percent of the "
            "second variety's seeds germinated. What percent of all the seeds sown in the trial "
            "germinated?"),
      answers=["79"],
      check="0.85(240) = 204 and 0.70(160) = 112, and 316/400 = 0.79."),

 dict(n="H2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the results of a germination trial in which 800 seeds were sown, "
            "half of them stored beforehand at the lower moisture content and half at the higher. "
            "By how many percentage points was the germination rate of the seeds stored at the "
            "lower moisture content greater than that of the seeds stored at the higher moisture "
            "content?"
            + table(["Storage", "Germinated", "Failed to germinate", "Total"],
                    [["Lower moisture content", "380", "20", "400"],
                     ["Higher moisture content", "260", "140", "400"]])),
      choices=["15", "25", "30", "35"], correct="C",
      check="380/400 = 95 percent and 260/400 = 65 percent, a difference of 30 percentage points."),

 dict(n="H2H-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives, for each of four seed lots, the number of seeds sown in a trial and "
            "the number of those seeds that germinated. For which lot did the greatest percentage "
            "of the seeds sown germinate?"
            + table(["Lot", "Seeds sown", "Seeds germinated"],
                    [["Aldworth", "250", "200"], ["Bramfield", "320", "272"],
                     ["Culworth", "180", "144"], ["Denshaw", "400", "312"]])),
      choices=["Aldworth", "Bramfield", "Culworth", "Denshaw"], correct="B",
      check="The rates are 80, 85, 80 and 78 percent, and Bramfield's 85 percent is the greatest."),

 dict(n="H2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A dispensing bottle is a right circular cylinder whose height is equal to the "
            "diameter of its base, and the curved surface of the bottle has an area of "
            "\\(100\\pi\\) square centimetres. What is the volume of the bottle, in cubic "
            "centimetres?"),
      choices=["\\(125\\pi\\)", "\\(250\\pi\\)", "\\(500\\pi\\)", "\\(1{,}000\\pi\\)"],
      correct="B",
      check="With h = 2r the curved area is 2 pi r(2r) = 4 pi r^2 = 100 pi, so r = 5 and h = 10, "
            "and the volume is pi(25)(10) = 250 pi."),

 dict(n="H2H-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A rectangular seed drying tray has a perimeter of 210 centimetres, and the tray is "
            "twice as long as it is wide. What is the area of the tray, in square centimetres?"),
      answers=["2450"],
      check="2(w + 2w) = 210 gives w = 35 and a length of 70, and 35(70) = 2,450."),

 dict(n="H2H-21", domain="GT", skill="GT-LA", type="MC",
      stem=("In the xy-plane a circular herbarium label has its centre at the point (4, -3) and "
            "passes through the point (16, 2). What is the area of the label, in square units?"),
      choices=["\\(26\\pi\\)", "\\(84\\pi\\)", "\\(169\\pi\\)", "\\(338\\pi\\)"], correct="C",
      check="The radius is the distance from (4,-3) to (16,2), which is the square root of "
            "144 + 25 = 169, so 13, and the area is 169 pi."),

 dict(n="H2H-22", domain="GT", skill="GT-TR", type="MC",
      stem=("An apothecary's set square is a right triangle ABC with its right angle at B, and "
            "\\(\\tan A=k\\) for some positive constant k. Which expression gives \\(\\tan C\\) "
            "in terms of k?"),
      choices=["\\(\\frac{1}{k}\\)", "\\(-k\\)", "\\(k^{2}\\)", "\\(1-k\\)"], correct="A",
      check="tan A is BC/AB and tan C is AB/BC, so tan C is the reciprocal of k."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
