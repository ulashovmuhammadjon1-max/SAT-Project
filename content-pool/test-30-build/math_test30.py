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
      stem=("A physic garden raises young plants in two frames, and the number ready in each "
            "frame rises at a constant rate. The number ready in the first frame w weeks after "
            "sowing is given by n=35w+120. The table gives the number ready in the second frame. "
            "How many more plants does the second frame add each week than the first frame adds?"
            + table(["Weeks after sowing", "Plants ready in the second frame"],
                    [["2", "190"], ["6", "350"]])),
      choices=["3", "5", "8", "15"], correct="B",
      check="The second frame adds (350 - 190)/(6 - 2) = 40 a week and the first adds 35, "
            "a difference of 5."),

 dict(n="H1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A physic garden can obtain a plant in either of two ways. Buying one in costs $6. "
            "Raising them from cuttings instead costs $150 for the frame together with $2 for "
            "each cutting struck. What is the least number of plants for which raising them from "
            "cuttings costs less than buying them in?"),
      choices=["26", "32", "38", "45"], correct="C",
      check="150 + 2n < 6n gives n > 37.5, so the least whole number is 38."),

 dict(n="H1-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The length of oiled cord taken to bind a bundle of cut stems is "
            "\\(\\sqrt{72x^{5}}\\) centimetres, where x is a positive length in centimetres. "
            "Which expression gives that same length for every positive value of x?"),
      choices=["\\(6x^{2}\\sqrt{2x}\\)", "\\(6x^{2}\\sqrt{2}\\)", "\\(36x^{2}\\sqrt{2x}\\)",
               "\\(8x^{2}\\sqrt{3x}\\)"], correct="A",
      check="72x^5 = 36x^4 times 2x, and the square root of 36x^4 is 6x^2, leaving "
            "6x^2 times the square root of 2x."),

 dict(n="H1-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A physic garden's planting index is \\(\\frac{18a^{6}b^{2}}{6a^{2}b^{5}}\\), where a "
            "and b are positive numbers of beds and of quarters. Which expression gives that "
            "same index?"),
      choices=["\\(\\frac{3a^{4}}{b^{3}}\\)", "\\(3a^{4}b^{3}\\)", "\\(\\frac{3a^{8}}{b^{7}}\\)",
               "\\(\\frac{12a^{4}}{b^{3}}\\)"], correct="A",
      check="18/6 = 3, a^(6-2) = a^4 and b^(2-5) = b^(-3), so the index is 3a^4 over b^3."),

 dict(n="H1-10", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The mass of oil standing in a receiver under an alembic, in grams, t minutes after "
            "collection begins is modelled by \\(m(t)=-2t^{2}+24t\\). For how many minutes "
            "together does this model give a mass of at least 64 grams?"),
      choices=["2", "4", "6", "8"], correct="B",
      check="-2t^2 + 24t = 64 gives t^2 - 12t + 32 = 0, so t = 4 and t = 8, and the model is at "
            "or above 64 grams between them, a stretch of 8 - 4 = 4 minutes."),

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
      stem=("The table gives the mass of lavender in each of four charges put through an alembic "
            "in one week. The four charges together yielded 600 millilitres of oil, and every "
            "charge yielded the same volume of oil for each kilogram of lavender. How many "
            "millilitres of oil did the third charge yield?"
            + table(["Charge", "Mass of lavender (kilograms)"],
                    [["First", "40"], ["Second", "55"], ["Third", "35"], ["Fourth", "70"]])),
      answers=["105"],
      check="The four charges take 200 kilograms in all, so the yield is 600/200 = 3 millilitres "
            "a kilogram, and the third charge yields 3(35) = 105."),

 dict(n="H1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("Two copper heads for an alembic have exactly the same shape, and every length on "
            "the larger head is 3 times the matching length on the smaller head. The smaller "
            "head encloses 45 cubic centimetres. How many cubic centimetres does the larger "
            "head enclose?"),
      choices=["135", "405", "1,215", "3,645"], correct="C",
      check="Volume scales as the cube of the scale factor, so the larger head encloses "
            "45 times 3^3 = 45(27) = 1,215 cubic centimetres."),

 dict(n="H1-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A circular herb bed in a physic garden has a radius of 12 metres. A gravel walk "
            "covers the sector of the bed cut off by a central angle of 150&deg;, and the area "
            "of that sector is \\(k\\pi\\) square metres. What is the value of k?"),
      answers=["60"],
      check="The sector is 150/360 of the bed, so its area is (150/360)(12^2)pi = 60 pi."),

 dict(n="H1-21", domain="GT", skill="GT-LA", type="MC",
      stem=("A triangular corner bed PQR in a physic garden has PQ equal in length to PR, and "
            "the angle at P measures 44&deg;. A gravel walk runs from Q to a point S on "
            "\\(\\overline{PR}\\) and bisects the angle at Q. What is the measure, in degrees, of "
            "angle PQS?"),
      choices=["34", "44", "68", "90"], correct="A",
      check="The two base angles are each (180 - 44)/2 = 68 degrees, and half of 68 is 34."),

 dict(n="H1-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A brace cut for a cold frame is a right triangle ABC with its right angle at C. In "
            "this brace \\(\\sin A=\\frac{2}{7}\\). What is the value of \\(\\cos^{2}A\\)?"),
      choices=["\\(\\frac{45}{49}\\)", "\\(\\frac{5}{49}\\)", "\\(\\frac{4}{49}\\)",
               "\\(\\frac{5}{7}\\)"], correct="A",
      check="Since sin^2 A + cos^2 A = 1, cos^2 A = 1 - (2/7)^2 = 1 - 4/49 = 45/49."),
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
      choices=["360", "384", "408", "432"], correct="A",
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

 dict(n="H2E-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("An apothecary's packing rule is 5p+4q=96, where p is the number of pill boxes and q "
            "is the number of jars packed into one crate. If q=9, what is the value of p?"),
      choices=["6", "8", "10", "12"], correct="D",
      check="4(9) = 36, so 5p = 96 - 36 = 60 and p = 12."),

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
      stem=("A parcel made up by an apothecary holds \\(4k^{2}+7k-5\\) grains of one powder and "
            "\\(2k^{2}-7k+9\\) grains of another, where k is a whole number. Which expression "
            "gives the total number of grains in the parcel?"),
      choices=["\\(6k^{2}+4\\)", "\\(6k^{2}+14k+4\\)", "\\(6k^{4}+4\\)", "\\(6k^{2}-4\\)"],
      correct="A",
      check="The k terms cancel, 7k - 7k = 0, and 4k^2 + 2k^2 = 6k^2 with -5 + 9 = 4."),

 dict(n="H2E-09", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A herbarium case holds \\((x+6)(x+4)\\) mounted sheets. Which expression gives that "
            "same number of sheets for every value of x?"),
      choices=["\\(x^{2}+24x+10\\)", "\\(x^{2}+10x+24\\)", "\\(x^{2}+10x+10\\)",
               "\\(x^{2}+24\\)"], correct="B",
      check="(x+6)(x+4) = x^2 + 4x + 6x + 24 = x^2 + 10x + 24."),

 dict(n="H2E-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A seed counter reports a lot size as \\(\\left(3m^{4}\\right)^{2}\\) seeds, where m "
            "is a positive whole number. Which expression gives that same lot size?"),
      choices=["\\(6m^{8}\\)", "\\(9m^{8}\\)", "\\(9m^{6}\\)", "\\(3m^{8}\\)"], correct="B",
      check="Squaring gives 3^2 = 9 and m^(4 times 2) = m^8, so 9m^8."),

 dict(n="H2E-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A seed store's settling rule uses the function g defined by "
            "\\(g(p)=\\sqrt{p+15}\\). What is the value of g(49)?"),
      choices=["7", "8", "32", "64"], correct="B",
      check="49 + 15 = 64, and the square root of 64 is 8."),

 dict(n="H2E-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A herbarium's mounting rule is \\(\\left|x-19\\right|=6\\), where the gauge reading "
            "x is greater than 19. What is the value of x?"),
      choices=["13", "19", "25", "31"], correct="C",
      check="x - 19 = 6 gives x = 25 and x - 19 = -6 gives x = 13, and only 25 is greater "
            "than 19."),

 dict(n="H2E-13", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A seed grader's index x satisfies \\(x^{3}=343\\). What is the value of x?"),
      choices=["7", "9", "21", "49"], correct="A",
      check="7 times 7 times 7 = 343, so x = 7."),

 dict(n="H2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("An apothecary weighs powders with a set of weights in which 1 drachm is 60 grains. "
            "How many grains are there in 7 drachms?"),
      choices=["360", "380", "400", "420"], correct="D",
      check="7(60) = 420."),

 dict(n="H2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A lot of 2,400 seeds is divided equally among 16 packets. How many seeds go into "
            "each packet?"),
      choices=["100", "120", "140", "150"], correct="D",
      check="2,400/16 = 150."),

 dict(n="H2E-16", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("An apothecary recorded the number of doses made up on each of seven days as 12, 9, "
            "14, 9, 11, 9 and 15. What is the mode of these seven numbers?"),
      answers=["9"],
      check="9 appears three times and every other number appears once, so the mode is 9."),

 dict(n="H2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The numbers of seeds counted in each of six packets were 148, 155, 139, 162, 151 "
            "and 144. What is the range of these six numbers?"),
      choices=["11", "14", "23", "46"], correct="C",
      check="The greatest count is 162 and the least is 139, and 162 - 139 = 23."),

 dict(n="H2E-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of grains in each of four doses an apothecary made up. "
            "What is the difference between the greatest and the least of these numbers of "
            "grains?"
            + table(["Dose", "Grains"],
                    [["Alder", "45"], ["Bryony", "62"], ["Comfrey", "38"], ["Dittany", "57"]])),
      choices=["24", "29", "45", "62"], correct="A",
      check="The greatest is 62 and the least is 38, and 62 - 38 = 24."),

 dict(n="H2E-19", domain="GT", skill="GT-AV", type="MC",
      stem=("The base of a seed drying tray is a trapezium whose two parallel sides are 30 "
            "centimetres and 42 centimetres long and whose perpendicular height is 16 "
            "centimetres. What is the area of that base, in square centimetres?"),
      choices=["288", "480", "576", "1,152"], correct="C",
      check="Half of (30 + 42) is 36, and 36 times 16 = 576."),

 dict(n="H2E-20", domain="GT", skill="GT-AV", type="FR",
      stem=("A seed drying tray is a rectangular box 40 centimetres long, 24 centimetres wide "
            "and 16 centimetres deep. Cubical seed boxes whose edges are 8 centimetres long are "
            "packed into the tray so that the tray is completely filled. How many of those boxes "
            "does the tray hold?"),
      answers=["30"],
      check="The tray takes 40/8 = 5 boxes along its length, 24/8 = 3 across its width and "
            "16/8 = 2 up its depth, and 5(3)(2) = 30."),

 dict(n="H2E-21", domain="GT", skill="GT-LA", type="MC",
      stem=("An apothecary's folding weight rest has the shape of a triangle. An exterior angle "
            "at one of its vertices measures 126&deg;, and the two interior angles that are not "
            "adjacent to that exterior angle are equal in measure. What is the measure, in "
            "degrees, of each of those two interior angles?"),
      choices=["63", "72", "117", "126"], correct="A",
      check="An exterior angle equals the sum of the two non-adjacent interior angles, so each "
            "of the two equal angles is 126/2 = 63 degrees."),

 dict(n="H2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("A herbarium pressing screw turns through an angle of \\(\\frac{7\\pi}{10}\\) "
            "radians. What is the measure of that angle, in degrees?"),
      choices=["63", "108", "126", "252"], correct="C",
      check="pi radians is 180 degrees, so (7/10)(180) = 126 degrees."),
]


# ---------------------------------------------------------- Module 2 (Hard)
# Apothecary dispensing and weights, herbarium pressing, seed drying and storage.
MODULE_2_HARD = [
 dict(n="H2H-01", domain="ALG", skill="ALG-LE", type="FR",
      stem=("An apothecary's dispensing rule sets \\(\\frac{x+3}{4}+\\frac{x-1}{2}=7\\), where x "
            "is the number of grains in a dose. What is the value of x?"),
      answers=["9"],
      check="Multiplying through by 4 gives (x+3) + 2(x-1) = 28, so 3x + 1 = 28 and x = 9."),

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
      stem=("A herbarium's shrinkage rule is a linear function f, and the rule gives f(2) as 21 "
            "greater than f(9). What is the slope of the graph of y=f(x) in the xy-plane?"),
      choices=["-3", "\\(-\\frac{7}{3}\\)", "3", "21"], correct="A",
      check="f(9) - f(2) = -21 over a run of 9 - 2 = 7, so the slope is -21/7 = -3."),

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
      stem=("A seed store's wastage model is the function f defined by "
            "\\(f(x)=x^{3}-2x^{2}-15x\\). How many distinct x-intercepts does the graph of "
            "y=f(x) have in the xy-plane?"),
      choices=["1", "2", "3", "4"], correct="C",
      check="x^3 - 2x^2 - 15x = x(x-5)(x+3), whose zeros are 0, 5 and -3, so there are 3 "
            "distinct x-intercepts."),

 dict(n="H2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\(f(x)=x^{2}+bx+c\\), where b and c are constants. "
            "f(1)=f(9), and the least value f takes is -7. What is the value of c?"),
      choices=["18", "23", "32", "43"], correct="A",
      check="f(1) = f(9) puts the axis at x = 5, so b = -10, and 25 - 50 + c = -7 gives c = 18."),

 dict(n="H2H-12", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A seed physiologist's calibration satisfies \\(x+\\frac{18}{x}=11\\), where x is "
            "positive. What is the positive difference between the two values of x that satisfy "
            "this equation?"),
      choices=["5", "7", "9", "11"], correct="B",
      check="Multiplying through by x gives x^2 - 11x + 18 = 0, so x = 2 or x = 9, and "
            "9 - 2 = 7."),

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
      stem=("A circular herbarium seal of the largest size that will fit is cut from a square "
            "sheet of paper whose sides are 20 centimetres long. What is the area, in square "
            "centimetres, of the paper left over once the seal has been cut out?"),
      choices=["\\(400-100\\pi\\)", "\\(400-400\\pi\\)", "\\(400-20\\pi\\)",
               "\\(100-100\\pi\\)"], correct="A",
      check="The largest circle that fits has a diameter of 20, so a radius of 10 and an area "
            "of 100 pi, and the square's area is 20^2 = 400."),

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
