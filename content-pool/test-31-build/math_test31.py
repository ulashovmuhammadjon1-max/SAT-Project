#!/usr/bin/env python3
"""
Original Math content for Test 31 — all three modules, 66 questions.

Difficulty, per the standing rule that Module 1 routes students:

  MODULE_1      upper-medium. Almost every item recovers a constant, a rate or
                an unknown first and only then uses it — two or three steps
                throughout. Clearly harder than Module 2 (Easy), clearly below
                Module 2 (Hard).
  MODULE_2_EASY genuinely one-step: one operation, no recovery step. This is
                the lower branch of the adaptive split.
  MODULE_2_HARD hard — parameters instead of numbers, symbolic answer choices,
                a composed function, a system conditioned on a constant, a
                radical equation with an extraneous root, a discriminant
                condition, and geometry that chains two relationships.

Test 31's assigned territory is poultry and egg grading, dovecotes and pigeon
lofts, falconry and mews, decoy ponds and wildfowling, eel traps and fish
ponds. The settings are split so no setting appears in both Module 1 and
either Module 2 branch — a student sees Module 1 plus ONE Module 2 branch, and
the same packing station turning up twice in a sitting reads as a repeat even
when the mathematics differs:

  Module 1 only     egg grading and packing stations, laying flocks and
                    pullets, falconry and the mews, eel traps and eel bucks
  Module 2 branches dovecotes and pigeon lofts, decoy ponds and wildfowling,
                    stew ponds with carp and tench

Two templates the brief warned about were checked against the bank BEFORE
anything was drafted and then deliberately not used: egg grading by weight as a
table-and-mean question (76 banked items already compute a mean or median from a
table) and dovecote population as an exponential (44 banked items already carry
an exponential of the form a*b^t). The egg-grading table here asks a proportion
carried to a second, larger day's grading, and the dovecote items are linear or
proportional throughout.

Templates deliberately chosen because the bank barely uses them (counts from
content-pool/prod_math_stems.json, 1,386 live stems): arc length of a sector
(0), interquartile/quartile statistics, a two-way table conditional probability
(0 stems contain "two-way"), inverse proportion (0), a weighted average (0),
completing the square (0), a radical equation with an extraneous root, and a
combined-rate emptying problem.

House style follows Test 1/2 (see CLAUDE.md): stems are bare HTML, simple
inline math stays plain text, every data table is real <table> markup, degree
signs are &deg;, and every piece of LaTeX was typed by hand. No bulk conversion
step was used anywhere in this file.
"""

TABLE = '<table style="border-collapse:collapse;margin:0.75rem 0;">{head}{body}</table>'
TH = ('<th style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;'
      'text-align:left;background:#F4F6F8;">{}</th>')
TD = '<td style="border:1px solid #D9DEE5;padding:0.35rem 0.6rem;">{}</td>'


def table(headers, rows):
    head = "<tr>" + "".join(TH.format(h) for h in headers) + "</tr>"
    body = "".join("<tr>" + "".join(TD.format(c) for c in r) + "</tr>" for r in rows)
    return TABLE.format(head=head, body=body)


# =========================================================== Module 1 (upper-medium)
MODULE_1 = [

 dict(n="M1-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A packing station pays each grader a fixed amount for the week plus a further amount "
            "for every tray of eggs graded. A grader who graded 240 trays was paid $318 for the "
            "week, and a grader who graded 380 trays was paid $402. How many trays must a grader "
            "grade in a week to be paid $450?"),
      choices=["420", "440", "460", "480"], correct="C",
      check="The rate per tray is (402-318)/(380-240) = 0.6 dollars and the fixed amount is "
            "318 - 0.6(240) = 174 dollars, so 174 + 0.6t = 450 gives t = 460 trays."),

 dict(n="M1-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A falconer conditions a hawk by reducing its weight by the same number of grams each "
            "day. The hawk weighed 1,120 grams on the day conditioning began and 1,042 grams six "
            "days later. On which day of conditioning does the hawk first weigh less than 1,000 "
            "grams?"),
      choices=["day 9", "day 10", "day 11", "day 12"], correct="B",
      check="The daily loss is (1120-1042)/6 = 13 grams, so 1120 - 13d < 1000 needs d > 120/13, "
            "which is about 9.23; the first whole day is day 10."),

 dict(n="M1-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("A river fisherman buys eel traps and net stakes. Five traps and eight stakes cost "
            "$181, and three traps and four stakes cost $99. What is the total cost, in dollars, "
            "of four traps and five stakes?"),
      answers=["128"],
      check="Doubling the second equation gives 6t + 8s = 198; subtracting 5t + 8s = 181 gives "
            "t = 17, and then 4s = 99 - 51 = 48 so s = 12. Four traps and five stakes cost "
            "4(17) + 5(12) = 128 dollars."),

 dict(n="M1-04", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The cold room at a packing station has 96 cubic metres of usable space, of which 12 "
            "cubic metres must be left clear as a walkway. Eggs are stored in stacks that each "
            "occupy 0.75 cubic metres and each hold 30 trays. What is the greatest number of trays "
            "the cold room can hold?"),
      choices=["3,120", "3,240", "3,300", "3,360"], correct="D",
      check="The space available for stacks is 96 - 12 = 84 cubic metres, so 84/0.75 = 112 stacks "
            "fit and 112(30) = 3,360 trays."),

 dict(n="M1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A falconer walks from the mews out to the flying ground at 5 kilometres per hour and "
            "walks back along the same path at 3 kilometres per hour. The round trip takes 2 hours "
            "and 8 minutes. How many kilometres is the flying ground from the mews?"),
      choices=["4", "5", "6", "8"], correct="A",
      check="With d the one-way distance, d/5 + d/3 = 32/15 hours, so 8d/15 = 32/15 and d = 4 "
            "kilometres."),

 dict(n="M1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, line k passes through the points (2, 9) and (8, 3). Line m is "
            "perpendicular to line k and passes through the point (4, 5). What is the "
            "y-coordinate of the point on line m whose x-coordinate is 10?"),
      choices=["5", "7", "9", "11"], correct="D",
      check="Line k has slope (3-9)/(8-2) = -1, so line m has slope 1 and equation y = x + 1; at "
            "x = 10 the y-coordinate is 11."),

 dict(n="M1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A hawk may be flown only when its weight is within 12 grams of its flying weight of "
            "1,046 grams. The hawk weighs 1,079 grams today and loses 7 grams a day. After how "
            "many whole days will the hawk first be at an acceptable weight?"),
      choices=["2", "3", "4", "5"], correct="B",
      check="An acceptable weight satisfies 1,034 <= w <= 1,058, so 1079 - 7d <= 1058 needs "
            "7d >= 21 and d = 3; at d = 3 the weight is 1,058 grams, which is still at or above "
            "1,034."),

 dict(n="M1-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rectangular weathering ground where hawks are put out on their blocks is 8 metres "
            "longer than it is wide, and its area is 105 square metres. What is the perimeter of "
            "the weathering ground, in metres?"),
      choices=["38", "40", "44", "52"], correct="C",
      check="w(w+8) = 105 factors as (w+15)(w-7) = 0, so w = 7 and the length is 15; the perimeter "
            "is 2(7+15) = 44 metres."),

 dict(n="M1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A falconer swings a lure upward from the hand. Its height above the ground, in metres, "
            "t seconds after it leaves the hand is given by \\( h(t) = -5t^{2} + 20t + 2 \\) . For "
            "how many seconds is the lure more than 17 metres above the ground?"),
      choices=["2", "3", "4", "6"], correct="A",
      check="-5t^2 + 20t + 2 > 17 reduces to t^2 - 4t + 3 < 0, that is (t-1)(t-3) < 0, so "
            "1 < t < 3 and the lure is above 17 metres for 2 seconds."),

 dict(n="M1-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which of the following expressions is equivalent to \\( \\frac{6x^{2}+7x-20}{2x+5} \\) "
            "for all x for which the expression is defined?"),
      choices=["2x - 4", "3x + 4", "6x - 4", "3x - 4"], correct="D",
      check="(2x+5)(3x-4) = 6x^2 + 7x - 20, so the quotient is 3x - 4 wherever 2x + 5 is not 0."),

 dict(n="M1-11", domain="ADV", skill="ADV-NE", type="FR",
      stem=("What value of x satisfies the equation \\( 2^{3x-1} = 32^{x-2} \\) ?"),
      answers=["4.5", "9/2"],
      check="32 = 2^5, so the equation is 2^(3x-1) = 2^(5x-10); equating exponents gives "
            "3x - 1 = 5x - 10 and x = 9/2."),

 dict(n="M1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g satisfy f(x) = 4x - 7 and f(g(x)) = 8x + 5 for every value of x. "
            "What is the value of g(3)?"),
      choices=["5", "9", "11", "13"], correct="B",
      check="4g(x) - 7 = 8x + 5 gives g(x) = (8x+12)/4 = 2x + 3, so g(3) = 9."),

 dict(n="M1-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("The expression \\( x^{2}-14x+40 \\) can be written in the form \\( (x-h)^{2}+k \\) , "
            "where h and k are constants. What is the value of h + k?"),
      choices=["-2", "2", "9", "16"], correct="A",
      check="x^2 - 14x + 40 = (x-7)^2 - 49 + 40 = (x-7)^2 - 9, so h = 7, k = -9 and h + k = -2."),

 dict(n="M1-14", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the number of eggs placed in each weight class by a packing station on "
            "a day when 800 eggs were graded."
            + table(["Weight class", "Number of eggs"],
                    [["Small", "86"], ["Medium", "210"], ["Large", "336"],
                     ["Very Large", "168"]])
            + "On the following day the station graded 1,200 eggs, and the same proportion of them "
              "fell in the Large or Very Large classes. How many of the 1,200 eggs were graded "
              "Large or Very Large?"),
      choices=["720", "744", "756", "780"], correct="C",
      check="336 + 168 = 504 of the 800 eggs, or 63 percent, were Large or Very Large; "
            "0.63(1,200) = 756."),

 dict(n="M1-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("The time needed to lift and empty the eel traps on a stretch of river is inversely "
            "proportional to the number of workers doing it. Six workers need 45 minutes. How many "
            "minutes would ten workers need?"),
      choices=["22.5", "27", "30", "75"], correct="B",
      check="Inverse proportion means nt is constant, and 6(45) = 270, so ten workers need "
            "270/10 = 27 minutes."),

 dict(n="M1-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The mean mass of eleven eggs in a tray is 63 grams. One egg, with a mass of 53 grams, "
            "is taken out of the tray. What is the mean mass, in grams, of the ten eggs that "
            "remain?"),
      choices=["62", "63.5", "64", "65"], correct="C",
      check="The eleven eggs have total mass 11(63) = 693 grams; removing 53 leaves 640 grams "
            "across ten eggs, a mean of 64 grams."),

 dict(n="M1-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table records the hawks kept at a mews during one season and whether each was "
            "flown at quarry."
            + table(["", "Flown", "Not flown", "Total"],
                    [["Goshawks", "27", "13", "40"],
                     ["Peregrines", "33", "27", "60"],
                     ["Total", "60", "40", "100"]])
            + "One of the hawks that were flown at quarry is selected at random. What is the "
              "probability that the selected hawk is a peregrine?"),
      choices=["\\( \\frac{11}{20} \\)", "\\( \\frac{3}{5} \\)", "\\( \\frac{33}{100} \\)",
               "\\( \\frac{11}{40} \\)"], correct="A",
      check="Sixty hawks were flown and 33 of them were peregrines, so the probability is "
            "33/60 = 11/20."),

 dict(n="M1-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A grading line handles 45 trays of eggs every 4 minutes, and each tray holds 30 eggs. "
            "At this rate, how many eggs pass along the line in one hour?"),
      choices=["13,500", "18,000", "19,800", "20,250"], correct="D",
      check="45/4 trays a minute is 675 trays an hour, and 675(30) = 20,250 eggs."),

 dict(n="M1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A hawk is flown on a creance, a light line 12 metres long held at a fixed point. The "
            "hawk flies a circular arc about that point, turning through 150&deg; . What is the "
            "length, in metres, of the arc the hawk flies?"),
      choices=["\\( 10\\pi \\)", "\\( 12\\pi \\)", "\\( 20\\pi \\)", "\\( 24\\pi \\)"],
      correct="A",
      check="The full circle has circumference 24pi, and 150/360 of it is (5/12)(24pi) = 10pi "
            "metres."),

 dict(n="M1-20", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle ABC, the measure of angle A is 40&deg; , and the measure of angle B is "
            "three times the measure of angle C. What is the measure, in degrees, of the exterior "
            "angle of the triangle at vertex B?"),
      choices=["35", "75", "105", "140"], correct="B",
      check="Angles B and C sum to 140&deg;, so 4C = 140, C = 35&deg; and B = 105&deg;; the "
            "exterior angle at B is 180 - 105 = 75&deg;."),

 dict(n="M1-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC, the right angle is at vertex B, side AB has length 36, and "
            "\\( \\tan A = \\frac{5}{12} \\) . What is the length of side AC?"),
      choices=["15", "36", "39", "42"], correct="C",
      check="tan A = BC/AB = 5/12 gives BC = 15, and AC = sqrt(36^2 + 15^2) = sqrt(1521) = 39."),

 dict(n="M1-22", domain="GT", skill="GT-AV", type="FR",
      stem=("An egg crate is a rectangular box measuring 60 centimetres by 40 centimetres by 30 "
            "centimetres on the inside. It is filled completely, with no space left over, by trays "
            "measuring 30 centimetres by 20 centimetres by 5 centimetres. Each tray holds 30 eggs. "
            "How many eggs does a full crate hold?"),
      answers=["720"],
      check="The crate holds 60(40)(30) = 72,000 cubic centimetres and each tray occupies "
            "30(20)(5) = 3,000, so 24 trays fit and 24(30) = 720 eggs."),
]


# =========================================================== Module 2 Easy (one-step)
MODULE_2_EASY = [

 dict(n="M2E-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A pigeon loft has the same number of nest boxes in each of 5 rows, together with 18 "
            "further boxes on the end wall, and 63 nest boxes in all. How many nest boxes are in "
            "each row?"),
      choices=["6", "9", "12", "15"], correct="B",
      check="5p + 18 = 63 gives 5p = 45 and p = 9."),

 dict(n="M2E-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The number of squabs taken from a dovecote in its first m months of use is given by "
            "s = 24m + 15. How many squabs are taken in the first 6 months?"),
      choices=["159", "165", "174", "189"], correct="A",
      check="24(6) + 15 = 144 + 15 = 159."),

 dict(n="M2E-03", domain="ALG", skill="ALG-LE", type="FR",
      stem=("If 4x - 9 = 27, what is the value of x + 5?"),
      answers=["14"],
      check="4x = 36 gives x = 9, so x + 5 = 14."),

 dict(n="M2E-04", domain="ALG", skill="ALG-LF", type="MC",
      stem=("A tank used to carry carp from a stew pond has a total mass, in kilograms, given by "
            "M = 0.7n + 12, where n is the number of carp and 12 kilograms is the mass of the empty "
            "tank. What is the total mass when the tank holds 40 carp?"),
      choices=["12", "28", "40", "52"], correct="C",
      check="0.7(40) + 12 = 28 + 12 = 40 kilograms."),

 dict(n="M2E-05", domain="ALG", skill="ALG-LI", type="MC",
      stem=("The number of pigeons n a loft may hold satisfies \\( 3n+14 \\le 71 \\) . What is the "
            "greatest possible value of n?"),
      choices=["17", "19", "21", "24"], correct="B",
      check="3n <= 57 gives n <= 19, so the greatest value is 19."),

 dict(n="M2E-06", domain="ALG", skill="ALG-LE", type="MC",
      stem=("A dovecote has three times as many nest holes on its upper tier as on its lower tier, "
            "and 96 nest holes in all. How many nest holes are on the upper tier?"),
      choices=["24", "32", "64", "72"], correct="D",
      check="With l on the lower tier, 3l + l = 96 gives l = 24, so the upper tier has "
            "3(24) = 72."),

 dict(n="M2E-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A wildfowler records the number of decoys d set out on a pond as more than 15 but no "
            "more than 40. Which inequality represents this?"),
      choices=["\\( 15 \\le d \\le 40 \\)", "\\( 15 \\le d \\lt 40 \\)",
               "\\( 15 \\lt d \\lt 40 \\)", "\\( 15 \\lt d \\le 40 \\)"], correct="D",
      check="'More than 15' is a strict inequality at the lower end and 'no more than 40' allows "
            "40, giving 15 < d <= 40."),

 dict(n="M2E-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to 4(2x - 5) + 3x?"),
      choices=["5x - 20", "8x - 20", "11x - 5", "11x - 20"], correct="D",
      check="4(2x-5) = 8x - 20, and 8x - 20 + 3x = 11x - 20."),

 dict(n="M2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by \\( f(x) = 2x^{2} - 5 \\) . What is the value of "
            "f(-3)?"),
      choices=["13", "23", "31", "41"], correct="A",
      check="2(-3)^2 - 5 = 18 - 5 = 13."),

 dict(n="M2E-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The equation (x - 4)(x + 9) = 0 has two solutions. What is the sum of those two "
            "solutions?"),
      choices=["-5", "5", "13", "36"], correct="A",
      check="The solutions are 4 and -9, and 4 + (-9) = -5."),

 dict(n="M2E-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\( \\frac{18x^{7}}{3x^{2}} \\) for x not equal to "
            "0?"),
      choices=["\\( 15x^{5} \\)", "\\( 6x^{9} \\)", "\\( 21x^{5} \\)", "\\( 6x^{5} \\)"],
      correct="D",
      check="18/3 = 6 and x^7 divided by x^2 is x^5, giving 6x^5."),

 dict(n="M2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The function f is defined by f(x) = 3x + 1. For what value of x is f(x) = 22?"),
      choices=["7", "11", "21", "67"], correct="A",
      check="3x + 1 = 22 gives 3x = 21 and x = 7."),

 dict(n="M2E-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("What is the solution to the equation \\( \\sqrt{x+7} = 5 \\) ?"),
      answers=["18"],
      check="Squaring gives x + 7 = 25, so x = 18, and sqrt(25) = 5 confirms it."),

 dict(n="M2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A decoy pond took 240 wildfowl in one season, and 35% of them were teal. How many "
            "teal were taken?"),
      choices=["60", "84", "96", "105"], correct="B",
      check="0.35(240) = 84."),

 dict(n="M2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dovecote yields 7 squabs a year from each nest hole. How many nest holes are needed "
            "to yield 245 squabs a year at that rate?"),
      choices=["21", "28", "35", "42"], correct="C",
      check="245/7 = 35 nest holes."),

 dict(n="M2E-16", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The masses, in kilograms, of five carp taken from a stew pond were 2.4, 3.1, 2.8, 3.6, "
            "and 3.1. What is the mean mass, in kilograms, of these five carp?"),
      choices=["2.8", "2.9", "3.0", "3.1"], correct="C",
      check="The masses total 15.0 kilograms, and 15.0/5 = 3.0."),

 dict(n="M2E-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The numbers of wigeon counted flighting into a pond on five evenings were 23, 31, 18, "
            "27, and 24. What is the median of these five counts?"),
      choices=["18", "23", "24", "31"], correct="C",
      check="In order the counts are 18, 23, 24, 27, 31, and the middle value is 24."),

 dict(n="M2E-18", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives the numbers of teal and wigeon taken at a decoy pond in each of four "
            "months."
            + table(["Month", "Teal", "Wigeon"],
                    [["October", "62", "45"], ["November", "88", "134"],
                     ["December", "71", "96"], ["January", "54", "60"]])
            + "In November, how many more wigeon than teal were taken?"),
      choices=["46", "52", "88", "134"], correct="A",
      check="134 - 88 = 46."),

 dict(n="M2E-19", domain="GT", skill="GT-AV", type="FR",
      stem=("A stew pond is a rectangle measuring 18 metres by 25 metres. What is its area, in "
            "square metres?"),
      answers=["450"],
      check="18(25) = 450 square metres."),

 dict(n="M2E-20", domain="GT", skill="GT-LA", type="MC",
      stem=("Two angles are supplementary, and one of them measures 118&deg; . What is the measure, "
            "in degrees, of the other angle?"),
      choices=["22", "62", "118", "242"], correct="B",
      check="Supplementary angles sum to 180&deg;, so the other is 180 - 118 = 62&deg;."),

 dict(n="M2E-21", domain="GT", skill="GT-AV", type="MC",
      stem=("A cylindrical grain bin for a pigeon loft has a radius of 3 feet and a height of 10 "
            "feet. What is its volume, in cubic feet?"),
      choices=["\\( 30\\pi \\)", "\\( 90\\pi \\)", "\\( 180\\pi \\)", "\\( 900\\pi \\)"],
      correct="B",
      check="The volume is pi(3^2)(10) = 90pi cubic feet."),

 dict(n="M2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle XYZ, the right angle is at vertex Y, side XY has length 8, side YZ "
            "has length 15, and side XZ has length 17. What is the value of \\( \\tan Z \\) ?"),
      choices=["\\( \\frac{8}{17} \\)", "\\( \\frac{15}{17} \\)", "\\( \\frac{8}{15} \\)",
               "\\( \\frac{15}{8} \\)"], correct="C",
      check="From vertex Z the opposite side is XY = 8 and the adjacent side is YZ = 15, so "
            "tan Z = 8/15."),
]


# =========================================================== Module 2 Hard
MODULE_2_HARD = [

 dict(n="M2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("In the system of equations below, k is a constant.<br/>2x + 3y = 12<br/>6x + ky = 30"
            "<br/>The system has no solution. What is the value of k?"),
      choices=["9", "12", "18", "24"], correct="A",
      check="No solution means the two lines are parallel but distinct: multiplying the first "
            "equation by 3 gives 6x + 9y = 36, so k = 9, and 36 is not 30, so the lines really are "
            "distinct."),

 dict(n="M2H-02", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, the line through the points (a, 3) and (7, 15) has slope 4. What is "
            "the y-coordinate of the point where this line crosses the y-axis?"),
      choices=["-19", "-13", "3", "13"], correct="B",
      check="(15-3)/(7-a) = 4 gives 7 - a = 3 and a = 4; then y = 4x + c through (7, 15) gives "
            "c = 15 - 28 = -13."),

 dict(n="M2H-03", domain="ALG", skill="ALG-LI", type="MC",
      stem=("What is the least integer value of x that satisfies \\( -2 \\lt 5-3x \\le 11 \\) ?"),
      choices=["-4", "-3", "-2", "2"], correct="C",
      check="5 - 3x <= 11 gives x >= -2, and -2 < 5 - 3x gives x < 7/3, so -2 <= x < 7/3 and the "
            "least integer is -2."),

 dict(n="M2H-04", domain="ALG", skill="ALG-LE", type="MC",
      stem=("At a decoy pond, 5 teal and 2 wigeon together weigh 4.3 kilograms, and 3 teal and 4 "
            "wigeon together weigh 4.4 kilograms. Every teal weighs the same as every other teal, "
            "and every wigeon the same as every other wigeon. What is the mass, in grams, of one "
            "wigeon?"),
      choices=["350", "550", "600", "650"], correct="D",
      check="Doubling the first equation gives 10t + 4w = 8.6; subtracting 3t + 4w = 4.4 gives "
            "7t = 4.2, so t = 0.6 kilograms and w = (4.4 - 1.8)/4 = 0.65 kilograms, or 650 grams."),

 dict(n="M2H-05", domain="ALG", skill="ALG-LF", type="MC",
      stem=("The mass of feed a pigeon loft consumes in a week is modelled by "
            "\\( M = \\frac{kn}{n+c} \\) , where n is the number of birds in the loft and k and c "
            "are positive constants with M less than k. Which expression gives n in terms of M, k "
            "and c?"),
      choices=["\\( \\frac{Mc}{k+M} \\)", "\\( \\frac{kc}{M} \\)", "\\( \\frac{k-M}{Mc} \\)",
               "\\( \\frac{Mc}{k-M} \\)"], correct="D",
      check="M(n+c) = kn gives Mn + Mc = kn, so n(k - M) = Mc and n = Mc/(k - M)."),

 dict(n="M2H-06", domain="ALG", skill="ALG-LI", type="MC",
      stem=("A wildfowler has $600 to spend. Decoys cost $28 each and cartridges cost $7 each. She "
            "must buy at least 12 decoys, and she wants as many cartridges as possible. What is "
            "the greatest number of cartridges she can buy?"),
      choices=["37", "38", "40", "42"], correct="A",
      check="Twelve decoys cost 12(28) = 336 dollars, leaving 264 dollars; 264/7 is about 37.7, so "
            "37 cartridges is the greatest whole number affordable."),

 dict(n="M2H-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("What value of x satisfies \\( \\frac{x}{4} + \\frac{x}{6} = \\frac{x-14}{2} \\) ?"),
      answers=["84"],
      check="Multiplying through by 12 gives 3x + 2x = 6(x - 14), so 5x = 6x - 84 and x = 84."),

 dict(n="M2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For a constant k, \\( (3x+k)^{2} = 9x^{2}+42x+c \\) for every value of x, where c is a "
            "constant. What is the value of c?"),
      choices=["14", "49", "84", "441"], correct="B",
      check="Expanding gives 9x^2 + 6kx + k^2, so 6k = 42 and k = 7, and c = k^2 = 49."),

 dict(n="M2H-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The equation \\( 2x^{2}+kx+18=0 \\) has exactly one real solution, and k is positive. "
            "What is the value of k?"),
      choices=["6", "9", "12", "24"], correct="C",
      check="Exactly one real solution means k^2 - 4(2)(18) = 0, so k^2 = 144 and the positive "
            "value is k = 12."),

 dict(n="M2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("What is the solution to the equation \\( \\sqrt{2x+3} = x-6 \\) ?"),
      choices=["3", "7", "8", "11"], correct="D",
      check="Squaring gives 2x + 3 = x^2 - 12x + 36, so x^2 - 14x + 33 = 0 and x = 3 or x = 11. At "
            "x = 3 the right side is -3 while a square root is not negative, so 3 is extraneous and "
            "11 is the only solution."),

 dict(n="M2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g are defined by f(x) = ax + 3 and g(x) = x + a, where a is a "
            "positive constant. If f(g(2)) = 18, what is the value of a?"),
      choices=["3", "5", "6", "15"], correct="A",
      check="g(2) = 2 + a, so f(g(2)) = a(2+a) + 3 = a^2 + 2a + 3 = 18, giving a^2 + 2a - 15 = 0 "
            "and a = 3 or a = -5; only a = 3 is positive."),

 dict(n="M2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to \\( \\frac{1}{x-2} - \\frac{3}{x+1} \\) for all x "
            "for which the expression is defined?"),
      choices=["\\( \\frac{-2x-5}{(x-2)(x+1)} \\)", "\\( \\frac{-2x+7}{(x-2)(x+1)} \\)",
               "\\( \\frac{4x-5}{(x-2)(x+1)} \\)", "\\( \\frac{-2}{(x-2)(x+1)} \\)"],
      correct="B",
      check="Over the common denominator (x-2)(x+1) the numerator is (x+1) - 3(x-2) = -2x + 7."),

 dict(n="M2H-13", domain="ADV", skill="ADV-NF", type="FR",
      stem=("The function h is defined by \\( h(x) = 3(x-4)^{2} - 11 \\) . The minimum value of h "
            "occurs at x = a and that minimum value is b. What is the value of a + b?"),
      answers=["-7"],
      check="The squared term is least when x = 4, where h(4) = -11, so a = 4, b = -11 and "
            "a + b = -7."),

 dict(n="M2H-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A stew pond can be emptied by a large pipe alone in 6 hours or by a small pipe alone "
            "in 9 hours. Both pipes are opened together, and after 2 hours the large pipe is shut. "
            "How many more hours does the small pipe need to finish emptying the pond?"),
      choices=["2", "3", "4", "5"], correct="C",
      check="In 2 hours the two pipes empty 2(1/6 + 1/9) = 5/9 of the pond, leaving 4/9; the small "
            "pipe empties 1/9 of the pond an hour, so it needs 4 more hours."),

 dict(n="M2H-15", domain="PSDA", skill="PSDA-DI", type="MC",
      stem=("The table gives, for each of four stew ponds, the number of young fish put in at the "
            "start of a season and the number taken out at the end."
            + table(["Pond", "Fish stocked", "Fish harvested"],
                    [["Abbey Pond", "480", "396"], ["Mill Stew", "350", "280"],
                     ["Lower Stew", "600", "504"], ["Great Stew", "250", "210"]])
            + "For which pond was the number of fish lost during the season the greatest "
              "percentage of the number stocked?"),
      choices=["Abbey Pond", "Lower Stew", "Great Stew", "Mill Stew"], correct="D",
      check="The losses are 84/480 = 17.5%, 70/350 = 20%, 96/600 = 16% and 40/250 = 16%, so Mill "
            "Stew lost the greatest percentage."),

 dict(n="M2H-16", domain="PSDA", skill="PSDA-ST", type="FR",
      stem=("A stew pond holds 40 carp and 60 tench. The mean mass of the carp is 2.8 kilograms and "
            "the mean mass of the tench is 1.3 kilograms. What is the mean mass, in kilograms, of "
            "all 100 fish in the pond?"),
      answers=["1.9", "19/10"],
      check="The carp weigh 40(2.8) = 112 kilograms and the tench 60(1.3) = 78 kilograms, so the "
            "mean is 190/100 = 1.9 kilograms."),

 dict(n="M2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A basket holds 5 wigeon and 7 teal. Three birds are taken from the basket at random, "
            "one after another and without replacement. What is the probability that none of the "
            "three is a wigeon?"),
      choices=["\\( \\frac{7}{44} \\)", "\\( \\frac{5}{44} \\)", "\\( \\frac{35}{144} \\)",
               "\\( \\frac{7}{12} \\)"], correct="A",
      check="The probability is (7/12)(6/11)(5/10) = 210/1320 = 7/44."),

 dict(n="M2H-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dovecote with 320 nest holes yields 1,120 squabs a year. A new dovecote is to yield "
            "1,540 squabs a year at the same yield per nest hole, and its nest holes are to be "
            "built in tiers of 22. How many tiers will the new dovecote have?"),
      choices=["16", "20", "22", "25"], correct="B",
      check="The yield is 1120/320 = 3.5 squabs a hole, so 1540/3.5 = 440 holes are needed, and "
            "440/22 = 20 tiers."),

 dict(n="M2H-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A grain hopper for a dovecote is a cylinder of radius 2 feet and height 5 feet with a "
            "cone of the same radius and of height 3 feet joined below it, point downward. What is "
            "the total volume of the hopper, in cubic feet?"),
      choices=["\\( 12\\pi \\)", "\\( 20\\pi \\)", "\\( 24\\pi \\)", "\\( 32\\pi \\)"],
      correct="C",
      check="The cylinder holds pi(4)(5) = 20pi and the cone (1/3)pi(4)(3) = 4pi, so the total is "
            "24pi cubic feet."),

 dict(n="M2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle ABC, point P lies on side AB and point Q lies on side AC, and segment PQ "
            "is parallel to side BC. The length of AP is 6, the length of PB is 9, and the length "
            "of AQ is 8. What is the length of side AC?"),
      choices=["12", "20", "24", "27"], correct="B",
      check="PQ parallel to BC gives AP/PB = AQ/QC, so 6/9 = 8/QC and QC = 12; then "
            "AC = 8 + 12 = 20."),

 dict(n="M2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC, the right angle is at vertex C, the hypotenuse AB has length "
            "51, and \\( \\cos A = \\frac{8}{17} \\) . What is the area of triangle ABC?"),
      choices=["540", "612", "1,080", "1,224"], correct="A",
      check="cos A = AC/AB = 8/17 gives AC = 24, and BC = sqrt(51^2 - 24^2) = 45, so the area is "
            "(1/2)(24)(45) = 540."),

 dict(n="M2H-22", domain="GT", skill="GT-AV", type="MC",
      stem=("Two conical feed hoppers are similar in shape, and their heights are in the ratio 2 to "
            "5. The smaller hopper holds 96 litres. How many litres does the larger hopper hold?"),
      choices=["240", "600", "1,500", "6,000"], correct="C",
      check="Volumes of similar solids scale as the cube of the ratio, so the larger holds "
            "96(5/2)^3 = 96(125/8) = 1,500 litres."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
