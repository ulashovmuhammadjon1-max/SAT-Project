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

TWENTY-EIGHT of these 66 questions were rewritten after the first-ever
verification pass, and the reason is recorded here because it is the single most
transferable finding of this build. Only seven of the twenty-eight were caught
by the token-Jaccard screen. The other twenty-one were caught by
mechanism_search.py, which asks what mathematical MOVE a question makes and
counts how many banked stems make the same move, ignoring the setting words
entirely. The clearest cases, none of which the Jaccard screen would have
rejected:

  * a radical equation drafted as sqrt(x+7)=5 against Test 5 M2E Q14's
    sqrt(x+7)=6 — the same radicand, scoring 0.80 against an unrelated stem and
    never compared with the one it actually repeated;
  * a parallel-segment triangle drafted with AP=6, PB=9, AQ=8 against Test 15
    M2H Q19 and Test 17 M2H Q19, which use 6, 9 and 8;
  * tan A = 5/12 against Test 11 M2H Q18's tan A = 5/12;
  * a weighted mean of 40 carp and 60 tench against Test 15 M2H Q15's 14 salmon
    in one tank and 6 in another;
  * a cylinder-plus-cone hopper against Test 13 M2H Q17 and Test 15 M2H Q20,
    both of which are a "grain hopper" of a cylinder plus a cone;
  * a two-speed round trip against Test 14 M2H Q21, the only banked instance of
    that mechanism and an exact template match.

Two internal repeats were also mechanism-only findings: the draft's M1-02 and
M1-07 were both a hawk losing a fixed weight per day, in the same module; and
M1-04 and M1-22 both divided a volume by a volume and multiplied by 30.

Every replacement was pre-screened by mechanism BEFORE it was written, and the
mechanism chosen from the low-count end of the bank. Counts at the time of
writing, from content-pool/prod_math_stems.json (1,386 live stems): a cost
crossover inequality (0), a transfer between two groups (0), a scaled compound
inequality (0), a Pythagorean quadratic from a diagonal (0), factoring out a
common monomial completely (0), a quadratic recovered from its two roots (0), a
compound fraction (1), a standard-deviation comparison (1), counting values
above the mean (0), a rectangle-plus-semicircle composite area (1), a
quadrilateral angle sum (0), a value that makes a function undefined (0),
collecting like terms in two variables (0), a linear function extended from a
table (1), an ordered pair satisfying two inequalities (1), a line meeting a
parabola (2), a cube equation (3), a rational sum over a factorable quadratic
denominator (0), an average rate of change (0), a median from a frequency table
(0), a volume under percentage scaling of two dimensions (0), and a regular
polygon recovered from its interior angle (1).

Three trigonometry items sit in three different modules, and because a student
sees Module 1 plus ONE Module 2 branch they are differentiated by both their
given and their ask: M2E-22 gives all three sides and asks for a ratio, M1-21
gives a ratio and a leg and asks for the perimeter, M2H-21 gives a ratio and the
hypotenuse and asks for the area. Their Pythagorean triples are also disjoint —
9-40-41, 20-21-29 and 8-15-17 — so no two share a number.

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
      choices=["400", "420", "440", "460"], correct="D",
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
      stem=("A packing station can grade a day's eggs by hand at a cost of $90 for the day plus 16 "
            "cents for every tray graded, or hire a grading machine at a cost of $246 for the day "
            "plus 4 cents for every tray graded. What is the least number of trays graded in a day "
            "for which the machine costs less than grading by hand?"),
      choices=["1,299", "1,300", "1,301", "1,310"], correct="C",
      check="The machine is cheaper when 246 + 0.04t < 90 + 0.16t, that is 156 < 0.12t, so "
            "t > 1,300; at exactly 1,300 trays the two costs are equal, so the least whole number "
            "of trays is 1,301."),

 dict(n="M1-05", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two pullet houses hold a farm's laying birds. At the start of the season the first "
            "house holds four times as many birds as the second. After 210 birds are moved from "
            "the first house to the second, the first holds twice as many birds as the second. How "
            "many birds did the first house hold at the start of the season?"),
      choices=["840", "1,050", "1,260", "1,680"], correct="C",
      check="With s birds in the second house the first holds 4s, and 4s - 210 = 2(s + 210) gives "
            "2s = 630, so s = 315 and the first house held 4(315) = 1,260 birds."),

 dict(n="M1-06", domain="ALG", skill="ALG-LF", type="MC",
      stem=("In the xy-plane, line k passes through the points (2, 9) and (8, 3). Line m is "
            "perpendicular to line k and passes through the point (4, 5). What is the "
            "y-coordinate of the point on line m whose x-coordinate is 10?"),
      choices=["5", "7", "9", "11"], correct="D",
      check="Line k has slope (3-9)/(8-2) = -1, so line m has slope 1 and equation y = x + 1; at "
            "x = 10 the y-coordinate is 11."),

 dict(n="M1-07", domain="ALG", skill="ALG-LI", type="MC",
      stem=("At a packing station an egg is graded Medium when its mass m, in grams, satisfies "
            "\\( 53 \\le m \\lt 63 \\) . A tray is filled with 30 eggs, every one of them graded "
            "Medium. Which of the following could be the total mass, in grams, of the 30 eggs on "
            "that tray?"),
      choices=["1,760", "1,890", "1,920", "1,980"], correct="A",
      check="Thirty Medium eggs have a total mass T with 30(53) <= T < 30(63), that is "
            "1,590 <= T < 1,890. Of the four values only 1,760 lies in that interval."),

 dict(n="M1-08", domain="ADV", skill="ADV-NE", type="MC",
      stem=("A rectangular egg store is 14 metres longer than it is wide, and the distance from "
            "one corner of the store to the opposite corner is 26 metres. What is the area of the "
            "store, in square metres?"),
      choices=["240", "260", "288", "336"], correct="A",
      check="With w the width, w^2 + (w+14)^2 = 26^2 gives 2w^2 + 28w - 480 = 0, that is "
            "w^2 + 14w - 240 = (w+24)(w-10) = 0, so w = 10 and the length is 24; the area is "
            "10(24) = 240 square metres."),

 dict(n="M1-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A falconer swings a lure upward from the hand. Its height above the ground, in metres, "
            "t seconds after it leaves the hand is given by \\( h(t) = -5t^{2} + 20t + 2 \\) . For "
            "how many seconds is the lure more than 17 metres above the ground?"),
      choices=["2", "3", "4", "6"], correct="A",
      check="-5t^2 + 20t + 2 > 17 reduces to t^2 - 4t + 3 < 0, that is (t-1)(t-3) < 0, so "
            "1 < t < 3 and the lure is above 17 metres for 2 seconds."),

 dict(n="M1-10", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A packing plan gives the usable volume of an egg store, in cubic metres, as "
            "\\( 12x^{3}-27x \\) , where x is a length in metres. Which expression is equivalent "
            "to that volume, written as a product of factors that cannot be factored further?"),
      choices=["\\( 3x(2x-3)(2x+3) \\)", "\\( 3x(4x-9)(x+1) \\)",
               "\\( 3x(2x-9)(2x+3) \\)", "\\( 9x(x-3)(x+3) \\)"], correct="A",
      check="Taking out 3x leaves 3x(4x^2 - 9), and 4x^2 - 9 is a difference of two squares, so "
            "the full factorisation is 3x(2x-3)(2x+3)."),

 dict(n="M1-11", domain="ADV", skill="ADV-NE", type="FR",
      stem=("The solutions to the equation \\( x^{2}+bx+c=0 \\) are 3 and -11, where b and c are "
            "constants. What is the value of c - b?"),
      answers=["-41"],
      check="The two solutions sum to -b, so -b = 3 + (-11) = -8 and b = 8; they multiply to c, "
            "so c = 3(-11) = -33. Hence c - b = -33 - 8 = -41."),

 dict(n="M1-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g satisfy f(x) = 4x - 7 and f(g(x)) = 8x + 5 for every value of x. "
            "What is the value of g(3)?"),
      choices=["5", "6", "9", "13"], correct="C",
      check="4g(x) - 7 = 8x + 5 gives g(x) = (8x+12)/4 = 2x + 3, so g(3) = 9."),

 dict(n="M1-13", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("A grading line's timing rule reduces to "
            "\\( \\frac{\\frac{1}{x}-\\frac{1}{4}}{x-4} \\) , where x is a positive number other "
            "than 4. Which expression is equal to that rule?"),
      choices=["\\( \\frac{1}{4x} \\)", "\\( \\frac{1}{4x(x-4)} \\)",
               "\\( -\\frac{4}{x(x-4)} \\)", "\\( -\\frac{1}{4x} \\)"], correct="D",
      check="The numerator is 1/x - 1/4 = (4-x)/(4x). Dividing by x - 4 gives "
            "(4-x)/(4x(x-4)) = -(x-4)/(4x(x-4)) = -1/(4x)."),

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
      stem=("Two graders each weighed five eggs, in grams, and recorded these results.<br/>"
            "Grader P: 58, 60, 62, 64, 66<br/>Grader Q: 52, 57, 62, 67, 72<br/>"
            "Which statement correctly compares the two sets of five masses?"),
      choices=["The two means are equal, and the standard deviation of Grader P's masses is "
               "less than the standard deviation of Grader Q's masses.",
               "The two means are equal, and the standard deviation of Grader P's masses is "
               "greater than the standard deviation of Grader Q's masses.",
               "The mean of Grader P's masses is greater, and the two standard deviations are "
               "equal.",
               "The mean of Grader P's masses is less, and the standard deviation of Grader P's "
               "masses is greater."], correct="A",
      check="Both sets total 310 grams, so both means are 62 grams. Grader P's masses lie within "
            "4 grams of 62 while Grader Q's lie within 10 grams of 62, so Grader P's masses are "
            "less spread out and have the smaller standard deviation."),

 dict(n="M1-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("The table gives the number of eggs collected from a laying flock on each of six days."
            + table(["Day", "Eggs collected"],
                    [["Monday", "268"], ["Tuesday", "291"], ["Wednesday", "274"],
                     ["Thursday", "302"], ["Friday", "285"], ["Saturday", "264"]])
            + "On how many of these six days was the number of eggs collected greater than the "
              "mean number collected per day?"),
      choices=["2", "3", "4", "5"], correct="B",
      check="The six counts total 1,684 eggs, so the mean is 1,684/6, about 280.7. The counts "
            "above that mean are 291, 302 and 285, which is three days."),

 dict(n="M1-18", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A grading line handles 45 trays of eggs every 4 minutes, and each tray holds 30 eggs. "
            "At this rate, how many eggs pass along the line in one hour?"),
      choices=["13,500", "18,000", "19,800", "20,250"], correct="D",
      check="45/4 trays a minute is 675 trays an hour, and 675(30) = 20,250 eggs."),

 dict(n="M1-19", domain="GT", skill="GT-AV", type="MC",
      stem=("A weathering ground where hawks are put out on their blocks is a rectangle 14 metres "
            "long and 12 metres wide, with a semicircular bay of diameter 12 metres built out "
            "along one of the 12-metre sides. What is the total area of the weathering ground, in "
            "square metres?"),
      choices=["\\( 168+9\\pi \\)", "\\( 168+18\\pi \\)", "\\( 168+36\\pi \\)",
               "\\( 168+72\\pi \\)"],
      correct="B",
      check="The rectangle has area 14(12) = 168 square metres. The bay is a semicircle of radius "
            "6, with area (1/2)pi(6^2) = 18pi, so the total is 168 + 18pi."),

 dict(n="M1-20", domain="GT", skill="GT-LA", type="MC",
      stem=("In triangle ABC, the measure of angle A is 40&deg; , and the measure of angle B is "
            "three times the measure of angle C. What is the measure, in degrees, of the exterior "
            "angle of the triangle at vertex B?"),
      choices=["35", "75", "105", "140"], correct="B",
      check="Angles B and C sum to 140&deg;, so 4C = 140, C = 35&deg; and B = 105&deg;; the "
            "exterior angle at B is 180 - 105 = 75&deg;."),

 dict(n="M1-21", domain="GT", skill="GT-TR", type="MC",
      stem=("A falconer's flying lawn PQR is a triangle whose corner at R is a right angle. The "
            "side QR measures 60 metres, and \\( \\sin P = \\frac{20}{29} \\) . The lawn is to be "
            "fenced all the way round. How many metres of fencing are needed?"),
      choices=["150", "189", "210", "273"], correct="C",
      check="sin P = QR/PQ = 20/29 with QR = 60 gives PQ = 87, and "
            "PR = sqrt(87^2 - 60^2) = sqrt(3969) = 63; the perimeter is 60 + 63 + 87 = 210."),

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
      stem=("A loft keeper counting his birds writes 7n - 12 = 4n + 27, where n is the number of "
            "pigeons in the loft. What is the value of n?"),
      answers=["13"],
      check="Subtracting 4n from both sides gives 3n - 12 = 27, so 3n = 39 and n = 13."),

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
      stem=("A dovecote's floor plan gives an area, in square metres, of \\( (x+9)(x-4) \\) , "
            "where x is a length in metres. Which expression is equivalent to that area?"),
      choices=["\\( x^{2}+5x-36 \\)", "\\( x^{2}-5x-36 \\)", "\\( x^{2}+13x-36 \\)",
               "\\( x^{2}+5x+36 \\)"], correct="A",
      check="(x+9)(x-4) = x^2 - 4x + 9x - 36 = x^2 + 5x - 36."),

 dict(n="M2E-09", domain="ADV", skill="ADV-NF", type="MC",
      stem=("A loft keeper's feed rule is modelled by the function h defined by "
            "\\( h(x) = \\frac{9}{x+6} \\) . For what value of x is h(x) undefined?"),
      choices=["-9", "-6", "6", "9"], correct="B",
      check="A quotient is undefined only where its denominator is 0, and x + 6 = 0 when "
            "x = -6."),

 dict(n="M2E-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("The equation (x - 4)(x + 9) = 0 has two solutions. What is the sum of those two "
            "solutions?"),
      choices=["-5", "5", "13", "36"], correct="A",
      check="The solutions are 4 and -9, and 4 + (-9) = -5."),

 dict(n="M2E-11", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which expression is equivalent to 7a + 3b - 2a + 5b?"),
      choices=["9a + 2b", "13ab", "5a + 2b", "5a + 8b"], correct="D",
      check="Collecting the a terms gives 7a - 2a = 5a and collecting the b terms gives "
            "3b + 5b = 8b, so the expression is 5a + 8b."),

 dict(n="M2E-12", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The table gives four values of the linear function g."
            + table(["x", "1", "2", "3", "4"],
                    [["g(x)", "7", "11", "15", "19"]])
            + "What is the value of g(7)?"),
      choices=["23", "27", "31", "35"], correct="C",
      check="Each step of 1 in x raises g by 4, so g(x) = 4x + 3 and g(7) = 28 + 3 = 31."),

 dict(n="M2E-13", domain="ADV", skill="ADV-NE", type="FR",
      stem=("The product of two consecutive positive integers is 210. What is the greater of the "
            "two integers?"),
      answers=["15"],
      check="With n the smaller integer, n(n+1) = 210 gives n^2 + n - 210 = (n+15)(n-14) = 0, so "
            "the positive solution is n = 14 and the greater integer is 15."),

 dict(n="M2E-14", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A decoy pond took 240 wildfowl in one season, and 35% of them were teal. How many "
            "teal were taken?"),
      choices=["60", "84", "96", "105"], correct="B",
      check="0.35(240) = 84."),

 dict(n="M2E-15", domain="PSDA", skill="PSDA-RP", type="MC",
      stem=("A dovecote yields 7 squabs a year from each nest hole. How many nest holes are needed "
            "to yield 245 squabs a year at that rate?"),
      choices=["14", "21", "28", "35"], correct="D",
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
      stem=("Three of the four interior angles of a quadrilateral measure 95&deg; , 128&deg; , and "
            "62&deg; . What is the measure, in degrees, of the fourth interior angle?"),
      choices=["75", "85", "105", "115"], correct="A",
      check="The four interior angles of a quadrilateral sum to 360&deg;, and "
            "95 + 128 + 62 = 285, so the fourth angle measures 360 - 285 = 75&deg;."),

 dict(n="M2E-21", domain="GT", skill="GT-AV", type="MC",
      stem=("A decoy pond is shaped like a trapezium whose two parallel sides measure 14 metres "
            "and 22 metres and whose perpendicular width is 9 metres. What is the area of the "
            "pond, in square metres?"),
      choices=["126", "162", "198", "324"], correct="B",
      check="The area of a trapezium is half the sum of the parallel sides times the "
            "perpendicular width, so it is (1/2)(14 + 22)(9) = 18(9) = 162 square metres."),

 dict(n="M2E-22", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle ABC, the right angle is at vertex C, the hypotenuse AB has length "
            "74, and \\( \\cos A = \\frac{35}{37} \\) . What is the length of side AC?"),
      choices=["24", "35", "70", "74"], correct="C",
      check="cos A is the side adjacent to A over the hypotenuse, that is AC/AB, so "
            "AC = 74(35/37) = 70."),
]


# =========================================================== Module 2 Hard
MODULE_2_HARD = [

 dict(n="M2H-01", domain="ALG", skill="ALG-LE", type="MC",
      stem=("Two dovecotes yielded 148 squabs between them in one season. The larger dovecote "
            "yielded 16 more than twice as many squabs as the smaller. How many more squabs did "
            "the larger dovecote yield than the smaller?"),
      choices=["60", "88", "104", "148"], correct="A",
      check="With s squabs from the smaller dovecote the larger yielded 2s + 16, so "
            "s + 2s + 16 = 148 gives 3s = 132 and s = 44; the larger yielded 104, which is 60 "
            "more than 44."),

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
      stem=("A wildfowler sets x teal decoys and y wigeon decoys on a pond. The pond takes no more "
            "than 60 decoys altogether, and she always sets at least twice as many teal decoys as "
            "wigeon decoys. Which ordered pair (x, y) satisfies both of these conditions?"),
      choices=["(24, 14)", "(30, 20)", "(40, 18)", "(44, 20)"], correct="C",
      check="The conditions are x + y <= 60 and x >= 2y. For (24, 14), 24 < 28; for (30, 20), "
            "30 < 40; for (44, 20), 64 > 60. Only (40, 18) satisfies both, since 58 <= 60 and "
            "40 >= 36."),

 dict(n="M2H-07", domain="ALG", skill="ALG-LE", type="FR",
      stem=("What value of x satisfies \\( \\frac{x}{4} + \\frac{x}{6} = \\frac{x-14}{2} \\) ?"),
      answers=["84"],
      check="Multiplying through by 12 gives 3x + 2x = 6(x - 14), so 5x = 6x - 84 and x = 84."),

 dict(n="M2H-08", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("For a constant k, \\( (3x+k)^{2} = 9x^{2}+42x+c \\) for every value of x, where c is a "
            "constant. What is the value of c?"),
      choices=["14", "42", "49", "441"], correct="C",
      check="Expanding gives 9x^2 + 6kx + k^2, so 6k = 42 and k = 7, and c = k^2 = 49."),

 dict(n="M2H-09", domain="ADV", skill="ADV-NE", type="MC",
      stem=("One solution to the equation \\( 2x^{2}+kx-30=0 \\) is x = 5, where k is a constant. "
            "What is the other solution to that equation?"),
      choices=["-6", "-3", "3", "6"], correct="B",
      check="Substituting x = 5 gives 50 + 5k - 30 = 0, so k = -4 and the equation is "
            "2x^2 - 4x - 30 = 0, that is x^2 - 2x - 15 = (x-5)(x+3) = 0; the other solution is "
            "x = -3."),

 dict(n="M2H-10", domain="ADV", skill="ADV-NE", type="MC",
      stem=("In the equation \\( 2(x-3)^{3} = 54 \\) , what is the value of x?"),
      choices=["6", "9", "12", "30"], correct="A",
      check="Dividing by 2 gives (x-3)^3 = 27, so x - 3 = 3 and x = 6."),

 dict(n="M2H-11", domain="ADV", skill="ADV-NF", type="MC",
      stem=("The functions f and g are defined by f(x) = ax + 3 and g(x) = x + a, where a is a "
            "positive constant. If f(g(2)) = 18, what is the value of a?"),
      choices=["3", "5", "6", "15"], correct="A",
      check="g(2) = 2 + a, so f(g(2)) = a(2+a) + 3 = a^2 + 2a + 3 = 18, giving a^2 + 2a - 15 = 0 "
            "and a = 3 or a = -5; only a = 3 is positive."),

 dict(n="M2H-12", domain="ADV", skill="ADV-EQ", type="MC",
      stem=("Which single fraction is equal to \\( \\frac{5}{x^{2}-4} - \\frac{1}{x-2} \\) , where "
            "\\( x \\gt 2 \\) ?"),
      choices=["\\( \\frac{4}{x^{2}-4} \\)", "\\( \\frac{x+7}{x^{2}-4} \\)",
               "\\( \\frac{5-x}{x^{2}-4} \\)", "\\( \\frac{3-x}{x^{2}-4} \\)"],
      correct="D",
      check="Factoring the first denominator as (x-2)(x+2) shows the common denominator is "
            "x^2 - 4, over which the numerator is 5 - (x+2) = 3 - x."),

 dict(n="M2H-13", domain="ADV", skill="ADV-NF", type="FR",
      stem=("The function f is defined by \\( f(x) = x^{2}+3x \\) . What is the average rate of "
            "change of f from x = 2 to x = 5?"),
      answers=["10"],
      check="f(2) = 4 + 6 = 10 and f(5) = 25 + 15 = 40, so the average rate of change is "
            "(40 - 10)/(5 - 2) = 30/3 = 10."),

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
      stem=("The table gives the number of nest holes in a dovecote that yielded each number of "
            "squabs during one season. The dovecote has 25 nest holes in all."
            + table(["Squabs from the hole", "Number of nest holes"],
                    [["9", "3"], ["10", "5"], ["11", "7"], ["12", "6"], ["13", "4"]])
            + "What is the median number of squabs yielded by a nest hole?"),
      answers=["11"],
      check="With 25 nest holes the median is the 13th value in order. The running totals are 3, "
            "8, 15, 21 and 25, so the 13th value falls in the group that yielded 11 squabs."),

 dict(n="M2H-17", domain="PSDA", skill="PSDA-ST", type="MC",
      stem=("A basket holds 5 wigeon and 7 teal. Three birds are taken from the basket at random, "
            "one after another and without replacement. What is the probability that none of the "
            "three is a wigeon?"),
      choices=["\\( \\frac{7}{44} \\)", "\\( \\frac{35}{144} \\)", "\\( \\frac{5}{12} \\)",
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
      stem=("A rectangular tank measuring 60 centimetres by 40 centimetres holds water to a depth "
            "of 15 centimetres. A basket of carp is lowered in and sinks completely, raising the "
            "water to a depth of 22 centimetres. Given that 1 litre is 1,000 cubic centimetres, "
            "what is the volume, in litres, of the basket and its carp together?"),
      choices=["7", "16.8", "36", "52.8"], correct="B",
      check="The water rises 22 - 15 = 7 centimetres over a base of 60(40) = 2,400 square "
            "centimetres, so the basket and carp displace 2,400(7) = 16,800 cubic centimetres, "
            "which is 16.8 litres."),

 dict(n="M2H-20", domain="GT", skill="GT-LA", type="MC",
      stem=("The floor of a dovecote is a regular polygon, and each of its interior angles "
            "measures 156&deg; . How many sides does the polygon have?"),
      choices=["15", "18", "20", "24"], correct="A",
      check="Each exterior angle measures 180 - 156 = 24&deg;, and the exterior angles of any "
            "polygon sum to 360&deg;, so the polygon has 360/24 = 15 sides."),

 dict(n="M2H-21", domain="GT", skill="GT-TR", type="MC",
      stem=("In right triangle JKL, the right angle is at vertex L. The leg KL has length 33, and "
            "\\( \\tan J = \\frac{33}{56} \\) . What is the length of JK?"),
      choices=["56", "65", "89", "112"], correct="B",
      check="tan J is the side opposite J over the side adjacent to J, that is KL/JL, so "
            "JL = 56. JK is the hypotenuse, and sqrt(33^2 + 56^2) = sqrt(4225) = 65."),

 dict(n="M2H-22", domain="GT", skill="GT-AV", type="MC",
      stem=("Two conical feed hoppers are similar in shape, and their heights are in the ratio 2 to "
            "5. The smaller hopper holds 96 litres. How many litres does the larger hopper hold?"),
      choices=["240", "600", "1,500", "6,000"], correct="C",
      check="Volumes of similar solids scale as the cube of the ratio, so the larger holds "
            "96(5/2)^3 = 96(125/8) = 1,500 litres."),
]

ALL = MODULE_1 + MODULE_2_EASY + MODULE_2_HARD
